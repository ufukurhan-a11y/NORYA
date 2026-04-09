"""E-posta gönderimi: şifre sıfırlama (ülkeye göre dil, kurumsal kimlik)."""
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from app.core.config import settings

log = logging.getLogger("norya.email")

# Ülke kodu -> e-posta dili (şifre sıfırlama metinleri)
COUNTRY_TO_LANG = {
    "TR": "tr",
    "DE": "de",
    "AT": "de",
    "CH": "de",
    "FR": "fr",
    "BE": "fr",
    "ES": "es",
    "IT": "it",
    "NL": "nl",
    "PT": "pt",
    "GB": "en",
    "US": "en",
    "AU": "en",
    "CA": "en",
    "IN": "en",
    "PL": "pl",
    "RU": "ru",
    "SA": "ar",
    "AE": "ar",
    "GR": "el",
    "CZ": "cs",
    "RO": "ro",
    "HU": "hu",
    "SE": "sv",
    "NO": "no",
    "DK": "da",
    "FI": "fi",
    "JP": "ja",
    "KR": "ko",
    "CN": "zh",
}
DEFAULT_LANG = "en"

# Kurumsal kısa slogan (doğrulama / şifre sıfırlama şablonlarında; dil ile uyumlu)
_EMAIL_BRAND_TAGLINE = {
    "tr": "Norya — Güvenilir kan tahlili analizi",
    "en": "Norya — Trusted blood test analysis",
    "de": "Norya — Zuverlässige Bluttest-Analyse",
    "fr": "Norya — Analyse fiable des résultats sanguins",
    "es": "Norya — Análisis fiable de analíticas sanguíneas",
    "it": "Norya — Analisi affidabile degli esami del sangue",
    "nl": "Norya — Betrouwbare bloedtestanalyse",
    "pt": "Norya — Análise confiável de exames de sangue",
    "pl": "Norya — Niezawodna analiza badań krwi",
    "ru": "Norya — Надёжный анализ результатов анализа крови",
    "ar": "Norya — تحليل موثوق لنتائج فحص الدم",
    "el": "Norya — Αξιόπιστη ανάλυση αιματολογικών εξετάσεων",
    "cs": "Norya — Spolehlivá analýza krevních testů",
    "ja": "Norya — 信頼できる血液検査の分析",
    "ko": "Norya — 신뢰할 수 있는 혈액 검사 분석",
    "zh": "Norya — 值得信赖的验血分析",
    "sv": "Norya — Pålitlig blodprovskontroll",
    "no": "Norya — Pålitelig blodprøveanalyse",
    "da": "Norya — Pålidelig blodprøveanalyse",
    "fi": "Norya — Luotettava verikokeanalyysi",
    "ro": "Norya — Analiză de încredere a analizelor de sânge",
    "hu": "Norya — Megbízható vérvizsgálati elemzés",
}


def _email_brand_tagline(lang: str | None) -> str:
    code = (lang or DEFAULT_LANG).strip() if lang else DEFAULT_LANG
    return _EMAIL_BRAND_TAGLINE.get(code, _EMAIL_BRAND_TAGLINE["en"])


def country_to_lang(country_code: str | None) -> str:
    """Kullanıcı ülkesine göre e-posta dil kodu (tr, en, de, fr, ...)."""
    if not country_code or len(country_code) < 2:
        return DEFAULT_LANG
    key = (country_code or "").strip().upper()[:2]
    return COUNTRY_TO_LANG.get(key, DEFAULT_LANG)


# Şifre sıfırlama e-postası: konu ve gövde (dil bazlı). Kurumsal HTML.
_RESET_SUBJECT = {
    "tr": "Norya — Şifre sıfırlama",
    "en": "Norya — Password reset",
    "de": "Norya — Passwort zurücksetzen",
    "fr": "Norya — Réinitialisation du mot de passe",
    "es": "Norya — Restablecer contraseña",
    "it": "Norya — Reimpostazione password",
    "nl": "Norya — Wachtwoord opnieuw instellen",
    "pt": "Norya — Redefinir senha",
    "pl": "Norya — Reset hasła",
    "ru": "Norya — Сброс пароля",
    "ar": "Norya — إعادة تعيين كلمة المرور",
    "el": "Norya — Επαναφορά κωδικού",
    "cs": "Norya — Obnovení hesla",
    "ja": "Norya — パスワードのリセット",
    "ko": "Norya — 비밀번호 재설정",
    "zh": "Norya — 重置密码",
    "sv": "Norya — Återställ lösenord",
    "no": "Norya — Tilbakestill passord",
    "da": "Norya — Nulstil adgangskode",
    "fi": "Norya — Salasanan palautus",
    "ro": "Norya — Resetare parolă",
    "hu": "Norya — Jelszó visszaállítása",
}


def _reset_body_intro(lang: str, expiry_hours: int) -> str:
    snippets = {
        "tr": f"Şifrenizi sıfırlamak için aşağıdaki butona tıklayın. Link {expiry_hours} saat geçerlidir.",
        "en": f"Click the button below to reset your password. The link is valid for {expiry_hours} hour(s).",
        "de": f"Klicken Sie auf die Schaltfläche unten, um Ihr Passwort zurückzusetzen. Der Link ist {expiry_hours} Stunde(n) gültig.",
        "fr": f"Cliquez sur le bouton ci-dessous pour réinitialiser votre mot de passe. Le lien est valable {expiry_hours} heure(s).",
        "es": f"Haga clic en el botón de abajo para restablecer su contraseña. El enlace es válido durante {expiry_hours} hora(s).",
        "it": f"Clicca il pulsante qui sotto per reimpostare la password. Il link è valido per {expiry_hours} ora/e.",
        "nl": f"Klik op de knop hieronder om uw wachtwoord opnieuw in te stellen. De link is {expiry_hours} uur geldig.",
        "pt": f"Clique no botão abaixo para redefinir sua senha. O link é válido por {expiry_hours} hora(s).",
        "pl": f"Kliknij przycisk poniżej, aby zresetować hasło. Link jest ważny przez {expiry_hours} godz.",
        "ru": f"Нажмите кнопку ниже, чтобы сбросить пароль. Ссылка действительна {expiry_hours} ч.",
        "ar": f"انقر على الزر أدناه لإعادة تعيين كلمة المرور. الرابط صالح لمدة {expiry_hours} ساعة.",
        "el": f"Κάντε κλικ στο κουμπί παρακάτω για επαναφορά κωδικού. Ο σύνδεσμος ισχύει για {expiry_hours} ώρα(ες).",
        "cs": f"Klikněte na tlačítko níže pro obnovení hesla. Odkaz je platný {expiry_hours} hod.",
        "ja": f"下のボタンをクリックしてパスワードをリセットしてください。リンクの有効期限は{expiry_hours}時間です。",
        "ko": f"아래 버튼을 클릭하여 비밀번호를 재설정하세요. 링크는 {expiry_hours}시간 동안 유효합니다.",
        "zh": f"点击下方按钮重置密码。链接有效期为{expiry_hours}小时。",
        "sv": f"Klicka på knappen nedan för att återställa ditt lösenord. Länken är giltig i {expiry_hours} timme.",
        "no": f"Klikk på knappen nedenfor for å tilbakestille passordet. Lenken er gyldig i {expiry_hours} time(r).",
        "da": f"Klik på knappen nedenfor for at nulstille din adgangskode. Linket er gyldigt i {expiry_hours} time(r).",
        "fi": f"Napsauta alla olevaa painiketta salasanan palauttamiseksi. Linkki on voimassa {expiry_hours} tunti(a).",
        "ro": f"Faceți clic pe butonul de mai jos pentru a reseta parola. Linkul este valid {expiry_hours} oră(e).",
        "hu": f"A jelszó visszaállításához kattintson az alábbi gombra. A link {expiry_hours} óraig érvényes.",
    }
    return snippets.get(lang, snippets["en"])


def _reset_body_footer(lang: str) -> str:
    snippets = {
        "tr": "Bu isteği siz yapmadıysanız bu e-postayı yok sayabilirsiniz.",
        "en": "If you did not request this, you can ignore this email.",
        "de": "Wenn Sie dies nicht angefordert haben, können Sie diese E-Mail ignorieren.",
        "fr": "Si vous n'êtes pas à l'origine de cette demande, vous pouvez ignorer cet e-mail.",
        "es": "Si no solicitó esto, puede ignorar este correo.",
        "it": "Se non hai richiesto questo, puoi ignorare questa email.",
        "nl": "Als u dit niet heeft aangevraagd, kunt u deze e-mail negeren.",
        "pt": "Se você não solicitou isso, pode ignorar este e-mail.",
        "pl": "Jeśli tego nie żądałeś, zignoruj tę wiadomość.",
        "ru": "Если вы не запрашивали это, проигнорируйте письмо.",
        "ar": "إذا لم تطلب ذلك، يمكنك تجاهل هذا البريد الإلكتروني.",
        "el": "Αν δεν ζητήσατε αυτό, μπορείτε να αγνοήσετε αυτό το email.",
        "cs": "Pokud jste to nepožadovali, můžete tento e-mail ignorovat.",
        "ja": "心当たりがない場合は、このメールを無視してください。",
        "ko": "요청하지 않으셨다면 이 이메일을 무시하셔도 됩니다.",
        "zh": "如果您没有请求此操作，请忽略此邮件。",
        "sv": "Om du inte begärde detta kan du ignorera det här e-postmeddelandet.",
        "no": "Hvis du ikke ba om dette, kan du ignorere denne e-posten.",
        "da": "Hvis du ikke anmodede om dette, kan du ignorere denne e-mail.",
        "fi": "Jos et pyytänyt tätä, voit ohittaa tämän sähköpostin.",
        "ro": "Dacă nu ați solicitat acest lucru, puteți ignora acest e-mail.",
        "hu": "Ha Ön nem kérte ezt, hagyja figyelmen kívül ezt az e-mailt.",
    }
    return snippets.get(lang, snippets["en"])


def _button_text(lang: str) -> str:
    snippets = {
        "tr": "Şifremi sıfırla",
        "en": "Reset password",
        "de": "Passwort zurücksetzen",
        "fr": "Réinitialiser le mot de passe",
        "es": "Restablecer contraseña",
        "it": "Reimposta password",
        "nl": "Wachtwoord opnieuw instellen",
        "pt": "Redefinir senha",
        "pl": "Zresetuj hasło",
        "ru": "Сбросить пароль",
        "ar": "إعادة تعيين كلمة المرور",
        "el": "Επαναφορά κωδικού",
        "cs": "Obnovit heslo",
        "ja": "パスワードをリセット",
        "ko": "비밀번호 재설정",
        "zh": "重置密码",
        "sv": "Återställ lösenord",
        "no": "Tilbakestill passord",
        "da": "Nulstil adgangskode",
        "fi": "Palauta salasana",
        "ro": "Resetează parola",
        "hu": "Jelszó visszaállítása",
    }
    return snippets.get(lang, snippets["en"])


def build_reset_email_html(lang: str, reset_link: str, expiry_hours: int = 1) -> tuple[str, str]:
    """Kurumsal Norya şifre sıfırlama e-postası HTML + konu. (subject, html_body)."""
    lang = lang or DEFAULT_LANG
    if lang not in _RESET_SUBJECT:
        lang = DEFAULT_LANG
    subject = _RESET_SUBJECT[lang]
    intro = _reset_body_intro(lang, expiry_hours)
    footer = _reset_body_footer(lang)
    btn = _button_text(lang)
    tagline = _email_brand_tagline(lang)
    from_name = getattr(settings, "smtp_from_name", None) or "Norya"
    logo_url = (getattr(settings, "frontend_url", None) or "").strip().rstrip("/") or "https://norya.com"
    logo_url = f"{logo_url}/static/norya_logo_transparent_trim.png"
    # Kurumsal kimlik: logo + Norya renkleri, tek sütun
    html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{subject}</title>
</head>
<body style="margin:0;padding:0;background-color:#f1f5f9;font-family:'Segoe UI',system-ui,-apple-system,sans-serif;">
  <table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="background-color:#f1f5f9;">
    <tr>
      <td align="center" style="padding:32px 16px;">
        <table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="max-width:480px;background:#ffffff;border-radius:16px;box-shadow:0 4px 24px rgba(10,25,41,0.08);overflow:hidden;">
          <tr>
            <td style="background:linear-gradient(135deg,#1a2d42 0%,#2d4a6f 50%,#0d9488 100%);padding:28px 24px;text-align:center;">
              <img src="{logo_url}" alt="Norya" style="height:56px;width:auto;max-width:200px;display:block;margin:0 auto 8px;object-fit:contain;background:#fff;" />
              <div style="font-size:18px;font-weight:600;color:#ffffff;">{from_name}</div>
            </td>
          </tr>
          <tr>
            <td style="padding:28px 24px;">
              <p style="margin:0 0 20px;font-size:16px;line-height:1.6;color:#334155;">{intro}</p>
              <p style="margin:0 0 24px;text-align:center;">
                <a href="{reset_link}" style="display:inline-block;padding:14px 28px;background:#e07a5f;color:#ffffff!important;text-decoration:none;font-weight:600;font-size:15px;border-radius:10px;">{btn}</a>
              </p>
              <p style="margin:0;font-size:13px;line-height:1.5;color:#64748b;">{footer}</p>
            </td>
          </tr>
          <tr>
            <td style="padding:16px 24px;border-top:1px solid #e2e8f0;font-size:12px;color:#94a3b8;text-align:center;">
              &copy; {tagline}
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>"""
    return subject, html


def is_mail_configured() -> bool:
    """SMTP ayarları dolu mu?"""
    host = getattr(settings, "smtp_host", None) or ""
    return bool(host.strip())


def send_email(to: str, subject: str, html_body: str) -> bool:
    """Tek bir HTML e-posta gönderir. Başarılı ise True."""
    if not getattr(settings, "email_send_enabled", True):
        log.info("Email sending disabled by EMAIL_SEND_ENABLED; skipped recipient=%s", to)
        return False
    if not is_mail_configured():
        log.warning("SMTP not configured; email not sent to %s", to)
        return False
    host = (settings.smtp_host or "").strip()
    port = int(getattr(settings, "smtp_port", 587) or 587)
    user = (getattr(settings, "smtp_user", None) or "").strip()
    password = (getattr(settings, "smtp_password", None) or "").strip()
    from_addr = (getattr(settings, "smtp_from", None) or "noreply@norya.com").strip()
    from_name = (getattr(settings, "smtp_from_name", None) or "Norya").strip()
    use_tls = getattr(settings, "smtp_use_tls", True)
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = f"{from_name} <{from_addr}>" if from_name else from_addr
    msg["To"] = to
    msg.attach(MIMEText(html_body, "html", "utf-8"))
    try:
        with smtplib.SMTP(host, port, timeout=15) as smtp:
            if use_tls:
                smtp.starttls()
            if user and password:
                smtp.login(user, password)
            smtp.sendmail(from_addr, [to], msg.as_string())
        log.info("Email sent to %s subject=%s", to, subject[:50])
        return True
    except Exception as e:
        log.exception("Failed to send email to %s: %s", to, e)
        return False


def send_password_reset_email(to_email: str, reset_link: str, lang: str, expiry_hours: int = 1) -> bool:
    """Şifre sıfırlama e-postası gönderir (dil ve kurumsal şablon)."""
    subject, html = build_reset_email_html(lang, reset_link, expiry_hours)
    return send_email(to_email, subject, html)


# E-posta doğrulama: konu ve gövde (dil bazlı)
_VERIFY_SUBJECT = {
    "tr": "Norya — E-posta adresinizi doğrulayın",
    "en": "Norya — Verify your email address",
    "de": "Norya — E-Mail-Adresse bestätigen",
    "fr": "Norya — Vérifiez votre adresse e-mail",
    "es": "Norya — Verifique su dirección de correo",
    "it": "Norya — Verifica il tuo indirizzo email",
    "nl": "Norya — Bevestig je e-mailadres",
    "pt": "Norya — Verifique seu endereço de e-mail",
    "pl": "Norya — Potwierdź adres e-mail",
    "ru": "Norya — Подтвердите адрес электронной почты",
    "ar": "Norya — تحقق من بريدك الإلكتروني",
    "el": "Norya — Επιβεβαιώστε το email σας",
    "ja": "Norya — メールアドレスを確認してください",
    "ko": "Norya — 이메일 주소를 확인하세요",
    "zh": "Norya — 验证您的电子邮件地址",
    "sv": "Norya — Verifiera din e-postadress",
    "no": "Norya — Bekreft e-postadressen din",
    "da": "Norya — Bekræft din e-mailadresse",
    "fi": "Norya — Vahvista sähköpostiosoitteesi",
    "cs": "Norya — Potvrďte svou e-mailovou adresu",
    "ro": "Norya — Confirmați adresa de e-mail",
    "hu": "Norya — Erősítse meg e-mail-címét",
}
_VERIFY_INTRO = {
    "tr": "Kaydınızı tamamlamak için aşağıdaki butona tıklayarak e-posta adresinizi doğrulayın.",
    "en": "Click the button below to verify your email address and complete your registration.",
    "de": "Klicken Sie auf die Schaltfläche unten, um Ihre E-Mail-Adresse zu bestätigen.",
    "fr": "Cliquez sur le bouton ci-dessous pour vérifier votre adresse e-mail.",
    "es": "Haga clic en el botón de abajo para verificar su dirección de correo.",
    "it": "Clicca il pulsante qui sotto per verificare il tuo indirizzo email.",
    "nl": "Klik op de knop hieronder om uw e-mailadres te bevestigen.",
    "pt": "Clique no botão abaixo para verificar seu endereço de e-mail.",
    "pl": "Kliknij przycisk poniżej, aby potwierdzić adres e-mail.",
    "ru": "Нажмите кнопку ниже, чтобы подтвердить адрес электронной почты.",
    "ar": "انقر على الزر أدناه للتحقق من بريدك الإلكتروني.",
    "el": "Κάντε κλικ στο κουμπί παρακάτω για να επιβεβαιώσετε το email σας.",
    "ja": "下のボタンをクリックしてメールアドレスを確認してください。",
    "ko": "아래 버튼을 클릭하여 이메일 주소를 확인하세요.",
    "zh": "点击下方按钮验证您的电子邮件地址。",
    "sv": "Klicka på knappen nedan för att verifiera din e-postadress.",
    "no": "Klikk på knappen nedenfor for å bekrefte e-postadressen din.",
    "da": "Klik på knappen nedenfor for at bekræfte din e-mailadresse.",
    "fi": "Napsauta alla olevaa painiketta vahvistaaksesi sähköpostiosoitteesi.",
    "cs": "Klepnutím na tlačítko níže potvrďte svou e-mailovou adresu a dokončete registraci.",
    "ro": "Faceți clic pe butonul de mai jos pentru a confirma adresa de e-mail și a finaliza înregistrarea.",
    "hu": "Kattintson az alábbi gombra e-mail-címe megerősítéséhez és a regisztráció befejezéséhez.",
}
_VERIFY_BTN = {
    "tr": "E-postayı doğrula",
    "en": "Verify email",
    "de": "E-Mail bestätigen",
    "fr": "Vérifier",
    "es": "Verificar",
    "it": "Verifica",
    "nl": "Bevestigen",
    "pt": "Verificar",
    "pl": "Potwierdź",
    "ru": "Подтвердить",
    "ar": "تحقق",
    "el": "Επιβεβαίωση",
    "ja": "確認",
    "ko": "확인",
    "zh": "验证",
    "sv": "Verifiera",
    "no": "Bekreft",
    "da": "Bekræft",
    "fi": "Vahvista",
    "cs": "Potvrdit e-mail",
    "ro": "Confirmă e-mailul",
    "hu": "E-mail megerősítése",
}


def build_verify_email_html(lang: str, verify_link: str) -> tuple[str, str]:
    """E-posta doğrulama HTML + konu. (subject, html_body)."""
    lang = lang or DEFAULT_LANG
    if lang not in _VERIFY_SUBJECT:
        lang = DEFAULT_LANG
    subject = _VERIFY_SUBJECT.get(lang, _VERIFY_SUBJECT["en"])
    intro = _VERIFY_INTRO.get(lang, _VERIFY_INTRO["en"])
    btn = _VERIFY_BTN.get(lang, _VERIFY_BTN["en"])
    tagline = _email_brand_tagline(lang)
    from_name = getattr(settings, "smtp_from_name", None) or "Norya"
    html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{subject}</title>
</head>
<body style="margin:0;padding:0;background-color:#f1f5f9;font-family:'Segoe UI',system-ui,-apple-system,sans-serif;">
  <table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="background-color:#f1f5f9;">
    <tr>
      <td align="center" style="padding:32px 16px;">
        <table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="max-width:480px;background:#ffffff;border-radius:16px;box-shadow:0 4px 24px rgba(10,25,41,0.08);overflow:hidden;">
          <tr>
            <td style="background:linear-gradient(135deg,#1a2d42 0%,#2d4a6f 50%,#0d9488 100%);padding:28px 24px;text-align:center;">
              <div style="font-size:14px;letter-spacing:0.12em;color:rgba(255,255,255,0.9);font-weight:700;margin-bottom:4px;">NORYA</div>
              <div style="font-size:18px;font-weight:600;color:#ffffff;">{from_name}</div>
            </td>
          </tr>
          <tr>
            <td style="padding:28px 24px;">
              <p style="margin:0 0 20px;font-size:16px;line-height:1.6;color:#334155;">{intro}</p>
              <p style="margin:0 0 24px;text-align:center;">
                <a href="{verify_link}" style="display:inline-block;padding:14px 28px;background:#0d9488;color:#ffffff!important;text-decoration:none;font-weight:600;font-size:15px;border-radius:10px;">{btn}</a>
              </p>
              <p style="margin:0;font-size:13px;line-height:1.5;color:#64748b;">{tagline}</p>
            </td>
          </tr>
          <tr>
            <td style="padding:16px 24px;border-top:1px solid #e2e8f0;font-size:12px;color:#94a3b8;text-align:center;">
              &copy; Norya
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>"""
    return subject, html


def send_verify_email(to_email: str, verify_link: str, lang: str = "en") -> bool:
    """E-posta doğrulama linki gönderir (dil ve kurumsal şablon)."""
    subject, html = build_verify_email_html(lang, verify_link)
    return send_email(to_email, subject, html)


# ---------------------------------------------------------------------------
# Welcome email (lead subscribe sonrası)
# ---------------------------------------------------------------------------

_WELCOME_SUBJECT = {
    "tr": "Norya'ya hoş geldiniz — örnek raporu inceleyin",
    "en": "Welcome to NoryaAI — see what your report looks like",
    "de": "Willkommen bei NoryaAI — so sieht Ihr Bericht aus",
    "fr": "Bienvenue sur NoryaAI — découvrez votre rapport",
    "es": "Bienvenido a NoryaAI — vea cómo es su informe",
    "it": "Benvenuto su NoryaAI — ecco come appare il tuo report",
    "nl": "Welkom bij NoryaAI — zo ziet uw rapport eruit",
    "pt": "Bem-vindo à NoryaAI — veja como é o seu relatório",
    "pl": "Witamy w NoryaAI — zobacz, jak wygląda Twój raport",
    "ru": "Добро пожаловать в NoryaAI — посмотрите, как выглядит ваш отчёт",
    "ar": "مرحبًا بك في NoryaAI — شاهد نموذج التقرير",
    "el": "Καλώς ήρθατε στο NoryaAI — δείτε πώς φαίνεται η αναφορά σας",
    "cs": "Vítejte v NoryaAI — podívejte se, jak vypadá vaše zpráva",
    "ja": "NoryaAIへようこそ — レポートのイメージをご覧ください",
    "ko": "NoryaAI에 오신 것을 환영합니다 — 리포트 예시를 확인하세요",
    "zh": "欢迎来到 NoryaAI — 查看您的报告样例",
    "sv": "Välkommen till NoryaAI — så här kan din rapport se ut",
    "no": "Velkommen til NoryaAI — slik kan rapporten din se ut",
    "da": "Velkommen til NoryaAI — sådan kan din rapport se ud",
    "fi": "Tervetuloa NoryaAIhin — näin raporttisi voi näyttää",
    "ro": "Bun venit la NoryaAI — vezi cum arată raportul tău",
    "hu": "Üdvözöljük a NoryaAI-nál — így nézhet ki a jelentése",
    "he": "ברוכים הבאים ל-NoryaAI — צפו בדוגמת דוח",
    "hi": "NoryaAI में आपका स्वागत है — अपनी रिपोर्ट देखें",
}

_WELCOME_GREETING = {
    "tr": "Kaydınız için teşekkürler!",
    "en": "Thanks for signing up!",
    "de": "Vielen Dank für Ihre Anmeldung!",
    "fr": "Merci pour votre inscription !",
    "es": "¡Gracias por registrarse!",
    "it": "Grazie per l'iscrizione!",
    "nl": "Bedankt voor uw aanmelding!",
    "pt": "Obrigado por se cadastrar!",
    "pl": "Dziękujemy za rejestrację!",
    "ru": "Спасибо за регистрацию!",
    "ar": "!شكرًا لتسجيلك",
    "el": "Ευχαριστούμε για την εγγραφή σας!",
    "cs": "Děkujeme za registraci!",
    "ja": "ご登録ありがとうございます！",
    "ko": "가입해 주셔서 감사합니다!",
    "zh": "感谢您的注册！",
    "sv": "Tack för att du registrerade dig!",
    "no": "Takk for at du registrerte deg!",
    "da": "Tak for din tilmelding!",
    "fi": "Kiitos rekisteröitymisestä!",
    "ro": "Mulțumim că v-ați înscris!",
    "hu": "Köszönjük a regisztrációt!",
    "he": "!תודה שנרשמת",
    "hi": "साइन अप करने के लिए धन्यवाद!",
}

_WELCOME_BODY = {
    "tr": (
        "Norya, kan tahlili sonuçlarınızı yapılandırılmış, anlaşılır ve doktora hazır bir rapora dönüştürür. "
        "İşte size yardımcı olabileceği birkaç şey:"
    ),
    "en": (
        "NoryaAI turns your blood test results into a structured, easy-to-read, doctor-ready report. "
        "Here are a few things it can help with:"
    ),
    "de": (
        "NoryaAI verwandelt Ihre Blutwerte in einen strukturierten, leicht lesbaren und arztfertigen Bericht. "
        "Hier sind einige Möglichkeiten:"
    ),
    "fr": (
        "NoryaAI transforme vos résultats d'analyses sanguines en un rapport structuré, lisible et prêt pour votre médecin. "
        "Voici ce qu'il peut vous apporter :"
    ),
    "es": (
        "NoryaAI convierte sus resultados de análisis de sangre en un informe estructurado y listo para su médico. "
        "Esto es lo que puede hacer por usted:"
    ),
    "it": (
        "NoryaAI trasforma i tuoi risultati delle analisi del sangue in un report strutturato e pronto per il medico. "
        "Ecco cosa può fare per te:"
    ),
    "nl": (
        "NoryaAI zet uw bloedtestuitslagen om in een gestructureerd, leesbaar rapport, klaar voor uw arts. "
        "Dit kan het voor u doen:"
    ),
    "pt": (
        "A NoryaAI transforma os resultados dos seus exames de sangue num relatório estruturado e pronto para o médico. "
        "Eis o que pode fazer por si:"
    ),
    "pl": (
        "NoryaAI zamienia wyniki badań krwi w uporządkowany, czytelny raport gotowy dla lekarza. "
        "Oto kilka rzeczy, w których pomoże:"
    ),
    "ru": (
        "NoryaAI превращает результаты анализа крови в структурированный, понятный отчёт, готовый для врача. "
        "Вот чем он может помочь:"
    ),
    "ar": (
        "يحول NoryaAI نتائج تحاليل الدم إلى تقرير منظم وسهل القراءة وجاهز للطبيب. "
        "إليك بعض الأشياء التي يمكنه مساعدتك فيها:"
    ),
    "el": (
        "Το NoryaAI μετατρέπει τα αποτελέσματα των εξετάσεών σας σε μια δομημένη, ευανάγνωστη αναφορά έτοιμη για τον γιατρό. "
        "Ορίστε μερικά πράγματα που μπορεί να σας βοηθήσει:"
    ),
    "cs": (
        "NoryaAI přetvoří výsledky vašich krevních testů ve strukturovanou, srozumitelnou zprávu připravenou pro lékaře. "
        "Zde je několik oblastí, kde pomůže:"
    ),
    "ja": (
        "NoryaAIは血液検査の結果を、医師に見せやすい分かりやすいレポートにまとめます。"
        "次のようなことができます："
    ),
    "ko": (
        "NoryaAI는 혈액 검사 결과를 의사에게 보여주기 좋은 구조화된 보고서로 정리해 드립니다. "
        "도움이 되는 몇 가지:"
    ),
    "zh": (
        "NoryaAI 将您的验血结果整理成结构清晰、便于向医生展示的报告。"
        "它可以帮您："
    ),
    "sv": (
        "NoryaAI förvandlar dina blodprovssvar till en tydlig, strukturerad rapport redo för läkaren. "
        "Här är några saker den kan hjälpa till med:"
    ),
    "no": (
        "NoryaAI gjør blodprøvesvarene dine om til en strukturert, lettlest rapport klar for legen. "
        "Slik kan den hjelpe deg:"
    ),
    "da": (
        "NoryaAI forvandler dine blodprøveresultater til en struktureret, læsbar rapport klar til lægen. "
        "Her er nogle ting, den kan hjælpe med:"
    ),
    "fi": (
        "NoryaAI muuttaa verikokeiden tuloksesi jäsennellyksi, helppolukuiseksi raportiksi, jota voit näyttää lääkärille. "
        "Tässä muutamia asioita, joissa se auttaa:"
    ),
    "ro": (
        "NoryaAI transformă rezultatele analizelor de sânge într-un raport structurat, ușor de citit, pregătit pentru medic. "
        "Iată câteva lucruri cu care vă poate ajuta:"
    ),
    "hu": (
        "A NoryaAI a vérvizsgálati eredményeit strukturált, könnyen olvasható, orvosnak átadható jelentéssé alakítja. "
        "Íme néhány dolog, amiben segít:"
    ),
    "he": (
        "NoryaAI הופך את תוצאות בדיקות הדם שלך לדוח מובנה, קריא ומוכן לרופא. "
        "הנה כמה דברים שהוא יכול לעזור בהם:"
    ),
    "hi": (
        "NoryaAI आपकी रक्त जांच के परिणामों को एक संरचित, पढ़ने में आसान, डॉक्टर-रेडी रिपोर्ट में बदलता है। "
        "यहां कुछ चीज़ें हैं जिनमें यह मदद कर सकता है:"
    ),
}

_WELCOME_BULLETS = {
    "tr": [
        "Sağlık skoru ve işaretlenmiş değerler",
        "Referans aralıkları ile yapılandırılmış özet",
        "9+ dilde rapor desteği",
        "Doktora hazır, indirilebilir PDF",
    ],
    "en": [
        "Health score and flagged markers",
        "Structured summary with reference ranges",
        "Reports in 9+ languages",
        "Doctor-ready, downloadable PDF",
    ],
    "de": [
        "Gesundheits-Score und markierte Werte",
        "Strukturierte Zusammenfassung mit Referenzbereichen",
        "Berichte in 9+ Sprachen",
        "Arztfertiger, herunterladbarer PDF-Bericht",
    ],
    "fr": [
        "Score de santé et marqueurs signalés",
        "Résumé structuré avec valeurs de référence",
        "Rapports en 9+ langues",
        "PDF téléchargeable, prêt pour votre médecin",
    ],
    "es": [
        "Puntuación de salud y marcadores señalados",
        "Resumen estructurado con rangos de referencia",
        "Informes en más de 9 idiomas",
        "PDF descargable, listo para su médico",
    ],
    "it": [
        "Punteggio di salute e marcatori segnalati",
        "Riepilogo strutturato con intervalli di riferimento",
        "Report in oltre 9 lingue",
        "PDF scaricabile, pronto per il medico",
    ],
    "he": [
        "ציון בריאות וסמנים מסומנים",
        "סיכום מובנה עם טווחי ייחוס",
        "דוחות ב-9+ שפות",
        "PDF להורדה, מוכן לרופא",
    ],
    "hi": [
        "स्वास्थ्य स्कोर और फ़्लैग किए गए मार्कर",
        "संदर्भ सीमाओं के साथ संरचित सारांश",
        "9+ भाषाओं में रिपोर्ट",
        "डॉक्टर-रेडी, डाउनलोड करने योग्य PDF",
    ],
    "ar": [
        "درجة الصحة والعلامات المميزة",
        "ملخص منظم مع نطاقات مرجعية",
        "تقارير بأكثر من 9 لغات",
        "تقرير PDF جاهز للطبيب وقابل للتحميل",
    ],
    "nl": [
        "Gezondheidsscore en gemarkeerde waarden",
        "Gestructureerde samenvatting met referentiewaarden",
        "Rapporten in 9+ talen",
        "Downloadbare PDF, klaar voor uw arts",
    ],
    "pt": [
        "Pontuação de saúde e marcadores assinalados",
        "Resumo estruturado com valores de referência",
        "Relatórios em mais de 9 idiomas",
        "PDF transferível, pronto para o médico",
    ],
    "pl": [
        "Wynik zdrowia i oznaczone parametry",
        "Uporządkowane podsumowanie z zakresami referencyjnymi",
        "Raporty w ponad 9 językach",
        "PDF do pobrania, gotowy dla lekarza",
    ],
    "ru": [
        "Оценка здоровья и отмеченные показатели",
        "Структурированная сводка с референсными диапазонами",
        "Отчёты на 9+ языках",
        "PDF для скачивания, готовый для врача",
    ],
    "el": [
        "Βαθμολογία υγείας και επισημασμένοι δείκτες",
        "Δομημένη περίληψη με φυσιολογικές τιμές",
        "Αναφορές σε 9+ γλώσσες",
        "Λήψιμο PDF, έτοιμο για τον γιατρό",
    ],
    "cs": [
        "Skóre zdraví a zvýrazněné hodnoty",
        "Strukturované shrnutí s referenčními rozmezími",
        "Zprávy ve více než 9 jazycích",
        "PDF ke stažení, připravené pro lékaře",
    ],
    "ja": [
        "健康スコアと注意が必要な項目",
        "基準値付きの整理された要約",
        "9か国語以上のレポート",
        "医師に見せやすいPDFでダウンロード",
    ],
    "ko": [
        "건강 점수 및 주의 지표",
        "참고 범위가 포함된 구조화된 요약",
        "9개 이상 언어로 보고서",
        "의사에게 보여주기 좋은 다운로드 가능 PDF",
    ],
    "zh": [
        "健康评分与异常指标提示",
        "含参考范围的结构化摘要",
        "支持 9 种以上语言的报告",
        "可下载、便于向医生展示的 PDF",
    ],
    "sv": [
        "Hälsopoäng och markerade värden",
        "Strukturerad sammanfattning med referensintervall",
        "Rapporter på 9+ språk",
        "Nedladdningsbar PDF, redo för läkaren",
    ],
    "no": [
        "Helsepoeng og markerte verdier",
        "Strukturert sammendrag med referanseområder",
        "Rapporter på 9+ språk",
        "Nedlastbar PDF, klar for legen",
    ],
    "da": [
        "Helbredsscore og markerede værdier",
        "Struktureret oversigt med referenceintervaller",
        "Rapporter på 9+ sprog",
        "Downloadbar PDF, klar til lægen",
    ],
    "fi": [
        "Terveyspisteet ja korostetut arvot",
        "Rakennettu yhteenveto viitearvoineen",
        "Raportit yli 9 kielellä",
        "Ladattava PDF, valmis lääkärille",
    ],
    "ro": [
        "Scor de sănătate și markeri evidențiați",
        "Rezumat structurat cu intervale de referință",
        "Rapoarte în peste 9 limbi",
        "PDF descărcabil, pregătit pentru medic",
    ],
    "hu": [
        "Egészségpontszám és kiemelt értékek",
        "Strukturált összefoglaló referenciatartományokkal",
        "Jelentések 9+ nyelven",
        "Letölthető PDF, orvosnak átadható",
    ],
}

_WELCOME_CTA = {
    "tr": "Kan tahlilimi analiz et",
    "en": "Analyze my blood test",
    "de": "Meine Blutwerte analysieren",
    "fr": "Analyser mes résultats",
    "es": "Analizar mi análisis de sangre",
    "it": "Analizza le mie analisi",
    "nl": "Mijn bloedtest analyseren",
    "pt": "Analisar o meu exame de sangue",
    "pl": "Przeanalizuj moje badanie krwi",
    "ru": "Проанализировать мой анализ крови",
    "ar": "حلل تحليل الدم الخاص بي",
    "el": "Αναλύστε τις εξετάσεις αίματός μου",
    "cs": "Analyzovat mé krevní testy",
    "ja": "血液検査を分析する",
    "ko": "혈액 검사 분석하기",
    "zh": "分析我的验血报告",
    "sv": "Analysera mitt blodprov",
    "no": "Analyser blodprøven min",
    "da": "Analyser min blodprøve",
    "fi": "Analysoi verikokeeni",
    "ro": "Analizează analiza mea de sânge",
    "hu": "Vérvizsgálatom elemzése",
    "he": "נתח את בדיקת הדם שלי",
    "hi": "मेरी रक्त जांच का विश्लेषण करें",
}

_WELCOME_SAMPLE_LINK_TEXT = {
    "tr": "Örnek raporu inceleyin →",
    "en": "See a sample report →",
    "de": "Beispielbericht ansehen →",
    "fr": "Voir un exemple de rapport →",
    "es": "Ver un informe de ejemplo →",
    "it": "Vedi un report di esempio →",
    "nl": "Bekijk een voorbeeldrapport →",
    "pt": "Ver um relatório de exemplo →",
    "pl": "Zobacz przykładowy raport →",
    "ru": "Посмотреть пример отчёта →",
    "ar": "→ شاهد نموذج تقرير",
    "el": "Δείτε δείγμα αναφοράς →",
    "cs": "Zobrazit ukázkovou zprávu →",
    "ja": "サンプルレポートを見る →",
    "ko": "샘플 리포트 보기 →",
    "zh": "查看示例报告 →",
    "sv": "Se ett exempel på rapport →",
    "no": "Se en eksempelrapport →",
    "da": "Se en eksempelrapport →",
    "fi": "Katso esimerkkiraportti →",
    "ro": "Vezi un raport exemplu →",
    "hu": "Minta jelentés megtekintése →",
    "he": "→ צפו בדוגמת דוח",
    "hi": "एक नमूना रिपोर्ट देखें →",
}

_WELCOME_HOW_LINK_TEXT = {
    "tr": "Nasıl çalışır →",
    "en": "How it works →",
    "de": "So funktioniert's →",
    "fr": "Comment ça marche →",
    "es": "Cómo funciona →",
    "it": "Come funziona →",
    "nl": "Hoe het werkt →",
    "pt": "Como funciona →",
    "pl": "Jak to działa →",
    "ru": "Как это работает →",
    "ar": "→ كيف يعمل",
    "el": "Πώς λειτουργεί →",
    "cs": "Jak to funguje →",
    "ja": "仕組み →",
    "ko": "작동 방식 →",
    "zh": "如何运作 →",
    "sv": "Så funkar det →",
    "no": "Slik fungerer det →",
    "da": "Sådan virker det →",
    "fi": "Näin se toimii →",
    "ro": "Cum funcționează →",
    "hu": "Hogyan működik →",
    "he": "→ איך זה עובד",
    "hi": "यह कैसे काम करता है →",
}

_WELCOME_PRIVACY = {
    "tr": "Verileriniz şifrelenir ve asla üçüncü taraflarla paylaşılmaz.",
    "en": "Your data is encrypted and never shared with third parties.",
    "de": "Ihre Daten werden verschlüsselt und niemals an Dritte weitergegeben.",
    "fr": "Vos données sont chiffrées et ne sont jamais partagées avec des tiers.",
    "es": "Sus datos están encriptados y nunca se comparten con terceros.",
    "it": "I tuoi dati sono crittografati e non vengono mai condivisi con terze parti.",
    "nl": "Uw gegevens worden versleuteld en nooit met derden gedeeld.",
    "pt": "Os seus dados são encriptados e nunca são partilhados com terceiros.",
    "pl": "Twoje dane są szyfrowane i nigdy nie są udostępniane osobom trzecim.",
    "ru": "Ваши данные шифруются и никогда не передаются третьим лицам.",
    "ar": "بياناتك مشفرة ولن تتم مشاركتها مع أطراف ثالثة أبدًا.",
    "el": "Τα δεδομένα σας κρυπτογραφούνται και δεν κοινοποιούνται ποτέ σε τρίτους.",
    "cs": "Vaše data jsou šifrována a nikdy je nesdílíme s třetími stranami.",
    "ja": "お客様のデータは暗号化され、第三者と共有されることはありません。",
    "ko": "데이터는 암호화되며 제3자와 공유되지 않습니다.",
    "zh": "您的数据已加密，绝不会与第三方共享。",
    "sv": "Dina uppgifter krypteras och delas aldrig med tredje part.",
    "no": "Dataene dine krypteres og deles aldri med tredjeparter.",
    "da": "Dine data krypteres og deles aldrig med tredjeparter.",
    "fi": "Tietosi salataan eikä niitä koskaan jaeta kolmansille osapuolille.",
    "ro": "Datele dvs. sunt criptate și nu sunt niciodată partajate cu terți.",
    "hu": "Az adatai titkosítva vannak, és soha nem osztjuk meg harmadik felekkel.",
    "he": "הנתונים שלך מוצפנים ולעולם לא משותפים עם צדדים שלישיים.",
    "hi": "आपका डेटा एन्क्रिप्टेड है और कभी भी तीसरे पक्ष के साथ साझा नहीं किया जाता।",
}

_WELCOME_FOOTER = {
    "tr": "Bu e-postayı Norya bültenine kayıt olduğunuz için aldınız.",
    "en": "You are receiving this because you signed up for NoryaAI updates.",
    "de": "Sie erhalten diese E-Mail, weil Sie sich für NoryaAI-Updates angemeldet haben.",
    "fr": "Vous recevez cet e-mail car vous vous êtes inscrit aux mises à jour de NoryaAI.",
    "es": "Recibe este correo porque se suscribió a las actualizaciones de NoryaAI.",
    "it": "Ricevi questa email perché ti sei iscritto agli aggiornamenti di NoryaAI.",
    "nl": "U ontvangt dit omdat u zich heeft aangemeld voor NoryaAI-updates.",
    "pt": "Está a receber isto porque se inscreveu nas atualizações da NoryaAI.",
    "pl": "Otrzymujesz tę wiadomość, ponieważ zapisałeś się na aktualizacje NoryaAI.",
    "ru": "Вы получили это письмо, потому что подписались на обновления NoryaAI.",
    "ar": "تتلقى هذا البريد لأنك اشتركت في تحديثات NoryaAI.",
    "el": "Λαμβάνετε αυτό το email επειδή εγγραφήκατε για ενημερώσεις NoryaAI.",
    "cs": "Tento e-mail dostáváte, protože jste se zaregistrovali k aktualizacím NoryaAI.",
    "ja": "NoryaAIの更新情報にご登録いただいたため、このメールをお送りしています。",
    "ko": "NoryaAI 업데이트에 가입하셨기 때문에 이 메일을 받으셨습니다.",
    "zh": "您收到此邮件是因为您订阅了 NoryaAI 更新。",
    "sv": "Du får detta eftersom du registrerade dig för uppdateringar från NoryaAI.",
    "no": "Du mottar denne e-posten fordi du registrerte deg for oppdateringer fra NoryaAI.",
    "da": "Du modtager denne e-mail, fordi du tilmeldte dig opdateringer fra NoryaAI.",
    "fi": "Saat tämän sähköpostin, koska rekisteröidyit NoryaAI-päivityksiin.",
    "ro": "Primiți acest e-mail deoarece v-ați înscris pentru actualizări NoryaAI.",
    "hu": "Azért kapja ezt az e-mailt, mert feliratkozott a NoryaAI hírekre.",
    "he": "אתה מקבל מייל זה כי נרשמת לעדכוני NoryaAI.",
    "hi": "आपको यह ईमेल इसलिए मिल रहा है क्योंकि आपने NoryaAI अपडेट के लिए साइन अप किया है।",
}


def build_welcome_email_html(lang: str, base_url: str) -> tuple[str, str]:
    """Lead welcome email HTML + subject. Returns (subject, html_body)."""
    lang = lang or DEFAULT_LANG
    if lang not in _WELCOME_SUBJECT:
        lang = DEFAULT_LANG

    subject = _WELCOME_SUBJECT[lang]
    greeting = _WELCOME_GREETING.get(lang, _WELCOME_GREETING["en"])
    body = _WELCOME_BODY.get(lang, _WELCOME_BODY["en"])
    bullets = _WELCOME_BULLETS.get(lang, _WELCOME_BULLETS["en"])
    cta = _WELCOME_CTA.get(lang, _WELCOME_CTA["en"])
    sample_link_text = _WELCOME_SAMPLE_LINK_TEXT.get(lang, _WELCOME_SAMPLE_LINK_TEXT["en"])
    how_link_text = _WELCOME_HOW_LINK_TEXT.get(lang, _WELCOME_HOW_LINK_TEXT["en"])
    privacy = _WELCOME_PRIVACY.get(lang, _WELCOME_PRIVACY["en"])
    footer = _WELCOME_FOOTER.get(lang, _WELCOME_FOOTER["en"])
    from_name = getattr(settings, "smtp_from_name", None) or "Norya"

    base = base_url.rstrip("/")
    analyze_url = f"{base}/analyze"
    sample_url = f"{base}/en/sample-blood-test-reports"
    how_url = f"{base}/how-it-works"
    logo_url = f"{base}/static/norya_logo_transparent_trim.png"

    dir_attr = ' dir="rtl"' if lang in ("he", "ar") else ""
    bullet_html = "".join(
        f'<li style="margin-bottom:6px;font-size:15px;color:#334155;">{b}</li>'
        for b in bullets
    )

    html = f"""<!DOCTYPE html>
<html lang="{lang}"{dir_attr}>
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{subject}</title>
</head>
<body style="margin:0;padding:0;background-color:#f1f5f9;font-family:'Segoe UI',system-ui,-apple-system,sans-serif;">
  <table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="background-color:#f1f5f9;">
    <tr>
      <td align="center" style="padding:32px 16px;">
        <table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="max-width:480px;background:#ffffff;border-radius:16px;box-shadow:0 4px 24px rgba(10,25,41,0.08);overflow:hidden;">
          <tr>
            <td style="background:linear-gradient(135deg,#1a2d42 0%,#2d4a6f 50%,#0d9488 100%);padding:28px 24px;text-align:center;">
              <img src="{logo_url}" alt="Norya" style="height:56px;width:auto;max-width:200px;display:block;margin:0 auto 8px;object-fit:contain;" />
              <div style="font-size:18px;font-weight:600;color:#ffffff;">{from_name}</div>
            </td>
          </tr>
          <tr>
            <td style="padding:28px 24px;">
              <p style="margin:0 0 16px;font-size:20px;font-weight:700;color:#0f172a;">{greeting}</p>
              <p style="margin:0 0 20px;font-size:15px;line-height:1.6;color:#334155;">{body}</p>
              <ul style="margin:0 0 24px;padding-left:20px;list-style:disc;">
                {bullet_html}
              </ul>
              <p style="margin:0 0 24px;text-align:center;">
                <a href="{analyze_url}" style="display:inline-block;padding:14px 28px;background:#0d9488;color:#ffffff!important;text-decoration:none;font-weight:600;font-size:15px;border-radius:10px;">{cta}</a>
              </p>
              <p style="margin:0 0 8px;text-align:center;">
                <a href="{sample_url}" style="color:#0d9488;text-decoration:underline;font-size:14px;font-weight:500;">{sample_link_text}</a>
              </p>
              <p style="margin:0 0 20px;text-align:center;">
                <a href="{how_url}" style="color:#0d9488;text-decoration:underline;font-size:14px;font-weight:500;">{how_link_text}</a>
              </p>
              <p style="margin:0;padding:12px 16px;background:#f8fafc;border-radius:8px;font-size:13px;line-height:1.5;color:#64748b;">
                🔒 {privacy}
              </p>
            </td>
          </tr>
          <tr>
            <td style="padding:16px 24px;border-top:1px solid #e2e8f0;font-size:12px;color:#94a3b8;text-align:center;">
              {footer}<br/>&copy; NoryaAI
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>"""
    return subject, html


def send_welcome_email(to_email: str, lang: str = "en", base_url: str = "https://noryaai.com") -> bool:
    """Lead subscribe sonrası welcome e-postası gönderir."""
    subject, html = build_welcome_email_html(lang, base_url)
    return send_email(to_email, subject, html)


# ---------------------------------------------------------------------------
# Enterprise lead notification (admin bildirim)
# ---------------------------------------------------------------------------

def build_enterprise_lead_notification_html(
    kurum_adi: str,
    yetkili_ad: str,
    email: str,
    telefon: str | None = None,
    kurum_tipi: str | None = None,
    aylik_rapor: str | None = None,
    mesaj: str | None = None,
) -> tuple[str, str]:
    """Admin'e gönderilecek kurumsal demo talebi bildirim e-postası."""
    subject = f"Yeni kurumsal talep: {kurum_adi}"

    rows = f"""
    <tr><td style="padding:8px 12px;font-weight:600;color:#334155;white-space:nowrap;">Kurum adı</td><td style="padding:8px 12px;color:#1e293b;">{kurum_adi}</td></tr>
    <tr style="background:#f8fafc;"><td style="padding:8px 12px;font-weight:600;color:#334155;white-space:nowrap;">Yetkili</td><td style="padding:8px 12px;color:#1e293b;">{yetkili_ad}</td></tr>
    <tr><td style="padding:8px 12px;font-weight:600;color:#334155;white-space:nowrap;">E-posta</td><td style="padding:8px 12px;color:#1e293b;"><a href="mailto:{email}" style="color:#0d9488;">{email}</a></td></tr>
    """
    if telefon:
        rows += f'<tr style="background:#f8fafc;"><td style="padding:8px 12px;font-weight:600;color:#334155;white-space:nowrap;">Telefon</td><td style="padding:8px 12px;color:#1e293b;">{telefon}</td></tr>'
    if kurum_tipi:
        rows += f'<tr><td style="padding:8px 12px;font-weight:600;color:#334155;white-space:nowrap;">Kurum türü</td><td style="padding:8px 12px;color:#1e293b;">{kurum_tipi}</td></tr>'
    if aylik_rapor:
        rows += f'<tr style="background:#f8fafc;"><td style="padding:8px 12px;font-weight:600;color:#334155;white-space:nowrap;">Aylık rapor</td><td style="padding:8px 12px;color:#1e293b;">{aylik_rapor}</td></tr>'
    if mesaj:
        rows += f'<tr><td style="padding:8px 12px;font-weight:600;color:#334155;white-space:nowrap;">Mesaj</td><td style="padding:8px 12px;color:#1e293b;">{mesaj}</td></tr>'

    admin_url = (getattr(settings, "frontend_url", None) or "").strip().rstrip("/") or "https://noryaai.com"

    html = f"""<!DOCTYPE html>
<html lang="tr">
<head><meta charset="UTF-8"/><title>{subject}</title></head>
<body style="margin:0;padding:0;background-color:#f1f5f9;font-family:'Segoe UI',system-ui,sans-serif;">
  <table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="background-color:#f1f5f9;">
    <tr><td align="center" style="padding:32px 16px;">
      <table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="max-width:520px;background:#ffffff;border-radius:16px;box-shadow:0 4px 24px rgba(10,25,41,0.08);overflow:hidden;">
        <tr><td style="background:linear-gradient(135deg,#1a2d42 0%,#2d4a6f 50%,#0d9488 100%);padding:24px;text-align:center;">
          <div style="font-size:14px;letter-spacing:0.12em;color:rgba(255,255,255,0.9);font-weight:700;">NORYA</div>
          <div style="font-size:18px;font-weight:600;color:#ffffff;margin-top:4px;">Yeni Kurumsal Demo Talebi</div>
        </td></tr>
        <tr><td style="padding:24px;">
          <table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="border:1px solid #e2e8f0;border-radius:8px;overflow:hidden;font-size:14px;">
            {rows}
          </table>
          <p style="margin:24px 0 0;text-align:center;">
            <a href="{admin_url}/admin/enterprise-leads" style="display:inline-block;padding:12px 24px;background:#0d9488;color:#ffffff!important;text-decoration:none;font-weight:600;font-size:14px;border-radius:10px;">Admin panelde görüntüle</a>
          </p>
        </td></tr>
        <tr><td style="padding:16px 24px;border-top:1px solid #e2e8f0;font-size:12px;color:#94a3b8;text-align:center;">&copy; Norya — Kurumsal bildirim</td></tr>
      </table>
    </td></tr>
  </table>
</body>
</html>"""
    return subject, html


def send_enterprise_lead_notification(
    kurum_adi: str,
    yetkili_ad: str,
    email: str,
    telefon: str | None = None,
    kurum_tipi: str | None = None,
    aylik_rapor: str | None = None,
    mesaj: str | None = None,
) -> bool:
    """Kurumsal demo talebi geldiğinde admin e-postasına bildirim gönderir."""
    admin_email = getattr(settings, "admin_notification_email", None) or getattr(settings, "smtp_from", None)
    if not admin_email:
        log.warning("No admin_notification_email configured; enterprise lead notification skipped")
        return False
    subject, html = build_enterprise_lead_notification_html(
        kurum_adi=kurum_adi,
        yetkili_ad=yetkili_ad,
        email=email,
        telefon=telefon,
        kurum_tipi=kurum_tipi,
        aylik_rapor=aylik_rapor,
        mesaj=mesaj,
    )
    return send_email(admin_email, subject, html)


# ---------------------------------------------------------------------------
# Payment confirmation email (ödeme onay maili)
# ---------------------------------------------------------------------------

def build_payment_confirmation_html(
    customer_name: str,
    product: str,
    amount: str,
    currency: str,
    transaction_id: str,
    lang: str = "tr",
    base_url: str = "https://noryaai.com",
) -> tuple[str, str]:
    """Ödeme onay e-postası HTML içeriği."""
    product_labels = {
        "single": {"tr": "Tek Analiz", "en": "Single Analysis"},
        "monthly": {"tr": "Aylık Pro Plan", "en": "Monthly Pro Plan"},
        "yearly": {"tr": "Yıllık Pro Plan", "en": "Yearly Pro Plan"},
    }
    label = product_labels.get(product, {}).get(lang, product_labels.get(product, {}).get("en", product))

    if lang == "tr":
        subject = f"Norya — Ödeme Onayı: {label}"
        greeting = f"Sayın {customer_name},"
        thank_you = "Ödemeniz başarıyla alındı. İşlem detayları aşağıdadır:"
        order_summary = "Sipariş Özeti"
        product_label = "Ürün"
        amount_label = "Tutar"
        transaction_label = "İşlem No"
        next_steps_title = "Sonraki Adımlar"
        next_steps = [
            "Hesabınıza giriş yapın veya e-posta adresinizle oturum açın.",
            "Tahlilinizi yükleyin veya metin olarak yapıştırın.",
            "AI destekli raporunuz dakikalar içinde hazır olacak.",
        ]
        cta_text = "Analize Başla"
        support_text = "Sorularınız için support@noryaai.com adresinden bize ulaşabilirsiniz."
    else:
        subject = f"Norya — Payment Confirmation: {label}"
        greeting = f"Dear {customer_name},"
        thank_you = "Your payment has been successfully processed. Transaction details are below:"
        order_summary = "Order Summary"
        product_label = "Product"
        amount_label = "Amount"
        transaction_label = "Transaction ID"
        next_steps_title = "Next Steps"
        next_steps = [
            "Log in to your account or sign in with your email address.",
            "Upload your lab test or paste the text.",
            "Your AI-powered report will be ready in minutes.",
        ]
        cta_text = "Start Analysis"
        support_text = "For questions, contact us at support@noryaai.com."

    next_steps_html = "".join(f'<li style="margin-bottom:8px;color:#334155;">{step}</li>' for step in next_steps)

    html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head><meta charset="UTF-8"/><title>{subject}</title></head>
<body style="margin:0;padding:0;background-color:#f1f5f9;font-family:'Segoe UI',system-ui,sans-serif;">
  <table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="background-color:#f1f5f9;">
    <tr><td align="center" style="padding:32px 16px;">
      <table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="max-width:520px;background:#ffffff;border-radius:16px;box-shadow:0 4px 24px rgba(10,25,41,0.08);overflow:hidden;">
        <tr><td style="background:linear-gradient(135deg,#1a2d42 0%,#2d4a6f 50%,#0d9488 100%);padding:24px;text-align:center;">
          <div style="font-size:14px;letter-spacing:0.12em;color:rgba(255,255,255,0.9);font-weight:700;">NORYA</div>
          <div style="font-size:18px;font-weight:600;color:#ffffff;margin-top:4px;">{"Ödeme Onayı" if lang == "tr" else "Payment Confirmation"}</div>
        </td></tr>
        <tr><td style="padding:24px;">
          <p style="margin:0 0 16px;font-size:15px;color:#334155;">{greeting}</p>
          <p style="margin:0 0 24px;font-size:14px;color:#475569;">{thank_you}</p>
          <table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="border:1px solid #e2e8f0;border-radius:8px;overflow:hidden;font-size:14px;margin-bottom:24px;">
            <tr style="background:#f8fafc;"><td style="padding:10px 14px;font-weight:600;color:#334155;white-space:nowrap;">{product_label}</td><td style="padding:10px 14px;color:#1e293b;">{label}</td></tr>
            <tr><td style="padding:10px 14px;font-weight:600;color:#334155;white-space:nowrap;">{amount_label}</td><td style="padding:10px 14px;color:#1e293b;">{amount} {currency}</td></tr>
            <tr style="background:#f8fafc;"><td style="padding:10px 14px;font-weight:600;color:#334155;white-space:nowrap;">{transaction_label}</td><td style="padding:10px 14px;color:#1e293b;font-family:monospace;font-size:12px;">{transaction_id}</td></tr>
          </table>
          <h3 style="margin:0 0 12px;font-size:15px;color:#1e293b;">{next_steps_title}</h3>
          <ol style="margin:0 0 24px;padding-left:20px;">{next_steps_html}</ol>
          <p style="margin:0 0 20px;text-align:center;">
            <a href="{base_url}/#analyze" style="display:inline-block;padding:12px 28px;background:#0d9488;color:#ffffff!important;text-decoration:none;font-weight:600;font-size:15px;border-radius:10px;">{cta_text}</a>
          </p>
          <p style="margin:0;font-size:13px;color:#94a3b8;text-align:center;">{support_text}</p>
        </td></tr>
        <tr><td style="padding:16px 24px;border-top:1px solid #e2e8f0;font-size:12px;color:#94a3b8;text-align:center;">&copy; Norya — {"Ödeme onay bildirimi" if lang == "tr" else "Payment confirmation"}</td></tr>
      </table>
    </td></tr>
  </table>
</body>
</html>"""
    return subject, html


def send_payment_confirmation_email(
    to_email: str,
    customer_name: str,
    product: str,
    amount: str,
    currency: str,
    transaction_id: str,
    lang: str = "tr",
    base_url: str = "https://noryaai.com",
) -> bool:
    """Ödeme onay e-postası gönderir."""
    subject, html = build_payment_confirmation_html(
        customer_name=customer_name,
        product=product,
        amount=amount,
        currency=currency,
        transaction_id=transaction_id,
        lang=lang,
        base_url=base_url,
    )
    return send_email(to_email, subject, html)

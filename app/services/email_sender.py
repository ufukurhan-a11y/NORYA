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
    from_name = getattr(settings, "smtp_from_name", None) or "Norya"
    logo_url = (getattr(settings, "frontend_url", None) or "").strip().rstrip("/") or "https://norya.com"
    logo_url = f"{logo_url}/static/logo.png"
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
              &copy; Norya — Güvenilir kan tahlili analizi
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
}
_VERIFY_BTN = {"tr": "E-postayı doğrula", "en": "Verify email", "de": "E-Mail bestätigen", "fr": "Vérifier", "es": "Verificar", "it": "Verifica", "nl": "Bevestigen", "pt": "Verificar", "pl": "Potwierdź", "ru": "Подтвердить", "ar": "تحقق", "el": "Επιβεβαίωση", "ja": "確認", "ko": "확인", "zh": "验证", "sv": "Verifiera", "no": "Bekreft", "da": "Bekræft", "fi": "Vahvista"}


def build_verify_email_html(lang: str, verify_link: str) -> tuple[str, str]:
    """E-posta doğrulama HTML + konu. (subject, html_body)."""
    lang = lang or DEFAULT_LANG
    if lang not in _VERIFY_SUBJECT:
        lang = DEFAULT_LANG
    subject = _VERIFY_SUBJECT.get(lang, _VERIFY_SUBJECT["en"])
    intro = _VERIFY_INTRO.get(lang, _VERIFY_INTRO["en"])
    btn = _VERIFY_BTN.get(lang, _VERIFY_BTN["en"])
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
              <p style="margin:0;font-size:13px;line-height:1.5;color:#64748b;">Norya — Güvenilir kan tahlili analizi</p>
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

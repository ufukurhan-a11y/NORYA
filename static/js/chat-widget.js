/* NoryaAI Müşteri İletişim Merkezi — Chat Widget */
(function () {
  'use strict';

  var CHAT_API = '/api/chat';
  var WA_NUMBER = '905071703564';

  var T = {
    tr: {
      title: 'Müşteri İletişim Merkezi',
      status: 'Lisa · Genellikle saniyeler içinde yanıt verir',
      placeholder: 'Mesajınızı yazın…',
      welcome: 'Merhaba, ben Lisa! 👋 NoryaAI müşteri temsilcinizim. Size nasıl yardımcı olabilirim?',
      wa: 'Canlı destek ile görüşün',
      error: 'Bağlantı hatası, lütfen tekrar deneyin.',
      quick_home: ['Nasıl çalışır?', 'Fiyatlar ne kadar?', 'Verilerim güvende mi?', 'Hangi dilleri destekliyorsunuz?'],
      quick_pricing: ['Ödeme güvenli mi?', 'Hangi kartlar geçerli?', 'İade politikası nedir?', 'İndirim kodum var'],
      quick_payment: ['Ödeme güvenli mi?', 'Hesap açmam gerekiyor mu?', 'Fatura kesiliyor mu?', 'İade talebi nasıl yaparım?']
    },
    en: {
      title: 'Customer Support Center',
      status: 'Lisa · Typically replies in seconds',
      placeholder: 'Type your message…',
      welcome: 'Hi, I\'m Lisa! 👋 I\'m your NoryaAI customer representative. How can I help you?',
      wa: 'Talk to live support',
      error: 'Connection error, please try again.',
      quick_home: ['How does it work?', 'What are the prices?', 'Is my data secure?', 'Which languages do you support?'],
      quick_pricing: ['Is payment secure?', 'Which cards are accepted?', 'What is the refund policy?', 'I have a discount code'],
      quick_payment: ['Is payment secure?', 'Do I need an account?', 'Will I get an invoice?', 'How do I request a refund?']
    },
    de: {
      title: 'Kundensupport',
      status: 'Lisa · Antwortet in Sekunden',
      placeholder: 'Nachricht eingeben…',
      welcome: 'Hallo, ich bin Lisa! 👋 Ich bin Ihre NoryaAI-Kundenbetreuerin. Wie kann ich Ihnen helfen?',
      wa: 'Live-Support kontaktieren',
      error: 'Verbindungsfehler, bitte versuchen Sie es erneut.',
      quick_home: ['Wie funktioniert es?', 'Was kostet es?', 'Sind meine Daten sicher?', 'Welche Sprachen werden unterstützt?'],
      quick_pricing: ['Ist die Zahlung sicher?', 'Welche Karten werden akzeptiert?', 'Rückerstattungsrichtlinie?', 'Ich habe einen Rabattcode'],
      quick_payment: ['Ist die Zahlung sicher?', 'Brauche ich ein Konto?', 'Erhalte ich eine Rechnung?', 'Wie beantrage ich eine Rückerstattung?']
    },
    fr: {
      title: 'Centre d\'assistance',
      status: 'Lisa · Répond en quelques secondes',
      placeholder: 'Écrivez votre message…',
      welcome: 'Bonjour, je suis Lisa ! 👋 Je suis votre conseillère NoryaAI. Comment puis-je vous aider ?',
      wa: 'Contacter le support',
      error: 'Erreur de connexion, veuillez réessayer.',
      quick_home: ['Comment ça marche ?', 'Quels sont les prix ?', 'Mes données sont-elles sécurisées ?', 'Quelles langues supportez-vous ?'],
      quick_pricing: ['Le paiement est-il sécurisé ?', 'Quelles cartes sont acceptées ?', 'Politique de remboursement ?', 'J\'ai un code promo'],
      quick_payment: ['Le paiement est-il sécurisé ?', 'Ai-je besoin d\'un compte ?', 'Vais-je recevoir une facture ?', 'Comment demander un remboursement ?']
    },
    es: {
      title: 'Centro de atención',
      status: 'Lisa · Responde en segundos',
      placeholder: 'Escribe tu mensaje…',
      welcome: '¡Hola, soy Lisa! 👋 Soy tu representante de NoryaAI. ¿Cómo puedo ayudarte?',
      wa: 'Hablar con soporte',
      error: 'Error de conexión, inténtelo de nuevo.',
      quick_home: ['¿Cómo funciona?', '¿Cuáles son los precios?', '¿Mis datos están seguros?', '¿Qué idiomas soportan?'],
      quick_pricing: ['¿El pago es seguro?', '¿Qué tarjetas aceptan?', '¿Política de reembolso?', 'Tengo un código de descuento'],
      quick_payment: ['¿El pago es seguro?', '¿Necesito una cuenta?', '¿Recibiré una factura?', '¿Cómo solicito un reembolso?']
    },
    it: {
      title: 'Centro assistenza',
      status: 'Lisa · Risponde in pochi secondi',
      placeholder: 'Scrivi il tuo messaggio…',
      welcome: 'Ciao, sono Lisa! 👋 Sono la tua assistente NoryaAI. Come posso aiutarti?',
      wa: 'Contatta il supporto',
      error: 'Errore di connessione, riprova.',
      quick_home: ['Come funziona?', 'Quali sono i prezzi?', 'I miei dati sono al sicuro?', 'Quali lingue supportate?'],
      quick_pricing: ['Il pagamento è sicuro?', 'Quali carte accettate?', 'Politica di rimborso?', 'Ho un codice sconto'],
      quick_payment: ['Il pagamento è sicuro?', 'Ho bisogno di un account?', 'Riceverò una fattura?', 'Come richiedere un rimborso?']
    },
    he: {
      title: 'מרכז שירות לקוחות',
      status: 'Lisa · משיבה תוך שניות',
      placeholder: 'כתוב את ההודעה שלך…',
      welcome: 'שלום, אני ליסה! 👋 אני נציגת השירות של NoryaAI. איך אוכל לעזור לך?',
      wa: 'דבר עם תמיכה',
      error: 'שגיאת חיבור, נסה שוב.',
      quick_home: ['איך זה עובד?', 'מה המחירים?', 'האם הנתונים שלי מאובטחים?', 'אילו שפות נתמכות?'],
      quick_pricing: ['האם התשלום מאובטח?', 'אילו כרטיסים מתקבלים?', 'מדיניות החזרים?', 'יש לי קוד הנחה'],
      quick_payment: ['האם התשלום מאובטח?', 'האם אני צריך חשבון?', 'האם אקבל חשבונית?', 'איך מבקשים החזר?']
    },
    hi: {
      title: 'ग्राहक सहायता केंद्र',
      status: 'Lisa · आमतौर पर सेकंड में जवाब देती है',
      placeholder: 'अपना संदेश लिखें…',
      welcome: 'नमस्ते, मैं Lisa हूँ! 👋 मैं आपकी NoryaAI ग्राहक प्रतिनिधि हूँ। मैं आपकी कैसे मदद कर सकती हूँ?',
      wa: 'लाइव सपोर्ट से बात करें',
      error: 'कनेक्शन त्रुटि, कृपया पुनः प्रयास करें।',
      quick_home: ['यह कैसे काम करता है?', 'कीमतें क्या हैं?', 'क्या मेरा डेटा सुरक्षित है?', 'कौन सी भाषाएँ समर्थित हैं?'],
      quick_pricing: ['क्या भुगतान सुरक्षित है?', 'कौन से कार्ड स्वीकार किए जाते हैं?', 'रिफंड नीति?', 'मेरे पास डिस्काउंट कोड है'],
      quick_payment: ['क्या भुगतान सुरक्षित है?', 'क्या मुझे अकाउंट चाहिए?', 'क्या मुझे इनवॉइस मिलेगा?', 'रिफंड कैसे मांगें?']
    },
    ar: {
      title: 'مركز دعم العملاء',
      status: 'Lisa · ترد عادة في ثوانٍ',
      placeholder: 'اكتب رسالتك…',
      welcome: 'مرحباً، أنا ليسا! 👋 أنا ممثلة خدمة عملاء NoryaAI. كيف يمكنني مساعدتك؟',
      wa: 'تحدث مع الدعم المباشر',
      error: 'خطأ في الاتصال، يرجى المحاولة مرة أخرى.',
      quick_home: ['كيف يعمل؟', 'ما هي الأسعار؟', 'هل بياناتي آمنة؟', 'ما اللغات المدعومة؟'],
      quick_pricing: ['هل الدفع آمن؟', 'ما البطاقات المقبولة؟', 'سياسة الاسترداد؟', 'لدي رمز خصم'],
      quick_payment: ['هل الدفع آمن؟', 'هل أحتاج حساب؟', 'هل سأحصل على فاتورة؟', 'كيف أطلب استرداد؟']
    }
  };

  function detectLocale() {
    var htmlLang = (document.documentElement.lang || '').toLowerCase().split('-')[0];
    if (T[htmlLang]) return htmlLang;
    var cookie = (document.cookie.match(/norya_lang=([^;]+)/) || [])[1];
    if (cookie && T[cookie]) return cookie;
    var navLang = (navigator.language || '').toLowerCase().split('-')[0];
    if (T[navLang]) return navLang;
    return 'en';
  }

  function detectPage() {
    var path = window.location.pathname.toLowerCase();
    if (path.indexOf('/pricing') !== -1) return 'pricing';
    if (path.indexOf('/payment') !== -1 || path.indexOf('/pay') !== -1) return 'payment';
    return 'homepage';
  }

  function getQuickQuestions(t, page) {
    if (page === 'pricing') return t.quick_pricing;
    if (page === 'payment') return t.quick_payment;
    return t.quick_home;
  }

  function escapeHtml(str) {
    var div = document.createElement('div');
    div.appendChild(document.createTextNode(str));
    return div.innerHTML;
  }

  function formatReply(text) {
    text = escapeHtml(text);
    text = text.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
    text = text.replace(/\[([^\]]+)\]\((https?:\/\/[^)]+)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>');
    text = text.replace(/(https?:\/\/[^\s<]+)/g, function (m) {
      if (m.indexOf('href="') !== -1) return m;
      return '<a href="' + m + '" target="_blank" rel="noopener">' + m + '</a>';
    });
    text = text.replace(/\n/g, '<br>');
    return text;
  }

  function buildWidget() {
    var locale = detectLocale();
    var page = detectPage();
    var t = T[locale] || T.en;
    var history = [];
    var isOpen = false;

    var existingWa = document.querySelector('.wa-float, .whatsapp-fab');
    if (existingWa) existingWa.style.display = 'none';

    var btn = document.createElement('button');
    btn.className = 'norya-chat-btn';
    btn.setAttribute('aria-label', t.title);
    btn.innerHTML =
      '<svg class="norya-chat-open-icon" viewBox="0 0 24 24"><path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm0 14H5.17L4 17.17V4h16v12z"/><path d="M7 9h2v2H7zm4 0h2v2h-2zm4 0h2v2h-2z"/></svg>' +
      '<svg class="norya-chat-close-icon" viewBox="0 0 24 24"><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/></svg>' +
      '<span class="norya-chat-badge"></span>';

    var panel = document.createElement('div');
    panel.className = 'norya-chat-panel';
    panel.innerHTML =
      '<div class="norya-chat-header">' +
        '<div class="norya-chat-header-avatar"><img src="/static/images/lisa-avatar.png" alt="Lisa" width="44" height="44"></div>' +
        '<div class="norya-chat-header-info">' +
          '<div class="norya-chat-header-title">' + escapeHtml(t.title) + '</div>' +
          '<div class="norya-chat-header-status">' + escapeHtml(t.status) + '</div>' +
        '</div>' +
      '</div>' +
      '<div class="norya-chat-messages" id="norya-chat-messages"></div>' +
      '<div class="norya-chat-quick" id="norya-chat-quick"></div>' +
      '<div class="norya-chat-input-area">' +
        '<textarea class="norya-chat-input" id="norya-chat-input" rows="1" placeholder="' + escapeHtml(t.placeholder) + '"></textarea>' +
        '<button class="norya-chat-send" id="norya-chat-send" aria-label="Send"><svg viewBox="0 0 24 24"><path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/></svg></button>' +
      '</div>' +
      '<a class="norya-chat-wa-link" href="https://wa.me/' + WA_NUMBER + '?text=' + encodeURIComponent('Merhaba NoryaAI') + '" target="_blank" rel="noopener">' +
        '<svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>' +
        '<span>' + escapeHtml(t.wa) + '</span>' +
      '</a>';

    document.body.appendChild(btn);
    document.body.appendChild(panel);

    var msgContainer = document.getElementById('norya-chat-messages');
    var quickContainer = document.getElementById('norya-chat-quick');
    var input = document.getElementById('norya-chat-input');
    var sendBtn = document.getElementById('norya-chat-send');

    function addMessage(role, text) {
      var div = document.createElement('div');
      div.className = 'norya-chat-msg norya-chat-msg-' + role;
      div.innerHTML = role === 'assistant' ? formatReply(text) : escapeHtml(text);
      msgContainer.appendChild(div);
      msgContainer.scrollTop = msgContainer.scrollHeight;
      return div;
    }

    function showTyping() {
      var div = document.createElement('div');
      div.className = 'norya-chat-typing';
      div.id = 'norya-chat-typing';
      div.innerHTML = '<span></span><span></span><span></span>';
      msgContainer.appendChild(div);
      msgContainer.scrollTop = msgContainer.scrollHeight;
    }

    function hideTyping() {
      var el = document.getElementById('norya-chat-typing');
      if (el) el.remove();
    }

    function renderQuickQuestions() {
      var questions = getQuickQuestions(t, page);
      quickContainer.innerHTML = '';
      questions.forEach(function (q) {
        var b = document.createElement('button');
        b.type = 'button';
        b.textContent = q;
        b.addEventListener('click', function () { sendMessage(q); });
        quickContainer.appendChild(b);
      });
    }

    function sendMessage(text) {
      if (!text || !text.trim()) return;
      text = text.trim();

      addMessage('user', text);
      history.push({ role: 'user', content: text });
      quickContainer.style.display = 'none';

      input.value = '';
      input.style.height = 'auto';
      sendBtn.disabled = true;
      showTyping();

      fetch(CHAT_API, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          message: text,
          history: history.slice(0, -1),
          locale: locale,
          page: page
        })
      })
        .then(function (res) { return res.json(); })
        .then(function (data) {
          hideTyping();
          sendBtn.disabled = false;
          if (data.reply) {
            addMessage('assistant', data.reply);
            history.push({ role: 'assistant', content: data.reply });
          } else if (data.error) {
            addMessage('assistant', data.error);
          }
          try { sessionStorage.setItem('norya_chat_history', JSON.stringify(history)); } catch (e) {}
        })
        .catch(function () {
          hideTyping();
          sendBtn.disabled = false;
          addMessage('assistant', t.error);
        });
    }

    function toggleChat() {
      isOpen = !isOpen;
      panel.classList.toggle('open', isOpen);
      btn.classList.toggle('open', isOpen);
      if (isOpen) {
        if (msgContainer.children.length === 0) {
          try {
            var saved = sessionStorage.getItem('norya_chat_history');
            if (saved) {
              var parsed = JSON.parse(saved);
              if (Array.isArray(parsed) && parsed.length > 0) {
                history = parsed;
                addMessage('assistant', t.welcome);
                parsed.forEach(function (m) { addMessage(m.role, m.content); });
                quickContainer.style.display = 'none';
              } else {
                addMessage('assistant', t.welcome);
                renderQuickQuestions();
              }
            } else {
              addMessage('assistant', t.welcome);
              renderQuickQuestions();
            }
          } catch (e) {
            addMessage('assistant', t.welcome);
            renderQuickQuestions();
          }
        }
        setTimeout(function () { input.focus(); }, 300);
      }
    }

    btn.addEventListener('click', toggleChat);

    sendBtn.addEventListener('click', function () { sendMessage(input.value); });

    input.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage(input.value);
      }
    });

    input.addEventListener('input', function () {
      this.style.height = 'auto';
      this.style.height = Math.min(this.scrollHeight, 80) + 'px';
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && isOpen) toggleChat();
    });

    if (typeof gtag === 'function') {
      btn.addEventListener('click', function () {
        if (isOpen) gtag('event', 'chat_open', { event_category: 'engagement', page: page });
      });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', buildWidget);
  } else {
    buildWidget();
  }
})();

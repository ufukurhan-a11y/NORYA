#!/usr/bin/env python3
"""Premium corporate proposal PDF for Interlab Kosovo - Turkish, 2 pages."""
import sys
sys.path.insert(0, "/tmp/norya_pdf_venv/lib/python3.14/site-packages")

from fpdf import FPDF

BRAND = (14, 165, 164)
DARK = (30, 40, 55)
MID = (80, 90, 105)
LIGHT = (140, 150, 165)
BG = (248, 250, 252)
WHITE = (255, 255, 255)
LINE = (220, 225, 230)

class Proposal(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=False)
        self.add_font("Inter", "", "/Library/Fonts/Arial Unicode.ttf", uni=True)
        self.add_font("Inter", "B", "/Library/Fonts/Arial Unicode.ttf", uni=True)
        self.set_font("Inter", "", 10)

    def header(self):
        pass

    def footer(self):
        pass

    def accent_line(self, w=40):
        self.set_draw_color(*BRAND)
        self.set_line_width(0.6)
        self.cell(w, 0.5, "", border="B")
        self.ln(5)

    def section_head(self, title):
        self.set_font("Inter", "B", 12)
        self.set_text_color(*DARK)
        self.cell(0, 6, title)
        self.ln(1)
        self.accent_line(w=35)

    def body(self, text, size=9):
        self.set_font("Inter", "", size)
        self.set_text_color(*MID)
        self.multi_cell(0, 4.5, text)

    def bullet(self, text):
        start_x = self.get_x()
        self.set_font("Inter", "", 8.5)
        self.set_text_color(*MID)
        self.set_x(start_x + 3)
        self.cell(4, 4, "-")
        remaining = self.w - self.get_x() - self.r_margin
        self.multi_cell(remaining, 4, text)
        self.set_x(start_x)

    def card(self, x, y, w, h, title, price, desc, items, featured=False):
        if featured:
            self.set_fill_color(*BRAND)
            self.set_draw_color(*BRAND)
        else:
            self.set_fill_color(*WHITE)
            self.set_draw_color(*LINE)
        self.set_line_width(0.3)
        self.rect(x, y, w, h, style="DF")
        self.set_xy(x + 4, y + 4)
        self.set_font("Inter", "B", 8.5)
        self.set_text_color(*(WHITE if featured else DARK))
        self.multi_cell(w - 8, 4, title)
        self.set_xy(x + 4, y + 12)
        self.set_font("Inter", "B", 13)
        self.set_text_color(*(WHITE if featured else BRAND))
        self.cell(w - 8, 6, price)
        self.set_xy(x + 4, y + 21)
        self.set_font("Inter", "", 7)
        self.set_text_color(*(WHITE if featured else LIGHT))
        self.multi_cell(w - 8, 3.2, desc)
        item_y = y + 36
        self.set_xy(x + 4, item_y)
        self.set_font("Inter", "", 7)
        self.set_text_color(*(WHITE if featured else MID))
        for item in items:
            self.cell(w - 8, 3.5, f"- {item}")
            self.ln()

def generate():
    pdf = Proposal()
    LOGO_FULL = "/Users/ufukurhan/norya/static/norya_logo_transparent_trim.png"
    LOGO_ICON = "/Users/ufukurhan/norya/static/norya_logo_report.png"

    # PAGE 1
    pdf.add_page()
    pdf.set_fill_color(*BRAND)
    pdf.rect(0, 0, 210, 3, style="F")
    pdf.image(LOGO_FULL, x=25, y=12, w=45)
    pdf.set_xy(25, 42)
    pdf.set_font("Inter", "B", 24)
    pdf.set_text_color(*DARK)
    pdf.cell(0, 10, "Ticari Teklif")
    pdf.set_xy(25, 54)
    pdf.set_font("Inter", "", 12)
    pdf.set_text_color(*BRAND)
    pdf.cell(0, 7, "NoryaAI x Interlab")
    pdf.set_xy(25, 63)
    pdf.set_font("Inter", "", 9)
    pdf.set_text_color(*MID)
    pdf.multi_cell(160, 4.5, "Rutin kan tahlili sonuçlarının hastalar için daha anlaşılır, daha düzenli ve daha hasta dostu sunumu için iş birliği önerisi")
    pdf.set_draw_color(*LINE)
    pdf.set_line_width(0.3)
    pdf.line(25, 80, 185, 80)
    pdf.set_xy(25, 86)
    pdf.section_head("Yönetici Özeti")
    pdf.set_xy(25, 96)
    pdf.body("NoryaAI, rutin kan tahlili sonuçlarının hastalar açısından daha anlaşılır hale gelmesini destekleyen, daha düzenli ve profesyonel sonuç sunumu sağlayan bir dijital sağlık çözümüdür.")
    pdf.ln(1)
    pdf.body("Interlab için bu çözüm; hasta iletişimi, sonuç açıklığı, modern raporlama deneyimi ve kurumsal sunum kalitesi açısından değer oluşturabilir. NoryaAI, doktorların veya laboratuvar uzmanlarının yerini almaz; klinik iş akışını bozmadan, hasta iletişimini güçlendirmeyi amaçlayan bir destek katmanı olarak konumlanır.")
    pdf.set_xy(25, 135)
    pdf.section_head("Interlab İçin Değer Önerisi")
    pdf.set_xy(25, 145)
    pdf.bullet("Hastalar için daha anlaşılır sonuç iletişimi")
    pdf.bullet("Daha düzenli ve profesyonel sonuç sunumu")
    pdf.bullet("Çok dilli hasta iletişimine uygun yapı")
    pdf.bullet("Kurumsal marka algısını güçlendiren raporlama deneyimi")
    pdf.bullet("Klinik iş akışını bozmadan değer üretme")
    pdf.set_draw_color(*LINE)
    pdf.set_line_width(0.3)
    pdf.line(25, 175, 185, 175)
    pdf.set_xy(25, 180)
    pdf.set_font("Inter", "", 8)
    pdf.set_text_color(*LIGHT)
    pdf.cell(0, 4, "Hazırlayan: Ufuk Urhan, NoryaAI")
    pdf.ln(4)
    pdf.cell(0, 4, "support@noryaai.com  |  +90 507 170 35 64  |  noryaai.com")
    pdf.ln(4)
    pdf.cell(0, 4, "15 Nisan 2026")
    pdf.set_y(275)
    pdf.set_fill_color(*BRAND)
    pdf.rect(0, 275, 210, 3, style="F")

    # PAGE 2
    pdf.add_page()
    pdf.set_fill_color(*BRAND)
    pdf.rect(0, 0, 210, 3, style="F")
    pdf.image(LOGO_ICON, x=175, y=10, w=18)
    pdf.set_xy(25, 12)
    pdf.section_head("Önerilen İş Birliği Paketleri")
    card_w = 50
    card_h = 100
    card_gap = 5
    start_x = 25
    pdf.card(start_x, 26, card_w, card_h, "Standart İş Birliği", "2.000 EUR / ay", "Rutin test sonuçlarının daha anlaşılır ve profesyonel şekilde sunulması için güçlü başlangıç çözümü.", ["Hasta dostu sonuç sunumu", "Markalı rapor yapısı", "Anlaşılır açıklama katmanı", "Çok dilli raporlama", "Temel onboarding", "Uzaktan destek", "Kullanım değerlendirmesi"])
    pdf.card(start_x + card_w + card_gap, 26, card_w, card_h, "Kurumsal İş Birliği", "3.500 EUR / ay", "Daha yüksek hasta deneyimi standardı, güçlü marka uyumu ve kapsamlı kurumsal kullanım için gelişmiş model.", ["Gelişmiş markalama", "Güçlü çok dilli yapı", "Öncelikli destek", "Kuruma özel danışmanlık", "Premium rapor deneyimi", "Periyodik değerlendirme", "Gelişmiş onboarding"], featured=True)
    pdf.card(start_x + (card_w + card_gap) * 2, 26, card_w, card_h, "Ön Ödemeli Kredi", "Özel Fiyatlandırma", "Sabit aylık yapı yerine esnek ve kontrollü kullanım tercih eden kurumlar için uygun model.", ["Toplu kredi satışı", "İhtiyaca göre kullanım", "Sabit aylık yük yok", "Esnek yönetim", "Kurumsal faturalandırma", "Kullanım takibi", "Özel fiyatlandırma"])
    pdf.set_xy(25, 133)
    pdf.set_font("Inter", "", 8)
    pdf.set_text_color(*LIGHT)
    pdf.multi_cell(160, 4, "Talep halinde, sabit aylık yapı yerine ön ödemeli kredi modeli de sunulabilir. Bu modelde kurum, belirli sayıda kullanım kredisini toplu olarak satın alır ve ihtiyaç oldukça kullanır.")
    pdf.set_xy(25, 150)
    pdf.set_fill_color(*BG)
    pdf.set_draw_color(*LINE)
    pdf.set_line_width(0.3)
    pdf.rect(25, 150, 160, 28, style="DF")
    pdf.set_xy(30, 154)
    pdf.set_font("Inter", "B", 8.5)
    pdf.set_text_color(*DARK)
    pdf.cell(0, 4.5, "Yaklaşımımız")
    pdf.set_xy(30, 161)
    pdf.set_font("Inter", "", 8)
    pdf.set_text_color(*MID)
    pdf.cell(0, 3.8, "Doktorların ve laboratuvar profesyonellerinin yerini almaz")
    pdf.ln(3.8)
    pdf.cell(0, 3.8, "Tıbbi karar süreçlerine saygılıdır")
    pdf.ln(3.8)
    pdf.cell(0, 3.8, "Hasta iletişimini güçlendirmeyi amaçlayarak konumlanır")
    pdf.ln(3.8)
    pdf.cell(0, 3.8, "Profesyonel sunum ve veri gizliliği odaklıdır")
    pdf.set_xy(25, 185)
    pdf.section_head("Sonraki Adımlar")
    pdf.set_xy(25, 195)
    steps = ["Kısa tanışma görüşmesi", "Örnek rapor paylaşımı", "Uygun iş birliği modelinin belirlenmesi", "Başlangıç planlaması"]
    for i, step in enumerate(steps, 1):
        pdf.set_x(25)
        pdf.set_font("Inter", "B", 8.5)
        pdf.set_text_color(*BRAND)
        pdf.cell(7, 4.5, f"{i}.")
        pdf.set_font("Inter", "", 8.5)
        pdf.set_text_color(*MID)
        pdf.cell(0, 4.5, step)
        pdf.ln(4.5)
    pdf.set_draw_color(*LINE)
    pdf.set_line_width(0.3)
    pdf.line(25, 220, 185, 220)
    pdf.set_xy(25, 225)
    pdf.set_font("Inter", "", 7.5)
    pdf.set_text_color(*LIGHT)
    pdf.cell(0, 4, "Bu teklif 30 gün geçerlidir. Tüm fiyatlar EUR cinsindendir ve geçerli vergiler hariçtir.")
    pdf.ln(4)
    pdf.cell(0, 4, "support@noryaai.com  |  +90 507 170 35 64  |  noryaai.com")
    pdf.set_y(275)
    pdf.set_fill_color(*BRAND)
    pdf.rect(0, 275, 210, 3, style="F")

    output = "/Users/ufukurhan/norya/docs/INTERLAB-KOSOVO-TEKLIF.pdf"
    pdf.output(output)
    print(f"PDF olusturuldu: {output}")

if __name__ == "__main__":
    generate()
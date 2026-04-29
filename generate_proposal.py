#!/usr/bin/env python3
"""Generate premium PDF proposal for Interlab Kosovo."""
import os
import sys

# Add venv to path
sys.path.insert(0, "/tmp/norya_pdf_venv/lib/python3.14/site-packages")

from fpdf import FPDF
from datetime import datetime

class ProposalPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=20)
        # Colors
        self.PRIMARY = (15, 76, 129)      # Deep blue
        self.ACCENT = (0, 150, 136)       # Teal
        self.DARK = (33, 33, 33)          # Dark gray
        self.LIGHT_BG = (245, 248, 250)   # Light bg
        self.WHITE = (255, 255, 255)
        self.GOLD = (194, 154, 20)        # Gold accent

    def header(self):
        if self.page_no() > 1:
            self.set_font("Helvetica", "", 8)
            self.set_text_color(120, 120, 120)
            self.cell(0, 10, "NoryaAI - Interlab Kosovo Proposal | Confidential", align="R")
            self.ln(15)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def section_title(self, title):
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(*self.PRIMARY)
        self.ln(4)
        self.cell(0, 10, title)
        self.ln(2)
        self.set_draw_color(*self.ACCENT)
        self.set_line_width(0.5)
        self.cell(60, 0.5, "", border="B")
        self.ln(8)

    def subsection_title(self, title):
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(*self.DARK)
        self.ln(2)
        self.cell(0, 8, title)
        self.ln(6)

    def body_text(self, text):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(60, 60, 60)
        self.multi_cell(0, 5.5, text)
        self.ln(2)

    def bullet(self, text, indent=10):
        start_x = self.get_x()
        self.set_font("Helvetica", "", 10)
        self.set_text_color(60, 60, 60)
        self.set_x(start_x + indent)
        self.cell(5, 5.5, chr(149), align="L")
        remaining_w = self.w - self.get_x() - self.r_margin
        self.multi_cell(remaining_w, 5.5, text)
        self.set_x(start_x)

    def numbered_item(self, num, text):
        start_x = self.get_x()
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(*self.ACCENT)
        self.cell(10, 5.5, f"{num}.", align="L")
        self.set_font("Helvetica", "", 10)
        self.set_text_color(60, 60, 60)
        remaining_w = self.w - self.get_x() - self.r_margin
        self.multi_cell(remaining_w, 5.5, text)
        self.set_x(start_x)

    def metric_box(self, value, label):
        x = self.get_x()
        y = self.get_y()
        # Box background
        self.set_fill_color(*self.LIGHT_BG)
        self.set_draw_color(220, 220, 220)
        self.rect(x, y, 55, 22, style="DF")
        # Value
        self.set_xy(x, y + 3)
        self.set_font("Helvetica", "B", 16)
        self.set_text_color(*self.PRIMARY)
        self.cell(55, 8, value, align="C")
        # Label
        self.set_xy(x, y + 12)
        self.set_font("Helvetica", "", 8)
        self.set_text_color(100, 100, 100)
        self.multi_cell(55, 4, label, align="C")
        self.set_xy(x + 60, y)

    def pricing_card(self, name, price, features, is_featured=False):
        x = self.get_x()
        y = self.get_y()
        card_h = 75

        if is_featured:
            self.set_fill_color(*self.PRIMARY)
            self.set_draw_color(*self.PRIMARY)
        else:
            self.set_fill_color(*self.LIGHT_BG)
            self.set_draw_color(200, 200, 200)

        self.rect(x, y, 60, card_h, style="DF")

        # Name
        self.set_xy(x + 3, y + 4)
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(*self.WHITE if is_featured else self.DARK)
        self.cell(54, 6, name, align="C")

        # Price
        self.set_xy(x + 3, y + 13)
        self.set_font("Helvetica", "B", 18)
        self.set_text_color(*self.WHITE if is_featured else self.PRIMARY)
        self.cell(54, 10, price, align="C")

        # Features
        self.set_xy(x + 3, y + 26)
        self.set_font("Helvetica", "", 8)
        self.set_text_color(*self.WHITE if is_featured else (80, 80, 80))
        for feat in features:
            self.cell(54, 5, f"  {chr(149)} {feat}")
            self.ln()

        self.set_y(y + card_h + 3)

def generate_proposal():
    pdf = ProposalPDF()
    pdf.add_page()

    # ========== COVER PAGE ==========
    # Dark header bar
    pdf.set_fill_color(*pdf.PRIMARY)
    pdf.rect(0, 0, 210, 55, style="F")

    # NoryaAI title
    pdf.set_xy(20, 15)
    pdf.set_font("Helvetica", "B", 28)
    pdf.set_text_color(*pdf.WHITE)
    pdf.cell(0, 12, "NoryaAI")

    pdf.set_xy(20, 28)
    pdf.set_font("Helvetica", "", 12)
    pdf.set_text_color(200, 220, 240)
    pdf.cell(0, 8, "AI-Powered Patient-Friendly Lab Reports")

    # Proposal title
    pdf.set_xy(20, 65)
    pdf.set_font("Helvetica", "B", 22)
    pdf.set_text_color(*pdf.PRIMARY)
    pdf.cell(0, 12, "Business Proposal")

    pdf.set_xy(20, 78)
    pdf.set_font("Helvetica", "", 14)
    pdf.set_text_color(*pdf.ACCENT)
    pdf.cell(0, 10, "For Interlab Kosovo")

    # Divider
    pdf.set_draw_color(*pdf.ACCENT)
    pdf.set_line_width(0.8)
    pdf.line(20, 95, 190, 95)

    # Date and prepared by
    pdf.set_xy(20, 105)
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(80, 80, 80)
    today = datetime.now().strftime("%B %d, %Y")
    pdf.cell(0, 7, f"Prepared: {today}")
    pdf.ln(6)
    pdf.cell(0, 7, "Prepared by: Ufuk Urhan, NoryaAI")
    pdf.ln(6)
    pdf.cell(0, 7, "support@noryaai.com | +90 507 170 35 64")

    # Bottom accent bar
    pdf.set_fill_color(*pdf.ACCENT)
    pdf.rect(0, 270, 210, 5, style="F")

    # ========== PAGE 2: EXECUTIVE SUMMARY ==========
    pdf.add_page()

    pdf.section_title("Executive Summary")

    pdf.body_text(
        "NoryaAI is an AI-powered platform that transforms standard laboratory blood test "
        "results into clear, patient-friendly reports. We help laboratories and hospitals "
        "communicate results more effectively, reducing patient confusion and improving "
        "overall satisfaction."
    )
    pdf.ln(3)

    pdf.subsection_title("Why Interlab Kosovo?")
    pdf.body_text(
        "Interlab serves patients across Kosovo with comprehensive laboratory testing services. "
        "Many patients receive results they cannot fully understand, leading to unnecessary "
        "anxiety, repeat calls, and additional doctor visits. NoryaAI addresses this gap by "
        "providing instant, easy-to-understand explanations for every biomarker."
    )
    pdf.ln(3)

    # Metrics row
    pdf.set_x(20)
    pdf.metric_box("2M+", "Reports Generated")
    pdf.metric_box("120+", "Hospitals & Clinics")
    pdf.metric_box("98.7%", "Classification Accuracy*")
    pdf.metric_box("9+", "Languages Supported")
    pdf.ln(28)

    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(120, 120, 120)
    pdf.cell(0, 5, "*Biomarker classification accuracy from internal platform evaluation")
    pdf.ln(8)

    # ========== PAGE 3: SOLUTION OVERVIEW ==========
    pdf.add_page()

    pdf.section_title("Solution Overview")

    pdf.subsection_title("How NoryaAI Works")
    pdf.numbered_item(1, "Patient or staff uploads lab results (text, PDF, or photo)")
    pdf.numbered_item(2, "AI analyzes every biomarker and generates plain-language explanations")
    pdf.numbered_item(3, "Structured report is created in the patient's preferred language")
    pdf.numbered_item(4, "Professional PDF report is delivered instantly with QR verification")
    pdf.ln(4)

    pdf.subsection_title("Key Capabilities")
    pdf.bullet("Upload support: text, PDF, or photo of lab results")
    pdf.bullet("AI analysis in 9+ languages (Albanian, English, Turkish, Serbian, and more)")
    pdf.bullet("Structured reports with clear explanations of each biomarker")
    pdf.bullet("PDF report generation with QR verification")
    pdf.bullet("White-label branding with Interlab logo and colors")
    pdf.bullet("API integration with existing Laboratory Information System")
    pdf.bullet("24/7 automated report generation")
    pdf.ln(4)

    pdf.subsection_title("Benefits for Interlab Kosovo")
    pdf.bullet("Reduce patient confusion - results explained in plain language")
    pdf.bullet("Lower support load - fewer clarification calls to your team")
    pdf.bullet("Improve patient satisfaction - professional, easy-to-read reports")
    pdf.bullet("Differentiate from competitors - AI-enhanced reporting as a premium service")
    pdf.bullet("Multi-language support for Kosovo's diverse patient population")
    pdf.ln(4)

    # ========== PAGE 4: PRICING ==========
    pdf.add_page()

    pdf.section_title("Pricing Plans")

    pdf.body_text(
        "We offer flexible pricing models tailored to your patient volume. "
        "All plans include full platform access, technical support, and regular updates."
    )
    pdf.ln(5)

    # Pricing cards
    pdf.set_x(15)

    starter_features = [
        "500 analyses/month",
        "3 languages",
        "Email support",
        "Standard reports",
        "Basic analytics"
    ]
    pdf.pricing_card("Starter", "EUR 299/mo", starter_features)

    pdf.set_x(80)
    pdf.set_y(pdf.get_y() - 75)
    pro_features = [
        "2,000 analyses/month",
        "5 languages",
        "Priority support",
        "White-label branding",
        "API integration",
        "Advanced analytics"
    ]
    pdf.pricing_card("Professional", "EUR 599/mo", pro_features, is_featured=True)

    pdf.set_x(145)
    pdf.set_y(pdf.get_y() - 75)
    enterprise_features = [
        "Unlimited analyses",
        "All 9+ languages",
        "Dedicated support",
        "Full white-label",
        "Custom API integration",
        "On-premise option",
        "SLA guarantee"
    ]
    pdf.pricing_card("Enterprise", "EUR 999/mo", enterprise_features)

    pdf.ln(10)

    # Pilot offer
    pdf.set_fill_color(240, 248, 255)
    pdf.set_draw_color(*pdf.ACCENT)
    pdf.set_line_width(0.3)
    pdf.rect(15, pdf.get_y(), 180, 30, style="DF")

    pdf.set_xy(20, pdf.get_y() + 5)
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(*pdf.ACCENT)
    pdf.cell(0, 7, "Free Pilot Program")

    pdf.set_xy(20, pdf.get_y() + 8)
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(0, 5,
        "200 free analyses over 30 days - Albanian, English, and Turkish language support. "
        "No commitment required. Evaluate the platform risk-free before making a decision."
    )

    # ========== PAGE 5: INTEGRATION & NEXT STEPS ==========
    pdf.add_page()

    pdf.section_title("Integration Options")

    pdf.subsection_title("Deployment Models")
    pdf.bullet("White-label: Interlab branding on all patient reports")
    pdf.bullet("API integration: Connect with your existing Laboratory Information System")
    pdf.bullet("Standalone portal: Patients upload results via a dedicated Interlab page")
    pdf.bullet("On-premise or cloud deployment available")
    pdf.ln(4)

    pdf.subsection_title("Technical Requirements")
    pdf.bullet("No special hardware required - cloud-based SaaS platform")
    pdf.bullet("RESTful API for seamless integration")
    pdf.bullet("GDPR-compliant data handling")
    pdf.bullet("99.9% uptime SLA (Enterprise plan)")
    pdf.ln(4)

    pdf.section_title("Next Steps")

    pdf.numbered_item(1, "Schedule a 15-minute introductory call with your management team")
    pdf.numbered_item(2, "Provide a live demo with sample Interlab-style reports")
    pdf.numbered_item(3, "Launch free pilot program (200 analyses, 30 days)")
    pdf.numbered_item(4, "Review pilot results and discuss long-term partnership")
    pdf.numbered_item(5, "Sign agreement and begin full integration")
    pdf.ln(6)

    pdf.subsection_title("Contact Information")
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(60, 60, 60)
    pdf.cell(0, 6, "Ufuk Urhan - NoryaAI")
    pdf.ln(5)
    pdf.cell(0, 6, "Email: support@noryaai.com")
    pdf.ln(5)
    pdf.cell(0, 6, "Phone/WhatsApp: +90 507 170 35 64")
    pdf.ln(5)
    pdf.cell(0, 6, "Website: noryaai.com")
    pdf.ln(8)

    pdf.set_font("Helvetica", "I", 9)
    pdf.set_text_color(120, 120, 120)
    pdf.multi_cell(0, 5,
        "This proposal is valid for 30 days from the date of issue. "
        "All prices are in EUR and exclude applicable taxes. "
        "Custom pricing available based on patient volume and specific requirements."
    )

    # Bottom accent bar
    pdf.set_y(270)
    pdf.set_fill_color(*pdf.ACCENT)
    pdf.rect(0, 270, 210, 5, style="F")

    # Save
    output_path = "/Users/ufukurhan/norya/docs/INTERLAB-KOSOVO-TEKLIF.pdf"
    pdf.output(output_path)
    print(f"PDF generated successfully: {output_path}")

if __name__ == "__main__":
    generate_proposal()
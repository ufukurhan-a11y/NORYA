# -*- coding: utf-8 -*-
"""German — full B2B audience pages."""

from __future__ import annotations

from typing import Any

from app.b2b_locales._builder import mk
from app.b2b_locales.faq import faq_for


def build_pages(pages_en: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
    f = faq_for("de")
    return {
        "for-doctors": mk(
            pages_en["for-doctors"],
            faq=f,
            faq_title="Häufig gestellte Fragen",
            patch={
                "meta_title": "Norya für Ärzt:innen | Laborklarheit in Minuten",
                "meta_description": "Assistierende Labor-zu-Sprache-Berichte: strukturierte Marker, einfache Sprache, prüfbereite Ausgaben in 9+ Sprachen.",
                "hero_badge": "Für Kliniker:innen",
                "hero_title": "Komplexe Labore patientenverständlich erklären—ohne Mehraufwand in der Verwaltung.",
                "hero_desc": "Norya verwandelt Standard-Laborexporte in zweisprachig vorbereitete, einfache Zusammenfassungen. Für Praxen mit hohem Laboraufkommen im Umfeld von über 4.000 Krankenhäusern und Kliniken in unserem Netzwerk.",
                "who_title": "Für wen das gedacht ist",
                "who_desc": "Hausärzt:innen, Fachärzt:innen und Hospitalisten mit Bedarf an schnellen, konsistenten Erklärungen heterogener Labore.",
                "who_primary": "Hochdurchsatz-Ambulanzen und Gruppenpraxen",
                "who_secondary": "Mehrsprachige Patientenpopulationen",
                "who_points": [
                    "Ambulante und stationäre Abläufe",
                    "Teams mit externen Laboren",
                ],
                "benefits_title": "Was Sie gewinnen",
                "benefits": [
                    {
                        "title": "Schnellere Beratungspunkte",
                        "desc": "Strukturierte Marker-Gruppen heben im Besuchskontext zuerst Relevantes hervor.",
                        "points": ["Triage-orientiertes Layout", "Weniger Diktat-Nacharbeit", "Einheitliche Formulierung zwischen Besuchen"],
                    },
                    {
                        "title": "Patientenreife Sprache",
                        "desc": "Alltagstaugliche Erklärungen zum Weitergeben oder für eigene Notizen.",
                        "points": ["9+ Berichtssprachen", "Zurückhaltende Formulierung", "Ärztliche Prüfung vorgesehen"],
                    },
                    {
                        "title": "Betriebliche Verlässlichkeit",
                        "desc": "Für Teams, die bereits über 2M+ Berichte über die Plattform erzeugen.",
                        "points": ["Prüffreundlicher Aufbau", "Enterprise-Sicherheitspfad", "Dediziertes Onboarding"],
                    },
                    {
                        "title": "Vertrauen und Governance",
                        "desc": "Als assistierende Dokumentation konzipiert—kein Diagnostikersatz.",
                        "points": ["Mensch in der Schleife", "Klare Grenzen im Text", "Auf Compliance-Gespräche ausgerichtet"],
                    },
                ],
                "workflow_title": "Von Rohdaten bis zur prüfbereiten Patientensprache",
                "workflow_steps": [
                    {"title": "Import", "desc": "Sichere Aufnahme von CSV/PDF-Exports oder API-gespeisten Daten."},
                    {"title": "Strukturieren", "desc": "Marker-Normalisierung mit 98,7 % Biomarker-Klassifikationsgenauigkeit in der internen Plattformbewertung."},
                    {"title": "Erklären", "desc": "Alltagstext mit klinischem Tonalitäts-Steuerung und mehrsprachigem Output."},
                    {"title": "Prüfen", "desc": "Ärztliche Freigabe, bevor Inhalte ins Portalsystem oder die Akte gehen."},
                ],
            },
        ),
        "for-clinics": mk(
            pages_en["for-clinics"],
            faq=f,
            faq_title="FAQ für Praxen",
            patch={
                "meta_title": "Norya für Kliniken | Operative Laborkommunikation",
                "meta_description": "Patientennahe Laborerklärungen über Anbieter, Sprachen und Schichten standardisieren—ohne zusätzliches Personal.",
                "hero_badge": "Für Kliniken",
                "hero_title": "Ein Betriebsrhythmus für die Laborkommunikation in jedem Zimmer der Praxis.",
                "hero_desc": "Norya bietet Klinikbetreibern eine Pipeline von Labor zu geprüften, mehrsprachigen Materialien. Gleiche Qualität vom Einzelstandort bis zu regionalen Netzen in über 50 Ländern.",
                "who_title": "Für klinische Betreiber",
                "who_desc": "Ärztliche Leitung, Operations und Versorgungsteams, die nach jedem Abgang modernisieren, wie Labor erklärt wird.",
                "who_primary": "Ambulante Netze mit vielen Leistungserbringern",
                "who_secondary": "Hochvolumen-Phlebotomie und schnelle Nachsorge",
                "who_points": ["CCM / Care-Coordination", "Betriebs- und Arbeitsmedizin-Panels"],
                "benefits_title": "Ergebnisse, die Verwaltung trackt",
                "benefits": [
                    {
                        "title": "Durchsatz ohne Burnout",
                        "desc": "Ersten Entwurf der Patientenedukation je Ergebnismuster automatisieren.",
                        "points": ["Vorlagen für Eskalation", "Schichtfähige Übergaben", "Weniger manuelle Korrektur"],
                    },
                    {
                        "title": "Markensichere Patientenstimme",
                        "desc": "Ton, Disclaimer und Glossar zentral festlegen.",
                        "points": ["9+ Berichtssprachen", "Versionierte Snippets", "Juristische Prüfpunkte"],
                    },
                    {
                        "title": "Transparenz für die Leitung",
                        "desc": "Dashboard-Metriken zu Durchlaufzeit ab Deckung der Sprachen.",
                        "points": ["Volumen-Telemetrie", "SLA-Ausrichtung", "Export für QI-Maßnahmen"],
                    },
                    {
                        "title": "Enterprise-Kontrollen",
                        "desc": "Security-Reviews entsprechen Krankenhaus-Compliance-Erwartungen.",
                        "points": ["SSO-Roadmap", "DPA-Vorlagen", "Dedizierter Success-Partner"],
                    },
                ],
                "workflow_title": "Workflow in Praxisgröße",
                "workflow_steps": [
                    {"title": "Eingang", "desc": "Weiterleitung von LIMS oder Stapel-Uploads mit Klinik-Metadaten."},
                    {"title": "Normalisieren", "desc": "Analysen und Einheiten über gemischte Feeds vereinheitlichen."},
                    {"title": "Generieren", "desc": "Mehrsprachige Entwürfe plus interne Notizen für Ärzt:innen."},
                    {"title": "Veröffentlichen", "desc": "Nach Prüfung an Portale, Druck bei Anmeldung oder sichere Nachrichten."},
                ],
            },
        ),
        "for-hospitals": mk(
            pages_en["for-hospitals"],
            faq=f,
            faq_title="FAQ für Krankenhausverbünde",
            patch={
                "meta_title": "Norya für Krankenhäuser | Enterprise AI Plattform für Laborintelligenz",
                "meta_description": "Transformieren Sie Ihr Krankenhaus mit KI-gestützter Laboranalyse. 12+ Sprachen, Echtzeit-Überwachung, HL7/FHIR-Integration. 2M+ Berichte, 4.000+ Krankenhäuser weltweit.",
                "hero_badge": "Enterprise AI Plattform",
                "hero_title": "Transformieren Sie Ihr Labor mit KI",
                "hero_desc": "NoryaAI Clinical Enterprise: Die Unternehmenslösung, die Laborergebnisse in strukturierte, mehrsprachige und nachverfolgbare Prä-Analyse-Unterstützung für Krankenhäuser verwandelt.",
                "who_title": "Vertraut von führenden Krankenhäusern",
                "who_desc": "CMIOs, CNIOs, Pathologie-Informatik und Klinikleiter in 50+ Ländern.",
                "who_primary": "Krankenhausgruppen & Ketten",
                "who_secondary": "Universitätskliniken & Spezialkliniken",
                "who_points": ["Hochvolumige Labordienstleistungen", "Multi-Campus-Operationen", "Internationale Patientendienste"],
                "features_title": "Premium Enterprise-Funktionen",
                "pricing_title": "Unternehmenslösungen",
                "pricing_desc": "Skalierbare Lösungen je nach Größe und Bedarf Ihres Krankenhauses",
                "pilot_title": "Starten Sie mit Pilot-Implementierung",
                "workflow_title": "Krankenhaus-Workflow",
                "faq_title": "FAQ für Krankenhausverbünde",
            },
        ),
        "enterprise-security": mk(
            pages_en["enterprise-security"],
            faq=f,
            faq_title="Sicherheits-FAQ",
            patch={
                "meta_title": "Enterprise-Sicherheit | Norya",
                "meta_description": "Verschlüsselung, Zugriffskontrollen und Beschaffungsunterlagen für Teams, die Noryas assistierende Labointelligenz einführen.",
                "hero_badge": "Sicherheit und Compliance",
                "hero_title": "Security-Architektur, die im Healthcare-Procurement besteht.",
                "hero_desc": "Norya ist für regulierte Umgebungen gebaut: gestufte Datenverarbeitung, Least-Privilege-Zugriff und Audit-Pfade passend zu ISO/SOC-Prüfzyklen im Krankenhaus.",
                "who_title": "Stakeholder, die wir unterstützen",
                "who_desc": "CISOs, Informationssicherheit in der Diagnostik und Einkaufsteams, die jedes Subsystem dokumentieren müssen.",
                "who_primary": "Gesundheitskonzerne",
                "who_secondary": "Diagnostische Dienstorganisationen",
                "who_points": ["Cloud- und Hybrid-Landschaften", "Multinationale Datenschutzprüfungen"],
                "benefits_title": "Kontrollbereiche",
                "benefits": [
                    {
                        "title": "Datenschutz",
                        "desc": "Verschlüsselung in Transit, begrenzte Aufbewahrung und regionale Verarbeitungsoptionen mit Ihrer Rechtsabteilung.",
                        "points": ["TLS 1.2+", "Key-Management-Leitfaden", "Konfigurierbare Löschfenster"],
                    },
                    {
                        "title": "Zugriffsgovernance",
                        "desc": "Enterprise-SSO, granulare Rollen und Session-Policies.",
                        "points": ["SAML/OIDC-Roadmap", "JIT-Bereitstellung", "Break-Glass-Verfahren"],
                    },
                    {
                        "title": "Nachweisdokumente",
                        "desc": "Security-Paket mit Architekturdiagrammen, Pen-Test-Summaries und Subprozessoren.",
                        "points": ["SOC2-Programm-Ausrichtung", "DPA-Vorlagen", "Incident-Response-Runbooks"],
                    },
                    {
                        "title": "Klinische Passung",
                        "desc": "Darstellung, wie assistive Outputs in der ärztlichen Schleife bleiben.",
                        "points": ["Risikoanalyse-Memos", "Clinical-Safety-Narratives", "FAQ für Legal"],
                    },
                ],
                "workflow_title": "Wie Reviews ablaufen",
                "workflow_steps": [
                    {"title": "NDA & Scoping", "desc": "Standardunterlagen und Abstimmung der Deployment-Topologie."},
                    {"title": "Architektur-Review", "desc": "Gemeinsamer Durchgang zu Datenflüssen, Verschlüsselung und Subprozessoren."},
                    {"title": "Pilot", "desc": "Begrenzte Produktion mit Logging und Monitoring."},
                    {"title": "Scale-Entscheid", "desc": "BAA/DPA und regionale Konfigurationen für den breiten Rollout."},
                ],
            },
        ),
        "clinical-demo": mk(
            pages_en["clinical-demo"],
            faq=f,
            faq_title="Demo-FAQ",
            patch={
                "meta_title": "Klinische Demo | Norya-Workflow",
                "meta_description": "Wie Labor in einem Durchlauf von strukturierten Daten zu mehrsprachigen, prüfbereiten Patientenerklärungen wird.",
                "hero_badge": "Geführte Evaluation",
                "hero_title": "Ein echter klinischer Ablauf—von der Labordatei bis zur unterzeichneten Patientenkopie.",
                "hero_desc": "In 30 Minuten mappen wir Ihre Lab-Feeds, Sprachen und Review-Modell auf die Norya-Pipeline in über 50 Ländern und 4.000+ Krankenhäusern und Kliniken.",
                "who_title": "Ideale Evaluationsteams",
                "who_desc": "Klinische Innovation, Labordirektor:innen und Digital-Health-Sponsoren, die assistive Tools validieren.",
                "who_primary": "Multidisziplinäre Lenkungsgremien",
                "who_secondary": "Qualität und Patienteneducation Owner",
                "who_points": ["Innovationsbudgets für FY-Planung", "Bedarf an mehrsprachigen Nachweisen"],
                "benefits_title": "Was Sie validieren",
                "benefits": [
                    {
                        "title": "Hands-on-Pipeline",
                        "desc": "Anonymisierte Samples laden und Struktur-, Erklärungs- und Review-Schritte sehen.",
                        "points": ["Genauigkeit der Gruppierung", "Sprachqualität", "Review-UX für Ärzt:innen"],
                    },
                    {
                        "title": "Metrik-Transparenz",
                        "desc": "Wir kontextualisieren 98,7 % Biomarker-Klassifikation aus interner Bewertung—keine Diagnoseclaims.",
                        "points": ["QA pro Biomarker", "Diskussion von Grenzfällen", "Roadmap für Ihre Analyten"],
                    },
                    {
                        "title": "Stakeholder-Kits",
                        "desc": "Mit Security-FAQ, klinischem Positionierungstext und Beschaffungspfaden.",
                        "points": ["Folienentwurf", "DPA-Checkliste", "Integrationsvoraussetzungen"],
                    },
                    {
                        "title": "Nächste Schritte",
                        "desc": "Pilotumfang, Lizenzierung und Erfolgskennzahlen in einer Session.",
                        "points": ["Volumenannahmen", "Lokalisierungsplan", "Schulungsansatz"],
                    },
                ],
                "workflow_title": "Demo-Verlauf",
                "workflow_steps": [
                    {"title": "Szenario", "desc": "Repräsentatives Panel und Patientenkontext wählen."},
                    {"title": "Import & Normalisierung", "desc": "Mapping aus Ihrem typischen Exportformat zeigen."},
                    {"title": "Generierung", "desc": "Mehrsprachige Entwürfe mit Review-Annotationen."},
                    {"title": "Fragen", "desc": "Offene Diskussion für Medizin, IT und Recht."},
                ],
            },
        ),
    }

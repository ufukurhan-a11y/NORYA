# -*- coding: utf-8 -*-
"""Italian — full B2B audience pages."""

from __future__ import annotations

from typing import Any

from app.b2b_locales._builder import mk
from app.b2b_locales.faq import faq_for


def build_pages(pages_en: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
    f = faq_for("it")
    return {
        "for-doctors": mk(
            pages_en["for-doctors"],
            faq=f,
            faq_title="Domande frequenti",
            patch={
                "meta_title": "Norya per medici | Chiarezza di laboratorio",
                "meta_description": "Report assistiti laboratorio-linguaggio: marker strutturati, linguaggio semplice, output pronto alla revisione in 9+ lingue.",
                "hero_badge": "Per clinici",
                "hero_title": "Spiegare laboratori complessi in linguaggio per il paziente—senza più tempo amministrativo.",
                "hero_desc": "Norya trasforma gli export di laboratorio in riassunti chiari e multilingue. Per studi ad alto volume nella rete di oltre 120 ospedali e cliniche.",
                "who_title": "A chi è rivolto",
                "who_desc": "Medici di base, specialisti e ospedalisti che necessitano di spiegazioni rapide e coerenti su panel eterogenei.",
                "who_primary": "Cliniche ad alto volume e gruppi",
                "who_secondary": "Popolazioni multilingue",
                "who_points": ["Flussi ambulatoriali e di degenza", "Coordinamento con laboratori esterni"],
                "benefits_title": "Cosa ottenete",
                "benefits": [
                    {
                        "title": "Colloqui più rapidi",
                        "desc": "Il raggruppamento strutturato evidenzia prima ciò che conta nel contesto della visita.",
                        "points": ["Layout orientato al triage", "Meno correzioni alla dettatura", "Messaggio coerente tra le visite"],
                    },
                    {
                        "title": "Linguaggio pronto per il paziente",
                        "desc": "Spiegazioni in linguaggio semplice da consegnare o adattare alle note.",
                        "points": ["9+ lingue di report", "Formulazioni prudenti", "Passaggio di revisione clinica"],
                    },
                    {
                        "title": "Affidabilità operativa",
                        "desc": "Progettato per team che generano oltre 2M di report sulla piattaforma.",
                        "points": ["Struttura adatta agli audit", "Percorso sicurezza enterprise", "Onboarding dedicato"],
                    },
                    {
                        "title": "Fiducia e governance",
                        "desc": "Documentazione assistiva—non sostituto diagnostico.",
                        "points": ["Revisione con umano nel ciclo", "Limiti chiari nel testo", "Allineamento compliance"],
                    },
                ],
                "workflow_title": "Dati grezzi a linguaggio paziente pronto alla revisione",
                "workflow_steps": [
                    {"title": "Ingresso", "desc": "Ricezione sicura di export CSV/PDF o feed API."},
                    {"title": "Struttura", "desc": "Normalizzazione marker con accuratezza di classificazione 98,7% in valutazione interna."},
                    {"title": "Spiegazione", "desc": "Generazione in linguaggio semplice, tono clinico controllato, output multilingue."},
                    {"title": "Revisione", "desc": "Approvazione medica prima di cartella o portale."},
                ],
            },
        ),
        "for-clinics": mk(
            pages_en["for-clinics"],
            faq=f,
            faq_title="FAQ cliniche",
            patch={
                "meta_title": "Norya per le cliniche | Comunicazione di laboratorio",
                "meta_description": "Standardizzate le spiegazioni degli esami tra medici, lingue e turni senza aumentare il personale.",
                "hero_badge": "Per le cliniche",
                "hero_title": "Un solo ritmo operativo per la comunicazione di laboratorio in ogni stanza.",
                "hero_desc": "Un’unica pipeline da risultati a materiali multilingue pronti alla revisione. Stessa qualità dal singolo sito alle reti regionali in oltre 50 paesi.",
                "who_title": "Per operatori clinici",
                "who_desc": "Direzioni mediche, operations e team che modernizzano come si spiegano i referti dopo ogni prelievo.",
                "who_primary": "Reti ambulatoriali multi-provider",
                "who_secondary": "Alto volume di prelievi e follow-up rapido",
                "who_points": ["Programmi CCM/coordinamento", "Panel occupazionali"],
                "benefits_title": "Risultati che l’amministrazione misura",
                "benefits": [
                    {
                        "title": "Throughput senza burnout",
                        "desc": "Automatizzate la prima bozza di educazione al paziente per ogni pattern di risultato.",
                        "points": ["Escalation modellate", "Passaggi turno-friendly", "Meno editing manuale"],
                    },
                    {
                        "title": "Voce sul paziente on-brand",
                        "desc": "Tono, disclaimer e glossario centralizzati.",
                        "points": ["9+ lingue incluse", "Snippet versionati", "Check legali"],
                    },
                    {
                        "title": "Visibilità per la direzione",
                        "desc": "Metriche su tempi e copertura linguistica da dashboard.",
                        "points": ["Telemetria volumi", "Allineamento SLA", "Export per iniziative QI"],
                    },
                    {
                        "title": "Controlli enterprise",
                        "desc": "Le revisioni sicurezza rispondono alle aspettive compliance ospedaliera.",
                        "points": ["Roadmap SSO", "Template DPA", "Partner dedicato"],
                    },
                ],
                "workflow_title": "Flusso in scala di clinica",
                "workflow_steps": [
                    {"title": "Raccolta", "desc": "Instradamento da LIMS o upload batch con metadati clinici."},
                    {"title": "Normalizza", "desc": "Unificare analiti e unità su feed misti."},
                    {"title": "Genera", "desc": "Bozze multilingue e note interne per medici."},
                    {"title": "Pubblica", "desc": "Dopo revisione: portali, stampa accettazione o messaggistica sicura."},
                ],
            },
        ),
        "for-hospitals": mk(
            pages_en["for-hospitals"],
            faq=f,
            faq_title="FAQ ospedali",
            patch={
                "meta_title": "Norya per ospedali | Layer linguistico enterprise",
                "meta_description": "Distribuire comunicazione di laboratorio con governance su interni, esterni e reti affiliate.",
                "hero_badge": "Sistemi ospedalieri",
                "hero_title": "Un unico modello di governance per ogni risultato che lascia la vostra rete.",
                "hero_desc": "Layer assistivo unificato: terminologia coerente, varianti localizzate e operazioni orientate SOC2 per acquisti IDN.",
                "who_title": "Con chi collaboriamo",
                "who_desc": "CMIO, CNIO, informatica di laboratorio e leadership che allinea qualità e volume.",
                "who_primary": "Reti di delivery integrate",
                "who_secondary": "Ospedali universitari e istituti specialistici",
                "who_points": ["Servizi laboratorio con outreach", "Strategie ibride cloud/on-prem"],
                "benefits_title": "Valore per il sistema sanitario",
                "benefits": [
                    {
                        "title": "Automazione consapevole del rischio",
                        "desc": "Generazione con guardrail e posizionamento assistivo esplicito.",
                        "points": ["Overlay policy", "Escalation verso specialisti", "Audit log immutabili"],
                    },
                    {
                        "title": "Coerenza multi-sede",
                        "desc": "Sincronizzare lingue, livelli di lettura e linguaggio di escalation.",
                        "points": ["Glossario centrale", "Override regionali", "Progetti adiacenza Epic/Cerner"],
                    },
                    {
                        "title": "Eccellenza misurata",
                        "desc": "Stessa valutazione interna con 98,7% accuratezza classificazione biomarcatori.",
                        "points": ["Studi QA prima/dopo", "Reporting copertura biomarcatori", "Piloti comprensione paziente"],
                    },
                    {
                        "title": "Due diligence procurement",
                        "desc": "Documentazione sicurezza e workflow clinici per il comitato.",
                        "points": ["Readiness BAA", "Sintesi pen-test", "Playbook implementazione"],
                    },
                ],
                "workflow_title": "Rollout enterprise",
                "workflow_steps": [
                    {"title": "Allinea", "desc": "Sessione congiunta su linee di servizio, lingue e routing dati."},
                    {"title": "Integra", "desc": "Connettori middleware lab e identity provider."},
                    {"title": "Valida", "desc": "Parallelo con indicatori qualità e campionamento clinici."},
                    {"title": "Scala", "desc": "Attivazione progressiva per campus o affiliato."},
                ],
            },
        ),
        "enterprise-security": mk(
            pages_en["enterprise-security"],
            faq=f,
            faq_title="FAQ sicurezza",
            patch={
                "meta_title": "Sicurezza enterprise | Norya",
                "meta_description": "Crittografia, controlli di accesso e documentazione per l’adozione del layer assistito Norya.",
                "hero_badge": "Sicurezza e conformità",
                "hero_title": "Architettura di sicurezza per gli acquisti sanitari.",
                "hero_desc": "Progettato per ambienti regolamentati: dati a livelli, least privilege e tracce di audit per cicli ISO/SOC ospedalieri.",
                "who_title": "Stakeholder supportati",
                "who_desc": "CISO, sicurezza diagnostica e procurement che documentano ogni subsistema.",
                "who_primary": "Healthcare enterprise",
                "who_secondary": "Organizzazioni di servizi diagnostici",
                "who_points": ["Impronte cloud e ibride", "Revisioni privacy multilaterali"],
                "benefits_title": "Aree di controllo",
                "benefits": [
                    {
                        "title": "Protezione dati",
                        "desc": "Crittografia in transito, retention mirata e opzioni regionali con i vostri legali.",
                        "points": ["TLS 1.2+", "Guida key management", "Finestre di purge configurabili"],
                    },
                    {
                        "title": "Governance accessi",
                        "desc": "SSO enterprise, ruoli granulari e policy di sessione.",
                        "points": ["Roadmap SAML/OIDC", "Pattern JIT", "Procedure break-glass"],
                    },
                    {
                        "title": "Artefatti di assurance",
                        "desc": "Pacchetto sicurezza con diagrammi, sintesi pen-test e subprocessori.",
                        "points": ["Allineamento SOC2", "Template DPA", "Runbook incident response"],
                    },
                    {
                        "title": "Allineamento clinico",
                        "desc": "Come gli output assistivi restano in loop col clinico.",
                        "points": ["Memo analisi rischio", "Narrative clinical safety", "FAQ legali"],
                    },
                ],
                "workflow_title": "Come procedono le revisioni",
                "workflow_steps": [
                    {"title": "NDA e scoping", "desc": "Documentazione standard e topologia deploy."},
                    {"title": "Revisione architettura", "desc": "Flussi dati, crittografia e subprocessori."},
                    {"title": "Pilota", "desc": "Produzione limitata con logging e monitoraggio."},
                    {"title": "Decisione scale", "desc": "Finalizzare BAA/DPA e configurazioni regionali."},
                ],
            },
        ),
        "clinical-demo": mk(
            pages_en["clinical-demo"],
            faq=f,
            faq_title="FAQ esercitazione",
            patch={
                "meta_title": "Demo clinica | Workflow Norya",
                "meta_description": "Da dati strutturati a spiegazioni per il paziente multilingue pronte alla revisione.",
                "hero_badge": "Valutazione guidata",
                "hero_title": "Un workflow clinico reale—dal file di laboratorio alla copia firmata.",
                "hero_desc": "In 30 minuti mappiamo feed, lingue e modello di review sulla pipeline usata in oltre 50 paesi e 120+ ospedali e cliniche.",
                "who_title": "Team di valutazione ideali",
                "who_desc": "Innovazione clinica, direttori di laboratorio e sponsor digital health.",
                "who_primary": "Comitati steering multidisciplinari",
                "who_secondary": "Proprietari qualità ed educazione paziente",
                "who_points": ["Budget innovazione FY", "Bisogno prove multilingue"],
                "benefits_title": "Cosa validerete",
                "benefits": [
                    {
                        "title": "Pipeline hands-on",
                        "desc": "Caricate campioni anonimizzati e osservate struttura, spiegazione e review.",
                        "points": ["Fedeltà raggruppamento", "Qualità linguistica", "UX revisione clinico"],
                    },
                    {
                        "title": "Trasparenza metriche",
                        "desc": "Contestualizziamo 98,7% classificazione biomarcatori internamente—non claim diagnostico.",
                        "points": ["QA per biomarcatore", "Casi limite", "Roadmap analiti"],
                    },
                    {
                        "title": "Kit stakeholder",
                        "desc": "FAQ sicurezza, posizionamento clinico e percorsi procurement.",
                        "points": ["Outline slide", "Checklist DPA", "Prerequisiti integrazione"],
                    },
                    {
                        "title": "Passi successivi",
                        "desc": "Ambito pilota, licenza e metriche di successo in una sessione.",
                        "points": ["Assunzioni volume", "Piano localizzazione", "Approccio formazione"],
                    },
                ],
                "workflow_title": "Storia della demo",
                "workflow_steps": [
                    {"title": "Scenario", "desc": "Scegliete panel e contesto paziente rappresentativi."},
                    {"title": "Ingest e normalizza", "desc": "Mapping dal vostro export tipico."},
                    {"title": "Genera", "desc": "Bozze multilingue con annotazioni di review."},
                    {"title": "Q&A", "desc": "Discussione aperta medica, IT e legale."},
                ],
            },
        ),
    }

# -*- coding: utf-8 -*-
"""French — full B2B audience pages."""

from __future__ import annotations

from typing import Any

from app.b2b_locales._builder import mk
from app.b2b_locales.faq import faq_for


def build_pages(pages_en: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
    f = faq_for("fr")
    return {
        "for-doctors": mk(
            pages_en["for-doctors"],
            faq=f,
            faq_title="Questions fréquentes",
            patch={
                "meta_title": "Norya pour les médecins | Clarité des analyses",
                "meta_description": "Rapports assistés laboratoire-langage : marqueurs structurés, langage simple, sortie prête à examen en 9+ langues.",
                "hero_badge": "Pour les cliniciens",
                "hero_title": "Expliquez des analyses complexes en langage patient—sans charge administrative supplémentaire.",
                "hero_desc": "Norya transforme les exports laboratoire standard en résumés clairs et multilingues. Pour les cabinets à fort volume au sein de plus de 4 000 hôpitaux et cliniques de notre réseau.",
                "who_title": "À qui s’adresse cette offre",
                "who_desc": "Médecins généralistes, spécialistes et hospitalistes qui ont besoin d’explications rapides et cohérentes sur des bilans hétérogènes.",
                "who_primary": "Cliniques à haut débit et groupements",
                "who_secondary": "Populations patientes multilingues",
                "who_points": ["Parcours ambulatoires et hospitaliers", "Coordination avec laboratoires externes"],
                "benefits_title": "Ce que vous obtenez",
                "benefits": [
                    {
                        "title": "Consultations plus rapides",
                        "desc": "Le regroupement structuré met d’abord en avant l’essentiel selon le contexte de la visite.",
                        "points": ["Présentation orientée triage", "Moins de reprises de dictée", "Cadrage stable entre les visites"],
                    },
                    {
                        "title": "Langage prêt pour le patient",
                        "desc": "Explications en langage clair à remettre aux patients ou à adapter dans vos notes.",
                        "points": ["9+ langues de rapport", "Formulations prudentes", "Étape de reprise clinique intégrée"],
                    },
                    {
                        "title": "Fiabilité opérationnelle",
                        "desc": "Conçu pour les équipes qui génèrent déjà plus de 2M de rapports via la plateforme.",
                        "points": ["Structure favorable aux audits", "Parcours sécurité entreprise", "Onboarding dédié"],
                    },
                    {
                        "title": "Confiance et gouvernance",
                        "desc": "Positionné comme documentation d’aide—pas un substitut au diagnostic.",
                        "points": ["Revue avec humain dans la boucle", "Limites explicites", "Alignement conformité"],
                    },
                ],
                "workflow_title": "Des données brutes au langage patient prêt à examen",
                "workflow_steps": [
                    {"title": "Collecte", "desc": "Réception sécurisée d’exports CSV/PDF ou de flux API."},
                    {"title": "Structuration", "desc": "Normalisation des marqueurs avec 98,7 % de précision de classification en évaluation interne."},
                    {"title": "Explication", "desc": "Génération en langage clair, tonalité clinique contrôlée, sorties multilingues."},
                    {"title": "Revue", "desc": "Validation clinician avant tout envoi dossier patient ou portail."},
                ],
            },
        ),
        "for-clinics": mk(
            pages_en["for-clinics"],
            faq=f,
            faq_title="FAQ cliniques",
            patch={
                "meta_title": "Norya pour les cliniques | Communication laboratoire",
                "meta_description": "Uniformisez les explications d’analyses aux patients entre équipes, langues et postes—sans embaucher davantage.",
                "hero_badge": "Pour les cliniques",
                "hero_title": "Un rythme opérationnel unique pour la communication laboratoire dans chaque salle.",
                "hero_desc": "Une pipeline unique des résultats vers des supports multilingues prêts à examen. Même qualité du site unique au réseau régional dans plus de 50 pays.",
                "who_title": "Pour les opérateurs de soins",
                "who_desc": "Directions médicales, opérations et équipes qui modernisent l’explication des analyses après chaque prélèvement.",
                "who_primary": "Réseaux ambulatoires multi-praticiens",
                "who_secondary": "Phlébotomie à fort volume et suivi rapide",
                "who_points": ["Programmes CCM / coordination", "Panels médecine du travail"],
                "benefits_title": "Résultats suivis par l’administration",
                "benefits": [
                    {
                        "title": "Débit sans épuisement",
                        "desc": "Automatisez le premier jet d’éducation patient lié à chaque profil de résultats.",
                        "points": ["Escalades modélisées", "Passations compatibles équipes", "Moins d’édition manuelle"],
                    },
                    {
                        "title": "Voix patiente conforme à la marque",
                        "desc": "Verrouillez ton, clauses de non-exonération et glossaire au centre.",
                        "points": ["9+ langues de rapport", "Extraits versionnés", "Points de contrôle juridique"],
                    },
                    {
                        "title": "Visibilité direction",
                        "desc": "Indicateurs de délai et de couverture linguistique exploitables en tableau de bord.",
                        "points": ["Télémétrie de volume", "Alignement SLA", "Export pour initiatives QI"],
                    },
                    {
                        "title": "Contrôles entreprise",
                        "desc": "Les revues sécurité répondent aux attentes hospitalières.",
                        "points": ["Feuille de route SSO", "Modèles DPA", "Partenaire succès dédié"],
                    },
                ],
                "workflow_title": "Workflow à l’échelle d’une clinique",
                "workflow_steps": [
                    {"title": "Entrée", "desc": "Routage depuis LIMS ou imports groupés avec métadonnées clinique."},
                    {"title": "Normaliser", "desc": "Unifier analytes et unités sur flux hétérogènes."},
                    {"title": "Générer", "desc": "Brouillons multilingues et notes internes clinicien."},
                    {"title": "Publier", "desc": "Après revue : portails, impression accueil ou messagerie sécurisée."},
                ],
            },
        ),
        "for-hospitals": mk(
            pages_en["for-hospitals"],
            faq=f,
            faq_title="FAQ hôpitaux",
            patch={
                "meta_title": "Norya pour les hôpitaux | Couche langage laboratoire entreprise",
                "meta_description": "Déployez une couche de communication laboratoire avec gouvernance sur réseaux hospitaliers et affiliés.",
                "hero_badge": "Systèmes hospitaliers",
                "hero_title": "Un seul modèle de gouvernance pour chaque résultat quittant votre réseau intégré.",
                "hero_desc": "Une couche assistive unifiée : terminologie cohérente, variantes localisées et exploitation alignée SOC2 adaptée aux achats des IDN.",
                "who_title": "Avec qui nous travaillons",
                "who_desc": "CMIO, CNIO, informatique de laboratoire et finances alignant qualité et volume.",
                "who_primary": "Réseaux de prestation intégrés",
                "who_secondary": "Hôpitaux universitaires et instituts spécialisés",
                "who_points": ["Services de labo avec outreach", "Stratégies hybrides cloud / on-prem"],
                "benefits_title": "Valeur système",
                "benefits": [
                    {
                        "title": "Automatisation consciente des risques",
                        "desc": "Génération encadrée avec positionnement d’aide explicite.",
                        "points": ["Superpositions de politique", "Escalade vers spécialistes", "Journaux d’audit immuables"],
                    },
                    {
                        "title": "Cohérence inter-campus",
                        "desc": "Synchronisez langues, niveaux de lecture et formulations d’escalade.",
                        "points": ["Glossaire central", "Dérogations régionales", "Projets d’adjacence Epic/Cerner"],
                    },
                    {
                        "title": "Excellence mesurée",
                        "desc": "Tirez parti de la même évaluation interne à 98,7 % de précision de classification des biomarqueurs.",
                        "points": ["Études QA avant/après", "Couverture biomarqueurs", "Pilotes de compréhension patient"],
                    },
                    {
                        "title": "Due diligence achats",
                        "desc": "Documentation sécurité et parcours cliniques packagés pour comités.",
                        "points": ["Préparation BAA", "Synthèses pen-test", "Guide de déploiement"],
                    },
                ],
                "workflow_title": "Déploiement entreprise",
                "workflow_steps": [
                    {"title": "Aligner", "desc": "Atelier conjoint : filières, langues, routage données."},
                    {"title": "Intégrer", "desc": "Connecteurs middleware labo et fournisseurs d’identité."},
                    {"title": "Valider", "desc": "Parallèle avec indicateurs qualité et échantillonnage clinicien."},
                    {"title": "Étendre", "desc": "Activation progressive par campus, affilié ou partenaire."},
                ],
            },
        ),
        "enterprise-security": mk(
            pages_en["enterprise-security"],
            faq=f,
            faq_title="FAQ sécurité",
            patch={
                "meta_title": "Sécurité entreprise | Norya",
                "meta_description": "Chiffrement, contrôles d’accès et dossiers d’achat pour l’adoption de la couche assistive Norya.",
                "hero_badge": "Sécurité et conformité",
                "hero_title": "Architecture de sécurité adaptée aux achats santé.",
                "hero_desc": "Conçu pour environnements réglementés : traitement des données par niveaux, moindre privilège et pistes d’audit pour cycles ISO/SOC hospitaliers.",
                "who_title": "Parties prenantes accompagnées",
                "who_desc": "RSSI, sécurité du diagnostic et achats devant documenter chaque sous-système.",
                "who_primary": "Entreprises de santé",
                "who_secondary": "Organisations de services de diagnostic",
                "who_points": ["Empreintes cloud et hybrides", "Revues juridiques multinationales"],
                "benefits_title": "Domaines de contrôle",
                "benefits": [
                    {
                        "title": "Protection des données",
                        "desc": "Chiffrement en transit, conservation ciblée et options régionales avec vos juristes.",
                        "points": ["TLS 1.2+", "Guide gestion des clés", "Fenêtres de purge configurables"],
                    },
                    {
                        "title": "Gouvernance des accès",
                        "desc": "SSO entreprise, rôles fins et politiques de session.",
                        "points": ["Feuille de route SAML/OIDC", "Provisioning JIT", "Procédures break-glass"],
                    },
                    {
                        "title": "Artefacts d’assurance",
                        "desc": "Dossier sécurité : schémas, synthèses pen-test et sous-traitants.",
                        "points": ["Alignement programme SOC2", "Modèles DPA", "Runbooks incident"],
                    },
                    {
                        "title": "Alignement clinique",
                        "desc": "Expliciter comment les sorties assistées restent sous revue clinicien.",
                        "points": ["Mémos d’analyse de risque", "Récits clinical safety", "FAQ pour juridique"],
                    },
                ],
                "workflow_title": "Déroulement des revues",
                "workflow_steps": [
                    {"title": "NDA et cadrage", "desc": "Échanges contractuels standard et topologie de déploiement."},
                    {"title": "Revue d’architecture", "desc": "Parcours des flux, chiffrement et sous-traitants."},
                    {"title": "Pilote", "desc": "Production limitée avec journalisation et supervision."},
                    {"title": "Décision d’échelle", "desc": "Finaliser BAA/DPA et configurations régionales."},
                ],
            },
        ),
        "clinical-demo": mk(
            pages_en["clinical-demo"],
            faq=f,
            faq_title="FAQ démo",
            patch={
                "meta_title": "Démo clinique | Flux Norya",
                "meta_description": "Des données structurées aux explications patient multilingues prêtes à examen.",
                "hero_badge": "Évaluation guidée",
                "hero_title": "Un parcours clinique réel—du fichier laboratoire à la copie patient signée.",
                "hero_desc": "En 30 minutes nous alignons vos flux, langues et modèle de relecture sur le pipeline utilisé dans plus de 50 pays et 4 000+ hôpitaux et cliniques.",
                "who_title": "Équipes d’évaluation idéales",
                "who_desc": "Innovation clinique, directeurs de laboratoire et sponsors digital health validant l’outil d’aide.",
                "who_primary": "Comités de pilotage multidisciplinaires",
                "who_secondary": "Responsables qualité et éducation patient",
                "who_points": ["Budgets innovation pour le budget annuel", "Besoin de preuves multilingues"],
                "benefits_title": "Ce que vous validerez",
                "benefits": [
                    {
                        "title": "Pipeline en direct",
                        "desc": "Chargez des échantillons anonymisés et observez structure, explication et relecture.",
                        "points": ["Fidélité du regroupement", "Qualité linguistique", "UX de relecture"],
                    },
                    {
                        "title": "Transparence des métriques",
                        "desc": "Nous contextualisons 98,7 % de classification des biomarqueurs en interne—pas une revendication diagnostique.",
                        "points": ["QA par biomarqueur", "Cas limites", "Feuille de route analytes"],
                    },
                    {
                        "title": "Kits parties prenantes",
                        "desc": "FAQ sécurité, positionnement clinique et parcours d’achat.",
                        "points": ["Plan de slides", "Check-list DPA", "Prérequis d’intégration"],
                    },
                    {
                        "title": "Suite du parcours",
                        "desc": "Périmètre pilote, licence et indicateurs de succès en une session.",
                        "points": ["Hypothèses de volume", "Plan de localisation", "Approche formation"],
                    },
                ],
                "workflow_title": "Scénario de démo",
                "workflow_steps": [
                    {"title": "Scénario", "desc": "Choisir un panel représentatif et un contexte patient."},
                    {"title": "Import et normalisation", "desc": "Montrer le mapping depuis votre export typique."},
                    {"title": "Génération", "desc": "Brouillons multilingues avec annotations de relecture."},
                    {"title": "Q&R", "desc": "Discussion ouverte clinique, IT et juridique."},
                ],
            },
        ),
    }

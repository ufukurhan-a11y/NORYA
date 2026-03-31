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
            faq_title="FAQ médecins",
            patch={
                "meta_title": "Norya pour Médecins | Clarté laboratoire en minutes",
                "meta_description": "Rapports assistés laboratoire-vers-langage : marqueurs structurés, langage simple, sorties prêtes pour revue en 9+ langues.",
                "hero_badge": "Pour cliniciens",
                "hero_title": "Expliquer les laboratoires complexes aux patients—sans surcharge administrative.",
                "hero_desc": "Norya transforme les exports laboratoire standards en résumés bilingues prêts pour consultation. Pour pratiques à fort volume autour de 4 000+ hôpitaux et cliniques dans notre réseau.",
            },
        ),
        "for-clinics": mk(
            pages_en["for-clinics"],
            faq=f,
            faq_title="FAQ cliniques",
            patch={
                "meta_title": "Norya pour Cliniques | Communication laboratoire opérationnelle",
                "meta_description": "Standardisez les explications laboratoire entre fournisseurs, langues et shifts—sans personnel supplémentaire.",
                "hero_badge": "Pour cliniques",
                "hero_title": "Un rythme opérationnel pour la communication laboratoire dans chaque salle.",
                "hero_desc": "Norya offre aux opérateurs de cliniques un pipeline du laboratoire vers des matériaux multilingues vérifiés. Même qualité du site unique aux réseaux régionaux dans 50+ pays.",
            },
        ),
        "for-hospitals": mk(
            pages_en["for-hospitals"],
            faq=f,
            faq_title="FAQ hôpitaux",
            patch={
                "meta_title": "Norya pour Hôpitaux | Plateforme IA Enterprise",
                "meta_description": "Transformez votre hôpital avec l'IA. 12+ langues, HL7/FHIR, 2M+ rapports, 4 000+ hôpitaux.",
                "hero_badge": "Plateforme IA Enterprise",
                "hero_title": "Transformez Votre Laboratoire avec l'IA",
                "hero_desc": "NoryaAI Clinical Enterprise : Solution enterprise pour résultats structurés, multilingues et traçables.",
                "who_title": "Approuvé par les hôpitaux leaders",
                "who_primary": "Groupes hospitaliers",
                "who_secondary": "Hôpitaux universitaires",
                "features_title": "Fonctionnalités Premium",
                "pricing_title": "Solutions Enterprise",
                "pilot_title": "Déploiement pilote",
                "workflow_title": "Flux hospitalier",
            },
        ),
        "enterprise-security": mk(
            pages_en["enterprise-security"],
            faq=f,
            faq_title="FAQ sécurité",
            patch={
                "meta_title": "Sécurité Enterprise | Norya",
                "meta_description": "Chiffrement, contrôles d'accès et documentation achats pour équipes adoptant Norya.",
                "hero_badge": "Sécurité et conformité",
                "hero_title": "Architecture de sécurité pour achats santé.",
                "hero_desc": "Conçu pour environnements réglementés : traitement par niveaux, moindre privilège et pistes d'audit pour cycles ISO/SOC.",
            },
        ),
        "clinical-demo": mk(
            pages_en["clinical-demo"],
            faq=f,
            faq_title="FAQ démo",
            patch={
                "meta_title": "Démo Clinique | Norya",
                "meta_description": "Comment le laboratoire devient explications patient multilingues prêtes pour revue.",
                "hero_badge": "Évaluation guidée",
                "hero_title": "Un vrai flux clinique—du fichier laboratoire à la copie patient signée.",
                "hero_desc": "En 30 minutes, nous mappons vos feeds laboratoire, langues et modèle de revue sur le pipeline Norya dans 50+ pays et 4 000+ hôpitaux.",
            },
        ),
    }

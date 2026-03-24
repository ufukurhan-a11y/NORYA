# -*- coding: utf-8 -*-
"""Compare pages — FR, ES, IT, HE, HI, AR translations.

Called by compare_i18n.apply_translations() to keep the main module navigable.
"""
from __future__ import annotations


def apply_translations(_UI, _LABELS, _NORYA, _WHY, _CTA, _HUB, _COMP):
    _apply_fr(_UI, _LABELS, _NORYA, _WHY, _CTA, _HUB, _COMP)
    _apply_es(_UI, _LABELS, _NORYA, _WHY, _CTA, _HUB, _COMP)
    _apply_it(_UI, _LABELS, _NORYA, _WHY, _CTA, _HUB, _COMP)
    _apply_he(_UI, _LABELS, _NORYA, _WHY, _CTA, _HUB, _COMP)
    _apply_hi(_UI, _LABELS, _NORYA, _WHY, _CTA, _HUB, _COMP)
    _apply_ar(_UI, _LABELS, _NORYA, _WHY, _CTA, _HUB, _COMP)


# ══════════════════════════════════════════════════════════════════
# FRENCH
# ══════════════════════════════════════════════════════════════════
def _apply_fr(_UI, _LABELS, _NORYA, _WHY, _CTA, _HUB, _COMP):
    _UI["fr"] = {
        "home": "Accueil", "compare": "Comparer", "how_it_works": "Comment ça marche",
        "pricing": "Tarifs", "blog": "Blog", "analyze": "Analyser",
        "faq_heading": "Questions fréquentes",
        "related_heading": "Comparaisons associées",
        "badge": "Comparaison honnête · NoryaAI",
        "comparison_title": "Comparaison côte à côte",
        "comparison_sub": "Comment les deux approches diffèrent sur les fonctionnalités les plus importantes pour vos résultats d'analyses sanguines.",
        "disclaimer": "NoryaAI ne fournit pas de diagnostics médicaux. Tout le contenu est à des fins éducatives et informatives uniquement.",
        "privacy": "Confidentialité", "terms": "Conditions d'utilisation",
    }
    _LABELS["fr"] = {
        "report_upload": "Téléchargement du rapport", "reference_ranges": "Valeurs de référence",
        "units_formatting": "Unités et format de laboratoire", "output_structure": "Structure du résultat",
        "multilingual": "Rapports multilingues", "doctor_summary": "Résumé prêt pour le médecin",
        "privacy": "Confidentialité et gestion des données", "workflow": "Flux de travail spécifique aux analyses sanguines",
        "guided_flow": "Type de flux de travail",
    }
    _NORYA["fr"] = {
        "report_upload": "Téléchargez un PDF, prenez une photo ou collez du texte — les valeurs et plages sont analysées automatiquement",
        "reference_ranges": "Valeurs de référence affichées pour chaque résultat — normal, bas ou élevé — clairement indiquées",
        "units_formatting": "Reconnaît automatiquement les unités de laboratoire courantes, les structures de panels et les formats de résultats",
        "output_structure": "Score de santé structuré, répartition par catégories et marqueurs signalés — cohérent à chaque fois",
        "multilingual": "Rapports complets en 9+ langues avec contexte médical préservé",
        "doctor_summary": "PDF prêt pour le médecin avec vérification QR — imprimez, enregistrez ou partagez",
        "privacy": "Conforme au RGPD/KVKK — chiffré, jamais vendu, jamais utilisé pour l'entraînement",
        "workflow": "Pipeline de téléchargement, d'analyse et de rapport spécialement conçu pour les résultats de laboratoire",
        "guided_flow": "Analyse structurée et guidée — téléchargez une fois et obtenez un rapport complet, sans prompt nécessaire",
    }
    _WHY["fr"] = {
        "title": "Pourquoi les gens choisissent NoryaAI pour les analyses sanguines",
        "sub": "Quand la précision, la structure et une prochaine étape claire comptent plus qu'une conversation générale.",
        "items": [
            {"title": "Téléchargez une fois, obtenez un rapport structuré", "desc": "Pas de prompt engineering, pas de reformatage. Téléchargez vos résultats de laboratoire et recevez automatiquement un score de santé, une répartition par catégories et des marqueurs signalés."},
            {"title": "Format cohérent pour comparer dans le temps", "desc": "Chaque rapport suit la même structure, vous permettant de suivre les changements et de repérer les tendances d'un coup d'œil."},
            {"title": "PDF prêt pour le médecin que vous pouvez apporter", "desc": "Un résumé propre et professionnel avec vérification QR. Imprimez ou partagez numériquement — conçu pour votre prochain rendez-vous."},
            {"title": "Votre langue, votre rapport", "desc": "Choisissez parmi 9+ langues et obtenez votre rapport dans celle qui vous semble la plus naturelle — avec le contexte médical intact."},
        ],
    }
    _CTA["fr"] = {
        "title": "Prêt à essayer un rapport d'analyse sanguine structuré ?",
        "sub": "Téléchargez vos résultats de laboratoire et découvrez la différence d'un analyseur spécialisé.",
        "primary": "Télécharger et analyser",
        "secondary": "Voir les tarifs",
        "hero_primary": "Analyser mon bilan sanguin",
        "hero_secondary": "Voir un rapport exemple",
    }
    _HUB["fr"] = {
        "meta_title": "Comparer NoryaAI — Alternatives d'analyse sanguine | NoryaAI",
        "meta_description": "Comparez NoryaAI avec ChatGPT, Kantesti, SiPhox Health, Wizey et les chatbots IA pour l'analyse sanguine. Comparaisons honnêtes côte à côte.",
        "hero_title": "Comparer NoryaAI avec les outils d'analyse sanguine",
        "hero_sub": "Vous cherchez le bon outil pour comprendre vos résultats d'analyses sanguines ? Nous avons préparé des comparaisons honnêtes avec plusieurs alternatives populaires.",
        "trust_stats": [
            {"value": "98,7%", "label": "Précision des résultats", "sub": "Vérifiée avec des données de laboratoire"},
            {"value": "9+", "label": "Langues", "sub": "Rapports complets avec contexte médical"},
            {"value": "QR", "label": "PDF vérifié", "sub": "Résumé partageable prêt pour le médecin"},
        ],
        "cards": [
            {"slug": "norya-vs-chatgpt-for-blood-tests", "name": "ChatGPT", "summary": "Comment un analyseur d'analyses sanguines spécialisé se compare au chatbot IA le plus populaire au monde.", "link_text": "Lire la comparaison complète"},
            {"slug": "norya-vs-kantesti", "name": "Kantesti", "summary": "Deux plateformes d'analyse sanguine comparées — rapports structurés multilingues vs service turcophone.", "link_text": "Lire la comparaison complète"},
            {"slug": "norya-vs-siphox-health", "name": "SiPhox Health", "summary": "Kits de test de biomarqueurs à domicile vs analyse structurée de vos résultats de laboratoire existants.", "link_text": "Lire la comparaison complète"},
            {"slug": "norya-vs-wizey", "name": "Wizey", "summary": "Le flux de travail de rapports structurés de NoryaAI comparé à l'approche de Wizey.", "link_text": "Lire la comparaison complète"},
            {"slug": "norya-vs-generic-ai", "name": "IA générique", "summary": "Ce qu'un analyseur spécialisé offre par rapport aux chatbots IA génériques pour vos résultats.", "link_text": "Lire la comparaison complète"},
        ],
        "hub_faqs": [
            {"q": "Quel outil est le meilleur pour comprendre les résultats d'analyses sanguines ?", "a": "Cela dépend de vos besoins. Pour des rapports structurés avec scores de santé et résumés pour le médecin, NoryaAI est spécialement conçu. Les chatbots IA sont meilleurs pour l'éducation santé générale."},
            {"q": "Ces comparaisons sont-elles justes et honnêtes ?", "a": "Nous visons la transparence. Lorsque les fonctionnalités d'un concurrent ne sont pas clairement divulguées, nous le disons plutôt que de deviner."},
            {"q": "Puis-je utiliser NoryaAI avec d'autres outils ?", "a": "Oui. NoryaAI complète votre parcours santé. Consultez toujours un médecin qualifié pour les décisions médicales."},
        ],
        "matrix_title": "Comparez les outils côte à côte",
        "matrix_sub": "Un aperçu rapide de l'approche de chaque outil pour l'analyse sanguine.",
        "matrix_row_labels": [
            "Meilleur cas d'utilisation",
            "Flux de travail spécifique aux analyses sanguines",
            "Téléchargement de fichiers",
            "Structure tenant compte des valeurs de référence",
            "Résultat structuré",
            "Support multilingue des résultats",
            "Résumé prêt pour le médecin / partageable",
            "Confidentialité / cadre éducatif",
            "Adapté à la préparation d'une visite chez le médecin",
            "Précision des résultats",
        ],
        "matrix_columns": [
            {"key": "norya", "name": "NoryaAI", "slug": None},
            {"key": "chatgpt", "name": "ChatGPT", "slug": "norya-vs-chatgpt-for-blood-tests"},
            {"key": "kantesti", "name": "Kantesti", "slug": "norya-vs-kantesti"},
            {"key": "siphox", "name": "SiPhox Health", "slug": "norya-vs-siphox-health"},
            {"key": "wizey", "name": "Wizey", "slug": "norya-vs-wizey"},
            {"key": "generic", "name": "IA générique", "slug": "norya-vs-generic-ai"},
        ],
        "matrix_rows": [
            {"norya": "Analyse sanguine structurée", "chatgpt": "Q&R santé générale", "kantesti": "Interprétation d'analyses sanguines", "siphox": "Tests de biomarqueurs à domicile", "wizey": "Analyse sanguine", "generic": "Q&R santé générale"},
            {"norya": "Fort", "chatgpt": "Limité", "kantesti": "Disponible", "siphox": "Partiel", "wizey": "Disponible", "generic": "Limité"},
            {"norya": "PDF, photo ou texte", "chatgpt": "Copier-coller dans le prompt", "kantesti": "Disponible", "siphox": "Kits propres uniquement", "wizey": "Non clairement divulgué", "generic": "Copier-coller dans le prompt"},
            {"norya": "Fort", "chatgpt": "Limité", "kantesti": "Partiel", "siphox": "Panels propres uniquement", "wizey": "Non clairement divulgué", "generic": "Limité"},
            {"norya": "Score de santé + catégories", "chatgpt": "Texte libre", "kantesti": "Non clairement divulgué", "siphox": "Vue tableau de bord", "wizey": "Non clairement divulgué", "generic": "Texte libre"},
            {"norya": "9+ langues", "chatgpt": "Partiel", "kantesti": "Principalement turc", "siphox": "Principalement anglais", "wizey": "Non clairement divulgué", "generic": "Partiel"},
            {"norya": "PDF avec vérification QR", "chatgpt": "Non disponible", "kantesti": "Non clairement divulgué", "siphox": "Non clairement divulgué", "wizey": "Non clairement divulgué", "generic": "Non disponible"},
            {"norya": "RGPD/KVKK · éducatif uniquement", "chatgpt": "Peut être stocké pour l'entraînement", "kantesti": "Voir leur politique", "siphox": "Voir leur politique", "wizey": "Voir leur politique", "generic": "Peut être stocké pour l'entraînement"},
            {"norya": "Fort", "chatgpt": "Partiel", "kantesti": "Disponible", "siphox": "Limité", "wizey": "Non clairement divulgué", "generic": "Partiel"},
            {"norya": "98,7% · vérifié en labo", "chatgpt": "Non divulgué", "kantesti": "Non divulgué", "siphox": "Non divulgué", "wizey": "Non divulgué", "generic": "Non divulgué"},
        ],
        "suits_title": "Quel outil convient à qui ?",
        "suits_items": [
            {"label": "Analyse sanguine structurée", "text": "Si vous souhaitez un score de santé cohérent, des marqueurs signalés et un PDF pour le médecin à partir de vos résultats de laboratoire, NoryaAI est conçu pour cela.", "link_slug": None},
            {"label": "Q&R santé générale", "text": "Si vous souhaitez poser des questions ouvertes sur la santé ou préparer des questions pour votre médecin, un chatbot IA comme ChatGPT est un choix solide.", "link_slug": "norya-vs-chatgpt-for-blood-tests"},
            {"label": "Comparer les outils d'analyse de laboratoire", "text": "Si vous évaluez des plateformes spécialisées dans l'analyse de rapports sanguins, comparez NoryaAI avec Kantesti et Wizey pour trouver le flux de travail adapté à vos besoins.", "link_slug": "norya-vs-kantesti"},
        ],
    }
    for slug in ("norya-vs-chatgpt-for-blood-tests", "norya-vs-kantesti", "norya-vs-siphox-health", "norya-vs-wizey", "norya-vs-generic-ai"):
        _COMP[slug].setdefault("fr", {})
    _COMP["norya-vs-chatgpt-for-blood-tests"]["fr"] = {
        "meta_title": "NoryaAI vs ChatGPT pour les analyses sanguines — Comparaison | NoryaAI",
        "meta_description": "NoryaAI vs ChatGPT pour comprendre vos résultats d'analyses sanguines. Analyseur structuré vs chatbot IA — côte à côte.",
        "hero_title": "NoryaAI vs ChatGPT pour l'analyse sanguine",
        "hero_sub": "ChatGPT est un assistant IA puissant. NoryaAI est conçu spécifiquement pour l'analyse sanguine. Voici un regard honnête sur les forces de chacun.",
        "quick_answer_title": "En bref",
        "quick_answer": "ChatGPT peut expliquer des termes médicaux mais n'est pas conçu pour analyser des rapports de laboratoire. NoryaAI lit vos résultats directement, associe les valeurs aux plages de référence et produit un résumé structuré pour le médecin. Ils résolvent des problèmes différents.",
        "cells": {
            "report_upload": "Nécessite de copier-coller les valeurs dans un prompt ; pas d'analyse native de rapports de laboratoire",
            "reference_ranges": "Peut citer des plages générales ou halluciner des valeurs ; pas de garantie de correspondance avec votre laboratoire",
            "units_formatting": "Pas de connaissance intégrée des unités de laboratoire spécifiques ou des formats régionaux",
            "output_structure": "Texte libre qui varie à chaque fois — pas de format cohérent pour le suivi",
            "multilingual": "Peut traduire du texte sur demande, mais les nuances médicales peuvent être perdues",
            "doctor_summary": "Pas de rapport téléchargeable — vous devriez formater la conversation vous-même",
            "privacy": "Les conversations peuvent être stockées et utilisées pour l'entraînement par OpenAI",
            "workflow": "Interface de chat généraliste non conçue pour l'analyse de rapports de laboratoire",
            "guided_flow": "Conversation ouverte — la qualité dépend de la formulation de votre prompt",
        },
        "helps_title": "Quand ChatGPT peut encore aider",
        "helps_sub": "ChatGPT excelle dans de nombreuses tâches. Voici où il brille vraiment.",
        "helps_items": [
            {"icon": "📚", "title": "Éducation santé générale", "desc": "ChatGPT est excellent pour apprendre ce que signifie un biomarqueur ou comment fonctionne le système immunitaire."},
            {"icon": "💡", "title": "Préparer des questions pour le médecin", "desc": "Avant un rendez-vous, ChatGPT peut vous aider à organiser vos pensées et préparer des questions."},
            {"icon": "🔍", "title": "Recherche rapide de termes médicaux", "desc": "Si vous rencontrez un terme inconnu dans votre rapport, ChatGPT peut l'expliquer en langage simple."},
        ],
        "faqs": [
            {"q": "ChatGPT peut-il analyser mes résultats d'analyses sanguines ?", "a": "ChatGPT peut discuter des valeurs si vous les tapez, mais il n'analyse pas les rapports de laboratoire et peut halluciner des détails médicaux. NoryaAI est spécialement conçu pour une analyse structurée et cohérente."},
            {"q": "NoryaAI est-il un outil de diagnostic ?", "a": "Non. NoryaAI fournit des explications structurées et éducatives de vos valeurs de laboratoire. Il ne diagnostique pas et ne recommande pas de traitements. Consultez toujours un médecin qualifié."},
            {"q": "Mes données sont-elles en sécurité ?", "a": "OpenAI peut stocker les conversations pour l'entraînement. NoryaAI est conforme au RGPD — vos données sont chiffrées, jamais vendues et jamais utilisées pour l'entraînement."},
        ],
    }
    _COMP["norya-vs-kantesti"]["fr"] = {
        "meta_title": "NoryaAI vs Kantesti — Comparaison analyses sanguines | NoryaAI",
        "meta_description": "NoryaAI vs Kantesti pour l'analyse sanguine. Comparaison des fonctionnalités de deux plateformes.",
        "hero_title": "NoryaAI vs Kantesti pour l'analyse sanguine",
        "hero_sub": "NoryaAI et Kantesti aident tous deux à comprendre les résultats d'analyses sanguines. Voici une comparaison honnête.",
        "quick_answer_title": "En bref",
        "quick_answer": "Kantesti est un service d'analyse sanguine principalement pour les utilisateurs turcophones. NoryaAI offre un flux structuré multilingue avec scores de santé et PDFs pour le médecin en 9+ langues.",
        "cells": {
            "report_upload": "Accepte la saisie de résultats pour analyse", "reference_ranges": "Fournit des informations sur les plages de référence",
            "units_formatting": "Traite les formats de rapports de laboratoires turcs", "output_structure": "Fournit les résultats dans son propre format",
            "multilingual": "Principalement disponible en turc", "doctor_summary": "Format de rapport et options de partage non clairement divulgués",
            "privacy": "Politiques de données disponibles sur leur plateforme", "workflow": "Axé sur l'interprétation des résultats",
            "guided_flow": "Propose son propre flux d'analyse",
        },
        "helps_title": "Quand Kantesti peut mieux convenir", "helps_sub": "Différents outils conviennent à différentes personnes.",
        "helps_items": [
            {"icon": "🇹🇷", "title": "Expérience turque native", "desc": "Si vous voulez une plateforme conçue pour les utilisateurs turcophones, Kantesti offre une interface turque native."},
            {"icon": "🏥", "title": "Connaissance des labos locaux", "desc": "Kantesti peut être familier avec les formats de laboratoires turcs spécifiques."},
            {"icon": "📋", "title": "Analyse simple", "desc": "Pour une interprétation directe sans besoins multilingues, Kantesti peut convenir."},
        ],
        "faqs": [
            {"q": "Qu'est-ce que Kantesti ?", "a": "Kantesti est une plateforme d'analyse sanguine principalement pour les utilisateurs turcophones."},
            {"q": "NoryaAI est-il disponible en français ?", "a": "Oui. NoryaAI offre des analyses et rapports complets en français, ainsi qu'en 9+ autres langues."},
            {"q": "NoryaAI est-il un outil de diagnostic ?", "a": "Non. Consultez toujours un médecin qualifié pour les décisions médicales."},
        ],
    }
    _COMP["norya-vs-siphox-health"]["fr"] = {
        "meta_title": "NoryaAI vs SiPhox Health — Comparaison | NoryaAI",
        "meta_description": "NoryaAI vs SiPhox Health : kits de test à domicile vs analyse structurée de rapports de laboratoire.",
        "hero_title": "NoryaAI vs SiPhox Health",
        "hero_sub": "SiPhox Health propose des kits de test de biomarqueurs à domicile. NoryaAI analyse vos résultats de laboratoire existants. Voici la comparaison.",
        "quick_answer_title": "En bref",
        "quick_answer": "SiPhox Health et NoryaAI servent différentes étapes des tests de santé. SiPhox fournit des kits à domicile, NoryaAI analyse les résultats que vous avez déjà — de n'importe quel laboratoire. Ils peuvent se compléter.",
        "cells": {
            "report_upload": "Résultats de leurs propres kits à domicile — pas conçu pour les rapports externes", "reference_ranges": "Plages pour leurs propres panels",
            "units_formatting": "Standardisé sur leur format de kit", "output_structure": "Tableau de bord dans leur plateforme",
            "multilingual": "Principalement en anglais", "doctor_summary": "Résultats consultables dans leur plateforme ; export non clairement divulgué",
            "privacy": "Politiques de données sur leur site web", "workflow": "Test complet : commander le kit, collecter, recevoir les résultats",
            "guided_flow": "Flux de test à domicile lié à leurs kits propriétaires",
        },
        "helps_title": "Quand SiPhox Health peut mieux convenir", "helps_sub": "Ils servent des besoins différents.",
        "helps_items": [
            {"icon": "🏠", "title": "Confort à domicile", "desc": "SiPhox envoie un kit chez vous pour tester sans visite au laboratoire."},
            {"icon": "📊", "title": "Suivi régulier", "desc": "SiPhox propose des tests par abonnement pour un suivi régulier des biomarqueurs."},
            {"icon": "🔬", "title": "Panels sélectionnés", "desc": "Panels conçus pour des objectifs de santé spécifiques comme la longévité ou la santé métabolique."},
        ],
        "faqs": [
            {"q": "Qu'est-ce que SiPhox Health ?", "a": "SiPhox Health propose des kits de test de biomarqueurs à domicile."},
            {"q": "Ai-je besoin d'un kit pour utiliser NoryaAI ?", "a": "Non. NoryaAI fonctionne avec les résultats que vous avez déjà — de n'importe quel laboratoire."},
            {"q": "NoryaAI est-il un outil de diagnostic ?", "a": "Non. Consultez toujours un médecin qualifié pour les décisions médicales."},
        ],
    }
    _COMP["norya-vs-wizey"]["fr"] = {
        "meta_title": "NoryaAI vs Wizey — Comparaison analyses sanguines | NoryaAI",
        "meta_description": "NoryaAI vs Wizey pour l'analyse sanguine. Rapports structurés, support multilingue et flux de travail comparés.",
        "hero_title": "NoryaAI vs Wizey pour l'analyse sanguine",
        "hero_sub": "NoryaAI et Wizey aident tous deux à comprendre les résultats sanguins. Voici une comparaison honnête.",
        "quick_answer_title": "En bref",
        "quick_answer": "Wizey propose des outils d'analyse sanguine. NoryaAI fournit un flux structuré avec scores de santé, PDFs pour le médecin et rapports multilingues de n'importe quel format de laboratoire.",
        "cells": {
            "report_upload": "Accepte les résultats pour analyse", "reference_ranges": "Fournit des informations de référence",
            "units_formatting": "Support de format non clairement divulgué", "output_structure": "Analyse dans son propre format",
            "multilingual": "Support linguistique non clairement divulgué", "doctor_summary": "Options de partage non clairement divulguées",
            "privacy": "Politiques de données sur leur plateforme", "workflow": "Propose un flux d'interprétation sanguine",
            "guided_flow": "Propose son propre processus d'analyse",
        },
        "helps_title": "Quand Wizey peut encore aider", "helps_sub": "Différents outils pour différentes préférences.",
        "helps_items": [
            {"icon": "📱", "title": "Leur approche spécifique", "desc": "Wizey peut offrir des fonctionnalités adaptées à vos préférences."},
            {"icon": "🔄", "title": "Perspective alternative", "desc": "Une deuxième interprétation peut fournir un contexte supplémentaire."},
            {"icon": "💭", "title": "Préférence personnelle", "desc": "Le bon outil dépend de votre flux de travail, besoins linguistiques et type de sortie préféré."},
        ],
        "faqs": [
            {"q": "Qu'est-ce que Wizey ?", "a": "Wizey est une plateforme d'analyse sanguine. Consultez leur site web pour les détails."},
            {"q": "Comment NoryaAI diffère-t-il de Wizey ?", "a": "NoryaAI offre des scores de santé structurés, des PDFs avec vérification QR, des rapports en 9+ langues et accepte les rapports de n'importe quel laboratoire."},
            {"q": "NoryaAI est-il un outil de diagnostic ?", "a": "Non. Consultez toujours un médecin qualifié pour les décisions médicales."},
        ],
    }
    _COMP["norya-vs-generic-ai"]["fr"] = {
        "meta_title": "NoryaAI vs IA Générique pour analyses sanguines — Comparaison | NoryaAI",
        "meta_description": "NoryaAI vs ChatGPT ou autres chatbots IA pour les résultats d'analyses sanguines. Rapports structurés vs réponses de chat en texte libre.",
        "hero_title": "NoryaAI vs Chatbots IA Génériques pour les analyses sanguines",
        "hero_sub": "Les deux peuvent traiter des données de laboratoire — mais de manière très différente. Voici un regard honnête sur ce que chacun offre.",
        "quick_answer_title": "En bref",
        "quick_answer": "Les chatbots IA génériques peuvent expliquer des termes médicaux. NoryaAI est conçu pour les analyses sanguines : il lit votre rapport, associe les valeurs aux plages de référence et produit un résumé structuré avec score de santé. Les deux ont leur place, mais résolvent des problèmes différents.",
        "cells": {
            "report_upload": "Copier-coller les valeurs dans un prompt en espérant que le formatage tienne",
            "reference_ranges": "Peut deviner les plages ou les omettre ; aucune garantie de correspondance avec votre laboratoire",
            "units_formatting": "Pas de connaissance des unités de laboratoire spécifiques ou des formats de résultats",
            "output_structure": "Paragraphe en texte libre qui varie à chaque prompt — pas de format cohérent",
            "multilingual": "Peut traduire du texte, mais la nuance médicale peut être perdue",
            "doctor_summary": "Pas de rapport téléchargeable — vous devriez copier et formater le chat vous-même",
            "privacy": "Les conversations peuvent être stockées et utilisées pour l'entraînement",
            "workflow": "Interface de chat généraliste conçue pour tout sujet",
            "guided_flow": "Conversation ouverte — la qualité dépend de la formulation de votre prompt",
        },
        "helps_title": "Quand les chatbots IA génériques peuvent encore aider",
        "helps_sub": "Il ne s'agit pas d'un outil mauvais et d'un autre bon. Ils servent des objectifs différents.",
        "helps_items": [
            {"icon": "📚", "title": "Éducation santé générale", "desc": "Les chatbots sont excellents pour apprendre ce que signifie un biomarqueur ou comment fonctionne le système immunitaire."},
            {"icon": "💡", "title": "Préparer des questions pour votre médecin", "desc": "Avant un rendez-vous, un chatbot peut vous aider à réfléchir aux questions à poser."},
            {"icon": "🔍", "title": "Comprendre la terminologie médicale", "desc": "Un terme inconnu dans votre rapport ? Une IA générique peut l'expliquer rapidement en langage simple."},
        ],
        "faqs": [
            {"q": "ChatGPT peut-il expliquer les résultats d'analyses sanguines ?", "a": "Oui, dans une certaine mesure. Mais il n'analyse pas votre rapport réel, peut halluciner des valeurs de référence et donne une réponse différente à chaque fois. NoryaAI lit votre rapport directement et produit un résumé structuré et cohérent."},
            {"q": "NoryaAI est-il un outil de diagnostic ?", "a": "Non. NoryaAI fournit des explications structurées et éducatives. Consultez toujours un médecin qualifié pour les décisions médicales."},
            {"q": "Puis-je télécharger un PDF au lieu de copier les valeurs ?", "a": "Oui. NoryaAI accepte les PDFs, photos de rapports de laboratoire et texte collé. Les valeurs et plages sont analysées automatiquement."},
        ],
    }


# ══════════════════════════════════════════════════════════════════
# SPANISH
# ══════════════════════════════════════════════════════════════════
def _apply_es(_UI, _LABELS, _NORYA, _WHY, _CTA, _HUB, _COMP):
    _UI["es"] = {
        "home": "Inicio", "compare": "Comparar", "how_it_works": "Cómo funciona",
        "pricing": "Precios", "blog": "Blog", "analyze": "Analizar",
        "faq_heading": "Preguntas frecuentes",
        "related_heading": "Comparaciones relacionadas",
        "badge": "Comparación honesta · NoryaAI",
        "comparison_title": "Comparación lado a lado",
        "comparison_sub": "Cómo difieren los dos enfoques en las funciones más importantes para los resultados de análisis de sangre.",
        "disclaimer": "NoryaAI no proporciona diagnósticos médicos. Todo el contenido es solo con fines educativos e informativos.",
        "privacy": "Privacidad", "terms": "Términos de uso",
    }
    _LABELS["es"] = {
        "report_upload": "Carga de informes", "reference_ranges": "Rangos de referencia",
        "units_formatting": "Unidades y formato de laboratorio", "output_structure": "Estructura del resultado",
        "multilingual": "Informes multilingües", "doctor_summary": "Resumen listo para el médico",
        "privacy": "Privacidad y gestión de datos", "workflow": "Flujo específico para análisis de sangre",
        "guided_flow": "Tipo de flujo de trabajo",
    }
    _NORYA["es"] = {
        "report_upload": "Suba un PDF, tome una foto o pegue texto — los valores y rangos se analizan automáticamente",
        "reference_ranges": "Rangos de referencia mostrados para cada valor — normal, bajo o alto — claramente etiquetados",
        "units_formatting": "Reconoce automáticamente las unidades de laboratorio comunes, estructuras de paneles y formatos de resultados",
        "output_structure": "Puntuación de salud estructurada, desglose por categorías y marcadores señalados — consistente cada vez",
        "multilingual": "Informes completos en 9+ idiomas con contexto médico preservado",
        "doctor_summary": "PDF listo para el médico con verificación QR — imprima, guarde o comparta",
        "privacy": "Compatible con RGPD/KVKK — cifrado, nunca vendido, nunca usado para entrenamiento",
        "workflow": "Pipeline de carga, análisis e informe diseñado específicamente para resultados de laboratorio",
        "guided_flow": "Análisis estructurado y guiado — suba una vez y obtenga un informe completo, sin prompt necesario",
    }
    _WHY["es"] = {
        "title": "Por qué la gente elige NoryaAI para análisis de sangre",
        "sub": "Cuando la precisión, la estructura y un próximo paso claro importan más que una conversación general.",
        "items": [
            {"title": "Suba una vez, obtenga un informe estructurado", "desc": "Sin ingeniería de prompts, sin reformateo. Suba sus resultados de laboratorio y reciba automáticamente una puntuación de salud, desglose por categorías y marcadores señalados."},
            {"title": "Formato consistente para comparar a lo largo del tiempo", "desc": "Cada informe sigue la misma estructura, permitiéndole seguir cambios y detectar tendencias de un vistazo."},
            {"title": "PDF listo para el médico que realmente puede llevar", "desc": "Un resumen limpio y profesional con verificación QR. Imprima o comparta digitalmente — diseñado para su próxima cita."},
            {"title": "Su idioma, su informe", "desc": "Elija entre 9+ idiomas y obtenga su informe en el que le resulte más natural — con el contexto médico intacto."},
        ],
    }
    _CTA["es"] = {
        "title": "¿Listo para probar un informe de análisis de sangre estructurado?",
        "sub": "Suba sus resultados de laboratorio y vea la diferencia de un analizador especializado.",
        "primary": "Subir y analizar", "secondary": "Ver precios",
        "hero_primary": "Analizar mi análisis de sangre", "hero_secondary": "Ver informe de ejemplo",
    }
    _HUB["es"] = {
        "meta_title": "Comparar NoryaAI — Alternativas de análisis de sangre | NoryaAI",
        "meta_description": "Compare NoryaAI con ChatGPT, Kantesti, SiPhox Health, Wizey y chatbots de IA para análisis de sangre. Comparaciones honestas.",
        "hero_title": "Compare NoryaAI con herramientas de análisis de sangre",
        "hero_sub": "¿Busca la herramienta adecuada para entender sus resultados de análisis de sangre? Hemos preparado comparaciones honestas con varias alternativas populares.",
        "trust_stats": [
            {"value": "98,7%", "label": "Precisión de resultados", "sub": "Verificada con datos de laboratorio"},
            {"value": "9+", "label": "Idiomas", "sub": "Informes completos con contexto médico"},
            {"value": "QR", "label": "PDF verificado", "sub": "Resumen compartible listo para el médico"},
        ],
        "cards": [
            {"slug": "norya-vs-chatgpt-for-blood-tests", "name": "ChatGPT", "summary": "Cómo un analizador especializado se compara con el chatbot de IA más popular del mundo.", "link_text": "Leer comparación completa"},
            {"slug": "norya-vs-kantesti", "name": "Kantesti", "summary": "Dos plataformas de análisis de sangre comparadas — informes estructurados multilingües vs servicio turco.", "link_text": "Leer comparación completa"},
            {"slug": "norya-vs-siphox-health", "name": "SiPhox Health", "summary": "Kits de prueba de biomarcadores en casa vs análisis estructurado de sus resultados de laboratorio existentes.", "link_text": "Leer comparación completa"},
            {"slug": "norya-vs-wizey", "name": "Wizey", "summary": "El flujo de informes estructurados de NoryaAI comparado con el enfoque de Wizey.", "link_text": "Leer comparación completa"},
            {"slug": "norya-vs-generic-ai", "name": "IA genérica", "summary": "Lo que un analizador especializado ofrece frente a los chatbots de IA genéricos.", "link_text": "Leer comparación completa"},
        ],
        "hub_faqs": [
            {"q": "¿Cuál es la mejor herramienta para entender resultados de análisis de sangre?", "a": "Depende de sus necesidades. Para informes estructurados con puntuaciones de salud y resúmenes para el médico, NoryaAI está especialmente diseñado."},
            {"q": "¿Son estas comparaciones justas?", "a": "Buscamos transparencia. Cuando las características de un competidor no están claramente divulgadas, lo indicamos en lugar de adivinar."},
            {"q": "¿Puedo usar NoryaAI junto con otras herramientas?", "a": "Sí. NoryaAI complementa su flujo de salud. Consulte siempre a un médico cualificado para decisiones médicas."},
        ],
        "matrix_title": "Compare las herramientas lado a lado",
        "matrix_sub": "Una vista rápida de cómo cada herramienta aborda el análisis de sangre.",
        "matrix_row_labels": [
            "Mejor caso de uso",
            "Flujo de trabajo para análisis de sangre",
            "Carga de archivos",
            "Estructura con rangos de referencia",
            "Resultado estructurado",
            "Soporte multilingüe de resultados",
            "Resumen listo para el médico / compartible",
            "Privacidad / enfoque educativo",
            "Adecuado para preparar una visita al médico",
            "Precisión de resultados",
        ],
        "matrix_columns": [
            {"key": "norya", "name": "NoryaAI", "slug": None},
            {"key": "chatgpt", "name": "ChatGPT", "slug": "norya-vs-chatgpt-for-blood-tests"},
            {"key": "kantesti", "name": "Kantesti", "slug": "norya-vs-kantesti"},
            {"key": "siphox", "name": "SiPhox Health", "slug": "norya-vs-siphox-health"},
            {"key": "wizey", "name": "Wizey", "slug": "norya-vs-wizey"},
            {"key": "generic", "name": "IA genérica", "slug": "norya-vs-generic-ai"},
        ],
        "matrix_rows": [
            {"norya": "Análisis de sangre estructurado", "chatgpt": "Preguntas generales de salud", "kantesti": "Interpretación de análisis de sangre", "siphox": "Pruebas de biomarcadores en casa", "wizey": "Análisis de sangre", "generic": "Preguntas generales de salud"},
            {"norya": "Fuerte", "chatgpt": "Limitado", "kantesti": "Disponible", "siphox": "Parcial", "wizey": "Disponible", "generic": "Limitado"},
            {"norya": "PDF, foto o texto", "chatgpt": "Copiar y pegar en el prompt", "kantesti": "Disponible", "siphox": "Solo sus kits propios", "wizey": "No divulgado claramente", "generic": "Copiar y pegar en el prompt"},
            {"norya": "Fuerte", "chatgpt": "Limitado", "kantesti": "Parcial", "siphox": "Solo sus paneles propios", "wizey": "No divulgado claramente", "generic": "Limitado"},
            {"norya": "Puntuación de salud + categorías", "chatgpt": "Texto libre", "kantesti": "No divulgado claramente", "siphox": "Vista de panel", "wizey": "No divulgado claramente", "generic": "Texto libre"},
            {"norya": "9+ idiomas", "chatgpt": "Parcial", "kantesti": "Principalmente turco", "siphox": "Principalmente inglés", "wizey": "No divulgado claramente", "generic": "Parcial"},
            {"norya": "PDF con verificación QR", "chatgpt": "No disponible", "kantesti": "No divulgado claramente", "siphox": "No divulgado claramente", "wizey": "No divulgado claramente", "generic": "No disponible"},
            {"norya": "RGPD/KVKK · solo educativo", "chatgpt": "Puede almacenarse para entrenamiento", "kantesti": "Consulte su política", "siphox": "Consulte su política", "wizey": "Consulte su política", "generic": "Puede almacenarse para entrenamiento"},
            {"norya": "Fuerte", "chatgpt": "Parcial", "kantesti": "Disponible", "siphox": "Limitado", "wizey": "No divulgado claramente", "generic": "Parcial"},
            {"norya": "98,7% · verificado en laboratorio", "chatgpt": "No divulgado", "kantesti": "No divulgado", "siphox": "No divulgado", "wizey": "No divulgado", "generic": "No divulgado"},
        ],
        "suits_title": "¿Qué herramienta se adapta a quién?",
        "suits_items": [
            {"label": "Análisis de sangre estructurado", "text": "Si desea una puntuación de salud consistente, marcadores señalados y un PDF listo para el médico a partir de sus resultados de laboratorio, NoryaAI está diseñado para eso.", "link_slug": None},
            {"label": "Preguntas generales de salud", "text": "Si desea hacer preguntas abiertas sobre salud o preparar preguntas para su médico, un chatbot de IA como ChatGPT es una opción sólida.", "link_slug": "norya-vs-chatgpt-for-blood-tests"},
            {"label": "Comparar herramientas de análisis de laboratorio", "text": "Si está evaluando plataformas especializadas en análisis de informes de sangre, compare NoryaAI con Kantesti y Wizey para ver cuál se adapta mejor a sus necesidades.", "link_slug": "norya-vs-kantesti"},
        ],
    }
    _comp_cells_es = {
        "chatgpt": {
            "report_upload": "Requiere copiar y pegar valores en un prompt; sin análisis nativo de informes de laboratorio",
            "reference_ranges": "Puede citar rangos generales o alucinar valores; sin garantía de coincidencia con su laboratorio",
            "units_formatting": "Sin conocimiento integrado de unidades de laboratorio específicas o formatos regionales",
            "output_structure": "Texto libre que varía cada vez — sin formato consistente para seguimiento",
            "multilingual": "Puede traducir texto a pedido, pero los matices médicos pueden perderse",
            "doctor_summary": "Sin informe descargable — tendría que formatear la conversación usted mismo",
            "privacy": "Las conversaciones pueden ser almacenadas y usadas para entrenamiento por OpenAI",
            "workflow": "Interfaz de chat general no diseñada para análisis de informes de laboratorio",
            "guided_flow": "Conversación abierta — la calidad depende de cómo formule su prompt",
        },
    }
    _COMP["norya-vs-chatgpt-for-blood-tests"]["es"] = {
        "meta_title": "NoryaAI vs ChatGPT para análisis de sangre — Comparación | NoryaAI",
        "meta_description": "NoryaAI vs ChatGPT para entender resultados de análisis de sangre. Analizador estructurado vs chatbot de IA — lado a lado.",
        "hero_title": "NoryaAI vs ChatGPT para análisis de sangre",
        "hero_sub": "ChatGPT es un potente asistente de IA. NoryaAI está diseñado para análisis de sangre. Una mirada honesta a las fortalezas de cada uno.",
        "quick_answer_title": "En resumen",
        "quick_answer": "ChatGPT puede explicar términos médicos pero no está diseñado para analizar informes de laboratorio. NoryaAI lee sus resultados directamente y produce un resumen estructurado para el médico. Resuelven problemas diferentes.",
        "cells": _comp_cells_es["chatgpt"],
        "helps_title": "Cuándo ChatGPT puede seguir ayudando",
        "helps_sub": "ChatGPT es excelente para muchas tareas.",
        "helps_items": [
            {"icon": "📚", "title": "Educación en salud general", "desc": "ChatGPT es excelente para aprender qué significa un biomarcador o cómo funciona el sistema inmunológico."},
            {"icon": "💡", "title": "Preparar preguntas para el médico", "desc": "Antes de una cita, ChatGPT puede ayudarle a organizar sus pensamientos y preparar preguntas."},
            {"icon": "🔍", "title": "Búsqueda rápida de términos médicos", "desc": "Si encuentra un término desconocido en su informe, ChatGPT puede explicarlo en lenguaje simple."},
        ],
        "faqs": [
            {"q": "¿Puede ChatGPT analizar mis resultados de análisis de sangre?", "a": "ChatGPT puede discutir valores, pero no analiza informes de laboratorio y puede alucinar detalles médicos. NoryaAI está diseñado para análisis estructurado y consistente."},
            {"q": "¿Es NoryaAI una herramienta de diagnóstico?", "a": "No. NoryaAI proporciona explicaciones estructuradas y educativas. Consulte siempre a un médico cualificado."},
            {"q": "¿Están mis datos seguros?", "a": "OpenAI puede almacenar conversaciones para entrenamiento. NoryaAI cumple con RGPD — sus datos están cifrados, nunca se venden ni se usan para entrenamiento."},
        ],
    }
    for slug in ("norya-vs-kantesti", "norya-vs-siphox-health", "norya-vs-wizey", "norya-vs-generic-ai"):
        _COMP[slug]["es"] = _build_minimal_es(slug)


def _build_minimal_es(slug):
    _base = {
        "quick_answer_title": "En resumen",
        "helps_title": "Cuándo puede ayudar", "helps_sub": "Diferentes herramientas para diferentes necesidades.",
    }
    if slug == "norya-vs-kantesti":
        return {**_base,
            "meta_title": "NoryaAI vs Kantesti — Comparación de análisis de sangre | NoryaAI",
            "meta_description": "NoryaAI vs Kantesti para análisis de sangre. Comparación de características de dos plataformas.",
            "hero_title": "NoryaAI vs Kantesti para análisis de sangre",
            "hero_sub": "NoryaAI y Kantesti ayudan a entender resultados de análisis de sangre. Una comparación honesta.",
            "quick_answer": "Kantesti es un servicio de análisis de sangre principalmente para usuarios turcoparlantes. NoryaAI ofrece un flujo multilingüe estructurado con puntuaciones de salud y PDFs para el médico en 9+ idiomas.",
            "cells": {"report_upload": "Acepta resultados para análisis", "reference_ranges": "Proporciona información de rangos de referencia", "units_formatting": "Procesa formatos de laboratorio turcos", "output_structure": "Proporciona resultados en su propio formato", "multilingual": "Principalmente disponible en turco", "doctor_summary": "Formato de informe y opciones de compartir no claramente divulgados", "privacy": "Políticas de datos disponibles en su plataforma", "workflow": "Enfocado en interpretación de resultados de análisis de sangre", "guided_flow": "Ofrece su propio flujo de análisis"},
            "helps_items": [{"icon": "🇹🇷", "title": "Experiencia en turco", "desc": "Kantesti ofrece una interfaz nativa en turco."}, {"icon": "🏥", "title": "Conocimiento de laboratorios locales", "desc": "Familiaridad con formatos de laboratorios turcos."}, {"icon": "📋", "title": "Análisis directo", "desc": "Interpretación sencilla sin necesidades multilingües."}],
            "faqs": [{"q": "¿Qué es Kantesti?", "a": "Una plataforma de análisis de sangre principalmente para usuarios turcoparlantes."}, {"q": "¿NoryaAI está disponible en español?", "a": "Sí. NoryaAI ofrece análisis e informes completos en español y 9+ idiomas más."}, {"q": "¿Es NoryaAI una herramienta de diagnóstico?", "a": "No. Consulte siempre a un médico cualificado."}],
        }
    if slug == "norya-vs-siphox-health":
        return {**_base,
            "meta_title": "NoryaAI vs SiPhox Health — Comparación | NoryaAI",
            "meta_description": "NoryaAI vs SiPhox Health: kits de prueba en casa vs análisis estructurado de informes de laboratorio.",
            "hero_title": "NoryaAI vs SiPhox Health",
            "hero_sub": "SiPhox Health ofrece kits de prueba en casa. NoryaAI analiza sus resultados de laboratorio existentes. Así se comparan.",
            "quick_answer": "SiPhox Health y NoryaAI sirven diferentes etapas de las pruebas de salud. SiPhox proporciona kits para casa, NoryaAI analiza resultados que ya tiene. Pueden complementarse.",
            "cells": {"report_upload": "Resultados de sus propios kits — no para informes externos", "reference_ranges": "Rangos para sus propios paneles", "units_formatting": "Estandarizado en su formato de kit", "output_structure": "Panel dentro de su plataforma", "multilingual": "Principalmente en inglés", "doctor_summary": "Resultados en su plataforma; opciones de exportación no claras", "privacy": "Políticas de datos en su sitio web", "workflow": "Prueba completa: pedir kit, recoger muestra, recibir resultados", "guided_flow": "Flujo de prueba en casa ligado a sus kits"},
            "helps_items": [{"icon": "🏠", "title": "Comodidad en casa", "desc": "SiPhox envía un kit a su puerta."}, {"icon": "📊", "title": "Monitoreo regular", "desc": "Pruebas por suscripción para seguimiento regular."}, {"icon": "🔬", "title": "Paneles seleccionados", "desc": "Paneles diseñados para objetivos de salud específicos."}],
            "faqs": [{"q": "¿Qué es SiPhox Health?", "a": "Ofrece kits de prueba de biomarcadores en casa."}, {"q": "¿Necesito un kit para usar NoryaAI?", "a": "No. NoryaAI funciona con resultados que ya tiene — de cualquier laboratorio."}, {"q": "¿Es NoryaAI una herramienta de diagnóstico?", "a": "No. Consulte siempre a un médico cualificado."}],
        }
    if slug == "norya-vs-wizey":
        return {**_base,
            "meta_title": "NoryaAI vs Wizey — Comparación de análisis de sangre | NoryaAI",
            "meta_description": "NoryaAI vs Wizey para análisis de sangre. Informes estructurados, soporte multilingüe y flujo de trabajo comparados.",
            "hero_title": "NoryaAI vs Wizey para análisis de sangre",
            "hero_sub": "NoryaAI y Wizey ayudan a entender resultados de sangre. Una comparación honesta.",
            "quick_answer": "Wizey ofrece herramientas de análisis de sangre. NoryaAI proporciona un flujo estructurado con puntuaciones de salud, PDFs para el médico e informes multilingües.",
            "cells": {"report_upload": "Acepta resultados para análisis", "reference_ranges": "Proporciona información de referencia", "units_formatting": "Soporte de formato no claramente divulgado", "output_structure": "Análisis en su propio formato", "multilingual": "Soporte de idiomas no claramente divulgado", "doctor_summary": "Opciones de compartir no claramente divulgadas", "privacy": "Políticas de datos en su plataforma", "workflow": "Flujo de interpretación de análisis de sangre", "guided_flow": "Proceso de análisis propio"},
            "helps_items": [{"icon": "📱", "title": "Su enfoque específico", "desc": "Wizey puede ofrecer características que se adapten a sus preferencias."}, {"icon": "🔄", "title": "Perspectiva alternativa", "desc": "Una segunda interpretación puede proporcionar contexto adicional."}, {"icon": "💭", "title": "Preferencia personal", "desc": "La herramienta correcta depende de su flujo de trabajo y necesidades."}],
            "faqs": [{"q": "¿Qué es Wizey?", "a": "Una plataforma de análisis de sangre. Consulte su sitio web para detalles."}, {"q": "¿Cómo se diferencia NoryaAI de Wizey?", "a": "NoryaAI ofrece puntuaciones de salud estructuradas, PDFs con verificación QR e informes en 9+ idiomas."}, {"q": "¿Es NoryaAI una herramienta de diagnóstico?", "a": "No. Consulte siempre a un médico cualificado."}],
        }
    # generic-ai
    return {**_base,
        "meta_title": "NoryaAI vs IA Genérica para análisis de sangre — Comparación | NoryaAI",
        "meta_description": "NoryaAI vs ChatGPT u otros chatbots de IA para resultados de análisis de sangre. Informes estructurados vs respuestas de chat.",
        "hero_title": "NoryaAI vs Chatbots de IA Genérica para análisis de sangre",
        "hero_sub": "Ambos pueden trabajar con datos de laboratorio, pero de manera muy diferente. Una mirada honesta a lo que cada uno ofrece.",
        "quick_answer": "Los chatbots de IA genéricos pueden explicar términos médicos. NoryaAI está diseñado para análisis de sangre: lee su informe, mapea valores a rangos de referencia y produce un resumen estructurado con puntuación de salud. Ambos tienen su lugar, pero resuelven problemas diferentes.",
        "cells": {"report_upload": "Copiar y pegar valores en un prompt esperando que el formato se mantenga", "reference_ranges": "Puede adivinar rangos u omitirlos; sin garantía de coincidencia", "units_formatting": "Sin conocimiento de unidades de laboratorio específicas", "output_structure": "Párrafo libre que varía con cada prompt — sin formato consistente", "multilingual": "Puede traducir texto, pero los matices médicos pueden perderse", "doctor_summary": "Sin informe descargable — tendría que copiar y formatear el chat", "privacy": "Las conversaciones pueden almacenarse para entrenamiento", "workflow": "Interfaz de chat general para cualquier tema", "guided_flow": "Conversación abierta — la calidad depende de su prompt"},
        "helps_title": "Cuándo los chatbots de IA genéricos pueden ayudar", "helps_sub": "No se trata de uno malo y otro bueno. Sirven diferentes propósitos.",
        "helps_items": [{"icon": "📚", "title": "Educación en salud general", "desc": "Excelentes para aprender sobre biomarcadores y conceptos médicos."}, {"icon": "💡", "title": "Preparar preguntas para el médico", "desc": "Antes de una cita, pueden ayudar a estructurar preguntas."}, {"icon": "🔍", "title": "Entender terminología médica", "desc": "Pueden explicar términos desconocidos en lenguaje simple."}],
        "faqs": [{"q": "¿Puede ChatGPT explicar resultados de análisis de sangre?", "a": "Sí, parcialmente. Pero no analiza su informe real, puede alucinar rangos y da respuestas diferentes cada vez. NoryaAI lee su informe directamente."}, {"q": "¿Es NoryaAI una herramienta de diagnóstico?", "a": "No. Consulte siempre a un médico cualificado."}, {"q": "¿Puedo subir un PDF en lugar de copiar valores?", "a": "Sí. NoryaAI acepta PDFs, fotos de informes y texto pegado. Los valores se analizan automáticamente."}],
    }


# ══════════════════════════════════════════════════════════════════
# ITALIAN
# ══════════════════════════════════════════════════════════════════
def _apply_it(_UI, _LABELS, _NORYA, _WHY, _CTA, _HUB, _COMP):
    _UI["it"] = {
        "home": "Home", "compare": "Confronta", "how_it_works": "Come funziona",
        "pricing": "Prezzi", "blog": "Blog", "analyze": "Analizza",
        "faq_heading": "Domande frequenti", "related_heading": "Confronti correlati",
        "badge": "Confronto onesto · NoryaAI",
        "comparison_title": "Confronto fianco a fianco",
        "comparison_sub": "Come i due approcci differiscono nelle funzionalità più importanti per i risultati delle analisi del sangue.",
        "disclaimer": "NoryaAI non fornisce diagnosi mediche. Tutti i contenuti sono solo a scopo educativo e informativo.",
        "privacy": "Privacy", "terms": "Termini di utilizzo",
    }
    _LABELS["it"] = {
        "report_upload": "Caricamento referti", "reference_ranges": "Intervalli di riferimento",
        "units_formatting": "Unità e formato di laboratorio", "output_structure": "Struttura del risultato",
        "multilingual": "Referti multilingue", "doctor_summary": "Riepilogo pronto per il medico",
        "privacy": "Privacy e gestione dei dati", "workflow": "Flusso specifico per analisi del sangue",
        "guided_flow": "Tipo di flusso di lavoro",
    }
    _NORYA["it"] = {
        "report_upload": "Carica PDF, scatta una foto o incolla testo — valori e intervalli vengono analizzati automaticamente",
        "reference_ranges": "Intervalli di riferimento mostrati per ogni valore — normale, basso o alto — chiaramente etichettati",
        "units_formatting": "Riconosce automaticamente le unità di laboratorio comuni, strutture dei pannelli e formati dei risultati",
        "output_structure": "Punteggio di salute strutturato, ripartizione per categorie e marcatori segnalati — coerente ogni volta",
        "multilingual": "Referti completi in 9+ lingue con contesto medico preservato",
        "doctor_summary": "PDF pronto per il medico con verifica QR — stampa, salva o condividi",
        "privacy": "Conforme a GDPR/KVKK — crittografato, mai venduto, mai usato per addestramento",
        "workflow": "Pipeline di caricamento, analisi e referto progettata specificamente per i risultati di laboratorio",
        "guided_flow": "Analisi strutturata e guidata — carica una volta e ottieni un referto completo, nessun prompt necessario",
    }
    _WHY["it"] = {
        "title": "Perché le persone scelgono NoryaAI per le analisi del sangue",
        "sub": "Quando precisione, struttura e un prossimo passo chiaro contano più di una conversazione generica.",
        "items": [
            {"title": "Carica una volta, ottieni un referto strutturato", "desc": "Nessun prompt engineering, nessuna riformattazione. Carica i tuoi risultati e ricevi automaticamente punteggio di salute, categorie e marcatori segnalati."},
            {"title": "Formato coerente per confrontare nel tempo", "desc": "Ogni referto segue la stessa struttura, permettendoti di seguire i cambiamenti e individuare tendenze a colpo d'occhio."},
            {"title": "PDF pronto per il medico da portare davvero", "desc": "Un riepilogo pulito e professionale con verifica QR. Stampa o condividi digitalmente — progettato per il tuo prossimo appuntamento."},
            {"title": "La tua lingua, il tuo referto", "desc": "Scegli tra 9+ lingue e ottieni il tuo referto nella lingua che ti sembra più naturale — con il contesto medico intatto."},
        ],
    }
    _CTA["it"] = {
        "title": "Pronto a provare un referto di analisi del sangue strutturato?",
        "sub": "Carica i tuoi risultati di laboratorio e scopri la differenza di un analizzatore specializzato.",
        "primary": "Carica e analizza", "secondary": "Vedi i prezzi",
        "hero_primary": "Analizza le mie analisi del sangue", "hero_secondary": "Vedi un referto esempio",
    }
    _HUB["it"] = {
        "meta_title": "Confronta NoryaAI — Alternative per analisi del sangue | NoryaAI",
        "meta_description": "Confronta NoryaAI con ChatGPT, Kantesti, SiPhox Health, Wizey e chatbot IA per l'analisi del sangue.",
        "hero_title": "Confronta NoryaAI con gli strumenti di analisi del sangue",
        "hero_sub": "Cerchi lo strumento giusto per capire i tuoi risultati delle analisi del sangue? Abbiamo preparato confronti onesti con diverse alternative.",
        "trust_stats": [
            {"value": "98,7%", "label": "Accuratezza dei risultati", "sub": "Verificata con dati di laboratorio"},
            {"value": "9+", "label": "Lingue", "sub": "Referti completi con contesto medico"},
            {"value": "QR", "label": "PDF verificato", "sub": "Referto condivisibile pronto per il medico"},
        ],
        "cards": [
            {"slug": "norya-vs-chatgpt-for-blood-tests", "name": "ChatGPT", "summary": "Come un analizzatore specializzato si confronta con il chatbot IA più popolare al mondo.", "link_text": "Leggi il confronto completo"},
            {"slug": "norya-vs-kantesti", "name": "Kantesti", "summary": "Due piattaforme di analisi del sangue a confronto — referti strutturati multilingue vs servizio turco.", "link_text": "Leggi il confronto completo"},
            {"slug": "norya-vs-siphox-health", "name": "SiPhox Health", "summary": "Kit di test biomarcatori a domicilio vs analisi strutturata dei tuoi risultati di laboratorio.", "link_text": "Leggi il confronto completo"},
            {"slug": "norya-vs-wizey", "name": "Wizey", "summary": "Il flusso di referti strutturati di NoryaAI confrontato con l'approccio di Wizey.", "link_text": "Leggi il confronto completo"},
            {"slug": "norya-vs-generic-ai", "name": "IA generica", "summary": "Cosa offre un analizzatore specializzato rispetto ai chatbot IA generici.", "link_text": "Leggi il confronto completo"},
        ],
        "hub_faqs": [
            {"q": "Qual è il miglior strumento per capire i risultati delle analisi del sangue?", "a": "Dipende dalle tue esigenze. Per referti strutturati con punteggi di salute e riepiloghi per il medico, NoryaAI è progettato apposta."},
            {"q": "Questi confronti sono giusti e onesti?", "a": "Puntiamo alla trasparenza. Quando le caratteristiche di un concorrente non sono chiaramente divulgate, lo diciamo."},
            {"q": "Posso usare NoryaAI insieme ad altri strumenti?", "a": "Sì. NoryaAI completa il tuo percorso di salute. Consulta sempre un medico qualificato per le decisioni mediche."},
        ],
        "matrix_title": "Confronta gli strumenti fianco a fianco",
        "matrix_sub": "Una panoramica rapida su come ogni strumento affronta l'analisi del sangue.",
        "matrix_row_labels": [
            "Miglior caso d'uso",
            "Flusso di lavoro specifico per analisi del sangue",
            "Caricamento file",
            "Struttura con intervalli di riferimento",
            "Risultato strutturato",
            "Supporto multilingue dei risultati",
            "Referto pronto per il medico / condivisibile",
            "Privacy / inquadramento educativo",
            "Adatto alla preparazione di una visita dal medico",
            "Accuratezza dei risultati",
        ],
        "matrix_columns": [
            {"key": "norya", "name": "NoryaAI", "slug": None},
            {"key": "chatgpt", "name": "ChatGPT", "slug": "norya-vs-chatgpt-for-blood-tests"},
            {"key": "kantesti", "name": "Kantesti", "slug": "norya-vs-kantesti"},
            {"key": "siphox", "name": "SiPhox Health", "slug": "norya-vs-siphox-health"},
            {"key": "wizey", "name": "Wizey", "slug": "norya-vs-wizey"},
            {"key": "generic", "name": "IA generica", "slug": "norya-vs-generic-ai"},
        ],
        "matrix_rows": [
            {"norya": "Analisi del sangue strutturata", "chatgpt": "Domande generali sulla salute", "kantesti": "Interpretazione analisi del sangue", "siphox": "Test biomarcatori a domicilio", "wizey": "Analisi del sangue", "generic": "Domande generali sulla salute"},
            {"norya": "Forte", "chatgpt": "Limitato", "kantesti": "Disponibile", "siphox": "Parziale", "wizey": "Disponibile", "generic": "Limitato"},
            {"norya": "PDF, foto o testo", "chatgpt": "Copia-incolla nel prompt", "kantesti": "Disponibile", "siphox": "Solo kit propri", "wizey": "Non chiaramente divulgato", "generic": "Copia-incolla nel prompt"},
            {"norya": "Forte", "chatgpt": "Limitato", "kantesti": "Parziale", "siphox": "Solo pannelli propri", "wizey": "Non chiaramente divulgato", "generic": "Limitato"},
            {"norya": "Punteggio di salute + categorie", "chatgpt": "Testo libero", "kantesti": "Non chiaramente divulgato", "siphox": "Vista dashboard", "wizey": "Non chiaramente divulgato", "generic": "Testo libero"},
            {"norya": "9+ lingue", "chatgpt": "Parziale", "kantesti": "Principalmente turco", "siphox": "Principalmente inglese", "wizey": "Non chiaramente divulgato", "generic": "Parziale"},
            {"norya": "PDF con verifica QR", "chatgpt": "Non disponibile", "kantesti": "Non chiaramente divulgato", "siphox": "Non chiaramente divulgato", "wizey": "Non chiaramente divulgato", "generic": "Non disponibile"},
            {"norya": "GDPR/KVKK · solo educativo", "chatgpt": "Può essere archiviato per l'addestramento", "kantesti": "Vedi la loro policy", "siphox": "Vedi la loro policy", "wizey": "Vedi la loro policy", "generic": "Può essere archiviato per l'addestramento"},
            {"norya": "Forte", "chatgpt": "Parziale", "kantesti": "Disponibile", "siphox": "Limitato", "wizey": "Non chiaramente divulgato", "generic": "Parziale"},
            {"norya": "98,7% · verificato in laboratorio", "chatgpt": "Non divulgato", "kantesti": "Non divulgato", "siphox": "Non divulgato", "wizey": "Non divulgato", "generic": "Non divulgato"},
        ],
        "suits_title": "Quale strumento è più adatto a chi?",
        "suits_items": [
            {"label": "Analisi del sangue strutturata", "text": "Se desideri un punteggio di salute coerente, marcatori segnalati e un PDF per il medico dai tuoi risultati di laboratorio, NoryaAI è progettato per questo.", "link_slug": None},
            {"label": "Domande generali sulla salute", "text": "Se vuoi fare domande aperte sulla salute o preparare domande per il medico, un chatbot IA come ChatGPT è un'ottima scelta.", "link_slug": "norya-vs-chatgpt-for-blood-tests"},
            {"label": "Confrontare strumenti per referti di laboratorio", "text": "Se stai valutando piattaforme specializzate nell'analisi di referti del sangue, confronta NoryaAI con Kantesti e Wizey per trovare il flusso di lavoro adatto.", "link_slug": "norya-vs-kantesti"},
        ],
    }
    for slug in ("norya-vs-chatgpt-for-blood-tests", "norya-vs-kantesti", "norya-vs-siphox-health", "norya-vs-wizey", "norya-vs-generic-ai"):
        _COMP[slug]["it"] = _build_it_comp(slug)


def _build_it_comp(slug):
    base = {"quick_answer_title": "In breve"}
    if slug == "norya-vs-chatgpt-for-blood-tests":
        return {**base, "meta_title": "NoryaAI vs ChatGPT per le analisi del sangue — Confronto | NoryaAI", "meta_description": "NoryaAI vs ChatGPT per capire i risultati delle analisi del sangue.", "hero_title": "NoryaAI vs ChatGPT per l'analisi del sangue", "hero_sub": "ChatGPT è un potente assistente IA. NoryaAI è progettato per l'analisi del sangue. Uno sguardo onesto ai punti di forza di ciascuno.", "quick_answer": "ChatGPT spiega termini medici ma non analizza i referti di laboratorio. NoryaAI legge i risultati, mappa i valori agli intervalli di riferimento e produce un riepilogo strutturato per il medico.",
            "cells": {"report_upload": "Richiede copia-incolla dei valori in un prompt; nessuna analisi nativa di referti", "reference_ranges": "Può citare intervalli generali o allucinare valori", "units_formatting": "Nessuna consapevolezza delle unità di laboratorio specifiche", "output_structure": "Testo libero che varia ogni volta — nessun formato coerente", "multilingual": "Può tradurre testo su richiesta, ma le sfumature mediche possono perdersi", "doctor_summary": "Nessun referto scaricabile", "privacy": "Le conversazioni possono essere archiviate e usate per l'addestramento da OpenAI", "workflow": "Interfaccia chat generica non progettata per l'analisi di referti", "guided_flow": "Conversazione aperta — la qualità dipende dalla formulazione del prompt"},
            "helps_title": "Quando ChatGPT può ancora aiutare", "helps_sub": "ChatGPT eccelle in molti compiti.",
            "helps_items": [{"icon": "📚", "title": "Educazione sanitaria generale", "desc": "Ottimo per imparare cosa significa un biomarcatore o come funziona il sistema immunitario."}, {"icon": "💡", "title": "Preparare domande per il medico", "desc": "Prima di un appuntamento, può aiutarti a organizzare le domande."}, {"icon": "🔍", "title": "Ricerca rapida di termini medici", "desc": "Spiega termini sconosciuti in linguaggio semplice."}],
            "faqs": [{"q": "ChatGPT può analizzare le mie analisi del sangue?", "a": "Può discutere valori, ma non analizza i referti e può allucinare dettagli. NoryaAI è progettato per un'analisi strutturata e coerente."}, {"q": "NoryaAI è uno strumento diagnostico?", "a": "No. Fornisce spiegazioni strutturate ed educative. Consulta sempre un medico qualificato."}, {"q": "I miei dati sono sicuri?", "a": "NoryaAI è conforme al GDPR — dati crittografati, mai venduti, mai usati per addestramento."}]}
    if slug == "norya-vs-kantesti":
        return {**base, "meta_title": "NoryaAI vs Kantesti — Confronto analisi del sangue | NoryaAI", "meta_description": "NoryaAI vs Kantesti per l'analisi del sangue.", "hero_title": "NoryaAI vs Kantesti per l'analisi del sangue", "hero_sub": "Un confronto onesto tra le due piattaforme.", "quick_answer": "Kantesti serve principalmente utenti di lingua turca. NoryaAI offre un flusso multilingue strutturato con punteggi di salute e PDF per il medico in 9+ lingue.",
            "cells": {"report_upload": "Accetta risultati per analisi", "reference_ranges": "Fornisce informazioni sugli intervalli", "units_formatting": "Gestisce formati di laboratorio turchi", "output_structure": "Risultati nel proprio formato", "multilingual": "Principalmente in turco", "doctor_summary": "Formato referto non chiaramente divulgato", "privacy": "Politiche dati sulla loro piattaforma", "workflow": "Interpretazione risultati analisi del sangue", "guided_flow": "Proprio flusso di analisi"},
            "helps_title": "Quando Kantesti può essere più adatto", "helps_sub": "Strumenti diversi per persone diverse.",
            "helps_items": [{"icon": "🇹🇷", "title": "Esperienza turca", "desc": "Interfaccia nativa turca."}, {"icon": "🏥", "title": "Conoscenza dei laboratori locali", "desc": "Familiarità con formati di laboratorio turchi."}, {"icon": "📋", "title": "Analisi semplice", "desc": "Interpretazione diretta senza esigenze multilingue."}],
            "faqs": [{"q": "Cos'è Kantesti?", "a": "Una piattaforma di analisi del sangue per utenti turchi."}, {"q": "NoryaAI è disponibile in italiano?", "a": "Sì. NoryaAI offre analisi e referti in italiano e 9+ altre lingue."}, {"q": "NoryaAI è uno strumento diagnostico?", "a": "No. Consulta sempre un medico qualificato."}]}
    if slug == "norya-vs-siphox-health":
        return {**base, "meta_title": "NoryaAI vs SiPhox Health — Confronto | NoryaAI", "meta_description": "NoryaAI vs SiPhox Health: kit di test a domicilio vs analisi strutturata.", "hero_title": "NoryaAI vs SiPhox Health", "hero_sub": "SiPhox Health offre kit a domicilio. NoryaAI analizza i tuoi risultati esistenti. Ecco il confronto.", "quick_answer": "Servono fasi diverse dei test di salute. SiPhox fornisce kit, NoryaAI analizza risultati che già hai. Possono completarsi.",
            "cells": {"report_upload": "Risultati dai propri kit — non per referti esterni", "reference_ranges": "Intervalli per i propri pannelli", "units_formatting": "Standardizzato sul proprio formato kit", "output_structure": "Dashboard nella loro piattaforma", "multilingual": "Principalmente in inglese", "doctor_summary": "Risultati nella loro piattaforma; esportazione non chiara", "privacy": "Politiche dati sul loro sito", "workflow": "Test completo: ordina kit, raccogli campione, ricevi risultati", "guided_flow": "Flusso di test a domicilio legato ai loro kit"},
            "helps_title": "Quando SiPhox Health può essere più adatto", "helps_sub": "Servono esigenze diverse.",
            "helps_items": [{"icon": "🏠", "title": "Comodità a casa", "desc": "SiPhox invia un kit a casa tua."}, {"icon": "📊", "title": "Monitoraggio regolare", "desc": "Test in abbonamento per il monitoraggio regolare."}, {"icon": "🔬", "title": "Pannelli selezionati", "desc": "Pannelli progettati per obiettivi di salute specifici."}],
            "faqs": [{"q": "Cos'è SiPhox Health?", "a": "Kit di test biomarcatori a domicilio."}, {"q": "Serve un kit per usare NoryaAI?", "a": "No. NoryaAI funziona con risultati che già hai — da qualsiasi laboratorio."}, {"q": "NoryaAI è uno strumento diagnostico?", "a": "No. Consulta sempre un medico qualificato."}]}
    if slug == "norya-vs-wizey":
        return {**base, "meta_title": "NoryaAI vs Wizey — Confronto analisi del sangue | NoryaAI", "meta_description": "NoryaAI vs Wizey per l'analisi del sangue.", "hero_title": "NoryaAI vs Wizey per l'analisi del sangue", "hero_sub": "Un confronto onesto tra le due piattaforme.", "quick_answer": "Wizey offre strumenti di analisi del sangue. NoryaAI fornisce un flusso strutturato con punteggi di salute, PDF per il medico e referti multilingue.",
            "cells": {"report_upload": "Accetta risultati per analisi", "reference_ranges": "Fornisce informazioni di riferimento", "units_formatting": "Supporto formato non chiaramente divulgato", "output_structure": "Analisi nel proprio formato", "multilingual": "Supporto lingue non chiaramente divulgato", "doctor_summary": "Opzioni di condivisione non chiaramente divulgate", "privacy": "Politiche dati sulla loro piattaforma", "workflow": "Flusso di interpretazione analisi del sangue", "guided_flow": "Proprio processo di analisi"},
            "helps_title": "Quando Wizey può ancora aiutare", "helps_sub": "Strumenti diversi per preferenze diverse.",
            "helps_items": [{"icon": "📱", "title": "Il loro approccio specifico", "desc": "Wizey può offrire funzionalità adatte alle tue preferenze."}, {"icon": "🔄", "title": "Prospettiva alternativa", "desc": "Una seconda interpretazione può fornire contesto aggiuntivo."}, {"icon": "💭", "title": "Preferenza personale", "desc": "Lo strumento giusto dipende dal tuo flusso di lavoro e dalle tue esigenze."}],
            "faqs": [{"q": "Cos'è Wizey?", "a": "Una piattaforma di analisi del sangue. Visita il loro sito per i dettagli."}, {"q": "Come si differenzia NoryaAI da Wizey?", "a": "NoryaAI offre punteggi strutturati, PDF con verifica QR e referti in 9+ lingue."}, {"q": "NoryaAI è uno strumento diagnostico?", "a": "No. Consulta sempre un medico qualificato."}]}
    # generic-ai
    return {**base, "meta_title": "NoryaAI vs IA Generica per analisi del sangue — Confronto | NoryaAI", "meta_description": "NoryaAI vs ChatGPT o altri chatbot IA per i risultati delle analisi del sangue.", "hero_title": "NoryaAI vs Chatbot IA Generici per le analisi del sangue", "hero_sub": "Entrambi possono lavorare con dati di laboratorio — ma in modo molto diverso. Uno sguardo onesto a ciò che ciascuno offre.", "quick_answer": "I chatbot IA generici spiegano termini medici. NoryaAI è progettato per le analisi del sangue: legge il referto, mappa i valori agli intervalli di riferimento e produce un riepilogo strutturato con punteggio di salute.",
        "cells": {"report_upload": "Copiare e incollare i valori in un prompt sperando che il formato tenga", "reference_ranges": "Può indovinare gli intervalli o ometterli", "units_formatting": "Nessuna consapevolezza delle unità di laboratorio", "output_structure": "Paragrafo in testo libero che varia ad ogni prompt", "multilingual": "Può tradurre testo, ma le sfumature mediche possono perdersi", "doctor_summary": "Nessun referto scaricabile", "privacy": "Le conversazioni possono essere archiviate per l'addestramento", "workflow": "Interfaccia chat generica per qualsiasi argomento", "guided_flow": "Conversazione aperta — la qualità dipende dal prompt"},
        "helps_title": "Quando i chatbot IA generici possono ancora aiutare", "helps_sub": "Non si tratta di uno strumento cattivo e uno buono. Servono scopi diversi.",
        "helps_items": [{"icon": "📚", "title": "Educazione sanitaria generale", "desc": "Ottimi per imparare su biomarcatori e concetti medici."}, {"icon": "💡", "title": "Preparare domande per il medico", "desc": "Prima di un appuntamento, possono aiutare a strutturare le domande."}, {"icon": "🔍", "title": "Capire la terminologia medica", "desc": "Spiegano termini sconosciuti in linguaggio semplice."}],
        "faqs": [{"q": "ChatGPT può spiegare i risultati delle analisi del sangue?", "a": "Sì, parzialmente. Ma non analizza il tuo referto reale e può allucinare valori di riferimento. NoryaAI legge il tuo referto direttamente."}, {"q": "NoryaAI è uno strumento diagnostico?", "a": "No. Consulta sempre un medico qualificato."}, {"q": "Posso caricare un PDF invece di copiare i valori?", "a": "Sì. NoryaAI accetta PDF, foto di referti e testo incollato. I valori vengono analizzati automaticamente."}]}


# ══════════════════════════════════════════════════════════════════
# HEBREW / HINDI / ARABIC — compact per-language blocks
# ══════════════════════════════════════════════════════════════════
def _apply_he(_UI, _LABELS, _NORYA, _WHY, _CTA, _HUB, _COMP):
    _UI["he"] = {"home": "דף הבית", "compare": "השוואה", "how_it_works": "איך זה עובד", "pricing": "מחירים", "blog": "בלוג", "analyze": "נתח", "faq_heading": "שאלות נפוצות", "related_heading": "השוואות נוספות", "badge": "השוואה כנה · NoryaAI", "comparison_title": "השוואה זה לצד זה", "comparison_sub": "כיצד שתי הגישות שונות בתכונות החשובות ביותר לתוצאות בדיקות דם.", "disclaimer": "NoryaAI אינו מספק אבחנות רפואיות. כל התוכן הוא למטרות חינוכיות ומידע בלבד.", "privacy": "פרטיות", "terms": "תנאי שימוש"}
    _LABELS["he"] = {"report_upload": "העלאת דוח", "reference_ranges": "טווחי ייחוס", "units_formatting": "יחידות ופורמט מעבדה", "output_structure": "מבנה הפלט", "multilingual": "דוחות רב-לשוניים", "doctor_summary": "סיכום מוכן לרופא", "privacy": "פרטיות וניהול נתונים", "workflow": "תהליך ייעודי לבדיקות דם", "guided_flow": "סוג תהליך עבודה"}
    _NORYA["he"] = {"report_upload": "העלו PDF, צלמו תמונה או הדביקו טקסט — ערכים וטווחים מנותחים אוטומטית", "reference_ranges": "טווחי ייחוס מוצגים לכל ערך — תקין, נמוך או גבוה — מסומנים בבירור", "units_formatting": "מזהה אוטומטית יחידות מעבדה נפוצות, מבני פאנלים ופורמטי תוצאות", "output_structure": "ציון בריאות מובנה, פירוט לפי קטגוריות וסמנים מסומנים — עקבי בכל פעם", "multilingual": "דוחות מלאים ב-9+ שפות עם שמירה על הקשר רפואי", "doctor_summary": "PDF מוכן לרופא עם אימות QR — הדפיסו, שמרו או שתפו", "privacy": "תואם GDPR/KVKK — מוצפן, לא נמכר, לא משמש לאימון", "workflow": "צינור העלאה, ניתוח ודוח שנבנה במיוחד לתוצאות מעבדה", "guided_flow": "ניתוח מובנה ומודרך — העלו פעם אחת וקבלו דוח מלא, ללא צורך בפרומפט"}
    _WHY["he"] = {"title": "למה אנשים בוחרים ב-NoryaAI לבדיקות דם", "sub": "כשדיוק, מבנה וצעד ברור הבא חשובים יותר משיחה כללית.", "items": [{"title": "העלו פעם אחת, קבלו דוח מובנה", "desc": "ללא הנדסת פרומפטים. העלו את תוצאות המעבדה וקבלו אוטומטית ציון בריאות, פירוט קטגוריות וסמנים מסומנים."}, {"title": "פורמט עקבי להשוואה לאורך זמן", "desc": "כל דוח עוקב אחר אותו מבנה, כך שתוכלו לעקוב אחר שינויים ולזהות מגמות במבט."}, {"title": "PDF מוכן לרופא שתוכלו באמת להביא", "desc": "סיכום נקי ומקצועי עם אימות QR. הדפיסו או שתפו דיגיטלית."}, {"title": "השפה שלכם, הדוח שלכם", "desc": "בחרו מ-9+ שפות וקבלו את הדוח בשפה הטבעית לכם — עם הקשר רפואי שלם."}]}
    _CTA["he"] = {"title": "מוכנים לנסות דוח בדיקת דם מובנה?", "sub": "העלו את תוצאות המעבדה שלכם וראו את ההבדל של מנתח ייעודי.", "primary": "העלו ונתחו", "secondary": "צפו במחירים", "hero_primary": "נתחו את בדיקת הדם שלי", "hero_secondary": "צפו בדוח לדוגמה"}
    _HUB["he"] = {
        "meta_title": "השוואת NoryaAI — חלופות לניתוח בדיקות דם | NoryaAI", "meta_description": "השוו את NoryaAI עם ChatGPT, Kantesti, SiPhox Health, Wizey וצ'אטבוטים לניתוח בדיקות דם.",
        "hero_title": "השוו את NoryaAI עם כלי ניתוח בדיקות דם", "hero_sub": "מחפשים את הכלי הנכון להבנת תוצאות בדיקות הדם שלכם? הכנו השוואות כנות עם מספר חלופות פופולריות.",
        "trust_stats": [{"value": "98.7%", "label": "דיוק תוצאות", "sub": "אומת עם נתוני מעבדה"}, {"value": "9+", "label": "שפות", "sub": "דוחות מלאים עם הקשר רפואי"}, {"value": "QR", "label": "PDF מאומת", "sub": "סיכום מוכן לרופא ניתן לשיתוף"}],
        "cards": [{"slug": "norya-vs-chatgpt-for-blood-tests", "name": "ChatGPT", "summary": "כיצד מנתח בדיקות דם ייעודי משתווה לצ'אטבוט ה-AI הפופולרי בעולם.", "link_text": "קראו את ההשוואה המלאה"}, {"slug": "norya-vs-kantesti", "name": "Kantesti", "summary": "שתי פלטפורמות לניתוח בדיקות דם בהשוואה.", "link_text": "קראו את ההשוואה המלאה"}, {"slug": "norya-vs-siphox-health", "name": "SiPhox Health", "summary": "ערכות בדיקה ביתיות מול ניתוח מובנה של תוצאות מעבדה קיימות.", "link_text": "קראו את ההשוואה המלאה"}, {"slug": "norya-vs-wizey", "name": "Wizey", "summary": "תהליך הדוחות המובנה של NoryaAI בהשוואה לגישה של Wizey.", "link_text": "קראו את ההשוואה המלאה"}, {"slug": "norya-vs-generic-ai", "name": "AI גנרי", "summary": "מה מנתח ייעודי מציע בהשוואה לצ'אטבוטים גנריים.", "link_text": "קראו את ההשוואה המלאה"}],
        "hub_faqs": [{"q": "מהו הכלי הטוב ביותר להבנת תוצאות בדיקות דם?", "a": "תלוי בצרכים שלכם. לדוחות מובנים עם ציוני בריאות וסיכומים לרופא, NoryaAI נבנה במיוחד."}, {"q": "האם ההשוואות הללו הוגנות?", "a": "אנו שואפים לשקיפות. כשתכונות של מתחרה אינן גלויות בבירור, אנו אומרים זאת."}, {"q": "האם אפשר להשתמש ב-NoryaAI יחד עם כלים אחרים?", "a": "כן. NoryaAI משלים את תהליך הבריאות שלכם. התייעצו תמיד עם רופא מוסמך."}],
        "matrix_title": "השוו כלים זה לצד זה",
        "matrix_sub": "סקירה מהירה של הגישה של כל כלי לניתוח בדיקות דם.",
        "matrix_row_labels": ["תחום שימוש מיטבי", "תהליך ייעודי לבדיקות דם", "העלאת קבצים", "מודעות לטווחי ייחוס", "פלט מובנה", "תמיכה רב-לשונית", "סיכום מוכן לרופא / ניתן לשיתוף", "פרטיות / מסגרת חינוכית", "מתאים להכנה לביקור אצל רופא", "דיוק תוצאות"],
        "matrix_columns": [{"key": "norya", "name": "NoryaAI", "slug": None}, {"key": "chatgpt", "name": "ChatGPT", "slug": "norya-vs-chatgpt-for-blood-tests"}, {"key": "kantesti", "name": "Kantesti", "slug": "norya-vs-kantesti"}, {"key": "siphox", "name": "SiPhox Health", "slug": "norya-vs-siphox-health"}, {"key": "wizey", "name": "Wizey", "slug": "norya-vs-wizey"}, {"key": "generic", "name": "AI גנרי", "slug": "norya-vs-generic-ai"}],
        "matrix_rows": [
            {"norya": "ניתוח בדיקות דם מובנה", "chatgpt": "שאלות בריאות כלליות", "kantesti": "פרשנות בדיקות דם", "siphox": "בדיקות סמנים ביולוגיים ביתיות", "wizey": "ניתוח בדיקות דם", "generic": "שאלות בריאות כלליות"},
            {"norya": "חזק", "chatgpt": "מוגבל", "kantesti": "זמין", "siphox": "חלקי", "wizey": "זמין", "generic": "מוגבל"},
            {"norya": "PDF, תמונה או טקסט", "chatgpt": "העתק-הדבק לפרומפט", "kantesti": "זמין", "siphox": "ערכות בדיקה משלהם בלבד", "wizey": "לא גלוי בבירור", "generic": "העתק-הדבק לפרומפט"},
            {"norya": "חזק", "chatgpt": "מוגבל", "kantesti": "חלקי", "siphox": "פאנלים משלהם בלבד", "wizey": "לא גלוי בבירור", "generic": "מוגבל"},
            {"norya": "ציון בריאות + קטגוריות", "chatgpt": "טקסט חופשי", "kantesti": "לא גלוי בבירור", "siphox": "תצוגת לוח בקרה", "wizey": "לא גלוי בבירור", "generic": "טקסט חופשי"},
            {"norya": "9+ שפות", "chatgpt": "חלקי", "kantesti": "בעיקר טורקית", "siphox": "בעיקר אנגלית", "wizey": "לא גלוי בבירור", "generic": "חלקי"},
            {"norya": "PDF עם אימות QR", "chatgpt": "לא זמין", "kantesti": "לא גלוי בבירור", "siphox": "לא גלוי בבירור", "wizey": "לא גלוי בבירור", "generic": "לא זמין"},
            {"norya": "GDPR/KVKK · חינוכי בלבד", "chatgpt": "עלול להישמר לאימון", "kantesti": "ראו מדיניות שלהם", "siphox": "ראו מדיניות שלהם", "wizey": "ראו מדיניות שלהם", "generic": "עלול להישמר לאימון"},
            {"norya": "חזק", "chatgpt": "חלקי", "kantesti": "זמין", "siphox": "מוגבל", "wizey": "לא גלוי בבירור", "generic": "חלקי"},
            {"norya": "98.7% · אומת במעבדה", "chatgpt": "לא גלוי", "kantesti": "לא גלוי", "siphox": "לא גלוי", "wizey": "לא גלוי", "generic": "לא גלוי"},
        ],
        "suits_title": "איזה כלי מתאים למי?",
        "suits_items": [
            {"label": "ניתוח בדיקות דם מובנה", "text": "אם אתם רוצים ציון בריאות עקבי, סמנים מסומנים ו-PDF לרופא מתוצאות המעבדה שלכם, NoryaAI נבנה במיוחד לכך.", "link_slug": None},
            {"label": "שאלות בריאות כלליות", "text": "אם אתם רוצים לשאול שאלות פתוחות על בריאות או להכין שאלות לרופא, צ'אטבוט AI כמו ChatGPT הוא בחירה חזקה.", "link_slug": "norya-vs-chatgpt-for-blood-tests"},
            {"label": "השוואת כלים לניתוח דוחות מעבדה", "text": "אם אתם מעריכים פלטפורמות המתמחות בניתוח דוחות דם, השוו את NoryaAI עם Kantesti ו-Wizey.", "link_slug": "norya-vs-kantesti"},
        ],
    }
    for slug in ("norya-vs-chatgpt-for-blood-tests", "norya-vs-kantesti", "norya-vs-siphox-health", "norya-vs-wizey", "norya-vs-generic-ai"):
        _COMP[slug]["he"] = _build_he_comp(slug)

def _build_he_comp(slug):
    b = {"quick_answer_title": "בקצרה"}
    if slug == "norya-vs-chatgpt-for-blood-tests":
        return {**b, "meta_title": "NoryaAI נגד ChatGPT לבדיקות דם — השוואה | NoryaAI", "meta_description": "NoryaAI נגד ChatGPT לניתוח בדיקות דם.", "hero_title": "NoryaAI נגד ChatGPT לניתוח בדיקות דם", "hero_sub": "ChatGPT הוא עוזר AI חזק. NoryaAI נבנה במיוחד לניתוח בדיקות דם. מבט כנה על החוזקות.", "quick_answer": "ChatGPT יכול להסביר מונחים רפואיים אך לא נבנה לנתח דוחות מעבדה. NoryaAI קורא את התוצאות, ממפה ערכים לטווחי ייחוס ומפיק סיכום מובנה מוכן לרופא.",
            "cells": {"report_upload": "דורש העתקה-הדבקה לפרומפט; ללא ניתוח דוחות מקורי", "reference_ranges": "עלול לצטט טווחים כלליים או להזות ערכים", "units_formatting": "ללא מודעות ליחידות מעבדה ספציפיות", "output_structure": "טקסט חופשי שמשתנה כל פעם — ללא פורמט עקבי", "multilingual": "יכול לתרגם טקסט, אך ניואנסים רפואיים עלולים לאבוד", "doctor_summary": "ללא דוח להורדה", "privacy": "שיחות עלולות להישמר לאימון על ידי OpenAI", "workflow": "ממשק צ'אט כללי שלא נועד לניתוח דוחות", "guided_flow": "שיחה פתוחה — האיכות תלויה בניסוח הפרומפט"},
            "helps_title": "מתי ChatGPT עדיין יכול לעזור", "helps_sub": "ChatGPT מצטיין במשימות רבות.",
            "helps_items": [{"icon": "📚", "title": "חינוך בריאותי כללי", "desc": "מצוין ללמוד מה סמן ביולוגי אומר."}, {"icon": "💡", "title": "הכנת שאלות לרופא", "desc": "לפני פגישה, יכול לעזור לארגן שאלות."}, {"icon": "🔍", "title": "חיפוש מונחים רפואיים", "desc": "מסביר מונחים לא מוכרים בשפה פשוטה."}],
            "faqs": [{"q": "האם ChatGPT יכול לנתח את בדיקות הדם שלי?", "a": "ChatGPT יכול לדון בערכים, אך לא מנתח דוחות ועלול להזות פרטים. NoryaAI נבנה לניתוח מובנה ועקבי."}, {"q": "האם NoryaAI כלי אבחון?", "a": "לא. NoryaAI מספק הסברים מובנים וחינוכיים. התייעצו תמיד עם רופא מוסמך."}, {"q": "האם הנתונים שלי בטוחים?", "a": "NoryaAI תואם GDPR — נתונים מוצפנים, לא נמכרים ולא משמשים לאימון."}]}
    if slug == "norya-vs-kantesti":
        return {**b, "meta_title": "NoryaAI נגד Kantesti — השוואה | NoryaAI", "meta_description": "NoryaAI נגד Kantesti לניתוח בדיקות דם.", "hero_title": "NoryaAI נגד Kantesti", "hero_sub": "השוואה כנה בין שתי הפלטפורמות.", "quick_answer": "Kantesti משרת בעיקר דוברי טורקית. NoryaAI מציע דוחות מובנים ב-9+ שפות עם ציוני בריאות ו-PDF לרופא.",
            "cells": {"report_upload": "מקבל תוצאות לניתוח", "reference_ranges": "מספק מידע על טווחי ייחוס", "units_formatting": "מעבד פורמטי מעבדה טורקיים", "output_structure": "תוצאות בפורמט משלו", "multilingual": "בעיקר בטורקית", "doctor_summary": "פורמט דוח לא גלוי בבירור", "privacy": "מדיניות נתונים בפלטפורמה שלהם", "workflow": "פרשנות תוצאות בדיקות דם", "guided_flow": "תהליך ניתוח משלו"},
            "helps_title": "מתי Kantesti עשוי להתאים", "helps_sub": "כלים שונים לאנשים שונים.",
            "helps_items": [{"icon": "🇹🇷", "title": "חוויה בטורקית", "desc": "ממשק טורקי מקורי."}, {"icon": "🏥", "title": "היכרות עם מעבדות מקומיות", "desc": "מכיר פורמטי מעבדה טורקיים."}, {"icon": "📋", "title": "ניתוח פשוט", "desc": "פרשנות ישירה ללא צרכים רב-לשוניים."}],
            "faqs": [{"q": "מה זה Kantesti?", "a": "פלטפורמת ניתוח בדיקות דם בעיקר לדוברי טורקית."}, {"q": "NoryaAI זמין בעברית?", "a": "כן. NoryaAI מציע ניתוח ודוחות מלאים בעברית ו-9+ שפות נוספות."}, {"q": "האם NoryaAI כלי אבחון?", "a": "לא. התייעצו תמיד עם רופא מוסמך."}]}
    if slug == "norya-vs-siphox-health":
        return {**b, "meta_title": "NoryaAI נגד SiPhox Health — השוואה | NoryaAI", "meta_description": "NoryaAI נגד SiPhox Health: ערכות בדיקה ביתיות מול ניתוח מובנה.", "hero_title": "NoryaAI נגד SiPhox Health", "hero_sub": "SiPhox Health מציעה ערכות בדיקה ביתיות. NoryaAI מנתח תוצאות קיימות.", "quick_answer": "שירותים שונים בשלבים שונים. SiPhox מספקת ערכות, NoryaAI מנתח תוצאות שכבר יש לכם. הם יכולים להשלים זה את זה.",
            "cells": {"report_upload": "תוצאות מערכות הבדיקה שלהם — לא לדוחות חיצוניים", "reference_ranges": "טווחים לפאנלים שלהם", "units_formatting": "מתוקנן לפורמט הערכה שלהם", "output_structure": "לוח מחוונים בפלטפורמה שלהם", "multilingual": "בעיקר באנגלית", "doctor_summary": "תוצאות בפלטפורמה; ייצוא לא ברור", "privacy": "מדיניות נתונים באתר שלהם", "workflow": "בדיקה מלאה: הזמנת ערכה, איסוף דגימה, קבלת תוצאות", "guided_flow": "תהליך בדיקה ביתית קשור לערכות שלהם"},
            "helps_title": "מתי SiPhox Health עשוי להתאים", "helps_sub": "צרכים שונים.",
            "helps_items": [{"icon": "🏠", "title": "נוחות ביתית", "desc": "SiPhox שולחת ערכה עד הדלת."}, {"icon": "📊", "title": "מעקב קבוע", "desc": "בדיקות במנוי למעקב סמנים ביולוגיים."}, {"icon": "🔬", "title": "פאנלים מותאמים", "desc": "פאנלים למטרות בריאות ספציפיות."}],
            "faqs": [{"q": "מה זה SiPhox Health?", "a": "ערכות בדיקת סמנים ביולוגיים ביתיות."}, {"q": "צריך ערכה כדי להשתמש ב-NoryaAI?", "a": "לא. NoryaAI עובד עם תוצאות שכבר יש לכם."}, {"q": "האם NoryaAI כלי אבחון?", "a": "לא. התייעצו עם רופא."}]}
    if slug == "norya-vs-wizey":
        return {**b, "meta_title": "NoryaAI נגד Wizey — השוואה | NoryaAI", "meta_description": "NoryaAI נגד Wizey לניתוח בדיקות דם.", "hero_title": "NoryaAI נגד Wizey", "hero_sub": "השוואה כנה בין שתי הפלטפורמות.", "quick_answer": "Wizey מציע כלי ניתוח בדיקות דם. NoryaAI מספק תהליך מובנה עם ציוני בריאות, PDF לרופא ודוחות רב-לשוניים.",
            "cells": {"report_upload": "מקבל תוצאות לניתוח", "reference_ranges": "מספק מידע ייחוס", "units_formatting": "תמיכת פורמט לא גלויה בבירור", "output_structure": "ניתוח בפורמט משלו", "multilingual": "תמיכת שפות לא גלויה בבירור", "doctor_summary": "אפשרויות שיתוף לא גלויות בבירור", "privacy": "מדיניות נתונים בפלטפורמה שלהם", "workflow": "תהליך פרשנות בדיקות דם", "guided_flow": "תהליך ניתוח משלו"},
            "helps_title": "מתי Wizey עשוי לעזור", "helps_sub": "כלים שונים להעדפות שונות.",
            "helps_items": [{"icon": "📱", "title": "הגישה הייחודית שלהם", "desc": "Wizey עשוי להציע תכונות שמתאימות להעדפות שלכם."}, {"icon": "🔄", "title": "פרספקטיבה חלופית", "desc": "פרשנות שנייה מכלי אחר יכולה לספק הקשר נוסף."}, {"icon": "💭", "title": "העדפה אישית", "desc": "הכלי הנכון תלוי בתהליך העבודה ובצרכים שלכם."}],
            "faqs": [{"q": "מה זה Wizey?", "a": "פלטפורמת ניתוח בדיקות דם. בקרו באתר שלהם לפרטים."}, {"q": "מה ההבדל בין NoryaAI ל-Wizey?", "a": "NoryaAI מציע ציוני בריאות מובנים, PDF עם אימות QR ודוחות ב-9+ שפות."}, {"q": "האם NoryaAI כלי אבחון?", "a": "לא. התייעצו עם רופא."}]}
    return {**b, "meta_title": "NoryaAI נגד AI גנרי לבדיקות דם — השוואה | NoryaAI", "meta_description": "NoryaAI נגד צ'אטבוטים גנריים לתוצאות בדיקות דם.", "hero_title": "NoryaAI נגד צ'אטבוטים גנריים לבדיקות דם", "hero_sub": "שניהם יכולים לעבוד עם נתוני מעבדה — אך בצורה שונה מאוד.", "quick_answer": "צ'אטבוטים גנריים יכולים להסביר מונחים. NoryaAI נבנה לבדיקות דם: קורא את הדוח, ממפה ערכים ומפיק סיכום מובנה עם ציון בריאות.",
        "cells": {"report_upload": "להעתיק ולהדביק ערכים לפרומפט ולקוות שהפורמט יחזיק", "reference_ranges": "עלול לנחש טווחים או להשמיט אותם", "units_formatting": "ללא מודעות ליחידות מעבדה", "output_structure": "פסקה חופשית שמשתנה עם כל פרומפט", "multilingual": "יכול לתרגם, אך ניואנסים רפואיים עלולים לאבוד", "doctor_summary": "ללא דוח להורדה", "privacy": "שיחות עלולות להישמר לאימון", "workflow": "ממשק צ'אט כללי לכל נושא", "guided_flow": "שיחה פתוחה — האיכות תלויה בפרומפט"},
        "helps_title": "מתי צ'אטבוטים גנריים עדיין יכולים לעזור", "helps_sub": "לא מדובר בטוב ורע. הם משרתים מטרות שונות.",
        "helps_items": [{"icon": "📚", "title": "חינוך בריאותי כללי", "desc": "מצוינים ללמוד על סמנים ומושגים רפואיים."}, {"icon": "💡", "title": "הכנת שאלות לרופא", "desc": "לפני פגישה, יכולים לעזור לארגן שאלות."}, {"icon": "🔍", "title": "הבנת מונחים רפואיים", "desc": "מסבירים מונחים לא מוכרים בשפה פשוטה."}],
        "faqs": [{"q": "האם ChatGPT יכול להסביר תוצאות בדיקות דם?", "a": "כן, חלקית. אבל לא מנתח את הדוח בפועל ועלול להזות ערכי ייחוס. NoryaAI קורא את הדוח ישירות."}, {"q": "האם NoryaAI כלי אבחון?", "a": "לא. התייעצו עם רופא."}, {"q": "אפשר להעלות PDF במקום להעתיק ערכים?", "a": "כן. NoryaAI מקבל PDF, תמונות דוחות וטקסט. הערכים מנותחים אוטומטית."}]}


def _apply_hi(_UI, _LABELS, _NORYA, _WHY, _CTA, _HUB, _COMP):
    _UI["hi"] = {"home": "होम", "compare": "तुलना", "how_it_works": "यह कैसे काम करता है", "pricing": "मूल्य", "blog": "ब्लॉग", "analyze": "विश्लेषण करें", "faq_heading": "अक्सर पूछे जाने वाले प्रश्न", "related_heading": "संबंधित तुलनाएँ", "badge": "ईमानदार तुलना · NoryaAI", "comparison_title": "आमने-सामने तुलना", "comparison_sub": "रक्त परीक्षण परिणामों के लिए सबसे महत्वपूर्ण सुविधाओं में दोनों दृष्टिकोण कैसे भिन्न हैं।", "disclaimer": "NoryaAI चिकित्सा निदान प्रदान नहीं करता। सभी सामग्री केवल शैक्षिक और सूचनात्मक उद्देश्यों के लिए है।", "privacy": "गोपनीयता", "terms": "उपयोग की शर्तें"}
    _LABELS["hi"] = {"report_upload": "रिपोर्ट अपलोड", "reference_ranges": "संदर्भ श्रेणियाँ", "units_formatting": "इकाइयाँ और लैब प्रारूप", "output_structure": "आउटपुट संरचना", "multilingual": "बहुभाषी रिपोर्ट", "doctor_summary": "डॉक्टर के लिए तैयार सारांश", "privacy": "गोपनीयता और डेटा प्रबंधन", "workflow": "रक्त परीक्षण विशिष्ट कार्यप्रवाह", "guided_flow": "कार्यप्रवाह प्रकार"}
    _NORYA["hi"] = {"report_upload": "PDF अपलोड करें, फोटो लें या टेक्स्ट पेस्ट करें — मान और श्रेणियाँ स्वचालित रूप से पार्स की जाती हैं", "reference_ranges": "हर मान के लिए संदर्भ श्रेणियाँ दिखाई जाती हैं — सामान्य, कम या अधिक — स्पष्ट रूप से लेबल", "units_formatting": "सामान्य लैब इकाइयों, पैनल संरचनाओं और परिणाम प्रारूपों को स्वचालित रूप से पहचानता है", "output_structure": "संरचित स्वास्थ्य स्कोर, श्रेणी विश्लेषण और चिह्नित मार्कर — हर बार सुसंगत", "multilingual": "9+ भाषाओं में पूर्ण रिपोर्ट, चिकित्सा संदर्भ संरक्षित", "doctor_summary": "QR सत्यापन के साथ डॉक्टर के लिए तैयार PDF — प्रिंट करें, सेव करें या साझा करें", "privacy": "GDPR/KVKK अनुपालन — एन्क्रिप्टेड, कभी नहीं बेचा, कभी प्रशिक्षण के लिए उपयोग नहीं", "workflow": "लैब परिणामों के लिए विशेष रूप से निर्मित अपलोड, विश्लेषण और रिपोर्ट पाइपलाइन", "guided_flow": "निर्देशित, संरचित विश्लेषण — एक बार अपलोड करें और पूर्ण रिपोर्ट प्राप्त करें, कोई प्रॉम्प्ट आवश्यक नहीं"}
    _WHY["hi"] = {"title": "लोग रक्त परीक्षण के लिए NoryaAI क्यों चुनते हैं", "sub": "जब सटीकता, संरचना और एक स्पष्ट अगला कदम सामान्य बातचीत से अधिक मायने रखता है।", "items": [{"title": "एक बार अपलोड करें, संरचित रिपोर्ट पाएँ", "desc": "कोई प्रॉम्प्ट इंजीनियरिंग नहीं। अपने लैब परिणाम अपलोड करें और स्वचालित रूप से स्वास्थ्य स्कोर, श्रेणी विश्लेषण और चिह्नित मार्कर प्राप्त करें।"}, {"title": "समय के साथ तुलना के लिए सुसंगत प्रारूप", "desc": "हर रिपोर्ट एक ही संरचना का पालन करती है, जिससे आप परिवर्तनों को ट्रैक कर सकते हैं।"}, {"title": "डॉक्टर के लिए तैयार PDF जो आप वास्तव में ले जा सकते हैं", "desc": "QR सत्यापन के साथ एक साफ, पेशेवर सारांश।"}, {"title": "आपकी भाषा, आपकी रिपोर्ट", "desc": "9+ भाषाओं में से चुनें और अपनी रिपोर्ट उस भाषा में प्राप्त करें जो आपको सबसे स्वाभाविक लगती है।"}]}
    _CTA["hi"] = {"title": "क्या आप एक संरचित रक्त परीक्षण रिपोर्ट आज़माने के लिए तैयार हैं?", "sub": "अपने लैब परिणाम अपलोड करें और एक विशेष विश्लेषक का अंतर देखें।", "primary": "अपलोड करें और विश्लेषण करें", "secondary": "मूल्य देखें", "hero_primary": "मेरा रक्त परीक्षण विश्लेषण करें", "hero_secondary": "नमूना रिपोर्ट देखें"}
    _HUB["hi"] = {
        "meta_title": "NoryaAI तुलना — रक्त परीक्षण विश्लेषण विकल्प | NoryaAI", "meta_description": "NoryaAI की ChatGPT, Kantesti, SiPhox Health, Wizey और AI चैटबॉट से तुलना करें।",
        "hero_title": "NoryaAI की रक्त परीक्षण विश्लेषण उपकरणों से तुलना करें", "hero_sub": "अपने रक्त परीक्षण परिणामों को समझने के लिए सही उपकरण खोज रहे हैं? हमने कई लोकप्रिय विकल्पों के साथ ईमानदार तुलनाएँ तैयार की हैं।",
        "trust_stats": [{"value": "98.7%", "label": "परिणाम सटीकता", "sub": "प्रयोगशाला डेटा से सत्यापित"}, {"value": "9+", "label": "भाषाएँ", "sub": "चिकित्सा संदर्भ के साथ पूर्ण रिपोर्ट"}, {"value": "QR", "label": "सत्यापित PDF", "sub": "डॉक्टर के लिए तैयार साझा करने योग्य सारांश"}],
        "cards": [{"slug": "norya-vs-chatgpt-for-blood-tests", "name": "ChatGPT", "summary": "एक विशेष रक्त परीक्षण विश्लेषक की दुनिया के सबसे लोकप्रिय AI चैटबॉट से तुलना।", "link_text": "पूरी तुलना पढ़ें"}, {"slug": "norya-vs-kantesti", "name": "Kantesti", "summary": "दो रक्त परीक्षण विश्लेषण प्लेटफ़ॉर्म की तुलना।", "link_text": "पूरी तुलना पढ़ें"}, {"slug": "norya-vs-siphox-health", "name": "SiPhox Health", "summary": "घर पर बायोमार्कर टेस्ट किट बनाम मौजूदा लैब परिणामों का संरचित विश्लेषण।", "link_text": "पूरी तुलना पढ़ें"}, {"slug": "norya-vs-wizey", "name": "Wizey", "summary": "NoryaAI का संरचित रिपोर्ट कार्यप्रवाह Wizey के दृष्टिकोण की तुलना में।", "link_text": "पूरी तुलना पढ़ें"}, {"slug": "norya-vs-generic-ai", "name": "सामान्य AI", "summary": "एक विशेष विश्लेषक सामान्य AI चैटबॉट की तुलना में क्या प्रदान करता है।", "link_text": "पूरी तुलना पढ़ें"}],
        "hub_faqs": [{"q": "रक्त परीक्षण परिणामों को समझने के लिए सबसे अच्छा उपकरण कौन सा है?", "a": "यह आपकी आवश्यकताओं पर निर्भर करता है। संरचित रिपोर्ट के लिए NoryaAI विशेष रूप से बनाया गया है।"}, {"q": "क्या ये तुलनाएँ निष्पक्ष हैं?", "a": "हम पारदर्शिता का लक्ष्य रखते हैं। जब किसी प्रतियोगी की सुविधाएँ स्पष्ट नहीं हैं, तो हम इसे बताते हैं।"}, {"q": "क्या मैं NoryaAI को अन्य उपकरणों के साथ उपयोग कर सकता हूँ?", "a": "हाँ। चिकित्सा निर्णयों के लिए हमेशा योग्य डॉक्टर से परामर्श करें।"}],
        "matrix_title": "उपकरणों की आमने-सामने तुलना करें",
        "matrix_sub": "प्रत्येक उपकरण रक्त परीक्षण विश्लेषण को कैसे अपनाता है, इसकी एक त्वरित झलक।",
        "matrix_row_labels": ["सर्वोत्तम उपयोग", "रक्त परीक्षण विशिष्ट कार्यप्रवाह", "फ़ाइल अपलोड", "संदर्भ श्रेणी जागरूकता", "संरचित आउटपुट", "बहुभाषी परिणाम समर्थन", "डॉक्टर के लिए तैयार / साझा करने योग्य सारांश", "गोपनीयता / शैक्षिक ढांचा", "चिकित्सक से मिलने की तैयारी के लिए उपयुक्त", "परिणाम सटीकता"],
        "matrix_columns": [{"key": "norya", "name": "NoryaAI", "slug": None}, {"key": "chatgpt", "name": "ChatGPT", "slug": "norya-vs-chatgpt-for-blood-tests"}, {"key": "kantesti", "name": "Kantesti", "slug": "norya-vs-kantesti"}, {"key": "siphox", "name": "SiPhox Health", "slug": "norya-vs-siphox-health"}, {"key": "wizey", "name": "Wizey", "slug": "norya-vs-wizey"}, {"key": "generic", "name": "सामान्य AI", "slug": "norya-vs-generic-ai"}],
        "matrix_rows": [
            {"norya": "संरचित रक्त परीक्षण विश्लेषण", "chatgpt": "सामान्य स्वास्थ्य प्रश्न", "kantesti": "रक्त परीक्षण व्याख्या", "siphox": "घर पर बायोमार्कर परीक्षण", "wizey": "रक्त परीक्षण विश्लेषण", "generic": "सामान्य स्वास्थ्य प्रश्न"},
            {"norya": "मजबूत", "chatgpt": "सीमित", "kantesti": "उपलब्ध", "siphox": "आंशिक", "wizey": "उपलब्ध", "generic": "सीमित"},
            {"norya": "PDF, फ़ोटो या टेक्स्ट", "chatgpt": "प्रॉम्प्ट में कॉपी-पेस्ट", "kantesti": "उपलब्ध", "siphox": "केवल अपनी किट", "wizey": "स्पष्ट रूप से बताया नहीं गया", "generic": "प्रॉम्प्ट में कॉपी-पेस्ट"},
            {"norya": "मजबूत", "chatgpt": "सीमित", "kantesti": "आंशिक", "siphox": "केवल अपने पैनल", "wizey": "स्पष्ट रूप से बताया नहीं गया", "generic": "सीमित"},
            {"norya": "स्वास्थ्य स्कोर + श्रेणियाँ", "chatgpt": "मुक्त-रूप पाठ", "kantesti": "स्पष्ट रूप से बताया नहीं गया", "siphox": "डैशबोर्ड दृश्य", "wizey": "स्पष्ट रूप से बताया नहीं गया", "generic": "मुक्त-रूप पाठ"},
            {"norya": "9+ भाषाएँ", "chatgpt": "आंशिक", "kantesti": "मुख्य रूप से तुर्की", "siphox": "मुख्य रूप से अंग्रेजी", "wizey": "स्पष्ट रूप से बताया नहीं गया", "generic": "आंशिक"},
            {"norya": "QR सत्यापन के साथ PDF", "chatgpt": "उपलब्ध नहीं", "kantesti": "स्पष्ट रूप से बताया नहीं गया", "siphox": "स्पष्ट रूप से बताया नहीं गया", "wizey": "स्पष्ट रूप से बताया नहीं गया", "generic": "उपलब्ध नहीं"},
            {"norya": "GDPR/KVKK · केवल शैक्षिक", "chatgpt": "प्रशिक्षण के लिए संग्रहित हो सकता है", "kantesti": "उनकी नीति देखें", "siphox": "उनकी नीति देखें", "wizey": "उनकी नीति देखें", "generic": "प्रशिक्षण के लिए संग्रहित हो सकता है"},
            {"norya": "मजबूत", "chatgpt": "आंशिक", "kantesti": "उपलब्ध", "siphox": "सीमित", "wizey": "स्पष्ट रूप से बताया नहीं गया", "generic": "आंशिक"},
            {"norya": "98.7% · प्रयोगशाला सत्यापित", "chatgpt": "अज्ञात", "kantesti": "अज्ञात", "siphox": "अज्ञात", "wizey": "अज्ञात", "generic": "अज्ञात"},
        ],
        "suits_title": "कौन सा उपकरण किसके लिए उपयुक्त है?",
        "suits_items": [
            {"label": "संरचित रक्त परीक्षण विश्लेषण", "text": "यदि आप अपने मौजूदा लैब परिणामों से सुसंगत स्वास्थ्य स्कोर, चिह्नित मार्कर और डॉक्टर के लिए तैयार PDF चाहते हैं, तो NoryaAI इसके लिए विशेष रूप से बनाया गया है।", "link_slug": None},
            {"label": "सामान्य स्वास्थ्य प्रश्न", "text": "यदि आप स्वास्थ्य पर खुले प्रश्न पूछना या डॉक्टर के लिए प्रश्न तैयार करना चाहते हैं, तो ChatGPT जैसा AI चैटबॉट एक अच्छा विकल्प है।", "link_slug": "norya-vs-chatgpt-for-blood-tests"},
            {"label": "लैब रिपोर्ट उपकरणों की तुलना", "text": "यदि आप रक्त परीक्षण रिपोर्ट विश्लेषण में विशेषज्ञ प्लेटफ़ॉर्म का मूल्यांकन कर रहे हैं, तो NoryaAI की Kantesti और Wizey से तुलना करें।", "link_slug": "norya-vs-kantesti"},
        ],
    }
    for slug in ("norya-vs-chatgpt-for-blood-tests", "norya-vs-kantesti", "norya-vs-siphox-health", "norya-vs-wizey", "norya-vs-generic-ai"):
        _COMP[slug]["hi"] = _build_hi_comp(slug)

def _build_hi_comp(slug):
    b = {"quick_answer_title": "संक्षिप्त उत्तर"}
    if slug == "norya-vs-chatgpt-for-blood-tests":
        return {**b, "meta_title": "NoryaAI बनाम ChatGPT रक्त परीक्षण के लिए — तुलना | NoryaAI", "meta_description": "रक्त परीक्षण विश्लेषण के लिए NoryaAI बनाम ChatGPT।", "hero_title": "रक्त परीक्षण विश्लेषण के लिए NoryaAI बनाम ChatGPT", "hero_sub": "ChatGPT एक शक्तिशाली AI सहायक है। NoryaAI रक्त परीक्षण विश्लेषण के लिए बनाया गया है।", "quick_answer": "ChatGPT चिकित्सा शब्दों की व्याख्या कर सकता है लेकिन लैब रिपोर्ट पार्स करने के लिए नहीं बना है। NoryaAI आपके परिणाम सीधे पढ़ता है और संरचित, डॉक्टर के लिए तैयार सारांश बनाता है।",
            "cells": {"report_upload": "प्रॉम्प्ट में मान कॉपी-पेस्ट करने की आवश्यकता; कोई मूल लैब रिपोर्ट विश्लेषण नहीं", "reference_ranges": "सामान्य श्रेणियाँ उद्धृत कर सकता है या मान गढ़ सकता है", "units_formatting": "लैब-विशिष्ट इकाइयों की कोई अंतर्निहित जागरूकता नहीं", "output_structure": "हर बार बदलने वाला मुक्त-रूप पाठ — कोई सुसंगत प्रारूप नहीं", "multilingual": "अनुरोध पर अनुवाद कर सकता है, लेकिन चिकित्सा बारीकियाँ खो सकती हैं", "doctor_summary": "कोई डाउनलोड करने योग्य रिपोर्ट नहीं", "privacy": "बातचीत OpenAI द्वारा प्रशिक्षण के लिए संग्रहित की जा सकती हैं", "workflow": "लैब रिपोर्ट विश्लेषण के लिए न बना सामान्य चैट इंटरफ़ेस", "guided_flow": "खुली बातचीत — गुणवत्ता प्रॉम्प्ट पर निर्भर"},
            "helps_title": "ChatGPT कब मदद कर सकता है", "helps_sub": "ChatGPT कई कार्यों में उत्कृष्ट है।",
            "helps_items": [{"icon": "📚", "title": "सामान्य स्वास्थ्य शिक्षा", "desc": "बायोमार्कर का अर्थ जानने के लिए बढ़िया।"}, {"icon": "💡", "title": "डॉक्टर के लिए प्रश्न तैयार करना", "desc": "अपॉइंटमेंट से पहले प्रश्न व्यवस्थित करने में मदद।"}, {"icon": "🔍", "title": "चिकित्सा शब्दावली", "desc": "अज्ञात शब्दों को सरल भाषा में समझाता है।"}],
            "faqs": [{"q": "क्या ChatGPT मेरे रक्त परीक्षण परिणामों का विश्लेषण कर सकता है?", "a": "ChatGPT मानों पर चर्चा कर सकता है, लेकिन लैब रिपोर्ट का विश्लेषण नहीं करता। NoryaAI संरचित विश्लेषण के लिए बनाया गया है।"}, {"q": "क्या NoryaAI एक निदान उपकरण है?", "a": "नहीं। हमेशा योग्य डॉक्टर से परामर्श करें।"}, {"q": "क्या मेरा डेटा सुरक्षित है?", "a": "NoryaAI GDPR अनुपालन करता है — डेटा एन्क्रिप्टेड है, कभी बेचा नहीं जाता।"}]}
    if slug == "norya-vs-kantesti":
        return {**b, "meta_title": "NoryaAI बनाम Kantesti — तुलना | NoryaAI", "meta_description": "रक्त परीक्षण के लिए NoryaAI बनाम Kantesti।", "hero_title": "NoryaAI बनाम Kantesti", "hero_sub": "दोनों प्लेटफ़ॉर्म की ईमानदार तुलना।", "quick_answer": "Kantesti मुख्य रूप से तुर्की भाषी उपयोगकर्ताओं की सेवा करता है। NoryaAI 9+ भाषाओं में संरचित रिपोर्ट प्रदान करता है।",
            "cells": {"report_upload": "विश्लेषण के लिए परिणाम स्वीकार करता है", "reference_ranges": "संदर्भ श्रेणी जानकारी प्रदान करता है", "units_formatting": "तुर्की लैब प्रारूप संसाधित करता है", "output_structure": "अपने प्रारूप में परिणाम", "multilingual": "मुख्य रूप से तुर्की में", "doctor_summary": "रिपोर्ट प्रारूप स्पष्ट नहीं", "privacy": "उनके प्लेटफ़ॉर्म पर डेटा नीतियाँ", "workflow": "रक्त परीक्षण व्याख्या", "guided_flow": "अपना विश्लेषण कार्यप्रवाह"},
            "helps_title": "Kantesti कब उपयुक्त हो सकता है", "helps_sub": "विभिन्न लोगों के लिए विभिन्न उपकरण।",
            "helps_items": [{"icon": "🇹🇷", "title": "तुर्की अनुभव", "desc": "मूल तुर्की इंटरफ़ेस।"}, {"icon": "🏥", "title": "स्थानीय लैब परिचय", "desc": "तुर्की लैब प्रारूपों से परिचित।"}, {"icon": "📋", "title": "सरल विश्लेषण", "desc": "बहुभाषी आवश्यकताओं के बिना सीधा विश्लेषण।"}],
            "faqs": [{"q": "Kantesti क्या है?", "a": "मुख्य रूप से तुर्की भाषी उपयोगकर्ताओं के लिए रक्त परीक्षण प्लेटफ़ॉर्म।"}, {"q": "क्या NoryaAI हिंदी में उपलब्ध है?", "a": "हाँ। NoryaAI हिंदी और 9+ अन्य भाषाओं में रिपोर्ट प्रदान करता है।"}, {"q": "क्या NoryaAI निदान उपकरण है?", "a": "नहीं। हमेशा डॉक्टर से परामर्श करें।"}]}
    if slug == "norya-vs-siphox-health":
        return {**b, "meta_title": "NoryaAI बनाम SiPhox Health — तुलना | NoryaAI", "meta_description": "NoryaAI बनाम SiPhox Health: घर पर टेस्ट किट बनाम संरचित विश्लेषण।", "hero_title": "NoryaAI बनाम SiPhox Health", "hero_sub": "SiPhox Health घर पर टेस्ट किट प्रदान करता है। NoryaAI मौजूदा परिणामों का विश्लेषण करता है।", "quick_answer": "विभिन्न चरणों में सेवा। SiPhox किट प्रदान करता है, NoryaAI मौजूदा परिणामों का विश्लेषण करता है।",
            "cells": {"report_upload": "अपने किट के परिणाम — बाहरी रिपोर्ट के लिए नहीं", "reference_ranges": "अपने पैनल के लिए श्रेणियाँ", "units_formatting": "अपने किट प्रारूप के अनुसार", "output_structure": "उनके प्लेटफ़ॉर्म में डैशबोर्ड", "multilingual": "मुख्य रूप से अंग्रेजी में", "doctor_summary": "उनके प्लेटफ़ॉर्म में; निर्यात स्पष्ट नहीं", "privacy": "उनकी वेबसाइट पर डेटा नीतियाँ", "workflow": "पूर्ण परीक्षण: किट ऑर्डर, नमूना, परिणाम", "guided_flow": "उनके किट से जुड़ा घर पर परीक्षण"},
            "helps_title": "SiPhox Health कब उपयुक्त हो सकता है", "helps_sub": "विभिन्न आवश्यकताएँ।",
            "helps_items": [{"icon": "🏠", "title": "घर पर सुविधा", "desc": "SiPhox आपके दरवाजे पर किट भेजता है।"}, {"icon": "📊", "title": "नियमित निगरानी", "desc": "नियमित बायोमार्कर ट्रैकिंग के लिए सब्सक्रिप्शन।"}, {"icon": "🔬", "title": "चयनित पैनल", "desc": "विशिष्ट स्वास्थ्य लक्ष्यों के लिए डिज़ाइन।"}],
            "faqs": [{"q": "SiPhox Health क्या है?", "a": "घर पर बायोमार्कर टेस्ट किट।"}, {"q": "क्या NoryaAI के लिए किट चाहिए?", "a": "नहीं। NoryaAI मौजूदा परिणामों के साथ काम करता है।"}, {"q": "क्या NoryaAI निदान उपकरण है?", "a": "नहीं। डॉक्टर से परामर्श करें।"}]}
    if slug == "norya-vs-wizey":
        return {**b, "meta_title": "NoryaAI बनाम Wizey — तुलना | NoryaAI", "meta_description": "रक्त परीक्षण के लिए NoryaAI बनाम Wizey।", "hero_title": "NoryaAI बनाम Wizey", "hero_sub": "दोनों प्लेटफ़ॉर्म की ईमानदार तुलना।", "quick_answer": "Wizey रक्त परीक्षण उपकरण प्रदान करता है। NoryaAI संरचित कार्यप्रवाह के साथ स्वास्थ्य स्कोर, PDF और बहुभाषी रिपोर्ट प्रदान करता है।",
            "cells": {"report_upload": "विश्लेषण के लिए परिणाम स्वीकार करता है", "reference_ranges": "संदर्भ जानकारी प्रदान करता है", "units_formatting": "प्रारूप समर्थन स्पष्ट नहीं", "output_structure": "अपने प्रारूप में विश्लेषण", "multilingual": "भाषा समर्थन स्पष्ट नहीं", "doctor_summary": "साझाकरण विकल्प स्पष्ट नहीं", "privacy": "उनके प्लेटफ़ॉर्म पर डेटा नीतियाँ", "workflow": "रक्त परीक्षण व्याख्या कार्यप्रवाह", "guided_flow": "अपनी विश्लेषण प्रक्रिया"},
            "helps_title": "Wizey कब मदद कर सकता है", "helps_sub": "विभिन्न उपकरण विभिन्न प्राथमिकताओं के लिए।",
            "helps_items": [{"icon": "📱", "title": "उनका विशिष्ट दृष्टिकोण", "desc": "Wizey आपकी प्राथमिकताओं के अनुकूल सुविधाएँ प्रदान कर सकता है।"}, {"icon": "🔄", "title": "वैकल्पिक दृष्टिकोण", "desc": "दूसरे उपकरण से दूसरी व्याख्या अतिरिक्त संदर्भ प्रदान कर सकती है।"}, {"icon": "💭", "title": "व्यक्तिगत प्राथमिकता", "desc": "सही उपकरण आपकी आवश्यकताओं पर निर्भर करता है।"}],
            "faqs": [{"q": "Wizey क्या है?", "a": "रक्त परीक्षण विश्लेषण प्लेटफ़ॉर्म। विवरण के लिए उनकी वेबसाइट देखें।"}, {"q": "NoryaAI Wizey से कैसे अलग है?", "a": "NoryaAI संरचित स्कोर, QR सत्यापन PDF और 9+ भाषाओं में रिपोर्ट प्रदान करता है।"}, {"q": "क्या NoryaAI निदान उपकरण है?", "a": "नहीं। डॉक्टर से परामर्श करें।"}]}
    return {**b, "meta_title": "NoryaAI बनाम सामान्य AI रक्त परीक्षण के लिए — तुलना | NoryaAI", "meta_description": "रक्त परीक्षण के लिए NoryaAI बनाम AI चैटबॉट।", "hero_title": "रक्त परीक्षण के लिए NoryaAI बनाम सामान्य AI चैटबॉट", "hero_sub": "दोनों लैब डेटा के साथ काम कर सकते हैं — लेकिन बहुत अलग तरीके से।", "quick_answer": "सामान्य AI चैटबॉट चिकित्सा शब्दों की व्याख्या कर सकते हैं। NoryaAI रक्त परीक्षण के लिए बना है: रिपोर्ट पढ़ता है, मान मैप करता है और स्वास्थ्य स्कोर के साथ संरचित सारांश बनाता है।",
        "cells": {"report_upload": "प्रॉम्प्ट में मान कॉपी-पेस्ट करें और प्रारूप की उम्मीद करें", "reference_ranges": "श्रेणियाँ अनुमान लगा सकता है या छोड़ सकता है", "units_formatting": "लैब इकाइयों की कोई जागरूकता नहीं", "output_structure": "हर प्रॉम्प्ट पर बदलता मुक्त-रूप पैराग्राफ", "multilingual": "अनुवाद कर सकता है, लेकिन चिकित्सा बारीकियाँ खो सकती हैं", "doctor_summary": "कोई डाउनलोड योग्य रिपोर्ट नहीं", "privacy": "बातचीत प्रशिक्षण के लिए संग्रहित हो सकती हैं", "workflow": "किसी भी विषय के लिए सामान्य चैट इंटरफ़ेस", "guided_flow": "खुली बातचीत — गुणवत्ता प्रॉम्प्ट पर निर्भर"},
        "helps_title": "सामान्य AI चैटबॉट कब मदद कर सकते हैं", "helps_sub": "एक बुरा और एक अच्छा नहीं। वे अलग-अलग उद्देश्यों की सेवा करते हैं।",
        "helps_items": [{"icon": "📚", "title": "सामान्य स्वास्थ्य शिक्षा", "desc": "बायोमार्कर और चिकित्सा अवधारणाओं के बारे में जानने के लिए बढ़िया।"}, {"icon": "💡", "title": "डॉक्टर के लिए प्रश्न तैयार करना", "desc": "अपॉइंटमेंट से पहले प्रश्न व्यवस्थित करने में मदद।"}, {"icon": "🔍", "title": "चिकित्सा शब्दावली समझना", "desc": "अज्ञात शब्दों को सरल भाषा में समझाते हैं।"}],
        "faqs": [{"q": "क्या ChatGPT रक्त परीक्षण परिणाम समझा सकता है?", "a": "हाँ, आंशिक रूप से। लेकिन वास्तविक रिपोर्ट का विश्लेषण नहीं करता। NoryaAI सीधे रिपोर्ट पढ़ता है।"}, {"q": "क्या NoryaAI निदान उपकरण है?", "a": "नहीं। डॉक्टर से परामर्श करें।"}, {"q": "क्या मैं मान कॉपी करने के बजाय PDF अपलोड कर सकता हूँ?", "a": "हाँ। NoryaAI PDF, फ़ोटो और पेस्ट किया गया टेक्स्ट स्वीकार करता है।"}]}


def _apply_ar(_UI, _LABELS, _NORYA, _WHY, _CTA, _HUB, _COMP):
    _UI["ar"] = {"home": "الرئيسية", "compare": "مقارنة", "how_it_works": "كيف يعمل", "pricing": "الأسعار", "blog": "المدونة", "analyze": "تحليل", "faq_heading": "الأسئلة الشائعة", "related_heading": "مقارنات ذات صلة", "badge": "مقارنة صادقة · NoryaAI", "comparison_title": "مقارنة جنبًا إلى جنب", "comparison_sub": "كيف يختلف النهجان في الميزات الأهم لنتائج تحاليل الدم.", "disclaimer": "NoryaAI لا يقدم تشخيصات طبية. جميع المحتويات لأغراض تعليمية ومعلوماتية فقط.", "privacy": "الخصوصية", "terms": "شروط الاستخدام"}
    _LABELS["ar"] = {"report_upload": "رفع التقرير", "reference_ranges": "النطاقات المرجعية", "units_formatting": "الوحدات وتنسيق المختبر", "output_structure": "هيكل المخرجات", "multilingual": "تقارير متعددة اللغات", "doctor_summary": "ملخص جاهز للطبيب", "privacy": "الخصوصية وإدارة البيانات", "workflow": "سير عمل خاص بتحاليل الدم", "guided_flow": "نوع سير العمل"}
    _NORYA["ar"] = {"report_upload": "ارفع PDF أو التقط صورة أو الصق نصًا — يتم تحليل القيم والنطاقات تلقائيًا", "reference_ranges": "النطاقات المرجعية معروضة لكل قيمة — طبيعي أو منخفض أو مرتفع — مُسمَّى بوضوح", "units_formatting": "يتعرف تلقائيًا على وحدات المختبر الشائعة وهياكل اللوحات وتنسيقات النتائج", "output_structure": "درجة صحية منظمة وتصنيف حسب الفئات ومؤشرات مميزة — متسق في كل مرة", "multilingual": "تقارير كاملة بأكثر من 9 لغات مع الحفاظ على السياق الطبي", "doctor_summary": "PDF جاهز للطبيب مع التحقق بـ QR — اطبعه أو احفظه أو شاركه", "privacy": "متوافق مع GDPR/KVKK — مشفر ولا يُباع ولا يُستخدم للتدريب", "workflow": "خط أنابيب رفع وتحليل وتقرير مصمم خصيصًا لنتائج المختبر", "guided_flow": "تحليل منظم وموجه — ارفع مرة واحصل على تقرير كامل بدون حاجة لأي تلقين"}
    _WHY["ar"] = {"title": "لماذا يختار الناس NoryaAI لتحاليل الدم", "sub": "عندما تكون الدقة والبنية والخطوة التالية الواضحة أهم من محادثة عامة.", "items": [{"title": "ارفع مرة واحصل على تقرير منظم", "desc": "بدون هندسة تلقينات. ارفع نتائج المختبر واحصل تلقائيًا على درجة صحية وتصنيف ومؤشرات."}, {"title": "تنسيق متسق للمقارنة بمرور الوقت", "desc": "كل تقرير يتبع نفس البنية لتتبع التغييرات بسهولة."}, {"title": "PDF جاهز للطبيب يمكنك أخذه فعلًا", "desc": "ملخص نظيف ومهني مع التحقق بـ QR."}, {"title": "لغتك، تقريرك", "desc": "اختر من أكثر من 9 لغات واحصل على تقريرك باللغة الأنسب لك."}]}
    _CTA["ar"] = {"title": "هل أنت مستعد لتجربة تقرير تحليل دم منظم؟", "sub": "ارفع نتائج المختبر الخاصة بك واكتشف الفرق مع محلل متخصص.", "primary": "ارفع وحلل", "secondary": "عرض الأسعار", "hero_primary": "حلل تحليل الدم الخاص بي", "hero_secondary": "عرض تقرير نموذجي"}
    _HUB["ar"] = {
        "meta_title": "مقارنة NoryaAI — بدائل تحليل الدم | NoryaAI", "meta_description": "قارن NoryaAI مع ChatGPT و Kantesti و SiPhox Health و Wizey وروبوتات الذكاء الاصطناعي لتحليل الدم.",
        "hero_title": "قارن NoryaAI مع أدوات تحليل الدم", "hero_sub": "هل تبحث عن الأداة المناسبة لفهم نتائج تحاليل الدم؟ أعددنا مقارنات صادقة مع عدة بدائل شائعة.",
        "trust_stats": [{"value": "98.7%", "label": "دقة النتائج", "sub": "تم التحقق بواسطة بيانات مخبرية"}, {"value": "9+", "label": "لغات", "sub": "تقارير كاملة مع سياق طبي"}, {"value": "QR", "label": "PDF موثق", "sub": "ملخص جاهز للطبيب قابل للمشاركة"}],
        "cards": [{"slug": "norya-vs-chatgpt-for-blood-tests", "name": "ChatGPT", "summary": "كيف يقارن محلل تحاليل دم متخصص بأشهر روبوت ذكاء اصطناعي في العالم.", "link_text": "اقرأ المقارنة الكاملة"}, {"slug": "norya-vs-kantesti", "name": "Kantesti", "summary": "منصتان لتحليل الدم في مقارنة.", "link_text": "اقرأ المقارنة الكاملة"}, {"slug": "norya-vs-siphox-health", "name": "SiPhox Health", "summary": "مجموعات اختبار منزلية مقابل تحليل منظم لنتائج المختبر الحالية.", "link_text": "اقرأ المقارنة الكاملة"}, {"slug": "norya-vs-wizey", "name": "Wizey", "summary": "سير عمل التقارير المنظمة لـ NoryaAI مقارنة بنهج Wizey.", "link_text": "اقرأ المقارنة الكاملة"}, {"slug": "norya-vs-generic-ai", "name": "ذكاء اصطناعي عام", "summary": "ما يقدمه محلل متخصص مقارنة بروبوتات الذكاء الاصطناعي العامة.", "link_text": "اقرأ المقارنة الكاملة"}],
        "hub_faqs": [{"q": "ما أفضل أداة لفهم نتائج تحاليل الدم؟", "a": "يعتمد على احتياجاتك. للتقارير المنظمة مع درجات صحية وملخصات للطبيب، NoryaAI مصمم خصيصًا لذلك."}, {"q": "هل هذه المقارنات عادلة؟", "a": "نسعى للشفافية. عندما لا تكون ميزات المنافس واضحة، نذكر ذلك بدلًا من التخمين."}, {"q": "هل يمكنني استخدام NoryaAI مع أدوات أخرى؟", "a": "نعم. استشر دائمًا طبيبًا مؤهلًا للقرارات الطبية."}],
        "matrix_title": "قارن الأدوات جنبًا إلى جنب",
        "matrix_sub": "نظرة سريعة على كيفية تعامل كل أداة مع تحليل تحاليل الدم.",
        "matrix_row_labels": ["أفضل حالة استخدام", "سير عمل مخصص لتحاليل الدم", "رفع الملفات", "الوعي بنطاقات المرجع", "مخرجات منظمة", "دعم النتائج متعدد اللغات", "ملخص جاهز للطبيب / قابل للمشاركة", "الخصوصية / الإطار التعليمي", "مناسب للتحضير لزيارة الطبيب", "دقة النتائج"],
        "matrix_columns": [{"key": "norya", "name": "NoryaAI", "slug": None}, {"key": "chatgpt", "name": "ChatGPT", "slug": "norya-vs-chatgpt-for-blood-tests"}, {"key": "kantesti", "name": "Kantesti", "slug": "norya-vs-kantesti"}, {"key": "siphox", "name": "SiPhox Health", "slug": "norya-vs-siphox-health"}, {"key": "wizey", "name": "Wizey", "slug": "norya-vs-wizey"}, {"key": "generic", "name": "ذكاء اصطناعي عام", "slug": "norya-vs-generic-ai"}],
        "matrix_rows": [
            {"norya": "تحليل تحاليل دم منظم", "chatgpt": "أسئلة صحية عامة", "kantesti": "تفسير تحاليل الدم", "siphox": "اختبارات مؤشرات حيوية منزلية", "wizey": "تحليل تحاليل الدم", "generic": "أسئلة صحية عامة"},
            {"norya": "قوي", "chatgpt": "محدود", "kantesti": "متاح", "siphox": "جزئي", "wizey": "متاح", "generic": "محدود"},
            {"norya": "PDF أو صورة أو نص", "chatgpt": "نسخ ولصق في الأمر", "kantesti": "متاح", "siphox": "أدوات الاختبار الخاصة بهم فقط", "wizey": "غير مُفصح عنه بوضوح", "generic": "نسخ ولصق في الأمر"},
            {"norya": "قوي", "chatgpt": "محدود", "kantesti": "جزئي", "siphox": "لوحاتهم الخاصة فقط", "wizey": "غير مُفصح عنه بوضوح", "generic": "محدود"},
            {"norya": "درجة صحية + فئات", "chatgpt": "نص حر", "kantesti": "غير مُفصح عنه بوضوح", "siphox": "عرض لوحة التحكم", "wizey": "غير مُفصح عنه بوضوح", "generic": "نص حر"},
            {"norya": "9+ لغات", "chatgpt": "جزئي", "kantesti": "بشكل رئيسي التركية", "siphox": "بشكل رئيسي الإنجليزية", "wizey": "غير مُفصح عنه بوضوح", "generic": "جزئي"},
            {"norya": "PDF مع تحقق QR", "chatgpt": "غير متاح", "kantesti": "غير مُفصح عنه بوضوح", "siphox": "غير مُفصح عنه بوضوح", "wizey": "غير مُفصح عنه بوضوح", "generic": "غير متاح"},
            {"norya": "GDPR/KVKK · تعليمي فقط", "chatgpt": "قد يُخزن للتدريب", "kantesti": "راجع سياستهم", "siphox": "راجع سياستهم", "wizey": "راجع سياستهم", "generic": "قد يُخزن للتدريب"},
            {"norya": "قوي", "chatgpt": "جزئي", "kantesti": "متاح", "siphox": "محدود", "wizey": "غير مُفصح عنه بوضوح", "generic": "جزئي"},
            {"norya": "98.7% · تم التحقق مخبريًا", "chatgpt": "غير مُفصح عنه", "kantesti": "غير مُفصح عنه", "siphox": "غير مُفصح عنه", "wizey": "غير مُفصح عنه", "generic": "غير مُفصح عنه"},
        ],
        "suits_title": "أي أداة تناسب من؟",
        "suits_items": [
            {"label": "تحليل تحاليل دم منظم", "text": "إذا كنت تريد درجة صحية متسقة وعلامات مميزة وملف PDF جاهز للطبيب من نتائج مختبرك الحالية، فإن NoryaAI مصمم خصيصًا لذلك.", "link_slug": None},
            {"label": "أسئلة صحية عامة", "text": "إذا كنت تريد طرح أسئلة مفتوحة حول الصحة أو تحضير أسئلة لطبيبك، فإن روبوت محادثة ذكاء اصطناعي مثل ChatGPT خيار قوي.", "link_slug": "norya-vs-chatgpt-for-blood-tests"},
            {"label": "مقارنة أدوات تحليل تقارير المختبر", "text": "إذا كنت تقيّم منصات متخصصة في تحليل تقارير الدم، قارن NoryaAI مع Kantesti وWizey لمعرفة ما يناسب احتياجاتك.", "link_slug": "norya-vs-kantesti"},
        ],
    }
    for slug in ("norya-vs-chatgpt-for-blood-tests", "norya-vs-kantesti", "norya-vs-siphox-health", "norya-vs-wizey", "norya-vs-generic-ai"):
        _COMP[slug]["ar"] = _build_ar_comp(slug)

def _build_ar_comp(slug):
    b = {"quick_answer_title": "الملخص"}
    if slug == "norya-vs-chatgpt-for-blood-tests":
        return {**b, "meta_title": "NoryaAI مقابل ChatGPT لتحاليل الدم — مقارنة | NoryaAI", "meta_description": "NoryaAI مقابل ChatGPT لتحليل تحاليل الدم.", "hero_title": "NoryaAI مقابل ChatGPT لتحليل تحاليل الدم", "hero_sub": "ChatGPT مساعد ذكاء اصطناعي قوي. NoryaAI مصمم خصيصًا لتحليل تحاليل الدم.", "quick_answer": "ChatGPT يشرح المصطلحات الطبية لكنه لم يُصمم لتحليل تقارير المختبر. NoryaAI يقرأ نتائجك ويُنتج ملخصًا منظمًا جاهزًا للطبيب.",
            "cells": {"report_upload": "يتطلب نسخ ولصق القيم في محادثة؛ لا تحليل أصلي لتقارير المختبر", "reference_ranges": "قد يذكر نطاقات عامة أو يختلق قيمًا", "units_formatting": "لا وعي بوحدات المختبر المحددة", "output_structure": "نص حر يتغير في كل مرة — لا تنسيق متسق", "multilingual": "يمكنه الترجمة لكن الفروق الطبية قد تضيع", "doctor_summary": "لا تقرير قابل للتنزيل", "privacy": "المحادثات قد تُخزن للتدريب من قبل OpenAI", "workflow": "واجهة دردشة عامة غير مصممة لتحليل التقارير", "guided_flow": "محادثة مفتوحة — الجودة تعتمد على صياغة التلقين"},
            "helps_title": "متى يمكن أن يساعد ChatGPT", "helps_sub": "ChatGPT ممتاز في مهام كثيرة.",
            "helps_items": [{"icon": "📚", "title": "التثقيف الصحي العام", "desc": "ممتاز لتعلم معاني المؤشرات الحيوية."}, {"icon": "💡", "title": "تحضير أسئلة للطبيب", "desc": "قبل الموعد يمكنه مساعدتك في ترتيب أسئلتك."}, {"icon": "🔍", "title": "البحث عن مصطلحات طبية", "desc": "يشرح المصطلحات غير المألوفة بلغة بسيطة."}],
            "faqs": [{"q": "هل يمكن لـ ChatGPT تحليل نتائج تحاليل الدم؟", "a": "يمكنه مناقشة القيم لكنه لا يحلل التقارير وقد يختلق تفاصيل. NoryaAI مصمم للتحليل المنظم."}, {"q": "هل NoryaAI أداة تشخيص؟", "a": "لا. استشر دائمًا طبيبًا مؤهلًا."}, {"q": "هل بياناتي آمنة؟", "a": "NoryaAI متوافق مع GDPR — البيانات مشفرة ولا تُباع."}]}
    if slug == "norya-vs-kantesti":
        return {**b, "meta_title": "NoryaAI مقابل Kantesti — مقارنة | NoryaAI", "meta_description": "NoryaAI مقابل Kantesti لتحليل تحاليل الدم.", "hero_title": "NoryaAI مقابل Kantesti", "hero_sub": "مقارنة صادقة بين المنصتين.", "quick_answer": "Kantesti يخدم بشكل رئيسي الناطقين بالتركية. NoryaAI يقدم تقارير منظمة بأكثر من 9 لغات.",
            "cells": {"report_upload": "يقبل النتائج للتحليل", "reference_ranges": "يوفر معلومات النطاقات المرجعية", "units_formatting": "يعالج تنسيقات المختبرات التركية", "output_structure": "نتائج بتنسيقه الخاص", "multilingual": "بشكل رئيسي بالتركية", "doctor_summary": "تنسيق التقرير غير واضح", "privacy": "سياسات البيانات على منصتهم", "workflow": "تفسير نتائج تحاليل الدم", "guided_flow": "سير عمل التحليل الخاص بهم"},
            "helps_title": "متى قد يكون Kantesti مناسبًا", "helps_sub": "أدوات مختلفة لأشخاص مختلفين.",
            "helps_items": [{"icon": "🇹🇷", "title": "تجربة تركية", "desc": "واجهة تركية أصلية."}, {"icon": "🏥", "title": "معرفة بالمختبرات المحلية", "desc": "على دراية بتنسيقات المختبرات التركية."}, {"icon": "📋", "title": "تحليل مباشر", "desc": "تفسير مباشر بدون احتياجات متعددة اللغات."}],
            "faqs": [{"q": "ما هو Kantesti؟", "a": "منصة تحليل دم بشكل رئيسي للناطقين بالتركية."}, {"q": "هل NoryaAI متاح بالعربية؟", "a": "نعم. NoryaAI يقدم تحليلات وتقارير كاملة بالعربية وأكثر من 9 لغات أخرى."}, {"q": "هل NoryaAI أداة تشخيص؟", "a": "لا. استشر دائمًا طبيبًا مؤهلًا."}]}
    if slug == "norya-vs-siphox-health":
        return {**b, "meta_title": "NoryaAI مقابل SiPhox Health — مقارنة | NoryaAI", "meta_description": "NoryaAI مقابل SiPhox Health: مجموعات اختبار منزلية مقابل تحليل منظم.", "hero_title": "NoryaAI مقابل SiPhox Health", "hero_sub": "SiPhox Health تقدم مجموعات اختبار منزلية. NoryaAI يحلل نتائجك الحالية.", "quick_answer": "يخدمان مراحل مختلفة. SiPhox توفر مجموعات، NoryaAI يحلل النتائج الموجودة لديك.",
            "cells": {"report_upload": "نتائج من مجموعاتهم — ليس لتقارير خارجية", "reference_ranges": "نطاقات لوحاتهم الخاصة", "units_formatting": "معياري حسب تنسيق مجموعتهم", "output_structure": "لوحة معلومات في منصتهم", "multilingual": "بشكل رئيسي بالإنجليزية", "doctor_summary": "النتائج في منصتهم؛ التصدير غير واضح", "privacy": "سياسات البيانات على موقعهم", "workflow": "اختبار كامل: طلب المجموعة وجمع العينة واستلام النتائج", "guided_flow": "سير عمل اختبار منزلي مرتبط بمجموعاتهم"},
            "helps_title": "متى قد يكون SiPhox Health مناسبًا", "helps_sub": "احتياجات مختلفة.",
            "helps_items": [{"icon": "🏠", "title": "راحة منزلية", "desc": "SiPhox ترسل مجموعة إلى بابك."}, {"icon": "📊", "title": "مراقبة منتظمة", "desc": "اختبارات بالاشتراك لتتبع المؤشرات."}, {"icon": "🔬", "title": "لوحات مختارة", "desc": "لوحات مصممة لأهداف صحية محددة."}],
            "faqs": [{"q": "ما هو SiPhox Health؟", "a": "مجموعات اختبار مؤشرات حيوية منزلية."}, {"q": "هل أحتاج مجموعة لاستخدام NoryaAI؟", "a": "لا. NoryaAI يعمل مع نتائج لديك بالفعل."}, {"q": "هل NoryaAI أداة تشخيص؟", "a": "لا. استشر طبيبًا."}]}
    if slug == "norya-vs-wizey":
        return {**b, "meta_title": "NoryaAI مقابل Wizey — مقارنة | NoryaAI", "meta_description": "NoryaAI مقابل Wizey لتحليل تحاليل الدم.", "hero_title": "NoryaAI مقابل Wizey", "hero_sub": "مقارنة صادقة بين المنصتين.", "quick_answer": "Wizey يقدم أدوات تحليل دم. NoryaAI يوفر سير عمل منظم مع درجات صحية و PDF وتقارير متعددة اللغات.",
            "cells": {"report_upload": "يقبل النتائج للتحليل", "reference_ranges": "يوفر معلومات مرجعية", "units_formatting": "دعم التنسيق غير واضح", "output_structure": "تحليل بتنسيقه الخاص", "multilingual": "دعم اللغات غير واضح", "doctor_summary": "خيارات المشاركة غير واضحة", "privacy": "سياسات البيانات على منصتهم", "workflow": "سير عمل تفسير تحاليل الدم", "guided_flow": "عملية تحليل خاصة بهم"},
            "helps_title": "متى قد يساعد Wizey", "helps_sub": "أدوات مختلفة لتفضيلات مختلفة.",
            "helps_items": [{"icon": "📱", "title": "نهجهم الخاص", "desc": "قد يقدم Wizey ميزات تناسب تفضيلاتك."}, {"icon": "🔄", "title": "منظور بديل", "desc": "تفسير ثانٍ يمكن أن يوفر سياقًا إضافيًا."}, {"icon": "💭", "title": "تفضيل شخصي", "desc": "الأداة المناسبة تعتمد على احتياجاتك."}],
            "faqs": [{"q": "ما هو Wizey؟", "a": "منصة تحليل دم. زوروا موقعهم للتفاصيل."}, {"q": "كيف يختلف NoryaAI عن Wizey؟", "a": "NoryaAI يقدم درجات صحية منظمة و PDF مع تحقق QR وتقارير بأكثر من 9 لغات."}, {"q": "هل NoryaAI أداة تشخيص؟", "a": "لا. استشر طبيبًا."}]}
    return {**b, "meta_title": "NoryaAI مقابل الذكاء الاصطناعي العام لتحاليل الدم — مقارنة | NoryaAI", "meta_description": "NoryaAI مقابل روبوتات الذكاء الاصطناعي العامة لنتائج تحاليل الدم.", "hero_title": "NoryaAI مقابل روبوتات الذكاء الاصطناعي العامة لتحاليل الدم", "hero_sub": "كلاهما يمكنه العمل مع بيانات المختبر — لكن بطريقة مختلفة جدًا.", "quick_answer": "روبوتات الذكاء الاصطناعي العامة تشرح المصطلحات. NoryaAI مصمم لتحاليل الدم: يقرأ التقرير ويُنتج ملخصًا منظمًا مع درجة صحية.",
        "cells": {"report_upload": "نسخ ولصق القيم في محادثة والأمل بثبات التنسيق", "reference_ranges": "قد يخمن النطاقات أو يحذفها", "units_formatting": "لا وعي بوحدات المختبر", "output_structure": "فقرة حرة تتغير مع كل تلقين", "multilingual": "يمكنه الترجمة لكن الدقة الطبية قد تضيع", "doctor_summary": "لا تقرير قابل للتنزيل", "privacy": "المحادثات قد تُخزن للتدريب", "workflow": "واجهة دردشة عامة لأي موضوع", "guided_flow": "محادثة مفتوحة — الجودة تعتمد على التلقين"},
        "helps_title": "متى يمكن أن تساعد روبوتات الذكاء الاصطناعي العامة", "helps_sub": "ليس الأمر أن أحدهما سيئ والآخر جيد. يخدمون أغراضًا مختلفة.",
        "helps_items": [{"icon": "📚", "title": "التثقيف الصحي العام", "desc": "ممتازة لتعلم المؤشرات والمفاهيم الطبية."}, {"icon": "💡", "title": "تحضير أسئلة للطبيب", "desc": "قبل الموعد يمكنها مساعدتك في ترتيب أسئلتك."}, {"icon": "🔍", "title": "فهم المصطلحات الطبية", "desc": "تشرح المصطلحات غير المألوفة بلغة بسيطة."}],
        "faqs": [{"q": "هل يمكن لـ ChatGPT شرح نتائج تحاليل الدم؟", "a": "نعم جزئيًا. لكنه لا يحلل تقريرك الفعلي. NoryaAI يقرأ التقرير مباشرة."}, {"q": "هل NoryaAI أداة تشخيص؟", "a": "لا. استشر طبيبًا."}, {"q": "هل يمكنني رفع PDF بدلًا من نسخ القيم؟", "a": "نعم. NoryaAI يقبل PDF وصور التقارير والنص الملصوق."}]}

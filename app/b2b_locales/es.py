# -*- coding: utf-8 -*-
"""Spanish — full B2B audience pages."""

from __future__ import annotations

from typing import Any

from app.b2b_locales._builder import mk
from app.b2b_locales.faq import faq_for


def build_pages(pages_en: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
    f = faq_for("es")
    return {
        "for-doctors": mk(
            pages_en["for-doctors"],
            faq=f,
            faq_title="Preguntas frecuentes",
            patch={
                "meta_title": "Norya para médicos | Claridad de laboratorio",
                "meta_description": "Informes asistidos de laboratorio a lenguaje: marcadores estructurados, lenguaje sencillo, listo para revisión en 9+ idiomas.",
                "hero_badge": "Para clínicos",
                "hero_title": "Explique análisis complejos en lenguaje comprensible—sin más carga administrativa.",
                "hero_desc": "Norya convierte exportaciones estándar en resúmenes claros y multilingües. Para prácticas de alto volumen en la red de más de 120 hospitales y clínicas.",
                "who_title": "Para quién es",
                "who_desc": "Médicos de atención primaria, especialistas y hospitalistas que necesitan explicaciones rápidas y coherentes.",
                "who_primary": "Clínicas de alto rendimiento y grupos",
                "who_secondary": "Poblaciones multilingües",
                "who_points": ["Flujos ambulatorios y hospitalarios", "Coordinación con laboratorios externos"],
                "benefits_title": "Lo que obtiene",
                "benefits": [
                    {
                        "title": "Consultas más rápidas",
                        "desc": "La agrupación estructurada destaca primero lo relevante en la visita.",
                        "points": ["Diseño orientado a triage", "Menos corrección de dictado", "Mensaje coherente entre visitas"],
                    },
                    {
                        "title": "Lenguaje listo para el paciente",
                        "desc": "Explicaciones claras para entregar o adaptar a sus notas.",
                        "points": ["9+ idiomas de informe", "Redacción conservadora", "Paso de revisión clínica"],
                    },
                    {
                        "title": "Fiabilidad operativa",
                        "desc": "Diseñado para equipos que ya generan más de 2M de informes en la plataforma.",
                        "points": ["Estructura favorable a auditoría", "Camino de seguridad enterprise", "Onboarding dedicado"],
                    },
                    {
                        "title": "Confianza y gobernanza",
                        "desc": "Documentación asistiva—no sustituto del diagnóstico.",
                        "points": ["Revisión con humano en el circuito", "Límites explícitos", "Alineación cumplimiento"],
                    },
                ],
                "workflow_title": "De datos brutos a lenguaje paciente listo para revisión",
                "workflow_steps": [
                    {"title": "Ingesta", "desc": "Recepción segura de CSV/PDF o feeds API."},
                    {"title": "Estructurar", "desc": "Normalización de marcadores con 98,7% precisión de clasificación en evaluación interna."},
                    {"title": "Explicar", "desc": "Generación en lenguaje claro, tono clínico controlado, salida multilingüe."},
                    {"title": "Revisar", "desc": "Aprobación clínica antes de historia o portal."},
                ],
            },
        ),
        "for-clinics": mk(
            pages_en["for-clinics"],
            faq=f,
            faq_title="FAQ clínicas",
            patch={
                "meta_title": "Norya para clínicas | Comunicación de laboratorio",
                "meta_description": "Estandarice explicaciones al paciente entre proveedores, idiomas y turnos sin más personal.",
                "hero_badge": "Para clínicas",
                "hero_title": "Un solo ritmo operativo para la comunicación de laboratorio en cada consulta.",
                "hero_desc": "Una tubería única hacia material multilingüe revisado. Misma calidad de un sitio a redes regionales en más de 50 países.",
                "who_title": "Para operadores clínicos",
                "who_desc": "Dirección médica, operaciones y equipos que modernizan cómo se explican los análisis tras cada extracción.",
                "who_primary": "Redes ambulatorias multi-proveedor",
                "who_secondary": "Alto volumen de flebotomía y seguimiento rápido",
                "who_points": ["Programas CCM/coordinación", "Paneles de salud laboral"],
                "benefits_title": "Resultados que administración mide",
                "benefits": [
                    {
                        "title": "Rendimiento sin agotamiento",
                        "desc": "Automatice el primer borrador de educación al paciente según el patrón de resultados.",
                        "points": ["Escaladas con plantilla", "Entregas amigables por turno", "Menos edición manual"],
                    },
                    {
                        "title": "Voz de marca segura",
                        "desc": "Tono, descargos y glosario centralizados.",
                        "points": ["9+ idiomas listos", "Fragmentos versionados", "Puntos de revisión legal"],
                    },
                    {
                        "title": "Visibilidad para liderazgo",
                        "desc": "Métricas de tiempo y cobertura idiomática en tablero.",
                        "points": ["Telemetría de volumen", "Alineación SLA", "Export para iniciativas QI"],
                    },
                    {
                        "title": "Controles enterprise",
                        "desc": "Revisiones de seguridad alineadas con cumplimiento hospitalario.",
                        "points": ["Hoja de ruta SSO", "Plantillas DPA", "Partner de éxito"],
                    },
                ],
                "workflow_title": "Flujo a escala de clínica",
                "workflow_steps": [
                    {"title": "Entrada", "desc": "Enrutamiento desde LIMS o cargas por lotes con metadatos."},
                    {"title": "Normalizar", "desc": "Unificar analitos y unidades en fuentes mixtas."},
                    {"title": "Generar", "desc": "Borradores multilingües y notas internas."},
                    {"title": "Publicar", "desc": "Tras revisión: portales, impresión en recepción o mensajería segura."},
                ],
            },
        ),
        "for-hospitals": mk(
            pages_en["for-hospitals"],
            faq=f,
            faq_title="FAQ hospitales",
            patch={
                "meta_title": "Norya para hospitales | Capa de lenguaje enterprise",
                "meta_description": "Despliegue comunicación de laboratorio con gobernanza en redes hospitalarias y afiliadas.",
                "hero_badge": "Sistemas hospitalarios",
                "hero_title": "Un solo modelo de gobernanza para cada resultado que sale de su IDN.",
                "hero_desc": "Capa asistiva unificada: terminología coherente, variantes localizadas y operación orientada SOC2 para compras IDN.",
                "who_title": "Con quién trabajamos",
                "who_desc": "CMIO, CNIO, informática de laboratorio y líderes que alinean calidad y volumen.",
                "who_primary": "Redes integradas de prestación",
                "who_secondary": "Hospitales docentes e institutos",
                "who_points": ["Servicios de laboratorio con outreach", "Estrategias híbridas cloud/on-prem"],
                "benefits_title": "Valor del sistema",
                "benefits": [
                    {
                        "title": "Automatización consciente del riesgo",
                        "desc": "Generación con barreras y posicionamiento asistivo explícito.",
                        "points": ["Superposición de políticas", "Escalada a especialistas", "Registros de auditoría inmutables"],
                    },
                    {
                        "title": "Consistencia entre campus",
                        "desc": "Sincronice idiomas, niveles de lectura y lenguaje de escalada.",
                        "points": ["Glosario central", "Excepciones regionales", "Proyectos adyacentes Epic/Cerner"],
                    },
                    {
                        "title": "Excelencia medida",
                        "desc": "Aproveche la misma evaluación interna con 98,7% precisión de clasificación de biomarcadores.",
                        "points": ["Estudios QA antes/después", "Informes de cobertura", "Pilotos de comprensión"],
                    },
                    {
                        "title": "Due diligence de compras",
                        "desc": "Documentación de seguridad y flujos clínicos empaquetados para comités.",
                        "points": ["Preparación BAA", "Resúmenes pen-test", "Manual de implementación"],
                    },
                ],
                "workflow_title": "Despliegue enterprise",
                "workflow_steps": [
                    {"title": "Alinear", "desc": "Sesión conjunta: líneas de servicio, idiomas y routing."},
                    {"title": "Integrar", "desc": "Conectores a middleware e identidad."},
                    {"title": "Validar", "desc": "Paralelo con indicadores y muestreo clínico."},
                    {"title": "Escalar", "desc": "Activación progresiva por campus o afiliado."},
                ],
            },
        ),
        "enterprise-security": mk(
            pages_en["enterprise-security"],
            faq=f,
            faq_title="FAQ seguridad",
            patch={
                "meta_title": "Seguridad empresarial | Norya",
                "meta_description": "Cifrado, controles de acceso y documentación para adopción de la capa asistida Norya.",
                "hero_badge": "Seguridad y cumplimiento",
                "hero_title": "Arquitectura de seguridad para compras en salud.",
                "hero_desc": "Diseñado para entornos regulados: datos por capas, mínimo privilegio y huellas de auditoría para ciclos ISO/SOC.",
                "who_title": "Stakeholders apoyados",
                "who_desc": "CISO, seguridad diagnóstica y contratación que documentan cada subsistema.",
                "who_primary": "Empresas de salud",
                "who_secondary": "Organizaciones de servicios diagnósticos",
                "who_points": ["Huellas cloud e híbridas", "Revisiones legales multinacionales"],
                "benefits_title": "Áreas de control",
                "benefits": [
                    {
                        "title": "Protección de datos",
                        "desc": "Cifrado en tránsito, retención acotada y opciones regionales con su asesoría.",
                        "points": ["TLS 1.2+", "Guía de gestión de claves", "Ventanas de purga"],
                    },
                    {
                        "title": "Gobernanza de acceso",
                        "desc": "SSO enterprise, roles granulares y políticas de sesión.",
                        "points": ["Hoja de ruta SAML/OIDC", "Aprovisionamiento JIT", "Procedimientos break-glass"],
                    },
                    {
                        "title": "Artefactos de aseguramiento",
                        "desc": "Paquete con diagramas, resúmenes pen-test y subprocesadores.",
                        "points": ["Alineación SOC2", "Plantillas DPA", "Runbooks de incidentes"],
                    },
                    {
                        "title": "Alineación clínica",
                        "desc": "Cómo las salidas asistidas permanecen con revisión clínica.",
                        "points": ["Memos de análisis de riesgo", "Narrativas clinical safety", "FAQ legal"],
                    },
                ],
                "workflow_title": "Cómo avanzan las revisiones",
                "workflow_steps": [
                    {"title": "NDA y alcance", "desc": "Papeleo estándar y topología de despliegue."},
                    {"title": "Revisión de arquitectura", "desc": "Flujos, cifrado y subprocesadores."},
                    {"title": "Piloto", "desc": "Producción limitada con registro y monitoreo."},
                    {"title": "Decisión de escala", "desc": "BAA/DPA y configuración regional."},
                ],
            },
        ),
        "clinical-demo": mk(
            pages_en["clinical-demo"],
            faq=f,
            faq_title="FAQ demo",
            patch={
                "meta_title": "Demo clínica | Flujo Norya",
                "meta_description": "De datos estructurados a explicaciones multilingües listas para revisión.",
                "hero_badge": "Evaluación guiada",
                "hero_title": "Flujo clínico real—desde el archivo de laboratorio hasta la copia firmada.",
                "hero_desc": "En 30 minutos alineamos feeds, idiomas y revisión con el pipeline usado en más de 50 países y 120+ hospitales y clínicas.",
                "who_title": "Equipos de evaluación ideales",
                "who_desc": "Innovación clínica, directores de laboratorio y sponsors de salud digital.",
                "who_primary": "Comités directivos multidisciplinarios",
                "who_secondary": "Propietarios de calidad y educación al paciente",
                "who_points": ["Presupuestos de innovación", "Necesidad de pruebas multilingües"],
                "benefits_title": "Qué validará",
                "benefits": [
                    {
                        "title": "Pipeline práctico",
                        "desc": "Cargue muestras anonimizadas y observe estructura, explicación y revisión.",
                        "points": ["Fidelidad de agrupación", "Calidad del idioma", "UX de revisión"],
                    },
                    {
                        "title": "Transparencia de métricas",
                        "desc": "Contextualizamos 98,7% clasificación de biomarcadores internamente—no diagnóstico.",
                        "points": ["QA por biomarcador", "Casos límite", "Hoja de ruta de analitos"],
                    },
                    {
                        "title": "Kits para stakeholders",
                        "desc": "FAQ de seguridad, posicionamiento clínico y rutas de compra.",
                        "points": ["Esquema de diapositivas", "Lista DPA", "Requisitos de integración"],
                    },
                    {
                        "title": "Próximos pasos",
                        "desc": "Alcance piloto, licencias y métricas en una sesión.",
                        "points": ["Supuestos de volumen", "Plan de localización", "Enfoque de formación"],
                    },
                ],
                "workflow_title": "Historia de la demo",
                "workflow_steps": [
                    {"title": "Escenario", "desc": "Elija panel y contexto representativos."},
                    {"title": "Ingesta y normalización", "desc": "Mapeo desde su export típico."},
                    {"title": "Generar", "desc": "Borradores multilingües con anotaciones."},
                    {"title": "P&R", "desc": "Discusión abierta médica, TI y legal."},
                ],
            },
        ),
    }

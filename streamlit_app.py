# streamlit_app.py (v2 - contenido ampliado y diseño mejorado)
import streamlit as st

st.set_page_config(page_title="Fiscalidad, capital y cripto (ES) · Presentación",
                   page_icon="💶", layout="wide")

# ======================= Estilos =======================
PRIMARY = "#0F6CBD"   # azul
ACCENT  = "#16A34A"   # verde
MUTED   = "#6B7280"   # gris
BG_SOFT = "#F3F4F6"

st.markdown(f"""
<style>
:root {{
  --primary: {PRIMARY};
  --accent: {ACCENT};
  --muted: {MUTED};
  --bgsoft: {BG_SOFT};
}}
html, body, [data-testid="stAppViewContainer"] {{
  background-color: var(--bgsoft);
}}
h1, h2, h3 {{
  text-transform: uppercase;
  color: var(--primary);
  margin-top: .25rem;
}}
.small {{ color: var(--muted); font-size: .95rem; }}
.card {{
  background: white; padding: 1.1rem 1.2rem; border-radius: 16px;
  box-shadow: 0 6px 14px rgba(15,108,189,.08);
  border: 1px solid #e5e7eb;
}}
.kpi {{
  font-size: 1.25rem;
  background: white; padding: .9rem 1rem; border-radius: 14px;
  border: 1px solid #e5e7eb; text-align:center
}}
.badge {{
  display:inline-block; padding:.15rem .55rem; border-radius:999px;
  background: rgba(15,108,189,.10); color: var(--primary); font-weight: 600; font-size:.85rem;
}}
.table-like div {{ font-size: 1.0rem; }}
img {{ border-radius: 14px; }}
blockquote {{ border-left: 4px solid var(--primary); padding-left: .75rem; color: #111827; background:#fff; border-radius:8px; }}
</style>
""", unsafe_allow_html=True)

# ======================= Navegación =======================
st.sidebar.title("Navegación")
sections = [
    "PORTADA", "AGENDA",
    "CONTEXTO ECONÓMICO",
    "NOTICIA 1: FIN DE LA GOLDEN VISA",
    "EFECTOS ECONÓMICOS Y FISCALES",
    "NOTICIA 2: CRIPTO Y NUEVA FISCALIDAD",
    "DESAFÍOS TÉCNICOS Y CUMPLIMIENTO",
    "COMPARATIVA GOLDEN VISA vs CRIPTO",
    "CASOS INTERNACIONALES",
    "RECOMENDACIONES DE POLÍTICA PÚBLICA",
    "CONCLUSIONES",
    "REFERENCIAS"
]
sec = st.sidebar.radio("Ir a la sección:", sections, index=0)

# Helper
def header(title, subtitle=None):
    st.markdown(f"<h1>{title}</h1>", unsafe_allow_html=True)
    if subtitle:
        st.markdown(f"<p class='small'>{subtitle}</p>", unsafe_allow_html=True)

# ======================= Contenido =======================
if sec == "PORTADA":
    header(" ", "Añade tu título aquí · Máster en Finanzas")
    st.markdown("**Subtítulo:** Fiscalidad, capital y criptomonedas en España  \n**Ponente:** (tu nombre) · **Fecha:** (hoy)")
    st.image("https://images.unsplash.com/photo-1534438327276-14e5300c3a48?q=80&w=1600&auto=format&fit=crop",
             caption="Madrid, España — Unsplash / Florian Wehde", use_column_width=True)

elif sec == "AGENDA":
    header("Agenda")
    left, right = st.columns([1,1])
    with left:
        st.markdown("""
- Contexto económico
- Noticia 1: fin de la Golden Visa
- Efectos económicos y fiscales
- Noticia 2: cripto y nueva fiscalidad
- Desafíos técnicos y de cumplimiento""")
    with right:
        st.markdown("""
- Comparativa de políticas
- Casos internacionales
- Recomendaciones
- Conclusiones
- Referencias""")
    st.info("Presentación dinámica (~20 minutos). Tono claro y visual.")

elif sec == "CONTEXTO ECONÓMICO":
    header("Contexto económico de España", "Dónde compite España por capital e inversión")
    c1, c2 = st.columns([1.1,1])
    with c1:
        st.markdown("""
<div class='card'>
<b>Panorama reciente</b><br>
• Crecimiento moderado y necesidad de inversión estable.<br>
• Competencia con otras jurisdicciones europeas por atraer capital.<br>
• Tensión estructural: <b>recaudación</b> vs <b>competitividad</b> fiscal.<br><br>
<b>Implicación para la política</b><br>
• Las decisiones fiscales generan señales potentes a grandes patrimonios.<br>
• Importa la <i>estabilidad normativa</i> y la previsibilidad.
</div>
""", unsafe_allow_html=True)
    with c2:
        st.image("https://images.unsplash.com/photo-1454165205744-3b78555e5572?q=80&w=1200&auto=format&fit=crop",
                 caption="Datos y mercados — Unsplash / Carlos Muza", use_column_width=True)

elif sec == "NOTICIA 1: FIN DE LA GOLDEN VISA":
    header("Noticia 1: fin de la Golden Visa", "Cambio de rumbo en atracción de inversión inmobiliaria")
    st.markdown("""
<div class='card'>
<b>Qué era</b> · Residencia para no comunitarios a cambio de inversión (p. ej., ≥ 500.000 € en inmuebles).<br>
<b>Situación</b> · Suspensión del programa en 2025.<br>
<b>Dato citado</b> · Salida estimada de <b>~500 grandes patrimonios</b> con <b>~2.700 M€</b>.<br><br>
<b>Argumentos políticos</b><br>
• Presión sobre la vivienda y precios.<br>
• Búsqueda de mayor equidad fiscal.<br>
• Reorientación de la política de atracción de capital.
</div>
""", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1512914890250-94d1e8b6f10d?q=80&w=1400&auto=format&fit=crop",
             caption="Inversión inmobiliaria — Unsplash / R Architecture", use_column_width=True)

elif sec == "EFECTOS ECONÓMICOS Y FISCALES":
    header("Efectos económicos y fiscales", "Qué podría pasar si se van patrimonios y capital")
    k1, k2, k3 = st.columns(3)
    k1.markdown("<div class='kpi'>Menor IED / menor inversión inmobiliaria</div>", unsafe_allow_html=True)
    k2.markdown("<div class='kpi'>Pérdida de base imponible futura</div>", unsafe_allow_html=True)
    k3.markdown("<div class='kpi'>Efecto señal: cautela o salida de capital</div>", unsafe_allow_html=True)
    st.markdown("""
<div class='card'>
<b>Lectura económica</b><br>
• Subidas bruscas pueden provocar <i>timing</i> defensivo en inversión.<br>
• A medio plazo, la recaudación puede verse afectada si la base imponible migra.<br>
• Pero la equidad fiscal puede mejorar si aumenta el aporte de rentas altas que permanecen.<br><br>
<b>Trade-off</b> · <span class='badge'>Equidad</span> vs <span class='badge'>Competitividad</span>
</div>
""", unsafe_allow_html=True)

elif sec == "NOTICIA 2: CRIPTO Y NUEVA FISCALIDAD":
    header("Noticia 2: cripto y nueva fiscalidad", "Capturar una base impositiva emergente")
    st.markdown("""
<div class='card'>
<b>Propuesta</b> · Aumentar la tributación sobre ganancias en cripto y habilitar embargos sobre criptoactivos por impago.<br>
<b>Marco actual (resumen)</b> · Las plusvalías tributan en la base del ahorro (≈19–26 % según tramos).<br>
<b>Obligaciones</b> · Declaración de tenencias en el extranjero (modelo 721) por encima de umbrales.<br><br>
<b>Motivación</b><br>
• Cerrar brechas de cumplimiento.<br>
• Integrar el ecosistema digital al sistema fiscal.<br>
• Mejorar la trazabilidad y la transparencia.
</div>
""", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1621416894569-0f39f4f2f1dc?q=80&w=1400&auto=format&fit=crop",
             caption="Criptomonedas — Unsplash / Kanchanara", use_column_width=True)

elif sec == "DESAFÍOS TÉCNICOS Y CUMPLIMIENTO":
    header("Desafíos técnicos y de cumplimiento", "Dónde se complica recaudar")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
<div class='card'>
<b>Rastreo</b> · Operaciones en DEX y wallets no custodiadas.<br>
<b>Deslocalización</b> · Cambio rápido de jurisdicción y plataformas.<br>
<b>Datos</b> · Necesidad de analítica blockchain, KYC/AML y cooperación internacional.<br>
<b>Riesgo</b> · Aumentar impuestos sin capacidad de control puede incentivar la opacidad.
</div>
""", unsafe_allow_html=True)
    with c2:
        st.image("https://cdn.pixabay.com/photo/2018/09/05/00/12/blockchain-3652588_1280.jpg",
                 caption="Red descentralizada — Pixabay", use_column_width=True)

elif sec == "COMPARATIVA GOLDEN VISA vs CRIPTO":
    header("Comparativa Golden Visa vs Cripto", "Dos frentes para un mismo objetivo fiscal")
    st.markdown("""
<div class='card table-like'>
<table>
<tr><th>Aspecto</th><th>Golden Visa</th><th>Cripto</th></tr>
<tr><td>Tipo de capital</td><td>Inmobiliario / tradicional</td><td>Digital / altamente móvil</td></tr>
<tr><td>Visibilidad / control</td><td>Alto (registros, notarios)</td><td>Menor (DEX, autocustodia)</td></tr>
<tr><td>Riesgo de fuga</td><td>Medio</td><td>Alto</td></tr>
<tr><td>Objetivo político</td><td>Equidad, vivienda, reputación</td><td>Recaudación, cumplimiento, transparencia</td></tr>
<tr><td>Riesgo colateral</td><td>Menor IED y empleo asociado</td><td>Desplazamiento a otras jurisdicciones</td></tr>
</table>
</div>
""", unsafe_allow_html=True)

elif sec == "CASOS INTERNACIONALES":
    header("Casos internacionales", "Qué hacen otros países para competir por capital")
    st.markdown("""
<div class='card'>
<b>Suiza</b> · Estabilidad regulatoria, hubs cripto (Zug).<br>
<b>Portugal</b> · Ha alternado periodos de trato fiscal favorable a cripto e inversión extranjera.<br>
<b>Singapur</b> · Marco pro-innovación y baja tributación corporativa.<br><br>
<b>Lección</b> · La combinación de <i>claridad regulatoria</i> + <i>estabilidad</i> + <i>incentivos</i> atrae capital sin renunciar a control.
</div>
""", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1465447142348-e9952c393450?q=80&w=1400&auto=format&fit=crop",
             caption="Mapa del mundo — Unsplash / NASA", use_column_width=True)

elif sec == "RECOMENDACIONES DE POLÍTICA PÚBLICA":
    header("Recomendaciones de política pública", "Cómo equilibrar recaudación y atractivo")
    st.markdown("""
<div class='card'>
• Subidas <b>graduales y previsibles</b>, evitando shocks.<br>
• <b>Incentivos</b> a inversión productiva (I+D, tecnología, empleo cualificado).<br>
• <b>Estabilidad normativa</b> y periodos de garantía para grandes inversores.<br>
• <b>Cooperación internacional</b> (intercambio de información, estándares).<br>
• Marco <b>claro</b> para cripto: definiciones, reporting, sanciones, custodia.<br>
• Comunicación pública sobre <b>destino del gasto</b> para reforzar legitimidad.
</div>
""", unsafe_allow_html=True)
    st.image("https://cdn.pixabay.com/photo/2017/08/06/22/32/handshake-2590565_1280.jpg",
             caption="Cooperación — Pixabay", use_column_width=True)

elif sec == "CONCLUSIONES":
    header("Conclusiones", "Idea fuerza para cerrar")
    st.markdown("""
<blockquote>
España está en un punto de equilibrio delicado: necesita recaudar más
sin frenar inversión ni innovación. El diseño fiscal debe ser <b>moderno,
estable y competitivo</b>, diferenciando entre capital <i>visible</i> (tradicional)
y <i>altamente móvil</i> (digital).
</blockquote>
""", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1499914485622-a88fac536970?q=80&w=1400&auto=format&fit=crop",
             caption="Finanzas urbanas — Unsplash / Jason Briscoe", use_column_width=True)

elif sec == "REFERENCIAS":
    header("Referencias")
    st.markdown("""
- Noticias de *El Economista* (25/10/2025) sobre fin de Golden Visa y fiscalidad cripto.  
- EY (2025): suspensión del programa de inversión para residencia en España.  
- Resúmenes de fiscalidad del ahorro aplicable a cripto en España (guías 2025).  
- Imágenes libres: **Unsplash** y **Pixabay** (créditos en pies de foto).  

> Añade los enlaces exactos de tu dossier si necesitas citar de forma canónica.
""")

st.markdown("---")
st.caption("Presentación educativa · Máster en Finanzas · Personaliza la portada con tu título")

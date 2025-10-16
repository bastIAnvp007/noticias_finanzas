# streamlit_app.py — Comparativa & Conclusión (v4, ES)
import streamlit as st

st.set_page_config(page_title="Comparativa & Conclusión · Noticias de Fiscalidad (ES)",
                   page_icon="⚖️", layout="wide")

# ======================= Estilos de alto contraste =======================
PRIMARY = "#0B57D0"   # azul
ACCENT  = "#0F9D58"   # verde
TEXT    = "#0B0F14"   # casi negro
BG      = "#FFFFFF"   # blanco

st.markdown(f"""
<style>
html, body, [data-testid="stAppViewContainer"] {{
  background-color: {BG};
  color: {TEXT};
}}
h1, h2, h3 {{ text-transform: uppercase; color: {PRIMARY}; margin-top:.25rem; }}
.small {{ color: {TEXT}; opacity: .85; font-size: .95rem; }}
.card {{
  background: #FFFFFF; padding: 1.1rem 1.2rem; border-radius: 16px;
  box-shadow: 0 6px 14px rgba(17,24,39,.08);
  border: 1px solid #e5e7eb;
  color: {TEXT};
}}
.badge {{
  display:inline-block; padding:.22rem .6rem; border-radius:999px;
  background: #E8F0FE; color: {PRIMARY}; font-weight:700; font-size:.85rem;
}}
.kpi {{
  font-size: 1.05rem;
  background: #F8FAFF; padding: .9rem 1rem; border-radius: 14px;
  border: 1px solid #dbeafe; text-align:center; color:{PRIMARY}; font-weight:700;
}}
.table {{ border:1px solid #e5e7eb; border-radius:14px; overflow:hidden; }}
.table table {{ width:100%; border-collapse:collapse; }}
.table th, .table td {{ border-bottom:1px solid #e5e7eb; padding:.65rem .8rem; text-align:left; }}
.table th {{ background:#F8FAFF; color:{PRIMARY}; text-transform:uppercase; font-size:.9rem; }}
blockquote {{ border-left: 4px solid {PRIMARY}; padding-left: .75rem; background:#F8FAFF; border-radius:8px; }}
hr {{ border:0; height:1px; background:#e5e7eb; }}
</style>
""", unsafe_allow_html=True)

# ======================= Navegación =======================
st.sidebar.title("Navegación")
sec = st.sidebar.radio("Ir a:", ["PORTADA", "COMPARATIVA: MEDIDAS", "COMPARATIVA: EFECTOS", "CONCLUSIÓN FINAL", "FUENTES"], index=0)
st.sidebar.caption("Presentación educativa · Máster en Finanzas")

# ======================= Contenido =======================
if sec == "PORTADA":
    st.markdown("#  ")
    st.markdown("### (Deja tu **título** aquí)")
    st.markdown("**Subtítulo:** Dos noticias clave de fiscalidad en España — *Golden Visa* y tributación cripto")
    st.markdown("**Ponente:** (tu nombre) · **Fecha:** (hoy)")
    st.markdown("---")
    st.markdown("#### Qué verás")
    col1, col2, col3 = st.columns(3)
    with col1: st.markdown("<div class='kpi'>Visa Golden ✈️🏠</div>", unsafe_allow_html=True)
    with col2: st.markdown("<div class='kpi'>Cripto & Impuestos 🪙📈</div>", unsafe_allow_html=True)
    with col3: st.markdown("<div class='kpi'>Comparativa & Conclusión ⚖️</div>", unsafe_allow_html=True)

elif sec == "COMPARATIVA: MEDIDAS":
    st.markdown("## Comparativa entre medidas")
    st.markdown("<div class='badge'>Naturaleza · Objetivos · Población · Capital</div>", unsafe_allow_html=True)
    st.markdown("<div class='table'>", unsafe_allow_html=True)
    st.markdown("""
<table>
<tr><th>Aspecto</th><th>Fin de la Golden Visa</th><th>Fiscalidad cripto (propuesta de Sumar)</th></tr>
<tr><td><b>Naturaleza</b></td><td>Elimina un incentivo migratorio/fiscal ligado a inversión inmobiliaria.</td>
<td>Endurece la tributación y el control sobre ganancias digitales.</td></tr>
<tr><td><b>Objetivo</b></td><td>Equidad y acceso a vivienda; frenar especulación inmobiliaria.</td>
<td>Justicia fiscal digital; aumentar recaudación y cumplimiento.</td></tr>
<tr><td><b>Población afectada</b></td><td>Grandes patrimonios extranjeros e inversores inmobiliarios.</td>
<td>Inversores/residentes con ganancias en criptoactivos.</td></tr>
<tr><td><b>Tipo de capital</b></td><td>Tradicional y tangible (inmuebles).</td>
<td>Digital e intangible (cripto, DeFi, tokens).</td></tr>
</table>
""", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

elif sec == "COMPARATIVA: EFECTOS":
    st.markdown("## Efectos y trade-offs")
    st.markdown("<div class='badge'>Efectos inmediatos · Riesgos · Comparativa internacional · Enfoque común</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
<div class='card'>
<b>Golden Visa — efectos</b><br>
• Menos inversión inmobiliaria y consumo asociado.<br>
• Posible salida de ~500 patrimonios y ~2.700 M€ (estimaciones de prensa).<br>
• Señal de menor “amistad” al capital especulativo.<br><br>
<b>Riesgo</b> · Pérdida de competitividad inmobiliaria frente a países que mantienen programas similares.
</div>
""", unsafe_allow_html=True)
    with col2:
        st.markdown("""
<div class='card'>
<b>Cripto — efectos</b><br>
• Mayor recaudación y trazabilidad si suben tipos y hay cooperación de plataformas.<br>
• Posible deslocalización de actividad cripto (empresas y traders).<br>
• Necesidad de más capacidad técnica (trazabilidad, DAC8, KYC/AML).<br><br>
<b>Riesgo</b> · Fuga de capital digital y freno a startups Web3 si el entorno se percibe hostil.
</div>
""", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""
<div class='card'>
<b>Enfoque común</b><br>
Ambas políticas refuerzan la <i>progresividad</i> y la <i>equidad</i> del sistema fiscal.<br>
El dilema es no erosionar la <b>competitividad</b> ni la <b>innovación</b> al mismo tiempo.
</div>
""", unsafe_allow_html=True)

elif sec == "CONCLUSIÓN FINAL":
    st.markdown("## Conclusión final")
    st.markdown("""
<blockquote>
España transita desde un modelo de atracción de capital hacia uno de <b>justicia fiscal</b> más marcada,
que alcanza tanto al capital tradicional (inmuebles) como al digital (cripto).<br><br>
El reto estratégico es diseñar un marco <b>estable y competitivo</b> que <b>recaude con equidad</b> sin
desincentivar la inversión y la innovación.
</blockquote>
""", unsafe_allow_html=True)
    st.markdown("<div class='kpi'>Claves: Estabilidad normativa · Incentivos a inversión productiva · Cooperación internacional</div>", unsafe_allow_html=True)

elif sec == "FUENTES":
    st.markdown("## Fuentes")
    st.markdown("""
- El Economista (25/10/2025): fin de la Golden Visa; fiscalidad cripto.  
- EY (2025): suspensión del programa de inversión para residencia.  
- Resúmenes de fiscalidad del ahorro aplicable a cripto en España (2024–2025).  
""")
    st.info("Añade aquí los enlaces completos de tu dossier para la versión final que enviarás al profesor.")

st.markdown("---")
st.caption("Comparativa & Conclusión · Listo para presentar en clase · Personaliza textos si lo necesitas")

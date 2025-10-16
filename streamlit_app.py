# streamlit_app.py
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Presentación: Fiscalidad, capital y cripto (ES)",
                   page_icon="💶", layout="centered")

# ---------- Sidebar / Navegación ----------
st.sidebar.title("Navegación")
secciones = [
    "PORTADA", "AGENDA", "CONTEXTO ECONÓMICO",
    "NOTICIA 1: GOLDEN VISA", "EFECTOS ECONÓMICOS",
    "NOTICIA 2: CRIPTOMONEDAS", "DESAFÍOS Y OPORTUNIDADES",
    "COMPARATIVA", "CASOS INTERNACIONALES",
    "RECOMENDACIONES", "CONCLUSIONES", "REFERENCIAS"
]
sec = st.sidebar.radio("Ir a la sección:", secciones, index=0)
st.sidebar.markdown("---")
st.sidebar.info("Modo presentación dinámico. Usa las flechas del teclado o el menú para avanzar.")

# Paleta suave
PRIMARY = "#0F6CBD"
ACCENT = "#00A676"
MUTED = "#6B7280"

def titulo(texto):
    st.markdown(f"<h1 style='text-transform:uppercase;color:{PRIMARY};margin-top:0'>{texto}</h1>", unsafe_allow_html=True)

def subtitulo(texto):
    st.markdown(f"<h3 style='color:{ACCENT};margin-top:0.25rem'>{texto}</h3>", unsafe_allow_html=True)

# ---------- Secciones ----------
if sec == "PORTADA":
    titulo(" ")
    subtitulo("Fiscalidad, capital y criptomonedas en España")
    st.write("**Máster en Finanzas** · Añade tu nombre y fecha")
    st.image("https://images.unsplash.com/photo-1534438327276-14e5300c3a48?q=80&w=1600&auto=format&fit=crop",
             caption="Madrid, España — Unsplash/Florian Wehde", use_column_width=True)

elif sec == "AGENDA":
    titulo("Agenda")
    st.markdown("""
1. Contexto económico actual  
2. Noticia 1: Fin de la Golden Visa  
3. Efectos económicos y fiscales  
4. Noticia 2: Criptomonedas y nueva fiscalidad  
5. Desafíos y oportunidades  
6. Comparativa  
7. Casos internacionales  
8. Recomendaciones  
9. Conclusiones  
10. Preguntas
""")

elif sec == "CONTEXTO ECONÓMICO":
    titulo("Contexto económico de España")
    st.write("- Crecimiento moderado; presión fiscal creciente.")
    st.write("- Competencia global por atraer inversión extranjera.")
    st.write("- Necesidad de equilibrio entre **recaudación** y **competitividad**.")
    st.image("https://images.unsplash.com/photo-1454165205744-3b78555e5572?q=80&w=1600&auto=format&fit=crop",
             caption="Datos y mercados — Unsplash/Carlos Muza", use_column_width=True)

elif sec == "NOTICIA 1: GOLDEN VISA":
    titulo("Noticia 1: fin de la golden visa")
    st.write("- Suspensión del programa de residencia para inversores (2025).")
    st.write("- La inversión mínima habitual: 500.000 € en inmuebles.")
    st.write("- Se reporta salida de **500 patrimonios** con **2.700 M€**.")
    st.image("https://images.unsplash.com/photo-1512914890250-94d1e8b6f10d?q=80&w=1600&auto=format&fit=crop",
             caption="Inversión inmobiliaria — Unsplash/R Architecture", use_column_width=True)

elif sec == "EFECTOS ECONÓMICOS":
    titulo("Efectos económicos y fiscales")
    col1, col2 = st.columns(2)
    with col1:
        st.write("- Fuga de capitales / menor IED.")
        st.write("- Pérdida de base imponible futura.")
        st.write("- Debate: **equidad vs. competitividad**.")
    with col2:
        # Gráfico simple de barras para ilustrar 2.700 M€ (no datos históricos)
        fig, ax = plt.subplots()
        ax.bar(["Capital saliente"], [2700])
        ax.set_ylabel("Millones de €")
        ax.set_title("Estimación de capital que sale")
        st.pyplot(fig)

elif sec == "NOTICIA 2: CRIPTOMONEDAS":
    titulo("Noticia 2: impuestos a criptomonedas")
    st.write("- Propuesta de mayor tributación a ganancias cripto.")
    st.write("- Posibilidad de embargar criptoactivos por impago.")
    st.write("- Hoy tributan como ganancias del ahorro (~19–26 % según tramos).")
    st.image("https://images.unsplash.com/photo-1621416894569-0f39f4f2f1dc?q=80&w=1600&auto=format&fit=crop",
             caption="Criptomonedas — Unsplash/Kanchanara", use_column_width=True)

elif sec == "DESAFÍOS Y OPORTUNIDADES":
    titulo("Desafíos y oportunidades")
    st.write("- Trazabilidad compleja en entornos descentralizados.")
    st.write("- Riesgo de deslocalización de actividad digital.")
    st.write("- Oportunidad: modernizar regulación, más transparencia y recaudación.")
    st.image("https://cdn.pixabay.com/photo/2018/09/05/00/12/blockchain-3652588_1280.jpg",
             caption="Blockchain — Pixabay", use_column_width=True)

elif sec == "COMPARATIVA":
    titulo("Comparativa")
    st.table({
        "Aspecto": ["Tipo de capital", "Control", "Riesgo de fuga", "Objetivo"],
        "Golden Visa": ["Inmobiliario", "Alto", "Medio", "Equidad / vivienda"],
        "Cripto": ["Digital", "Bajo", "Alto", "Recaudación y control"]
    })

elif sec == "CASOS INTERNACIONALES":
    titulo("Casos internacionales")
    st.write("- **Suiza**: entorno estable y cripto-friendly.")
    st.write("- **Portugal**: atracción fiscal en periodos recientes.")
    st.write("- **Singapur**: innovación + marco competitivo.")
    st.image("https://images.unsplash.com/photo-1465447142348-e9952c393450?q=80&w=1600&auto=format&fit=crop",
             caption="Mapa del mundo — Unsplash/NASA", use_column_width=True)

elif sec == "RECOMENDACIONES":
    titulo("Recomendaciones")
    st.write("- Estabilidad normativa y previsibilidad fiscal.")
    st.write("- Incentivos a inversión productiva y tecnológica.")
    st.write("- Cooperación internacional para fiscalidad digital.")
    st.write("- Comunicación clara sobre destino del gasto.")
    st.image("https://cdn.pixabay.com/photo/2017/08/06/22/32/handshake-2590565_1280.jpg",
             caption="Cooperación — Pixabay", use_column_width=True)

elif sec == "CONCLUSIONES":
    titulo("Conclusiones")
    st.success("España vive un momento clave: recaudar más **sin perder inversión ni innovación**.")
    st.write("Diseño fiscal **equilibrado, moderno y competitivo** como objetivo.")
    st.image("https://images.unsplash.com/photo-1499914485622-a88fac536970?q=80&w=1600&auto=format&fit=crop",
             caption="Ciudad y finanzas — Unsplash/Jason Briscoe", use_column_width=True)

elif sec == "REFERENCIAS":
    titulo("Referencias")
    st.markdown("""
- El Economista (25/10/2025): noticias sobre fin de Golden Visa y fiscalidad cripto.  
- EY (2025): suspensión del programa de inversión para residencia.  
- Guías de fiscalidad cripto en España (resumen de tramos del ahorro).  
- Imágenes libres: **Unsplash** y **Pixabay** (créditos en pie de foto).
""")
    st.info("Añade enlaces específicos a las noticias y legislación de tu dossier.")

# Pie
st.markdown("---")
st.caption("Presentación educativa · Máster en Finanzas · Personaliza el título en PORTADA")

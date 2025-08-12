import streamlit as st
import os
import openai

# Configurar la clave de API de OpenAI desde variable de entorno
openai.api_key = os.getenv("OPENAI_API_KEY")

# Título de la aplicación
st.set_page_config(page_title="Asistente de Planificación Territorial", layout="centered")
st.title("🧭 Asistente Inteligente - Instrumentos de Planificación Territorial")

# Descripción general
st.markdown("""
Este asistente apoya a los estudiantes del curso de maestría en **Planificación Urbana y Regional** en tres áreas clave:
1. 🗺️ Diagnóstico de problemas territoriales en regiones de Colombia  
2. 📜 Revisión normativa comparada en Latinoamérica  
3. ⚖️ Valoración y priorización de instrumentos de planificación  
""")

# Selección del módulo
modulo = st.selectbox("Selecciona el módulo de apoyo:", [
    "Diagnóstico Territorial",
    "Análisis Normativo Comparado",
    "Valoración y Priorización de Instrumentos"
])

# Entrada del usuario
consulta = st.text_area("Escribe tu consulta o información relevante:", height=200)

# Botón para generar respuesta
if st.button("Generar respuesta"):
    if not openai.api_key:
        st.error("⚠️ No se ha configurado la clave de API de OpenAI. Por favor, configúrala como variable de entorno.")
    elif not consulta.strip():
        st.warning("Por favor, escribe una consulta antes de continuar.")
    else:
        # Instrucciones específicas por módulo
        instrucciones = {
            "Diagnóstico Territorial": (
                "Actúa como experto en planificación territorial en Colombia. Ayuda al estudiante a estructurar un diagnóstico "
                "de problemas territoriales en una región específica, considerando aspectos sociales, ambientales, económicos y normativos."
            ),
            "Análisis Normativo Comparado": (
                "Actúa como analista normativo latinoamericano. Compara instrumentos de planificación territorial en países como "
                "Colombia, México, Brasil, Chile y Argentina. Resume marcos legales y destaca similitudes y diferencias."
            ),
            "Valoración y Priorización de Instrumentos": (
                "Actúa como asesor estratégico en planificación territorial. Ayuda a valorar instrumentos según criterios técnicos, "
                "institucionales, financieros y políticos. Sugiere métodos de priorización y estrategias de solución."
            )
        }

        # Construir el prompt
        prompt = f"""{instrucciones[modulo]}

Consulta del estudiante:
{consulta}"""

        # Llamada a la API de OpenAI
        try:
            respuesta = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Eres un asistente académico experto en planificación territorial."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=1000
            )
            texto_respuesta = respuesta['choices'][0]['message']['content']
            st.success("✅ Respuesta generada:")
            st.markdown(texto_respuesta)
        except Exception as e:
            st.error(f"❌ Error al generar respuesta: {e}")

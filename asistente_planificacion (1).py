
import streamlit as st
import openai
import os

# Configurar la clave de API desde las variables de entorno
openai.api_key = os.getenv("OPENAI_API_KEY")

# Título de la aplicación
st.title("🧭 Asistente de Planificación Territorial")
st.write("Este asistente apoya el curso de maestría en planificación urbana y regional.")

# Selección de módulo
modulo = st.selectbox("Selecciona el módulo:", [
    "Diagnóstico de Problemas Territoriales",
    "Análisis Normativo Comparado",
    "Valoración y Priorización de Instrumentos"
])

# Entrada de texto
consulta = st.text_area("Escribe tu consulta o información relevante:")

# Instrucciones específicas por módulo
instrucciones = {
    "Diagnóstico de Problemas Territoriales": (
        "Actúa como experto en planificación territorial en Colombia. "
        "Ayuda al estudiante a estructurar un diagnóstico de problemas territoriales en una región específica. "
        "Sugiere fuentes de datos, identifica actores, causas y consecuencias."
    ),
    "Análisis Normativo Comparado": (
        "Actúa como analista normativo en planificación territorial. "
        "Compara instrumentos de planificación territorial en países latinoamericanos como Colombia, México, Brasil, Chile y Argentina. "
        "Resume marcos normativos y destaca similitudes y diferencias."
    ),
    "Valoración y Priorización de Instrumentos": (
        "Actúa como asesor en formulación de estrategias territoriales. "
        "Ayuda a valorar instrumentos de planificación según criterios técnicos, políticos, financieros e institucionales. "
        "Sugiere matrices de priorización y estrategias de solución."
    )
}

# Generar respuesta
if st.button("Generar respuesta"):
    if not consulta:
        st.warning("Por favor ingresa una consulta.")
    else:
        prompt = f"{instrucciones[modulo]}

Consulta del estudiante: {consulta}"
        try:
            respuesta = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Eres un asistente académico experto en planificación territorial."},
                    {"role": "user", "content": prompt}
                ]
            )
            st.markdown("### 🧠 Respuesta del asistente:")
            st.write(respuesta.choices[0].message.content)
        except Exception as e:
            st.error(f"Ocurrió un error al generar la respuesta: {e}")

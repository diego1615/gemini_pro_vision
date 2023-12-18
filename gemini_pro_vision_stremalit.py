import streamlit as st
import google.generativeai as genai
from PIL import Image

# Función para configurar el modelo
def configure_model():
    GOOGLE_API_KEY = 'AIzaSyChImDFxhXwAHPOfTUMc0HxpExJA9CiaKQ'
    genai.configure(api_key=GOOGLE_API_KEY)
    return genai.GenerativeModel('gemini-pro-vision')

# Función para procesar la imagen y la pregunta
def process_image_and_question(model, image, question):
    response = model.generate_content([question, image], stream=True)
    response.resolve()
    return response.text

# Configura el modelo
model = configure_model()

# Interfaz de usuario en Streamlit
st.title("Explorador de Imágenes con IA")

# Carga de imagen
uploaded_file = st.file_uploader("Carga una imagen", type=["png", "jpg", "jpeg"])

# Campo de texto para la pregunta
question = st.text_input("Escribe tu pregunta sobre la imagen:")

if uploaded_file is not None and question:
    # Mostrar la imagen cargada
    image = Image.open(uploaded_file)
    st.image(image, caption='Imagen cargada', use_column_width=True)

    # Procesar la imagen y la pregunta
    response_text = process_image_and_question(model, image, question)

    # Mostrar el resultado
    st.write("Respuesta:")
    st.write(response_text)

# Ejecutar esto con: streamlit run your_script.py

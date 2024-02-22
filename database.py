import pandas as pd
import streamlit as st
from pymongo import MongoClient

# Conexion MongoDB
client = MongoClient("mongodb+srv://"+st.secrets["DB_USERNAME"]+":"+st.secrets["DB_PASSWORD"]+"@prediccion2024.tfde8xq.mongodb.net/")
db = client.sample_geospatial
collection = db.shipwrecks

def cargar_datos_desde_mongodb():
    # Obtener datos de la colección
    return pd.DataFrame(list(collection.find()))

df = cargar_datos_desde_mongodb()

# Formulario
with st.form("agregar_datos_form"):
    st.write("Agregar nuevos datos")

    nuevo_registro = st.text_input("Registro")
    nuevo_vesslterms = st.text_input("Términos de embarcación")
    nuevo_feature_type = st.text_input("Tipo de característica")
    nuevo_chart = st.text_input("Chart")
    nueva_latitud = st.number_input("Latitud")
    nueva_longitud = st.number_input("Longitud")
    nueva_profundidad = st.number_input("Profundidad")
    nuevo_sounding_type = st.text_input("Tipo de sondeo")
    nuevo_history = st.text_input("Historia")

    submitted = st.form_submit_button("Agregar")
    if submitted:
        nuevo_dato = {
            "recrd": nuevo_registro,
            "vesslterms": nuevo_vesslterms,
            "feature_type": nuevo_feature_type,
            "chart": nuevo_chart,
            "latdec": nueva_latitud,
            "londec": nueva_longitud,
            "depth": nueva_profundidad,
            "sounding_type": nuevo_sounding_type,
            "history": nuevo_history
        }
        collection.insert_one(nuevo_dato)
        st.success("Datos agregados correctamente")

columnas_seleccionadas = ['recrd', 'vesslterms', 'feature_type', 'chart', 'latdec', 'londec', 'depth', 'sounding_type', 'history', 'coordinates']
df_limpio = df[columnas_seleccionadas]
st.write("Dataframe con limpieza:")
st.write(df_limpio)

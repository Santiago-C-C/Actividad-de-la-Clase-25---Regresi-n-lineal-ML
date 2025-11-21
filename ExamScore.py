import numpy as np
import streamlit as st
import pandas as pd

st.write(''' # Predicción de calificaciones  ''')
st.image("examn.jpg", caption="Predicción de calificaciones.")

st.header('Datos')

def user_input_features():
  # Entrada
  Estudio = st.number_input('Estudio:', min_value=0.0, max_value=100.0, value = 0.0, step = 1.0)
  Sueño = st.number_input('Sueño:',  min_value=0.0, max_value=100.0, value = 0.0, step = 1.0)
  Asistencia = st.number_input('Asistencia:', min_value=0.0, max_value=100.0, value = 0.0, step = 1.0)
  Previa = st.number_input('Calificación previa:', min_value=0.0, max_value=100.0, value = 0.0, step = 1.0)


  user_input_data = {'hours_studied': Estudio,
                     'sleep_hours': Sueño,
                     'attendance_percent': Asistencia,
                     'previous_scores': Previa,
                     }

  features = pd.DataFrame(user_input_data, index=[0])

  return features

df = user_input_features()
datos =  pd.read_csv('Scores.csv', encoding='latin-1')
X = datos.drop(columns=['exam_score'])
y = datos['exam_score']

from sklearn.linear_model import LinearRegression
LR = LinearRegression()
LR.fit(X, y)

b1 = LR.coef_
b0 = LR.intercept_
prediccion = b0 + b1[0]*df['hours_studied'] + b1[1]*df['sleep_hours'] + b1[2]*df['attendance_percent'] + b1[3]*df['previous_scores']

st.subheader('Cálculo de calificación')
st.write('La calificacion es ', prediccion)

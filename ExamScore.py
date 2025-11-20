import numpy as np
import streamlit as st
import pandas as pd

st.write(''' # Predicción del exam score  ''')
st.image("examen.jpg", caption="Predicción del exam score de una persona.")

st.header('Datos personales')

def user_input_features():
  # Entrada
  Horas_estudiadas = st.number_input('Horas estudiadas:', min_value=0, max_value=15, value = 0,)
  Porcentaje_asistencia = st.number_input('Porcentaje asistencia:',  min_value=0, max_value=100, value = 0,)
  Scores_anteriores = st.number_input('Scores anteriores :', min_value=0, max_value=100, value = 0,)
  Horas_Dormidas = st.number_input('Horas Dormidas :', min_value=0, max_value=10, value = 0,)


  user_input_data = {'Horas estudiadas': Horas_estudiadas,
                     'Porcentaje asistencia': Porcentaje_asistencia,
                     'Scores anteriores': Scores_anteriores,
                     'Horas dormidas': Horas_Dormidas
                     }

  features = pd.DataFrame(user_input_data, index=[0])

  return features

df = user_input_features()
datos =  pd.read_csv('student_exam_scores.csv', encoding='latin-1')
X = datos.drop(columns='exam_score')
y = datos['exam_score']

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=1614175)
LR = LinearRegression()
LR.fit(X_train,y_train)

b1 = LR.coef_
b0 = LR.intercept_
prediccion = b0 + b1[0]*df['Horas estudiadas'] + b1[1]*df['Porcentaje asistencia'] + b1[2]*df['Scores anteriores'] + b1[3]*df['Horas dormidas']

st.subheader('Cálculo del score examn')
st.write('El score exam de la persona es ', prediccion)

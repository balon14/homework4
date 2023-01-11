import streamlit as st
from transformers import pipeline
# Создаем модель для определения комментариев 
classifier = pipeline(model="SkolkovoInstitute/russian_toxicity_classifier")
# Формируем заголовок для браузера
st.title("Приложение определения токсичный комментариев на русском языке")
# Строчка для ввода текста 
name = st.text_input("Введите текст")
# Кнопка для вывода результата 
if(st.button('Отправить')):
    result = classifier(name)
    st.success(result)

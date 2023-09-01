import streamlit as st
import pickle as pk
import pandas as pd

st.title("Weather Forecasting")
st.image('6278986_1571298721_Weather_Forecoast_Graphics.jpg')


pk.load(open('weather_list.pkl','rb'))
data=pk.load(open('predictions.pkl','rb'))

if st.button("Predict the weather today"):
    st.text(data.head())
if st.button("Other Forecastings"):
    st.button("Media Forecasting")
    st.text("This photo depicts about the ongoing haryana riots")
    st.image('download (1).jpg')
    st.button("Sports Forecasting")
    st.text("Asian Champions Trophy Live: Korea, Pakistan play out a 1-1 draw Asian Champions Trophy 2023 Live Score: We have three exciting matches line-up for the second day action of the Asian Champions Trophy in Chennai today.")
    st.image('download (2).jpg')
    st.button("Bollywood Forecasting")
    st.text("नाराज होकर मिथुन-अमिताभ के लिए गाना छोड़ा, घर के बाहर लिखवाया था- किशोर से सावधान!")
    st.image('2019158-kishore-kumar-2.jpg')

if st.button("HELP"):
    st.text("If you are facing any problem please comtact us at:")
    st.selectbox("Pick one", ["Email", "Phone", "Insta"])
st.slider("Rate Us:",0,10)


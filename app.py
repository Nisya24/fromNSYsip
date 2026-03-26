import streamlit as st
import time
from random import randint

st.set_page_config(page_title="Happy Birthday 🎂", layout="centered")

st.title("🎂 Happy Birthday Rifki! 🎉")
st.write("Happy Birtday Besfren ✨")

placeholder = st.empty()

space = ''
for i in range(1, 100):
    count = randint(1, 50)
    space = ' ' * count

    if(i % 10 == 0):
        text = space + '🎂 Happy Birthday!'
    elif(i % 9 == 0):
        text = space + "🎂"
    elif(i % 5 == 0):
        text = space + "💛"
    elif(i % 8 == 0):
        text = space + "🎉"
    elif(i % 7 == 0):
        text = space + "🍫"
    elif(i % 6 == 0):
        text = space + "Happy Birthday! 💖"
    else:
        text = space + "🔸"

    placeholder.text(text)
    time.sleep(0.2)

st.balloons()

import streamlit as st
import random

st.set_page_config(page_title="Birthday Surprise 🎂", layout="wide")

# ================= STYLE =================
st.markdown("""
<style>
body {
    overflow: hidden;
    background-color: black;
}

.title {
    text-align: center;
    color: white;
    font-size: 50px;
    margin-top: 20px;
}

.container {
    position: relative;
    height: 100vh;
    width: 100%;
}

.floating {
    position: absolute;
    bottom: -50px;
    font-size: 30px;
    animation: floatUp linear infinite;
}

@keyframes floatUp {
    0% {
        transform: translateY(0);
        opacity: 1;
    }
    100% {
        transform: translateY(-110vh);
        opacity: 0;
    }
}

button[kind="primary"] {
    background-color: #ff4b4b;
    color: white;
    font-size: 20px;
    padding: 10px 20px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ================= TITLE =================
st.markdown('<div class="title">🎂 Birthday Surprise 🎉</div>', unsafe_allow_html=True)

# ================= BUTTON =================
start = st.button("🎁 Start Surprise")

# ================= ANIMATION =================
if start:
    emojis = ["🎂", "🎉", "💛", "🍫", "✨", "💖"]

    elements = ""

    for i in range(60):
        left = random.randint(0, 100)
        duration = random.randint(5, 12)
        delay = random.randint(0, 5)
        emoji = random.choice(emojis)

        elements += f"""
        <div class="floating" 
             style="left:{left}%; 
                    animation-duration:{duration}s; 
                    animation-delay:{delay}s;">
            {emoji}
        </div>
        """

    st.markdown(f"""
    <div class="container">
        {elements}
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        "<h1 style='text-align:center; color:white;'>🎉 Happy Birthday Rifki! 💖</h1>",
        unsafe_allow_html=True
    )

    st.balloons()

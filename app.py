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

/* Title */
.title {
    text-align: center;
    color: white;
    font-size: 50px;
    margin-top: 20px;
}

/* Container */
.container {
    position: relative;
    height: 100vh;
    width: 100%;
}

/* Floating emojis */
.floating {
    position: absolute;
    bottom: -50px;
    font-size: 30px;
    animation: floatUp linear infinite;
}

/* Confetti */
.confetti {
    position: absolute;
    width: 8px;
    height: 8px;
    background-color: white;
    bottom: -10px;
    animation: confettiFall linear infinite;
}

/* Animations */
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

@keyframes confettiFall {
    0% {
        transform: translateY(0) rotate(0deg);
        opacity: 1;
    }
    100% {
        transform: translateY(-110vh) rotate(720deg);
        opacity: 0;
    }
}

/* Button styling */
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

    # Emoji floating
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

    # Confetti
    for i in range(80):
        left = random.randint(0, 100)
        duration = random.randint(4, 10)
        delay = random.randint(0, 5)

        elements += f"""
        <div class="confetti" 
             style="left:{left}%; 
                    animation-duration:{duration}s; 
                    animation-delay:{delay}s;">
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

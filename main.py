import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="감정 기반 음악 추천 🎵", page_icon="🎧", layout="centered")

# 타이틀
st.markdown(
    "<h1 style='text-align: center; color: #ff4b4b;'>🎶 감정으로 듣는 음악 추천 🎶</h1>",
    unsafe_allow_html=True
)

st.markdown("#### 지금 기분은 어떤가요? 😄😢😡😴")

# 감정 선택
emotion = st.selectbox("🎭 감정을 선택하세요:", ["행복 😊", "슬픔 😢", "화남 😡", "피곤 😴", "사랑 💖", "신남 🕺"])

# 감정별 음악 추천
music_dict = {
    "행복 😊": ["Pharrell Williams - Happy 🎵", "Katy Perry - Firework 🎆", "BTS - Dynamite 💥"],
    "슬픔 😢": ["Adele - Someone Like You 💔", "이소라 - 바람이 분다 🌬️", "IU - Love Poem 🖋️"],
    "화남 😡": ["Linkin Park - Numb ⚡", "Eminem - Lose Yourself 🔥", "G-Dragon - 삐딱하게 👊"],
    "피곤 😴": ["Lauv - I Like Me Better 🌌", "백예린 - Bye bye my blue 🌙", "적재 - 나랑 같이 걸을래 🚶‍♀️"],
    "사랑 💖": ["Crush - Beautiful 🌹", "Maroon 5 - Sugar 🍭", "백현 - Candy 🍬"],
    "신남 🕺": ["Bruno Mars - 24K Magic ✨", "ZICO - 아무노래 🎉", "세븐틴 - 아주 NICE 💃"]
}

# 결과 출력
if emotion:
    st.markdown("## 🎧 추천 플레이리스트")
    for song in music_dict[emotion]:
        st.markdown(f"- {song}")

st.markdown("---")
st.markdown("<center>Made with ❤️ using Streamlit</center>", unsafe_allow_html=True)

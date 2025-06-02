import streamlit as st

# 🎨 화려한 테마 구성
st.set_page_config(page_title="MBTI 진로 추천", page_icon="🎯", layout="centered")

# 🖌️ 사용자 인터페이스 꾸미기
st.markdown(
    """
    <h1 style='text-align: center; color: #ff69b4;'>🎯 MBTI 진로 추천 웹앱 🎯</h1>
    <h3 style='text-align: center; color: #00ced1;'>당신의 성격에 딱 맞는 직업은? 🧠💼</h3>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# 🎯 MBTI 목록
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# 🌈 사용자 입력 받기
selected_mbti = st.selectbox("💡 당신의 MBTI를 선택하세요!", mbti_types)

# 💼 MBTI별 추천 직업
job_recommendations = {
    "INTJ": ["🔬 데이터 사이언티스트", "🧠 전략 컨설턴트", "💻 소프트웨어 아키텍트"],
    "INTP": ["🧪 연구원", "👨‍💻 프로그래머", "🛠️ 기술 컨설턴트"],
    "ENTJ": ["📈 경영 컨설턴트", "🏛️ 기업 임원", "💼 프로젝트 매니저"],
    "ENTP": ["🎤 마케팅 전략가", "🧠 창업가", "📱 UX 디자이너"],
    "INFJ": ["🎨 예술 치료사", "📚 작가", "👩‍🏫 교사"],
    "INFP": ["✍️ 시나리오 작가", "🎭 배우", "🌱 환경운동가"],
    "ENFJ": ["🗣️ 커뮤니케이션 전문가", "💖 심리상담가", "📢 사회운동가"],
    "ENFP": ["🎬 콘텐츠 크리에이터", "🎨 디자이너", "🌍 NGO 활동가"],
    "ISTJ": ["🔍 회계사", "📋 행정 공무원", "⚖️ 법률 사무원"],
    "ISFJ": ["👩‍⚕️ 간호사", "👨‍👩‍👧‍👦 사회복지사", "🧾 문서 관리자"],
    "ESTJ": ["🏢 기업 관리자", "🧾 감사 전문가", "📦 운영 매니저"],
    "ESFJ": ["🧑‍🏫 초등 교사", "🏥 병원 행정", "🧑‍🍳 요리사"],
    "ISTP": ["🛠️ 엔지니어", "🏎️ 자동차 정비사", "🎮 게임 개발자"],
    "ISFP": ["🎨 일러스트레이터", "🎸 음악가", "📷 포토그래퍼"],
    "ESTP": ["💰 세일즈 매니저", "🎤 이벤트 플래너", "🕵️ 탐정"],
    "ESFP": ["🌟 연예인", "🎤 MC", "🛍️ 패션 스타일리스트"]
}

# 🎊 결과 출력
if selected_mbti:
    st.markdown(f"## 💖 {selected_mbti} 유형에게 추천하는 직업 💖")
    for job in job_recommendations[selected_mbti]:
        st.markdown(f"### {job}")

st.markdown("---")

st.markdown(
    """
    <div style='text-align: center;'>
        <p style='font-size: 18px;'>✨당신의 성향을 이해하고, 멋진 미래를 설계하세요!✨</p>
        <p>Made with ❤️ by [Your Name]</p>
    </div>
    """,
    unsafe_allow_html=True
)

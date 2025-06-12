import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="🎬 드라마 추천 🌟",
    page_icon="🎥",
    layout="centered",
    initial_sidebar_state="expanded",
)

# CSS로 꾸미기 (배경색, 폰트 등)
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 99%, #fad0c4 100%);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: #4b1c1c;
}
h1 {
    color: #b22222;
    text-shadow: 2px 2px #fff;
}
h2 {
    color: #8b0000;
}
.stButton>button {
    background-color: #ff6f61;
    color: white;
    font-weight: bold;
    border-radius: 12px;
    padding: 10px 24px;
    font-size: 18px;
    box-shadow: 2px 2px 8px rgba(255, 111, 97, 0.5);
    transition: all 0.3s ease;
}
.stButton>button:hover {
    background-color: #ff3b2f;
    box-shadow: 3px 3px 12px rgba(255, 59, 47, 0.7);
}
</style>
""", unsafe_allow_html=True)

# 제목
st.title("🎉 장르별 드라마 추천 프로그램 🎉")
st.write("안녕하세요! 원하는 장르를 선택하면 ✨최고의 드라마✨를 추천해 드려요! 📺🍿")

# 장르 선택
genre = st.selectbox(
    "원하는 장르를 선택해주세요! 🎭",
    ("로맨스 ❤️", "스릴러 🕵️‍♂️", "판타지 🧙‍♂️", "코미디 😂", "범죄 🔫", "역사 🏰", "SF 🚀")
)

# 드라마 추천 데이터
drama_recommendations = {
    "로맨스 ❤️": [
        "💖 '별에서 온 그대' - 사랑과 판타지가 만나는 최고의 로맨스!",
        "🌹 '도깨비' - 감성 가득한 판타지 로맨스 명작",
        "💕 '사랑의 불시착' - 국경을 넘은 사랑 이야기"
    ],
    "스릴러 🕵️‍♂️": [
        "🔪 '비밀의 숲' - 긴장감 넘치는 법정 스릴러",
        "🕵️‍♂️ '보이스' - 귀를 기울여라! 생존을 건 스릴",
        "😱 '나의 아저씨' - 인간 심리를 파고드는 명작"
    ],
    "판타지 🧙‍♂️": [
        "🐉 '도깨비' - 한국형 판타지의 정수",
        "🧙‍♀️ '호텔 델루나' - 어둠과 빛이 공존하는 환상세계",
        "🦄 '킹덤' - 좀비와 조선시대가 만난 이색 판타지"
    ],
    "코미디 😂": [
        "🤣 '응답하라 1988' - 가족과 친구들의 따뜻한 이야기",
        "😂 '미생' - 직장인들의 현실과 웃음",
        "😆 '내 사랑 치유기' - 코믹하면서도 감동적인 드라마"
    ],
    "범죄 🔫": [
        "🔫 '보이스' - 범죄와 싸우는 긴박한 이야기",
        "🚨 '비밀의 숲' - 냉철한 수사와 반전의 연속",
        "🕵️‍♀️ '시그널' - 과거와 현재를 잇는 수사극"
    ],
    "역사 🏰": [
        "👑 '이산' - 조선의 역사를 생생하게 재현",
        "⚔️ '미스터 션샤인' - 격동의 시대를 배경으로 한 이야기",
        "🏯 '해를 품은 달' - 궁중 로맨스와 역사"
    ],
    "SF 🚀": [
        "🚀 '알함브라 궁전의 추억' - 현실과 가상세계가 만나는 SF",
        "👽 '싸이코지만 괜찮아' - 독특한 감성의 SF 로맨스",
        "🌌 '시그널' - 시간을 초월한 미스터리"
    ],
}

# 추천 버튼
if st.button("추천 받기! 🎁"):
    st.subheader(f"🎬 {genre} 장르 추천 드라마 🎬")
    for drama in drama_recommendations[genre]:
        st.write(f"⭐ {drama}")

# 하단 푸터
st.markdown("---")
st.markdown("Made with ❤️ by ChatGPT | 즐거운 드라마 감상 되세요! 📺✨")

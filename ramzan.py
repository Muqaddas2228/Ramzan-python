import streamlit as st
import datetime

# Set Page Config
st.set_page_config(page_title="🌙 Ramzan App", page_icon="🌟", layout="wide")

# Add Background Image & Set Text Color to Black
st.markdown(
    """
    <style>
        .stApp {
            background: url('https://t4.ftcdn.net/jpg/07/44/50/35/240_F_744503503_mnN0GF5UGeaYThIYQpOJl4qYBqvDigoR.jpg') no-repeat center center fixed;
            background-size: cover;
        }
        /* Sidebar Styling */
        .css-1d391kg * {
            color: black !important;
        }
        /* Main App Content Text */
        h1, h2, h3, p, label {
            color: black !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("🛤️ Go to:", ["🏠 Home", "🤲 Dua List", "📖 Hadith List", "🔢 Tasbeeh Counter"])

if page == "🏠 Home":
    st.markdown("<h1 style='text-align: center;'>🌙 Ramzan App</h1>", unsafe_allow_html=True)
    current_date = datetime.date.today()
    st.markdown(f"<h3 style='text-align: center;'>📅 {current_date.strftime('%B %d, %Y')}</h3>", unsafe_allow_html=True)
    
    sehri_time = "🕋 05:10 AM"
    iftar_time = "🌅 06:45 PM"
    st.markdown(f"""
        <div class='highlight-box'>
            <h2>⏳ Ramzan Timings</h2>
            <p class='big-font'>🌙 Sehri Time: <b>{sehri_time}</b></p>
            <p class='big-font'>🌇 Iftar Time: <b>{iftar_time}</b></p>
        </div>
    """, unsafe_allow_html=True)

    daily_dua = "اللهم إنك عفو كريم تحب العفو فاعف عني"
    st.markdown(f"""
        <div class='highlight-box'>
            <h2>🤲 Daily Dua</h2>
            <p style='font-size:32px; font-weight:bold;'>📿 {daily_dua}</p>
        </div>
    """, unsafe_allow_html=True)

    daily_hadith = "The strong person is not the one who can overpower others, but the one who can control himself when angry. (📖 Bukhari)"
    st.markdown(f"""
        <div class='highlight-box'>
            <h2>📖 Daily Hadith</h2>
            <p class='big-font'>{daily_hadith}</p>
        </div>
    """, unsafe_allow_html=True)

elif page == "🤲 Dua List":
    st.markdown("<h1 style='text-align: center;'>🤲 Dua List</h1>", unsafe_allow_html=True)
    duas = [
        ("📿 Dua for Fasting", "اللهم لك صمت وبك آمنت وعليك توكلت وعلى رزقك أفطرت", "O Allah, I have fasted for You, I believe in You, I put my trust in You, and with Your provision, I break my fast."),
        ("💛 Dua for Forgiveness", "رب اغفر لي وتب علي إنك أنت التواب الرحيم", "My Lord, forgive me and accept my repentance. Indeed, You are the Most Forgiving, the Most Merciful."),
        ("🛤️ Dua for Guidance", "اللهم اهدني وسددني", "O Allah, guide me and make me steadfast."),
        ("❤️ Dua for Health", "اللهم إني أسألك العفو والعافية", "O Allah, I ask You for pardon and well-being."),
        ("👨‍👩‍👧‍👦 Dua for Parents", "رب ارحمهما كما ربياني صغيرا", "My Lord, have mercy on them as they brought me up when I was small."),
    ]
    for tag, arabic, translation in duas:
        st.markdown(f"<p style='font-size:18px;'>📌 {tag}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size:22px; font-weight:bold;'>{arabic}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size:18px; color:gray;'><i>{translation}</i></p>", unsafe_allow_html=True)

elif page == "📖 Hadith List":
    st.markdown("<h1 style='text-align: center;'>📖 Hadith List</h1>", unsafe_allow_html=True)
    hadiths = [
        "💡 The best among you are those who learn the Quran and teach it. (Bukhari)",
        "💖 The best among you are those who have the best manners and character. (Bukhari)",
        "🌱 A good word is charity. (Bukhari)",
        "😊 Smiling at your brother is a charity. (Tirmidhi)",
        "👐 He who does not thank people has not thanked Allah. (Abu Dawood)"
    ]
    for i, hadith in enumerate(hadiths, 1):
        st.markdown(f"<p style='font-size:22px; font-weight:bold;'>📖 Hadith {i}: {hadith}</p>", unsafe_allow_html=True)

elif page == "🔢 Tasbeeh Counter":
    st.markdown("<h1 style='text-align: center;'>🔢 Tasbeeh Counter</h1>", unsafe_allow_html=True)
    
    if 'tasbeeh_count' not in st.session_state:
        st.session_state.tasbeeh_count = 0
    
    st.markdown(f"""
        <div class='tasbeeh-container'>
            <div class='tasbeeh-box'>🕌 {st.session_state.tasbeeh_count}</div>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("➖ Subtract"):
            if st.session_state.tasbeeh_count > 0:
                st.session_state.tasbeeh_count -= 1
    with col2:
        if st.button("➕ Add"):
            st.session_state.tasbeeh_count += 1

# import streamlit as st
# import pickle
# import requests
# # Page configuration
# st.set_page_config(
#     page_title="Movie Recommendation System",
#     page_icon="🎬",
#     layout="wide"
# )
# st.markdown("""
# <style>

# /* Aurora gradient animated background */
# .stApp {
# background: radial-gradient(circle at 20% 30%, rgba(138,43,226,0.35), transparent 40%),
#             radial-gradient(circle at 80% 70%, rgba(0,191,255,0.35), transparent 40%),
#             radial-gradient(circle at 50% 50%, rgba(255,0,150,0.25), transparent 45%),
#             #0b0f19;
# background-attachment: fixed;
# color: white;
# }

# /* title */
# .main-title{
# font-size:65px;
# font-weight:700;
# text-align:center;
# letter-spacing:2px;
# }

# /* subtitle */
# .subtitle{
# text-align:center;
# font-size:20px;
# color:#cfcfcf;
# margin-bottom:40px;
# }

# /* glass container */
# .block-container{
# background: rgba(255,255,255,0.05);
# backdrop-filter: blur(12px);
# border-radius:18px;
# padding:40px;
# }

# /* button styling */
# .stButton>button{
# background: linear-gradient(90deg,#ff4b6e,#7a5cff);
# color:white;
# border:none;
# border-radius:10px;
# font-size:18px;
# height:3em;
# width:230px;
# transition:0.3s;
# }

# /* button hover */
# .stButton>button:hover{
# transform:scale(1.05);
# box-shadow:0px 0px 18px rgba(122,92,255,0.6);
# }

# /* poster hover */
# img{
# border-radius:12px;
# transition: transform .35s ease;
# }

# img:hover{
# transform: scale(1.1);
# }

# </style>
# """, unsafe_allow_html=True)

# st.markdown("""
# <style>

# /* background poster container */
# .bg-posters {
# position: fixed;
# top:0;
# left:0;
# width:100%;
# height:100%;
# z-index:-1;
# overflow:hidden;
# }

# /* poster style */
# .bg-posters img{
# position:absolute;
# width:220px;
# opacity:0.55;
# filter: blur(0.5px);
# animation: float 20s infinite ease-in-out;
# border-radius:10px;
# }

# /* floating positions */
# .poster1 {top:10%; left:5%;}
# .poster2 {top:60%; left:15%;}
# .poster3 {top:10%; right:10%;}
# .poster4 {bottom:5%; right:20%;}
# .poster5 {top:60%; right:40%;}
# .poster6 {top:15%; left:40%;}

# /* floating animation */
# @keyframes float{
# 0% {transform:translateY(0px);}
# 50% {transform:translateY(-40px);}
# 100% {transform:translateY(0px);}
# }

# /* responsive for small screens */
# @media (max-width:900px){
# .bg-posters img{
# width:140px;
# }
# }

# </style>

# <div class="bg-posters">

# <img class="poster1" src="https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg">
# <img class="poster2" src="https://image.tmdb.org/t/p/w500/6ELCZlTA5lGUops70hKdB83WJxH.jpg">
# <img class="poster3" src="https://image.tmdb.org/t/p/w500/udDclJoHjfjb8Ekgsd4FDteOkCU.jpg">
# <img class="poster4" src="https://image.tmdb.org/t/p/w500/xBHvZcjRiWyobQ9kxBhO6B2dtRI.jpg">
# <img class="poster5" src="https://image.tmdb.org/t/p/w500/8UlWHLMpgZm9bx6QYh0NFoq67TZ.jpg">
# <img class="poster6" src="https://image.tmdb.org/t/p/w500/9Gtg2DzBhmYamXBS1hKAhiwbBKS.jpg">

# </div>

# """, unsafe_allow_html=True)

# # Load data
# movies = pickle.load(open('movies.pkl','rb'))
# similarity = pickle.load(open('similarity.pkl','rb'))


# # TMDB API key
# API_KEY = "YOUR_API_KEY_HERE"


# # Fetch movie poster
# @st.cache_data
# def fetch_poster(movie_id):
#     try:
#         url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
#         response = requests.get(url, timeout=5)
#         data = response.json()

#         poster_path = data.get("poster_path")

#         if poster_path:
#             return "https://image.tmdb.org/t/p/w500/" + poster_path
#         else:
#             return "https://via.placeholder.com/500x750?text=No+Poster"

#     except:
#         return "https://via.placeholder.com/500x750?text=No+Poster"

# # Recommendation function
# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]

#     movies_list = sorted(
#         list(enumerate(distances)),
#         reverse=True,
#         key=lambda x: x[1]
#     )[1:6]

#     recommended_movies = []
#     recommended_posters = []

#     for i in movies_list:
#         movie_id = movies.iloc[i[0]].movie_id
#         recommended_movies.append(movies.iloc[i[0]].title)
#         recommended_posters.append(fetch_poster(movie_id))

#     return recommended_movies, recommended_posters


# # UI Title
# st.markdown("<h1>🎬 Movie Recommendation Engine</h1>", unsafe_allow_html=True)

# st.markdown(
# "<p class='subtitle'>Discover movies similar to your favorites using Machine Learning & Natural Language Processing.Select a movie and get instant recommendations</p>",
# unsafe_allow_html=True
# )

# # Sidebar
# st.sidebar.title("About")

# st.sidebar.write(
# """
# MOVIE RECOMMENDATION SYSTEM:

# Features:

# • Content-Based Filtering  
# • NLP Text Processing  
# • Cosine Similarity  

# Tech Stack:

# Python  
# Pandas  
# Scikit-learn  
# Streamlit  
# TMDB API
# """
# )

# # Movie selection dropdown
# selected_movie = st.selectbox(
#     "Select a movie",
#     movies['title'].values,
#     key="movie_select"
# )

# # Recommendation button
# if st.button("Recommend", key="recommend_button"):

#     with st.spinner("Finding similar movies..."):
#         names, posters = recommend(selected_movie)

#         st.subheader("Recommended Movies")

#         col1, col2, col3, col4, col5 = st.columns(5)

#         with col1:
#             st.image(posters[0])
#             st.markdown(f"**{names[0]}**")

#         with col2:
#             st.image(posters[1])
#             st.markdown(f"**{names[1]}**")

#         with col3:
#             st.image(posters[2])
#             st.markdown(f"**{names[2]}**")

#         with col4:
#             st.image(posters[3])
#             st.markdown(f"**{names[3]}**")

#         with col5:
#             st.image(posters[4])
#             st.markdown(f"**{names[4]}**")


import streamlit as st
import pickle
import requests

# Page configuration
st.set_page_config(
    page_title="CineMatch — Movie Recommendations",
    page_icon="🎬",
    layout="wide"
)

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">

<style>

/* ── RESET & BASE ─────────────────────────────── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

/* ── CINEMATIC BACKGROUND ─────────────────────── */
.stApp {
    background: #080c14;
    color: #e8e0d4;
    font-family: 'DM Sans', sans-serif;
    min-height: 100vh;
}

/* Film grain overlay */
.stApp::before {
    content: '';
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.04'/%3E%3C/svg%3E");
    pointer-events: none;
    z-index: 9999;
    opacity: 0.4;
}

/* Ambient light blobs */
.stApp::after {
    content: '';
    position: fixed;
    top: -20%; left: -10%;
    width: 600px; height: 600px;
    background: radial-gradient(circle, rgba(196, 154, 92, 0.07) 0%, transparent 70%);
    pointer-events: none;
    z-index: 0;
    animation: driftLight 18s ease-in-out infinite alternate;
}

@keyframes driftLight {
    0%   { transform: translate(0, 0); }
    100% { transform: translate(120px, 80px); }
}

/* ── LAYOUT ───────────────────────────────────── */
.block-container {
    padding: 0 3rem 4rem 3rem !important;
    max-width: 1280px !important;
    position: relative;
    z-index: 1;
}

/* ── HERO HEADER ──────────────────────────────── */
.hero-wrapper {
    position: relative;
    padding: 60px 0 50px 0;
    text-align: center;
    overflow: hidden;
}

.hero-eyebrow {
    font-family: 'DM Sans', sans-serif;
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 5px;
    text-transform: uppercase;
    color: #c49a5c;
    margin-bottom: 18px;
    display: block;
}

.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(52px, 7vw, 88px);
    font-weight: 900;
    line-height: 1.0;
    background: linear-gradient(135deg, #f5e6cc 0%, #c49a5c 45%, #f5e6cc 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: -1px;
    margin-bottom: 20px;
}

.hero-rule {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 16px;
    margin: 22px auto;
    max-width: 300px;
}

.hero-rule::before,
.hero-rule::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, transparent, #c49a5c88);
}

.hero-rule span {
    color: #c49a5c;
    font-size: 18px;
}

.hero-subtitle {
    font-family: 'DM Sans', sans-serif;
    font-size: 16px;
    font-weight: 300;
    color: #9a9080;
    letter-spacing: 0.3px;
    max-width: 520px;
    margin: 0 auto;
    line-height: 1.7;
}

/* ── FILMSTRIP DIVIDER ────────────────────────── */
.filmstrip {
    width: 100%;
    height: 28px;
    background:
        repeating-linear-gradient(90deg,
            #1a1a2e 0px, #1a1a2e 18px,
            transparent 18px, transparent 26px
        );
    border-top: 3px solid #1e2235;
    border-bottom: 3px solid #1e2235;
    margin: 10px 0 40px 0;
    position: relative;
    overflow: hidden;
}

.filmstrip::after {
    content: '';
    position: absolute;
    top: 0; left: -100%;
    width: 200%;
    height: 100%;
    background: linear-gradient(90deg,
        transparent 0%, rgba(196,154,92,0.15) 50%, transparent 100%
    );
    animation: scanline 4s linear infinite;
}

@keyframes scanline {
    0% { left: -100%; }
    100% { left: 100%; }
}

/* ── SELECTOR CARD ────────────────────────────── */
.selector-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(196,154,92,0.15);
    border-radius: 16px;
    padding: 36px 40px;
    margin-bottom: 36px;
    backdrop-filter: blur(20px);
    position: relative;
    overflow: hidden;
}

.selector-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 2px;
    background: linear-gradient(90deg, transparent, #c49a5c, transparent);
}

.selector-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 11px;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: #c49a5c;
    margin-bottom: 14px;
    display: block;
}

/* ── STREAMLIT SELECT OVERRIDE ────────────────── */
div[data-baseweb="select"] > div {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(196,154,92,0.3) !important;
    border-radius: 10px !important;
    color: #e8e0d4 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 16px !important;
    transition: border-color 0.3s ease !important;
}

div[data-baseweb="select"] > div:hover {
    border-color: rgba(196,154,92,0.7) !important;
    box-shadow: 0 0 0 3px rgba(196,154,92,0.08) !important;
}

div[data-baseweb="select"] span {
    color: #e8e0d4 !important;
}

/* Dropdown menu */
ul[role="listbox"] {
    background: #10151f !important;
    border: 1px solid rgba(196,154,92,0.25) !important;
    border-radius: 10px !important;
}

li[role="option"] {
    color: #c8bfb0 !important;
    font-family: 'DM Sans', sans-serif !important;
}

li[role="option"]:hover {
    background: rgba(196,154,92,0.12) !important;
    color: #f5e6cc !important;
}

/* ── BUTTON ───────────────────────────────────── */
.stButton > button {
    background: linear-gradient(135deg, #c49a5c 0%, #a07840 50%, #c49a5c 100%) !important;
    background-size: 200% !important;
    color: #0d1117 !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 14px !important;
    font-weight: 500 !important;
    letter-spacing: 3px !important;
    text-transform: uppercase !important;
    height: 52px !important;
    width: 100% !important;
    cursor: pointer !important;
    transition: all 0.4s ease !important;
    margin-top: 20px !important;
    box-shadow: 0 4px 24px rgba(196,154,92,0.25) !important;
}

.stButton > button:hover {
    background-position: right center !important;
    box-shadow: 0 8px 36px rgba(196,154,92,0.45) !important;
    transform: translateY(-2px) !important;
}

.stButton > button:active {
    transform: translateY(0px) !important;
}

/* ── SPINNER ──────────────────────────────────── */
.stSpinner > div {
    border-top-color: #c49a5c !important;
}

/* ── RESULTS SECTION ──────────────────────────── */
.results-header {
    font-family: 'Playfair Display', serif;
    font-size: 28px;
    font-weight: 700;
    color: #f5e6cc;
    margin-bottom: 28px;
    display: flex;
    align-items: center;
    gap: 14px;
}

.results-header::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, rgba(196,154,92,0.4), transparent);
}

/* ── MOVIE CARD COLUMNS ───────────────────────── */
div[data-testid="column"] {
    padding: 0 8px !important;
}

/* ── MOVIE CARD ───────────────────────────────── */
.movie-card {
    position: relative;
    border-radius: 12px;
    overflow: hidden;
    background: #0f1420;
    border: 1px solid rgba(255,255,255,0.06);
    transition: all 0.4s cubic-bezier(0.23, 1, 0.32, 1);
    group: true;
}

.movie-card:hover {
    transform: translateY(-8px) scale(1.02);
    border-color: rgba(196,154,92,0.4);
    box-shadow:
        0 20px 60px rgba(0,0,0,0.6),
        0 0 0 1px rgba(196,154,92,0.2),
        inset 0 1px 0 rgba(255,255,255,0.05);
}

/* Poster image */
div[data-testid="column"] img {
    border-radius: 10px 10px 0 0 !important;
    width: 100% !important;
    display: block !important;
    object-fit: cover !important;
    transition: transform 0.5s cubic-bezier(0.23, 1, 0.32, 1) !important;
    filter: brightness(0.92) saturate(1.1) !important;
}

div[data-testid="column"]:hover img {
    transform: scale(1.04) !important;
    filter: brightness(1.05) saturate(1.2) !important;
}

/* Movie title text */
div[data-testid="column"] p {
    font-family: 'DM Sans', sans-serif !important;
    font-size: 13px !important;
    font-weight: 500 !important;
    color: #c8bfb0 !important;
    text-align: center !important;
    padding: 12px 10px 14px 10px !important;
    letter-spacing: 0.2px !important;
    line-height: 1.4 !important;
    background: rgba(10,14,22,0.9) !important;
    border-radius: 0 0 10px 10px !important;
    border-top: 1px solid rgba(196,154,92,0.1) !important;
    transition: color 0.3s ease !important;
}

div[data-testid="column"]:hover p {
    color: #f5e6cc !important;
}

/* Number badge on each card */
.card-number {
    position: absolute;
    top: 10px;
    left: 10px;
    background: rgba(196,154,92,0.9);
    color: #0d1117;
    font-family: 'Playfair Display', serif;
    font-size: 12px;
    font-weight: 700;
    width: 26px;
    height: 26px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 10;
}

/* ── SUBHEADER OVERRIDE ───────────────────────── */
h3, .stSubheader {
    font-family: 'Playfair Display', serif !important;
    color: #f5e6cc !important;
    letter-spacing: -0.3px !important;
}

/* ── SIDEBAR ──────────────────────────────────── */
section[data-testid="stSidebar"] {
    background: rgba(8,12,20,0.95) !important;
    border-right: 1px solid rgba(196,154,92,0.12) !important;
    backdrop-filter: blur(20px) !important;
}

section[data-testid="stSidebar"] .block-container {
    padding: 2rem 1.5rem !important;
}

section[data-testid="stSidebar"] h1 {
    font-family: 'Playfair Display', serif !important;
    font-size: 22px !important;
    color: #c49a5c !important;
    border-bottom: 1px solid rgba(196,154,92,0.2) !important;
    padding-bottom: 14px !important;
    margin-bottom: 20px !important;
}

section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] div {
    font-family: 'DM Sans', sans-serif !important;
    font-size: 13px !important;
    color: #7a7060 !important;
    line-height: 2.0 !important;
}

/* Sidebar section divider */
.sidebar-section {
    margin-top: 20px;
    padding-top: 16px;
    border-top: 1px solid rgba(196,154,92,0.1);
}

.sidebar-badge {
    display: inline-block;
    background: rgba(196,154,92,0.12);
    border: 1px solid rgba(196,154,92,0.25);
    border-radius: 6px;
    padding: 3px 10px;
    font-size: 11px !important;
    color: #c49a5c !important;
    letter-spacing: 1px;
    margin: 3px 3px 3px 0;
}

/* ── BACKGROUND FLOATING POSTERS ─────────────── */
.bg-posters {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    z-index: 0;
    overflow: hidden;
    pointer-events: none;
}

.bg-posters img {
    position: absolute;
    width: 180px;
    opacity: 0.06;
    filter: blur(1.5px) grayscale(20%);
    border-radius: 8px;
    animation: floatPoster 25s infinite ease-in-out;
    transition: none !important;
}

.bg-posters img:hover { transform: none !important; }

.poster1 { top: 8%;   left: 2%;   animation-delay: 0s;   animation-duration: 22s; }
.poster2 { top: 55%;  left: 12%;  animation-delay: -6s;  animation-duration: 28s; }
.poster3 { top: 5%;   right: 3%;  animation-delay: -12s; animation-duration: 20s; }
.poster4 { bottom: 8%; right: 8%; animation-delay: -3s;  animation-duration: 30s; }
.poster5 { top: 45%;  right: 25%; animation-delay: -9s;  animation-duration: 24s; }
.poster6 { top: 20%;  left: 38%;  animation-delay: -15s; animation-duration: 26s; }

@keyframes floatPoster {
    0%   { transform: translateY(0px) rotate(-1deg); }
    33%  { transform: translateY(-30px) rotate(0.5deg); }
    66%  { transform: translateY(-15px) rotate(-0.5deg); }
    100% { transform: translateY(0px) rotate(-1deg); }
}

/* ── RESPONSIVE ───────────────────────────────── */
@media (max-width: 900px) {
    .hero-title { font-size: 42px; }
    .block-container { padding: 0 1rem 3rem 1rem !important; }
    .bg-posters img { width: 110px; opacity: 0.04; }
    .selector-card { padding: 24px 20px; }
}

/* hide streamlit branding */
#MainMenu, footer, header { visibility: hidden; }

/* selectbox label */
label[data-testid="stWidgetLabel"] p {
    font-family: 'DM Sans', sans-serif !important;
    font-size: 11px !important;
    letter-spacing: 4px !important;
    text-transform: uppercase !important;
    color: #c49a5c !important;
}

</style>
""", unsafe_allow_html=True)


# ── FLOATING BACKGROUND POSTERS ────────────────────────────────────────────
st.markdown("""
<div class="bg-posters">
    <img class="poster1" src="https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg" alt="">
    <img class="poster2" src="https://image.tmdb.org/t/p/w500/6ELCZlTA5lGUops70hKdB83WJxH.jpg" alt="">
    <img class="poster3" src="https://image.tmdb.org/t/p/w500/udDclJoHjfjb8Ekgsd4FDteOkCU.jpg" alt="">
    <img class="poster4" src="https://image.tmdb.org/t/p/w500/xBHvZcjRiWyobQ9kxBhO6B2dtRI.jpg" alt="">
    <img class="poster5" src="https://image.tmdb.org/t/p/w500/8UlWHLMpgZm9bx6QYh0NFoq67TZ.jpg" alt="">
    <img class="poster6" src="https://image.tmdb.org/t/p/w500/9Gtg2DzBhmYamXBS1hKAhiwbBKS.jpg" alt="">
</div>
""", unsafe_allow_html=True)


# ── HERO HEADER ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-wrapper">
    <span class="hero-eyebrow">✦ Powered by NLP & Cosine Similarity ✦</span>
    <h1 class="hero-title">CineMatch</h1>
    <div class="hero-rule"><span>✦</span></div>
    <p class="hero-subtitle">
        Discover your next obsession. Select a film and let our content-based
        engine surface the five most cinematically kindred titles.
    </p>
</div>
""", unsafe_allow_html=True)


# ── FILMSTRIP DIVIDER ────────────────────────────────────────────────────────
st.markdown('<div class="filmstrip"></div>', unsafe_allow_html=True)


# ── LOAD DATA ────────────────────────────────────────────────────────────────
movies = pickle.load(open('movies.pkl', 'rb'))
# similarity = pickle.load(open('similarity.pkl', 'rb'))
try:
    similarity = pickle.load(open('similarity.pkl','rb'))
except:
    similarity = None

API_KEY = "YOUR_API_KEY_HERE"


# ── FETCH POSTER ─────────────────────────────────────────────────────────────
@st.cache_data
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
        response = requests.get(url, timeout=5)
        data = response.json()
        poster_path = data.get("poster_path")
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        return "https://via.placeholder.com/500x750?text=No+Poster"
    except:
        return "https://via.placeholder.com/500x750?text=No+Poster"


# ── RECOMMENDATION LOGIC ─────────────────────────────────────────────────────
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(
        list(enumerate(distances)), reverse=True, key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_posters


# ── SELECTOR CARD ────────────────────────────────────────────────────────────
st.markdown('<div class="selector-card">', unsafe_allow_html=True)

selected_movie = st.selectbox(
    "Choose a title from the library",
    movies['title'].values,
    key="movie_select"
)

if st.button("FIND SIMILAR FILMS", key="recommend_button"):
    with st.spinner("Analysing cinematic DNA…"):
        names, posters = recommend(selected_movie)

    st.markdown("""
    <div class="results-header">
        Recommended for you
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns(5)

    for col, name, poster, num in zip(
        [col1, col2, col3, col4, col5], names, posters,
        ["01", "02", "03", "04", "05"]
    ):
        with col:
            # st.image(poster, use_container_width=True)
            #st.image(poster)
            st.write(name)

            st.markdown(f"**{name}**")

st.markdown('</div>', unsafe_allow_html=True)


# ── SIDEBAR ──────────────────────────────────────────────────────────────────
st.sidebar.title("About CineMatch")

st.sidebar.markdown("""
<div style="color:#9a9080; font-size:13px; line-height:1.8;">
    A content-based recommendation engine that analyses film metadata using
    natural language processing to surface titles with similar
    cinematic DNA.
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
<div class="sidebar-section">
    <div style="font-size:10px; letter-spacing:3px; text-transform:uppercase; color:#c49a5c; margin-bottom:12px;">
        How it works
    </div>
    <div style="color:#7a7060; font-size:13px; line-height:2.0;">
        ◆ &nbsp;Text vectorisation of metadata<br>
        ◆ &nbsp;Cosine similarity scoring<br>
        ◆ &nbsp;Top-5 nearest neighbours<br>
        ◆ &nbsp;Live poster via TMDB API
    </div>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
<div class="sidebar-section">
    <div style="font-size:10px; letter-spacing:3px; text-transform:uppercase; color:#c49a5c; margin-bottom:12px;">
        Tech Stack
    </div>
    <span class="sidebar-badge">Python</span>
    <span class="sidebar-badge">Pandas</span>
    <span class="sidebar-badge">Scikit-learn</span>
    <span class="sidebar-badge">Streamlit</span>
    <span class="sidebar-badge">TMDB API</span>
</div>
""", unsafe_allow_html=True)

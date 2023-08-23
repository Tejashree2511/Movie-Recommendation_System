import pickle
import streamlit as st
import pandas as pd
import requests
import pickle
def fetch_poster(movie_id):
# https://api.themoviedb.org/3/movie/550?api_key=
url =
&quot;https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&amp;l
anguage=en-US&quot;.format(movie_id)
data = requests.get(url)
data = data.json() # converting into json
poster_path = data[&#39;poster_path&#39;]
full_path = &quot;https://image.tmdb.org/t/p/w500/&quot; + poster_path
return full_path
def recommend(movie):
index = movies[movies[&#39;title&#39;] == movie].index[0]
distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
recommended_movie_names = []
recommended_movie_posters = []
for i in distances[1:6]:
# fetch the movie poster
movie_id = movies.iloc[i[0]].movie_id
recommended_movie_posters.append(fetch_poster(movie_id))
recommended_movie_names.append(movies.iloc[i[0]].title)
return recommended_movie_names,recommended_movie_posters

st.header(&#39;Movie Recommendation System&#39;)
movies = pickle.load(open(&#39;movie_list.pkl&#39;, &#39;rb&#39;))
similarity = pickle.load(open(&#39;similarity.pkl&#39;, &#39;rb&#39;))
movie_list = movies[&#39;title&#39;].values
selected_movie = st.selectbox(
&quot;Select a movie from the dropdown&quot;,
movie_list
)
if st.button(&#39; Recommended Movies for you&#39;):
recommended_movie_names,recommended_movie_posters =
recommend(selected_movie)
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
st.text(recommended_movie_names[0])
st.image(recommended_movie_posters[0])
with col2:
st.text(recommended_movie_names[1])
st.image(recommended_movie_posters[1])
with col3:
st.text(recommended_movie_names[2])
st.image(recommended_movie_posters[2])
with col4:
st.text(recommended_movie_names[3])
st.image(recommended_movie_posters[3])
with col5:
st.text(recommended_movie_names[4])
st.image(recommended_movie_posters[4])
import streamlit as st
import pickle
import pandas as pd
import requests
# extracting the df using the pickle 
All_movies  = pickle.load(open('final_dict.pkl', 'rb'))
similarity  = pickle.load(open('similarity.pkl', 'rb'))
Final_movies = pd.DataFrame(All_movies)
st.title("Movie Recommendation System")


# We are using this function to recommend movies based on the user input
def recom(movie):
    movie_idx = Final_movies[Final_movies['title']== movie].index[0]
    Difference =  similarity[movie_idx]
    recommendation = sorted(enumerate(Difference), reverse = True , key = lambda x:x[1])[1:6]
    res = []
    for i in recommendation:
        res.append(Final_movies.iloc[i[0]].title)
    return res

# This selection box used to provide input to the user
option = st.selectbox(
    "Choose Your favorite Movie",
    (Final_movies['title'].values),
)
if st.button("Recommend"):
    res = recom(option)
    for i in res :
        st.write(i)
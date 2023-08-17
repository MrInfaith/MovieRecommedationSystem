import pandas as pd
import streamlit as st
st.title('Movie Recommender System-SACHIN')

def recommend(movi):
   movie_index=movie[movie['title']==movi].index[0]
   distances=similarity[movie_index]

   movie_list=sorted(list(enumerate(distances)),reverse= True,key=lambda x:x[1])[1:6]
   recommended_movies=[]
   for i in movie_list:
      recommended_movies.append(movie.iloc[i[0]].title)
   return recommended_movies
import pickle
movie_list=pickle.load(open('movie.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
movie=pd.DataFrame(movie_list)
option = st.selectbox(
    'Please Write A Movie Name ',
    movie['title'].values)
if st.button('Recommend'):
    recommendation=recommend(option)
    for i in recommendation:
       st.write(i)
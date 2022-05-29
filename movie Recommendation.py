Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore
 
@praveenlr01 
praveenlr01
/
Projects
Public
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
Projects/movieRecommendation.py /
@praveenlr01
praveenlr01 movie_Recommendation_system_using_ML_algorithm_python
Latest commit 773e124 25 days ago
 History
 1 contributor
64 lines (48 sloc)  2.09 KB
   
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tkinter import *

#backend
movies_data = pd.read_csv(r"C:\Users\ELCOT\Downloads\movies - movies.csv")

features_selected = ['genres', 'keywords', 'tagline', 'cast', 'director']

for feature in features_selected:
    movies_data[feature] = movies_data[feature].fillna('')

combine_features = movies_data['genres']+''+movies_data['keywords']+\
                   ''+movies_data['tagline']+''+movies_data['cast']+''+movies_data['director']

features_vector = TfidfVectorizer()
numeric_features = features_vector.fit_transform(combine_features)

similarity_values = cosine_similarity(numeric_features)

list_of_titles = movies_data['title'].tolist()

def view_():
    movie_name = e_input.get()
    find_close_match = difflib.get_close_matches(movie_name, list_of_titles)

    close_match = find_close_match[0]

    index_of_movie = movies_data[movies_data.title == close_match]['index'].values[0]

    similarity_score=list(enumerate(similarity_values[index_of_movie]))

    sorted_similar_movies=sorted(similarity_score,key=lambda x : x[1],reverse=True)
    scroll_bar_movie = Scrollbar()
    scroll_bar_movie.place(x=300, y=80)
    movies_list=Listbox(root,yscrollcommand=scroll_bar_movie.set)
    i = 1
    for movies in sorted_similar_movies:
        index = movies[0]
        fav_movies = movies_data[movies_data.index == index]['title'].values[0]
        if i <= 30:
            movies_list.insert(END,i,fav_movies)
            i += 1
    movies_list.place(x=190,y=80)
    scroll_bar_movie.config(command=movies_list.yview)

#frontend

root = Tk()
root.title("Movie Recommendation System")
root.geometry("421x421")

l_title = Label(root,text="MOVIES RECOMMENDATION SYSTEM",bg="blue",fg="white")
l_title.pack()
l_movie_name = Label(root, text="Enter Your Favourite Movie Name")
l_movie_name.place(x=0, y=60)
e_input = Entry(root)
e_input.place(x=190, y=60)
button_view=Button(root, text="VIEW", bg="green", fg="white", command=view_)
button_view.place(x=325, y=55)

root.mainloop()
© 2022 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
Loading complete

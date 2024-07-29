# -*- coding: utf-8 -*-
"""movie recommendation project

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vB74C3ho7841yP7_gMVgz3hH2pK1QfAJ

**MOVIE RECOMMENDATION SYSTEM**

To create a movie recommendation system, we can use several approaches ranging from simple algorithms to more complex machine learning models. Here’s a basic overview of different methods:

1. Popularity-Based Recommendation:

	•	Description: Recommends movies based on their overall popularity.
	•	Pros: Simple and effective for new users with no viewing history.
	•	Cons: Not personalized.

2. Content-Based Filtering:

	•	Description: Recommends movies similar to those the user has liked in the past. Uses movie features such as genre, director, actors, etc.
	•	Pros: Personalizes recommendations based on user preferences.
	•	Cons: Limited to recommending movies similar to those already seen.

3. Collaborative Filtering:

	•	Description: Recommends movies based on the preferences of similar users. Can be user-based or item-based.
	•	Pros: Can discover new movies outside the user’s typical preferences.

**IMPORT LIBRARY**
"""

import pandas as pd;

import numpy as np;

"""**IMPORT DATASET**"""

df = pd.read_csv(r"https://github.com/YBI-Foundation/Dataset/raw/main/Movies%20Recommendation.csv")

df.head()

df.info()

df.shape

df.columns

"""**GET FEATURE SELECTION**"""

df_features = df[['Movie_Genre','Movie_Keywords','Movie_Tagline', 'Movie_Cast','Movie_Director']].fillna('')

"""selected five existing features to recommend movies.it may vary from one project to another"""

df_features.shape

df_features

x = df_features['Movie_Genre']+''+df_features['Movie_Keywords']+''+df_features['Movie_Tagline']+''+df_features['Movie_Cast']+''+df_features['Movie_Director']

x

x.shape

"""**Get Features Text Conversation to Tokens**"""

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf=TfidfVectorizer

x=Tfidf.fit_transform(x)

x.shape

print(x)

"""**Get Similarity Score using Cosline Similarity**

cosine_similarity computes the L2-normalized dot product of vectors. Euclidean (L2) normalization projects the vectors onto the unit sphere, and their dot product is then the cosine of the angle between the points denoted by the vectors.
"""

from sklearn.metrics.pairwise import cosine_similarity

similarity_score=cosine_similarity(x)

similarity_score

similarity_score.shape

"""**Get Movie Name as Input from User and Validate for Closest Spelling**"""

Favourite_Movie_Name=input('Enter your favourite movie name :')

All_Movies_Tiltle_List=df['Movie_Title'].tolist()

import difflib

Movie_Recommendation=difflib.get_close_matches(Favourite_Movie_Name,All_Movies_Tiltle_List)
print(Movie_Recommendation)

Close_Match= Movie_Recommendation[0]
print(Close_Match)

Index_of_Close_Match_Movie=df[df.Movie_Title==Close_Match]['Movie_ID'].values[0]
print(Index_of_Close_Match_Movie)

#getting a list of similar movies
Recommendation_Score = list(enumerate(similarity_score[Index_of_Close_Match_Movie]))
print (Recommendation_Score)

len(Recommendation_Score)

"""**Get All Movies Sort Based on Recommendation Score wrt Favourite Movie**"""

#sorting the movies based on their similarity score
Sorted_Similar_Movies = sorted(Recommendation_Score, key = lambda x:x[1], reverse = True)
print(Sorted_Similar_Movies)

#print the name of similar movies based on the index
print("Top 30 Movies Suggested for You : \n")
i= 1
for movie in Sorted_Similar_Movies:
  index = movie[0]
  title_from_index = df[df.index==index]['Movie_Title'].values[0]
  if (i<31):
          print(i,'.',title_from_index)
          i+=1

"""**Top 10 Movie Recommendation System**"""

Movie_Name = input('Enter your favourite movie name : ')
list_of_all_titles = df['Movie_Title'].tolist()
Find_Close_Match = difflib.get_close_matches(Movie_Name, list_of_all_titles)
Close_Match = Find_Close_Match[0]
Index_of_Movie = df[df.Movie_Title == Close_Match]['Movie_ID'].values[0]
Recommendation_Score = list(enumerate(similarity_score[Index_of_Movie]))
sorted_similar_movies = sorted(Recommendation_Score, key = lambda x:x[1], reverse = True)
print('Top 10 Movies suggested for you : \n')
i = 1
for movie in sorted_similar_movies:
   index = movie[0]
   title_from_index = df[df.Movie_ID==index]['Movie_Title'].values
   if (i<11):
       print(i,'.',title_from_index)
       i+=1
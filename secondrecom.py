#load libraries

import pandas as pd

#load data

data = pd.read_csv("file.tsv",sep = "\t" , names = ["user_id","item_id","rating","timestamp"])
movies = pd.read_csv("Movie_Id_Titles.csv")
data = pd.merge(data,movies,on = "item_id")

#calculate mean rating and number of ratings for each movie

(data.groupby("title")["rating"].mean().sort_values(ascending=False).head())
(data.groupby("title")["rating"].count().sort_values(ascending=False).head())

#create a new dataframe ratings containing mean and number of ratings

newratings = pd.DataFrame(data.groupby("title")["rating"].mean())
newratings["number_of_ratings"] = pd.DataFrame(data.groupby("title")["rating"].count())
(newratings.head())

#newratings["rating"].hist(bins=70)0
#x=str(input("please enter a movie name which you like"))
#x="Star Wars(1977)"
#sort according to number of ratings

movie_mat = data.pivot_table(index="user_id",columns="title",values="rating")
(movie_mat.head())
(newratings.sort_values('number_of_ratings', ascending = False).head(10))

#analysing correlation

x_user_rating = movie_mat["Raiders of the Lost Ark (1981)"]
print(x_user_rating.head())
#similar_x = movie_mat.corrwith(x_user_rating)
#corr_x = pd.DataFrame(similar_x, columns=['Correlation'])
#corr_x.dropna(inplace=True)
#
##top similar movies of input movie
#
#corr_x.sort_values('Correlation', ascending=False).head(10)
#corr_x = corr_x.join(newratings['number_of_ratings'])
#print(corr_x[corr_x['number_of_ratings'] > 100].sort_values('Correlation', ascending=False).head())

import requests
import pandas as pd
from bs4 import BeautifulSoup

#using request to send a request and soup to read the files
response = requests.get('https://www.imdb.com/list/ls538975035/')
soup = BeautifulSoup(response.content, 'html.parser')


# to get the movie name from imdb
name = soup.find_all('h3',class_='lister-item-header')
movie_name = []
for i in name:
    movie_name.append(i.find('a').get_text())

#to get the ratings from imdb
rate = soup.find_all('div',class_='ipl-rating-widget')
movie_rating = []
for j in rate:
    movie_rating.append(j.find('span',class_='ipl-rating-star__rating').get_text())

#to get the image from imdb
image = soup.find_all('div',class_='lister-item-image ribbonize')
movie_image = []
for k in image:
    movie_image.append(k.find('img',class_='loadlate')['loadlate'])

#to get the image from imdb
genre = soup.find_all('span',class_='genre')
movie_genre = []
for x in genre:
    movie_genre.append(x.get_text().lstrip('\n'))





# arranging the dats into rows and columns using pandas
d = pd.DataFrame()
d['movie_name'] = movie_name
d['movie_ratings'] = movie_rating
d['movie_image'] = movie_image
d['movie_genre'] = movie_genre


#creating an csv file 
d.to_csv('movie_ratings.csv')








    


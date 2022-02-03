# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 09:31:50 2022

@author: MiguelFrejoMarañón
"""

import pandas as pd

import numpy as np


userHeader=['user_id', 'gender', 'age', 'ocupation', 'zip']

users=pd.read_table('C:\ExamenRecuperacion\ml-1m/users.dat', 
                     engine='python', sep='::', header=None, names=userHeader)


movieHeader=['movie_id', 'title', 'genders']

movies=pd.read_table('C:\ExamenRecuperacion\ml-1m/movies.dat', 
                     engine='python', sep='::', header=None, names=movieHeader, encoding='latin1') #latin1 porque tiene algún caracter que utf-8 no lee


ratingHeader=['user_id', 'movie_id', 'rating', 'timestamp']

ratings=pd.read_table('C:\ExamenRecuperacion\ml-1m/ratings.dat', 
                   engine='python', sep='::', header=None, names=ratingHeader)


merge_users_ratings=pd.merge(users, ratings)

userRatingsMoviesDF=pd.merge(merge_users_ratings, movies)
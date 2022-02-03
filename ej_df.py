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

opcion=1
while opcion > 0:
    print("--------------------MENU-------------------")
    print("----- 1.- Rating Medio STAR WARS por género. -----")
    print("----- 2.- Películas Mejor Valoradas. -----")
    print("----- 3.- Media de los usuarios del Género Terror. -----")
    print("----- 4.- Actualización de datos(doble del rating, título a mayúsculas y géneros a minúsculas). -----")
    print("----- 0.- Salir.-----")
    print("---------------------------------------------------------------------------------------------------")
    opcion=int(input("Introduzca una opción: "))

    if opcion < 0 or opcion > 4:
                    opcion=int(input("Introduce una opción válida"))
                    
    elif(opcion==1):
        df1=userRatingsMoviesDF.copy()
        df1 = userRatingsMoviesDF.pivot_table(index=['title'], 
                                              values=['rating'], 
                                              columns=['gender'], 
                                              aggfunc=[np.mean], 
                                              fill_value=-1,
                                              margins=True)
    
        rm=df1.loc[(df1.index.get_level_values('title').str.contains('Star Wars'))]
        print("Proceso completado, cierre el programa para ver los resultados")

    elif(opcion==2):
        df2=userRatingsMoviesDF.copy()
        
        peliculas2= df2.groupby(['title'])['ratings'].agg(
                                                           COUNT=np.size,
                                                           MEDIA=np.mean
                                                           )

        consulta1=peliculas2.loc[
                      
                       (peliculas2['COUNT']>1000)

                                       ]

        mejorPeliculas = consulta1.sort_values(['MEDIA', 'COUNT'],ascending=False)   
        print("Proceso completado, cierre el programa para ver los resultados")
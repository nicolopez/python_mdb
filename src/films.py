#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import imdb

class Films():
    def __init__(self):
        self.film_list = {}
        self.ia = imdb.IMDb()

    def get_film_info(self, movie):
        info = self.ia.search_movie(movie)
        if info:
            return info[0]

    def get_film_list(self, directory):
        for dirpath, dirs, files in os.walk(directory):
            for movie in files:
                if movie.endswith('.mp4') or movie.endswith('.mkv'):
                    self.film_list[movie] = 'NoInfo'
        print self.film_list


def main():
    movies = Films()
    movies.get_film_list('/run/media/nico/New Volume/Videos/Peliculas/')

if __name__ == '__main__':
    main()

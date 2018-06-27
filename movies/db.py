import sys

from django.db.models import Q

from .models import Movies
import logging
from .abstraction import *


def get_movies_data():
    """
    Function which fetches all questions from the database
    :return:
    """
    logging.info("Inside " + str(__name__))
    qs_array = []
    try:
        q_models = Movies.objects.all()
        for m1 in q_models:
            m2 = MoviesAbs()
            m2.m_id = m1.m_id
            m2.m_title = m1.m_title
            m2.m_director = m1.m_director
            m2.m_genre = m1.m_genre
            m2.m_imdb_score = m1.m_imdb_score
            m2.m_99popularity = m1.m_99popularity

            qs_array.append(m2)

        return q_models
    except Exception:
        exc_type, exc_obj, tb = sys.exc_info()
        # logging.critical("EXCEPTION - " + str(e) + " in " + str(__name__) + " on line number: " + str(tb.tb_lineno))
        return None


def get_all_movies_with_charecter(movie_name):
    """
    :return:
    """
    q = Q(m_title__icontains=movie_name) | Q(m_director__icontains=movie_name)
    movies = Movies.objects.filter(q)

    # for movie in movies:
    #     print movie.m_title

    return movies
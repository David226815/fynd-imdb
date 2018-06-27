import json
# import logging
# import sys
from .models import *


def read_json_file():
    movies_data = []
    with open('imdb.json') as f:
        movies_data = json.loads(f.read())

    for data in movies_data:
        j = []
        for i in data['genre']:
            j.append(str(i))
        data['genre'] = j

    return movies_data


def store_movie_in_db():
    """
    Function to store question in database
    :return:
    """
    logging.info("Inside " + str(__name__))
    try:
        movies_data = read_json_file()
        # m = Movies()
        for movie_data in movies_data:
            m = Movies()
            m.m_title = movie_data['name']
            m.m_director = movie_data['director']
            m.m_genre = movie_data['genre']
            m.m_imdb_score = movie_data['imdb_score']
            m.m_99popularity = movie_data['99popularity']
            m.save()
        return "DONE"
    except Exception:
        # exc_type, exc_obj, tb = sys.exc_info()
        # logging.critical("EXCEPTION - " + str(e) + " in " + str(__name__) + " on line number: " + str(tb.tb_lineno))
        return None


# if __name__ == '__main__':
#     store_question_in_db()

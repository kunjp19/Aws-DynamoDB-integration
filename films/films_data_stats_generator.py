import datetime
from decimal import Decimal
import sys

class FilmsDataStatsGenerator(object):

    def __init__(self, films_db_service):
        self.films_db_service = films_db_service

    def get_best_rated_film(self, director_name):
        """
        TODO Implement
        Retrieves the name of the best rated film that was directed by the director with the given name.
        If there are no films directed the the given director, return the None object.
        Note there will only be one film with the best rating.
        """
        best_rated_film = None
        films = self.films_db_service.get_films(director_name)
        if len(films) != 0:
            best_rating = -1
            for film in films:
                if film["rating"]>best_rating:
                    best_rated_film = film
                    best_rating = film["rating"]
        return best_rated_film["filmName"]

    def get_average_rating(self, director_name):
        """
        TODO Implement
        Retrieves the average rating for the films directed by the given director, rounded to 1 decimal place.
        If there are no films directed the the given director, return the None object.
        """

        films = self.films_db_service.get_films(director_name)
        rating_sum = 0
        for film in films:
            rating_sum += film["rating"]
        return Decimal(rating_sum/len(films)).quantize(Decimal('0.1'))

    def get_shortest_number_of_days_between_film_releases(self, director_name):
        """
        TODO Implement
        Retrieves the shortest number of days between any two film releases directed by the given director.
        If there are no films directed by the given director, return the None object.
        If there is only one film directed by the given director, return 0.
        Note that no director released more than one film on any given day.

        For example, if the prod.films DynamoDB table contains the following 3 items for director Christopher Nolan,

        {
            "filmName": "Batman Begins",
            "length": 140,
            "rating": 8.2,
            "releaseDate": "2006-06-16",
            "directorName": "Christopher Nolan"
        },
        {
            "filmName": "Interstellar",
            "length": 169,
            "rating": 8.6,
            "releaseDate": "2014-11-07",
            "directorName": "Christopher Nolan"
        },
        {
            "filmName": "Prestige",
            "length": 130,
            "rating": 8.5,
            "releaseDate": "2006-11-10",
            "directorName": "Christopher Nolan"
         }

        then this method should return 147 for Christopher Nolan, as Prestige was released 147 days after Batman Begins.
        """
        days = None
        films = self.films_db_service.get_films(director_name)
        if len(films) == 1:
            days = 0
        else:
            day_list=[]
            for film in films:
                releaseDate = film['releaseDate'].split("-")
                year = int(releaseDate[0])
                month = int(releaseDate[1])
                day = int(releaseDate[2])
                day_list.append(datetime.date(year, month, day))

            day_list.sort()
            min_days=sys.maxsize
            for i in range(len(day_list)):
                for j in range(i,len(day_list)):
                    diff = day_list[j]-day_list[i]
                    if i!=j and min_days>diff.days:
                        min_days=diff.days
            days=min_days
        return days

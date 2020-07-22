"""
Note that this file cannot be modified.
If you would like to add your own unit tests, please put these in a separate test file.
"""

import pytest

from decimal import Decimal

from films.films_db_service import FilmsDBService
from films.films_data_stats_generator import FilmsDataStatsGenerator

RIDLEY_SCOTT_DIRECTOR = "Ridley Scott"

_generator = FilmsDataStatsGenerator(FilmsDBService())

@pytest.fixture
def stats_generator_setup():
    return _generator

def test_best_rated_film(stats_generator_setup):
    assert stats_generator_setup.get_best_rated_film(RIDLEY_SCOTT_DIRECTOR) == "Gladiator"

def test_get_average_rating(stats_generator_setup):
    assert stats_generator_setup.get_average_rating(RIDLEY_SCOTT_DIRECTOR) == Decimal("7.0")
    
def test_get_shortest_days_between_releases(stats_generator_setup):
    assert stats_generator_setup.get_shortest_number_of_days_between_film_releases(RIDLEY_SCOTT_DIRECTOR) == 29

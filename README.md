# Python-DynamoDB
The `prod.films` `DynamoDB` table stores stores data for various films.

Each `Item` in the `prod.films` table contains 5 `Attributes`:

* `filmName` - the name of the film, a DynamoDB `String`. 
* `directorName` - the name of the director who directed the film, a DynamoDB `String`.
* `length` - the duration of the film in minutes, a DynamoDB `Number`.
* `rating` - the <a href="https://www.imdb.com/" target="_blank">`IMDb`</a> rating for the film, a DynamoDB `Number`.
* `releaseDate` - the date in which the film was released in the United Kingdom, a DynamoDB `String`.


The `filmName` is the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.PrimaryKey" target="_blank">Hash (Partition) Key</a> of the table.
The `prod.films` table also contains one <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.SecondaryIndexes" target="_blank">Global Secondary Index (GSI)</a> called `DirectorName`. The `Hash Key` of this index is
the `directorName` attribute.

An example `Item` from the table, in JSON format, is given below:

    {
      "filmName": "Batman Begins",
      "directorName": "Christopher Nolan"
      "length": 140,
      "rating": 8.2,
      "releaseDate": "2006-06-16"
    }

## Your Task

You are required to implement the all the methods marked with `TODO Implement` in the [FilmsDBService](films/films_db_service.py) and [FilmDataStatsGenerator](films/films_data_stats_generator.py) classes in such a way that
all the unit tests in [test/test_films_data_stats_generator.py](test/test_films_data_stats_generator.py) pass.

[FilmsDBService](films/films_db_service.py) should be implemented in such a way that you only need to query the `prod.films`
table once per full run of the [test/test_films_data_stats_generator.py](test/test_films_data_stats_generator.py) test suite.

## Requirements

The [test/test_films_data_stats_generator.py](test/test_films_data_stats_generator.py) file should not be modified. If you would like to add your own unit tests, you
can add these in a separate file.

The [requirements.txt](requirements.txt) file should only be modified to add any third-party dependencies required for your solution. <br> Please note that all third-party depdencies required for your solution **MUST** be added to the [requirements.txt](requirements.txt) file.

You must use the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.html" target="_blank">`AWS DynamoDB SDK Python (Boto 3)`</a> library to work with DynamoDB.
The dependency for this library has already been added to the `requirements.txt` file.

Apart from that, you are free to use whichever libraries you want (Python or third-party) when implementing your solution. </br>
Note we recommend using the <a href="https://docs.python.org/3.7/library/datetime.html" target="_blank">`Python datetime`</a> library for working with dates.

Your solution also must use/be compatible with `Python version 3.7`.

##

This test should take no longer than 2 hours to complete successfully.

Good luck!

## Submitting your solution

Please push your changes to the `master branch` of this repository. You can push one or more commits. <br>

Once you are finished with the task, please click the `Complete task` link on <a href="https://app.codescreen.dev/#/codescreentest482cb078-0bb6-4854-a464-9648339e90fb" target="_blank">this screen</a>.

import boto3
import os


class FilmsDBService(object):

    # Setup. None of this should be modified.
    aws_credentials_path = "credentials"
    films_dynamo_db_table_name = "prod.films"
    region_name="eu-west-1"
    os.environ["AWS_SHARED_CREDENTIALS_FILE"] = aws_credentials_path
    dynamo_client = boto3.Session(region_name=region_name).resource('dynamodb')

    def get_films(self, director_name):
        """
        TODO Implement
        Retrieves the data for all films, for the given director, by querying the prod.films DynamoDB table.

        Each Item in the prod.films table contains 5 attributes:

        filmName - the name of the film.
        directorName - the name of the director who directed the film.
        length - the duration of the film in minutes.
        rating - the IMDb rating for the film.
        releaseDate - the date in which the film was released in the United Kingdom.

        The filmName is the Hash (Partition) Key of the table.
        The prod.films table also contains one Global Secondary Index (GSI) called DirectorName. The Hash Key of this index
        is the directorName attribute.
        """
        dynamodb_table = self.dynamo_client.Table(self.films_dynamo_db_table_name)
        records = dynamodb_table.query(IndexName="DirectorName", KeyConditionExpression=boto3.dynamodb.conditions.Key("directorName").eq(director_name))
        return records["Items"]
        

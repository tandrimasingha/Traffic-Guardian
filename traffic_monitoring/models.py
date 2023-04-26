import json
import urllib.request
from datetime import datetime
import boto3
import psycopg2


# This process_image() method code defines a function named process_image that takes three parameters:

# camera_ids: a list of camera ids
# phenomenon_time: a string representing a timestamp
# model_endpoint: a string representing the name of a endpoint
# The function first establishes a database connection to a database hosted on an Amazon RDS instance using the psycopg2 library. 
# The database connection string is stored in a variable named conn_string.
# Then, for each camera_id in the camera_ids list, the function retrieves an image from a specific URL using the urllib library. 
# The image data is stored in a variable named image.


def count_vehicles(event, context):
    phenomenon_time = datetime.now()
    camera_ids = [122, 107, 129, 95, 36, 75, 26, 32]
    process_image(camera_ids, phenomenon_time, 'vehicle-model-endpoint')


def count_humans(event, context):
    phenomenon_time = datetime.now()
    camera_ids = [122, 107, 129, 95, 36, 75, 26, 32]
    process_image(camera_ids, phenomenon_time, 'human-model-endpoint')


def count_bikes(event, context):
    phenomenon_time = datetime.now()
    camera_ids = [122, 107, 129, 95, 36, 75, 26, 32]
    process_image(camera_ids, phenomenon_time, 'bike-model-endpoint')

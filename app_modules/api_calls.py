import random
import requests
import logging

# Configure this module's logs to be stored in a separate file
logging.basicConfig(filename='logs/api_calls.log', 
                    encoding='utf-8', 
                    level=logging.INFO, 
                    format='%(asctime)s %(message)s', 
                    datefmt='%m/%d/%Y %I:%M:%S %p')

def get_10_random():
    "GET posts from the API and display 10 random ones."

    # Send a GET request to the server
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        # Check if an error code was returned
        response.raise_for_status()
        # Select 10 random posts
        random_posts = random.sample(response.json(), 10)
        # Log a successful request and return the sample
        logging.info('Successful GET request by get_10_random() method.')
        return random_posts

    # If an error occured, log it and return an empty list
    except (Exception) as err:
        logging.error(f'An error occurred while processing the request: {err}')
        return []

get_10_random()
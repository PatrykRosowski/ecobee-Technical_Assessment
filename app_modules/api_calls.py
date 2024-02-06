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
    """
    GET posts from the API and display 10 random ones.
    return -- a list of 10 random posts
    """

    # Send a GET request to the server
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        # Check if an error code was returned
        response.raise_for_status()
        # Set the correct sample size in case there are fewer than 10 posts
        sample_size = min(10, len(response.json()))
        print(sample_size)
        # Select 10 random posts
        random_posts = random.sample(response.json(), sample_size)
        # Log a successful request and return the sample
        logging.info('Successful GET request by get_10_random() method.')
        return random_posts

    # If an error occured, log it and return an empty list
    except (Exception) as err:
        logging.error(f'An error occurred while processing the request: {err}')
        return []

def get_1_post(post_id):
    """ 
    Select a single post from the API and return it. 
    post_id -- the ID of the post to be returned
    return -- a single post
    """

    # Send a GET request to the server
    try:
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
        # Check if an error code was returned
        response.raise_for_status()
        # Log a successful request and return the post
        logging.info('Successful GET request by choose_1_post() method.')
        return response.json()
    # If an error occured, log it and return an empty dictionary
    except (Exception) as err:
        logging.error(f'An error occurred while processing the request: {err}')
        return {}
    # If the post ID was not found, log it and return an empty dictionary
    except response == {}:
        logging.error('No post found with the given ID.')
        return {}

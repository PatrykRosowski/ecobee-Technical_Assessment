import requests
import logging
from app_modules import api_calls

''' 
Tests utilising the remote API.
This ensures that the methods return valid results when interacting with
the API hosted at https://jsonplaceholder.typicode.com/. 
'''

######################### get_10_random() method tests #########################


def test_get_10_random_remote_valid():
    """ Test the get_10_random() method for the correct sample size """

    # Call the get_10_random() method to fetch posts and return 10 random ones
    results = api_calls.get_10_random()
    logging.info(f'\n\nRESULTS RETURNED BY THIS METHOD: {results}\n')

    # Validate that the results contain a list of 10 random items
    assert len(results) == 10

    # Validate that each post has the correct structure
    for result in results:
        assert isinstance(result, dict), "Each post should be a dictionary"
        assert set(result.keys()) == {'userId', 'body', 'title', 'id'}


########################## get_1_post() method tests ###########################


def test_get_1_post_remote_valid():
    """ Test the get_1_post() method for the correct post ID """

    # Call the get_1_post() method to fetch a single post
    result = api_calls.get_1_post(3)
    logging.info(f'\n\nRESULTS RETURNED BY THIS METHOD: {result}\n')

    # Validate that the id of the returned post is 3
    assert result['id'] == 3

    # Validate that the post has the correct structure
    assert isinstance(result, dict)
    assert set(result.keys()) == {'userId', 'body', 'title', 'id'}
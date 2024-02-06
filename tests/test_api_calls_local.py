from random import randint
import logging
import requests
from app_modules import api_calls

''' 
Local tests utilising a mock API.
This ensures that the development can be carried out even when the API hosted
at https://jsonplaceholder.typicode.com/ is not available. 
'''

######################### get_10_random() method tests #########################


def test_get_10_random_valid(mocker):
    """ Test the get_10_random() method for the correct sample size. """

    # 100 items of data to be returned from mock API 
    data = [{'userID': randint(1, 10), 
             'id': i, 
             'title': f'Post {i}', 
             'body': 'abc'} 
             for i in range(100)]

    # Set up a Mock() object that simulates an API endpoint for local testing
    mocker_get = mocker.patch('requests.get')
    mocker_get.return_value = mocker.Mock()

    # Mock() object returns 100 mock posts
    mocker_get.return_value.json.return_value = data

    # Call the get_10_random() function and store the results in a variable
    results = api_calls.get_10_random()
    logging.info(f'\n\nRESULTS RETURNED BY THIS METHOD: {results}\n')

    # Verify that the results contain a list of 10 random items
    assert len(results) == 10

    # Validate that each post has the correct structure
    for result in results:
        assert isinstance(result, dict), "Each post should be a dictionary"
        assert set(result.keys()) == {'userID', 'id', 'title', 'body'}


def test_get_10_random_insuff_num(mocker):
    """ Test the get_10_random() method when the API returns insufficient data. """
    # 5 items of data to be returned from mock API 
    data = [{'userID': randint(1, 10), 
             'id': i, 
             'title': f'Post {i}', 
             'body': 'abc'} 
             for i in range(5)]

    # Set up a Mock() object that simulates an API endpoint for local testing
    mocker_get = mocker.patch('requests.get')
    mocker_get.return_value = mocker.Mock()

    # Mock() object returns 5 mock posts
    mocker_get.return_value.json.return_value = data

    # Call the get_10_random() function and store the results in a variable
    results = api_calls.get_10_random()
    logging.info(f'\n\nRESULTS RETURNED BY THIS METHOD: {results}\n')

    # Validate that the results contain a list of 5 random items
    assert len(results) == 5

    # Validate that each post has the correct structure
    for result in results:
        assert isinstance(result, dict), "Each post should be a dictionary"
        assert set(result.keys()) == {'userID', 'id', 'title', 'body'}


def test_get_10_random_connection_error(mocker):
    """ Test the get_10_random() method when a connection error occurs."""

    # Simulate a ConnectionError in a GET request
    mocker.patch('requests.get', side_effect=requests.exceptions.ConnectionError)
    # Validate that the results returned by get_10_random() are an empty list
    results = api_calls.get_10_random()
    assert results == []


def test_get_10_random_timeout_error(mocker):
    """ Test the get_10_random() method when a timeout error occurs. """

    # Simulate a Timeout error in a GET request
    mocker.patch('requests.get', side_effect=requests.exceptions.Timeout)
    # Validate that the results returned by get_10_random() are an empty list
    results = api_calls.get_10_random()
    assert results == []


def test_get_10_random_http_error(mocker):
    """ Test the get_10_random() method when an HTTP error occurs. """

    # Simulate an HTTPError in a GET request
    mocker.patch('requests.get', side_effect=requests.exceptions.HTTPError)
    # Validate that the results returned by get_10_random() are an empty list
    results = api_calls.get_10_random()
    assert results == []


########################## get_1_post() method tests ###########################


def test_get_1_post_valid(mocker):
    """ Test the get_1_post() method for the correct post ID. """

    # 1 item of data to be returned from mock API 
    data = {'userID': randint(1, 10), 
             'id': 3, 
             'title': 'Post 3', 
             'body': 'abc'}

    # Set up a Mock() object that simulates an API endpoint for local testing
    mocker_get = mocker.patch('requests.get')
    mocker_get.return_value = mocker.Mock()

    # Mock() object returns a single mock post
    mocker_get.return_value.json.return_value = data

    # Call the get_1_post() function and store the results in a variable
    result = api_calls.get_1_post(3)
    logging.info(f'\n\nRESULTS RETURNED BY THIS METHOD: {result}\n')

    # Validate that the post has the correct ID
    assert result['id'] == 3

    # Validate that the post has the correct structure
    assert isinstance(result, dict)
    assert set(result.keys()) == {'userID', 'id', 'title', 'body'}


def test_get_1_post_insuff_num(mocker):
    """ Test the get_1_post() method when the API returns insufficient data. """

    # An empty dictionary to be returned from mock API
    data = {}

    # Set up a Mock() object that simulates an API endpoint for local testing
    mocker_get = mocker.patch('requests.get')
    mocker_get.return_value = mocker.Mock()

    # Mock() object returns 5 mock posts
    mocker_get.return_value.json.return_value = data

    # Call the get_10_random() function and store the results in a variable
    result = api_calls.get_1_post(101)
    logging.info(f'\n\nRESULTS RETURNED BY THIS METHOD: {result}\n')

    # Validate that the result is an empty dictionary
    assert result == {}


def test_get_1_post_connection_error(mocker):
    """ Test the get_1_post() method when a connection error occurs."""

    # Simulate a ConnectionError in a GET request
    mocker.patch('requests.get', side_effect=requests.exceptions.ConnectionError)
    # Validate that the result is an empty dictionary
    result = api_calls.get_1_post(1)
    assert result == {}


def test_get_1_post_timeout_error(mocker):
    """ Test the get_1_post() method when a timeout error occurs. """

    # Simulate a Timeout in a GET request
    mocker.patch('requests.get', side_effect=requests.exceptions.Timeout)
    # Validate that the result is an empty dictionary
    result = api_calls.get_1_post(1)
    assert result == {}


def test_get_1_post_http_error(mocker):
    """ Test the get_1_post() method when an HTTP error occurs. """

    # Simulate an HTTPError in a GET request
    mocker.patch('requests.get', side_effect=requests.exceptions.HTTPError)
    # Validate that the result is an empty dictionary
    result = api_calls.get_1_post(1)
    assert result == {}

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


def test_get_1_post_invalid_id():
    """ Test the get_1_post() method for an invalid post ID """

    # Call the get_1_post() method to fetch a single post
    result = api_calls.get_1_post(999)
    logging.info(f'\n\nRESULTS RETURNED BY THIS METHOD: {result}\n')

    # Validate that the returned post is an empty dictionary
    assert result == {}


####################### get_comm_for_post() method tests #######################
    

def test_get_comm_for_post_remote_valid():
    """ Test the get_comm_for_post() method for the correct post ID """

    # Call the get_comm_for_post() method to fetch comments for a single post
    results = api_calls.get_comm_for_post(3)
    logging.info(f'\n\nRESULTS RETURNED BY THIS METHOD: {results}\n')

    # Validate that the results contain a list of comments
    assert isinstance(results, list)

    # Validate that each comment has the correct structure
    for result in results:
        assert isinstance(result, dict), "Each comment should be a dictionary"
        assert set(result.keys()) == {'postId', 'id', 'name', 'email', 'body'}

    # Validate that there are 5 comments for the post with ID 3
    assert len(results) == 5


def test_get_comm_for_post_remote_invalid_id():
    """ Test the get_comm_for_post() method for an invalid post ID """

    # Call the get_comm_for_post() method to fetch comments for a single post
    results = api_calls.get_comm_for_post(999)
    logging.info(f'\n\nRESULTS RETURNED BY THIS METHOD: {results}\n')

    # Validate that the results are an empty list
    assert results == []


######################### post_comment() method tests ##########################


def test_post_comment_remote_valid():
    """ Test the post_comment() method for a valid comment """

    # Call the post_comment() method to post a comment to the API
    result = api_calls.post_comment(1, 'name', 'email@gmail.com', 'body')
    logging.info(f'\n\nRESULTS RETURNED BY THIS METHOD: {result}\n')

    # Validate that the returned result is a dictionary
    assert isinstance(result.json(), dict)

    # Validate that the result has the correct structure
    assert set(result.json().keys()) == {'postId', 'id', 'name', 'email', 'body'}


######################## delete_comment() method tests #########################
    

def test_delete_comment_remote_valid():
    """ Test the delete_comment() method for a valid comment ID """

    # Call the delete_comment() method to delete a comment from the API
    result = api_calls.delete_comment(1)
    logging.info(f'\n\nRESULTS RETURNED BY THIS METHOD: {result}\n')

    # Validate that the returned result is an empty dictionary
    assert result == {}
    
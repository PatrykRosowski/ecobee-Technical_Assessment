from random import randint
import logging
from app_modules import api_calls

''' 
Local tests utilising a mock API.
This ensures that the development can be carried out even when the API hosted
at https://jsonplaceholder.typicode.com/ is not available. 
'''
# At the top of your test file
logging.basicConfig(handlers=[logging.StreamHandler()], level=logging.INFO)

# Test the get_10_random() method locally for the correct sample size
def test_get_10_random_valid(mocker):
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
    logging.info('\nRESULTS RETURNED BY THIS METHOD: ' + str(results))

    # Verify that the results contain a list of 10 random items
    assert len(results) == 10
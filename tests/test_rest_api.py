"""
This module contains basic REST API tests using requests.
Their purpose is to show how to use the pytest framework by example.

Terminal > pip install requests
# https://duckduckgo.com/api
"""

#----------------------------------------------------------------------
# imports
#----------------------------------------------------------------------
import pytest
import requests

#----------------------------------------------------------------------
# tests
#----------------------------------------------------------------------

@pytest.mark.duckduckgo
@pytest.mark.rest_api
def test_duckduckgo_instant_answer_api():

    # Arrange
    url = 'https://api.duckduckgo.com/?q=DuckDuckGo&format=json'

    # Act
    response = requests.get(url)
    body = response.json()

    # Assert
    assert response.status_code == 200
    assert 'DuckDuckGo is an internet search engine that emphasizes protecting searchers' in body['AbstractText']


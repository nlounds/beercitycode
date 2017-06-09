"""This module does tests"""

import pytest
from expecter import expect

from webcalc import app


@pytest.fixture
def client():
    return app.test_client()


def describe_index():

    def it_says_hello(client):
        response = client.get('/')

        expect(response.data).contains(b"Hello, world!")

#    def it_not_says_goodbye(client):
#        response = client.get('/')
#
#        expect(response.data).contains(b"Good-bye")
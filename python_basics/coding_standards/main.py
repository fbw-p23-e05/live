"""
This module contains functions for something
The functions do other things.
Author: Mason
Date: 12 October 2023
"""

from datetime import datetime


class Person:
    """
    This is the user class.
    """

    def create_users(self):
        """
        This function creates a new user
        and adds the user to the database.
        """

        users = {}

        # this the creation of user details
        user_details = [datetime.now(), 6000]

        for user_id in range(1, 10):
            users[user_id] = user_details


def example_func():
    """This is another function"""
    result = 2 + 1

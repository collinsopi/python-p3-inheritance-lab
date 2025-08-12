#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        # Call the parent class's __init__ method
        super().__init__(first_name, last_name)
        # Initialize the knowledge attribute as an empty list
        self.knowledge = []

    def learn(self, new_knowledge):
        # Add a new string to the knowledge list
        self.knowledge.append(new_knowledge)
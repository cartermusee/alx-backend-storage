#!/usr/bin/env python3
"""module to insert"""
from typing import List


def insert_school(mongo_collection: List, **kwargs) -> int:
    """adding items
    Keyword arguments:
    mongo_collection : collections
    kwargs: a number of arguments with the values
    Return: the id of added item
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id

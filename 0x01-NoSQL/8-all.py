#!/usr/bin/env python3
"""module to print all databases"""
from typing import List


def list_all(mongo_collection: List[str]) -> List:
    """sumary_line
    Keyword arguments:
    mongo_collection: list af all collections
    Return: list of name or empty
    """
    if mongo_collection is None:
        return []
    all_doc = []
    for collection in mongo_collection.find():
        all_doc.append(collection)
    return all_doc

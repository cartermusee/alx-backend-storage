#!/usr/bin/env python3
"""module for update"""
from typing import List


def update_topics(mongo_collection: List, name: str, topics: List[str]):
    """update
    Keyword arguments:
    mongo_collection: the collection
    name: name to use for updating
    topics: the topics to update
    Return: the updated
    """
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})

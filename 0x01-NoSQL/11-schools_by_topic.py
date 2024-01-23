#!/usr/bin/env python3
"""model for query"""
from typing import List


def schools_by_topic(mongo_collection: object, topic: str) -> List:
    """sumary_line
    Keyword arguments:
    mongo_collection: collection from mongo
    topic: string withn topiccs
    Return: return_description
    """
    topics = mongo_collection.find({"topics": topic})
    school_topics = list(topics)
    return school_topics

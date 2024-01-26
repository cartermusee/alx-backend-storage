#!/usr/bin/env python3
"""module for average"""
from pymongo import MongoClient
from typing import Union

def top_students(mongo_collection):
    """top studensts
    Keyword arguments:
    mongo_collection: pymongo collection
    Return: all students
    """
    result = mongo_collection.aggregate([
        {"$match": {}},
        { "$project": {
            "name": 1,
            "averageScore": {"$avg": "$topics.score"}
        }},
        { "$sort": {"averageScore": -1}}
    ])
    return result
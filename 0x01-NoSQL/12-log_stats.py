#!/usr/bin/env python3
"""module for nginx logs"""
from pymongo import MongoClient


if __name__ == "__main__":

    cluster = MongoClient('mongodb://localhost:27017')
    db = cluster['logs']
    collection = db['nginx']

    count_docs = collection.count_documents({})
    print("{} logs".format(count_docs))
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    status_count = collection.count_documents(
        {"method": "GET", "path": "/status"})
    print("{} status check".format(status_count))

#!/usr/bin/env python

import time
import requests
import logging
from datetime import datetime
from pymongo import MongoClient
from docker_context.data_processor import DataProcessor


def main():
    # set up mongo client
    # client = MongoClient("192.168.0.1", port=30001)
    client = MongoClient("localhost", port=30001)
    db = client.business
    c = db.prometheus.find({}).count()
    print("In prometheus: {}".format(c))
    print("In 35: {}".format(db.prometheus["35"].find({}).count()))
    print("In 75: {}".format(db.prometheus["75"].find({}).count()))
    db.prometheus.drop()
    db.prometheus["35"].drop()
    db.prometheus["45"].drop()
    db.prometheus["65"].drop()
    db.prometheus["75"].drop()

if __name__ == "__main__":
    main()

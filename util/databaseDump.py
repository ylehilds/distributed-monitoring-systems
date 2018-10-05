#!/usr/bin/env python

from pymongo import MongoClient

# set up mongo client
client = MongoClient("192.168.0.1", port=30001)
db = client.prometheus
db.prometheus.insert_many([{'lehi':'test'}])
print('collection find:')

for doc in db.prometheus.find({}):
  print(doc)


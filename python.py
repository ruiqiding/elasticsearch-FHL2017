from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

# index a message
message = {
    "search_fields": {
        "searchable_text": "Yammer is amazing",
        "access_data": {
            "public_access": True
        }
    },
    "model": {
        "id": {
            "id": 345,
            "type": "message",
            "network": 117
        },
        "state": "ACTIVE",
        "timestamp": 1501003000
    }
}

res = es.index(index="message", doc_type='message', id=345, body=message)
print(res['created'])

es.indices.refresh(index="message")

# get the message
res = es.get(index="message", doc_type='message', id=345)
print(res['_source'])

# search and display

res = es.search(index="message", 
  body={"query": { "match": { "search_fields.searchable_text": "Yammer" }}})

print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print( hit["_source"]['model']['id'])

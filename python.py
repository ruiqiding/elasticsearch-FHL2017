from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

doc = {
    "search_fields": {
        "searchable_text": "Yammer is amazing",
        "access_data": {
            "public_access": true
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

res = es.index(index="message", doc_type='message', id=345, body=doc)
print(res['created'])

res = es.get(index="message", doc_type='message', id=345)
print(res['_source'])

es.indices.refresh(index="message")

res = es.search(index="message", 
  body={"query": { "match": { "search_fields.searchable.text": "Yammer" }}})
print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print("%(model.id.id)s: %(search_fields.searchable_text)s" % hit["_source"])

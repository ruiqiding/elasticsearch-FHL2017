# MSFT FHL2017: Let's Build a Simplified Yammer Search

## We will create an index (table) for Yammer message, define index mapping (schema), add a few messages, and search for them. YAY!

0. Install [Java](http://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html)
1. Download [Elasticsearch](https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.5.1.zip)
2. Run bin/elasticsearch (or bin\elasticsearch.bat on Windows)

_Elasticsearch is up and running now_

3. (Optional if curl is your best friend) Install Postman
* [App](https://www.getpostman.com/apps)
* [Chrome](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en)

4. (Optional) Install elasticsearch python client if you have Python installed: "pip install elasticsearch"

_Next, let's create an index, then index and search yammer messages using Elasticsearch RESTful API_

5. Use Postman or curl to follow https://github.com/ruiqiding/elasticsearch-FHL2017/blob/master/restful.txt
6. Programmer's way: use Python to run https://github.com/ruiqiding/elasticsearch-FHL2017/blob/master/python.py

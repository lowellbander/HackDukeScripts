from twython import Twython
import urllib
from pprint import pprint
from firebase import Firebase

APP_KEY = 'hvddwcOWke5tcwZ7fqsylEUrD'
APP_SECRET = 'J0S2QdnMHa7dos3eX0xjho9rF8f0aw5OGsFAyiRzXMEBdF9Qxc'

def do_query(query):
    twitter = Twython(APP_KEY, APP_SECRET)
    query = urllib.quote_plus(query)
    query = query[:140] # twitter queries limited to 140 chars
    print "query: " + query
    return twitter.search(q=query, count=1)

def print_results(results, fields):
    for status in results['statuses']:
        print "\n\n --------------------------------- \n\n"
        for field in fields:
            print field + ": ",
            print status[field]

def upload(status):
    f = Firebase('https://amber-fire-5569.firebaseio.com/tweets')
    payload = {}
    payload['body'] = status['text']
    payload['geo'] = status['geo']
    payload['date'] = status['created_at']
    print payload
    f.push(payload)

def main():

    terms = ['I-40', 'I-85', 'I-440', 'I-540', 'US Route 1', 'US Route 15', 'US Route 64', 'US Route 70', 'US Route 264', 'US Route 401', 'US Route 501', 'NC147', 'NC540 ', 'car crash', 'car accident', 'car collision', 'car pile up']

    fields = ['text', 'geo', 'created_at']

    for term in terms:
        results = do_query(term)
        for status in results['statuses']:
            upload (status)

if __name__ == "__main__":
    main()

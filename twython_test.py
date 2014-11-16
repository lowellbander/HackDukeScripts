from twython import Twython
import urllib
from pprint import pprint

APP_KEY = 'hvddwcOWke5tcwZ7fqsylEUrD'
APP_SECRET = 'J0S2QdnMHa7dos3eX0xjho9rF8f0aw5OGsFAyiRzXMEBdF9Qxc'

def do_query(terms):
    twitter = Twython(APP_KEY, APP_SECRET)
    query = " OR ".join(terms)
    query = urllib.quote_plus(query)
    print "query: " + query
    return twitter.search(q=query)

def main():

    #terms = ['I-40', 'I-85', 'I-440', 'I-540', 'US Route 1', 'US Route 15', 'US Route 64', 'US Route 70', 'US Route 264', 'US Route 401', 'US Route 501', 'NC147', 'NC540 ', 'car crash', 'car accident', 'car pile up', 'car collision']

    terms = ['blue', 'red']

    results = do_query(terms)

    for status in results['statuses']:
        print "\n\n --------------------------------- \n\n"
        print "text:" + status['text']
        print "geo:" + str(status['geo'])


if __name__ == "__main__":
    main()

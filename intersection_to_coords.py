from urlparse import urlparse
from pprint import pprint
import json
import urllib
import urllib2

def intersection_to_coords(street1, street2):
    URL = "https://geocoder.cit.api.here.com/6.2/geocode.json?"
    city = 'Durham'
    app_id = 'mE6R9yyPKiEw4exQsim6'
    app_code = '2O22bck0uNEo2_xezVdIpg'
    gen = '6'
    street = street1 + " @ " + street2
    street = urllib.quote(street)

    URL += 'city=' + city
    URL += '&app_id=' + app_id
    URL += '&app_code=' + app_code
    URL += '&gen=' + gen
    URL += '&street=' + street

    response = urllib2.urlopen(URL)
    result = response.read()
    return json.loads(result)

def main():
    result = intersection_to_coords("South Alston", "Dayton")
    try:
        coords = result['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']
    except IndexError:
        print "No Coordinates Found!"
        return
    
    print coords

if __name__ == "__main__":
    main()

from firebase import Firebase
from pprint import pprint
from intersection_to_coords import intersection_to_coords


def main():
    BASE_URL = 'https://amber-fire-5569.firebaseio.com/Traffic/'
    f = Firebase(BASE_URL)
    
    results = f.get()
    
    for key in results:
        pprint(key)
        pprint(results[key])
        payload = results[key]
        
        street1 = results[key]['intersection1']
        street2 = results[key]['intersection2']

        coords = intersection_to_coords(street1, street2)
        print coords

        try:
            payload['Latitude'] = coords['Latitude']
        except TypeError:
            continue
        payload['Longitude'] = coords['Longitude']
        endpoint = Firebase(BASE_URL+key)
        pprint(payload)
        endpoint.set(payload)

if __name__ == '__main__':
    main()

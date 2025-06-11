import urllib.parse, urllib.request, urllib.error, json
import pprint
import keys

## PARAMETERS INTO URL TESTS
key = keys.secret_key
dict = {"lat": 47.658502, "lon": -122.309483,
        "address": "1119 8th Ave S, Seattle, WA,",
        "wsapikey": key, "transit": 1, "bike": 1, "format": "json"}
paramstr = urllib.parse.urlencode(dict)
#print(paramstr)

base_url = "https://api.walkscore.com/"

score_request = base_url + "score?" + paramstr
#print(score_request)

## DATA FROM WEB AND MAKE DICT
result = urllib.request.urlopen(score_request)
read_data = result.read()
score_response_str = read_data.decode()
score_data = json.loads(score_response_str)
result.close()

#pprint.pprint(score_data)

##GEN FUNC
def get_score_data(lat, lon, address, wsapikey=key, transit=1, bike=1, format="json"):
        score_dict = {"lat": lat, "lon": lon, "address": address, "wsapikey": wsapikey,
                      "transit": transit, "bike": bike, "format": format}
        score_string = urllib.parse.urlencode(score_dict)
        base_url = "https://api.walkscore.com/"
        score_request = base_url + "score?" + score_string
        result = urllib.request.urlopen(score_request)
        read_data = result.read()
        score_response_str = read_data.decode()
        score_data = json.loads(score_response_str)
        result.close()
        return score_data
#TEST
pprint.pprint(get_score_data(47.662006, -122.309186, "4524 17th Ave, Seattle, WA", key))


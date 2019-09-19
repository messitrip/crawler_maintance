import requests
import pprint

if __name__ == '__main__':
    url = "http://strip.tripstore.kr/simple/?id=271614115"
    response = requests.get(url)
    import json
    result = json.loads(response.content.decode("utf-8"))
    pprint.pprint(result)

to_finds = [
    {"pcode":"EWP376191014KEM"}
]



if __name__ == '__main__':
    import requests
    import json
    import pprint
    for item in to_finds:
        filename = ""
        for key, value in item.items():
            url = "https://api.tripstore.kr/guest/list?"
            url+=key+"="+value
            filename+=key+"="+value
            print(url)
            response = requests.get(url)
            result = json.loads(response.content.decode("utf-8"))

            with open(f"{filename}.json","w") as f:
                json.dump(result,f,ensure_ascii=False,indent=3)
            pprint.pprint(result['list'][0])

            print("placeId")
            print(result['list'][0]['placeId'])
            print("agencyId")
            print(result['list'][0]['agencyId'])

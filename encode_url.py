import urllib.parse as parse
import urllib
if __name__ == '__main__':
    base_url ="http://strip.tripstore.kr/web/?url="
    url = "https://www.tourbell.co.kr/mobile/tour/package/2285/458787/?aid=1079&utm_source=trip_store&utm_medium=ts&utm_campaign=201909"
    result = parse.quote(url,safe="")
    print(base_url+result)
import progressbar
from urllib.request import urlretrieve
import requests

class ProgressBar():
    def __init__(self):
        self.pbar = None

    def __call__(self, block_num, block_size, total_size):
        if not self.pbar:
            self.pbar=progressbar.ProgressBar(maxval=total_size)
            self.pbar.start()

        downloaded = block_num * block_size
        if downloaded < total_size:
            self.pbar.update(downloaded)
        else:
            self.pbar.finish()

url = "http://tripstore.lottetour.com/static/agent_api_xml/tripstore.xml";


def download_file_by_request(url,dest):
    response = requests.get(url)
    with open(dest,"w") as f:
        f.write(response.content.decode("utf-8"))

def test_urllib(benchmark):
    dest = "test.txt"
    benchmark(urlretrieve,url,dest)

def test_request(benchmark):
    dest = "test1.txt"
    benchmark(download_file_by_request,url,dest)



if __name__ == '__main__':
    dest = "test.txt"
    try:
        urlretrieve(url,dest,ProgressBar())
    except Exception as e:
        print(e)
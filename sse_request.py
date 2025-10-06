import requests
def make_sse_request(url):
    response = requests.get(url, stream=True)
    for line in response.iter_lines():
        if line:
            print(line.decode('utf-8'))

tif __name__ == '__main__':
    url = 'https://api.jarvised.net/v1/'
    make_sse_request(url)
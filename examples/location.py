import requests


def get_location_info():
    url = 'https://freegeoip.net/json/'
    return requests.get(url).json()


if __name__ == '__main__':
    print(get_location_info())

pi = 1
hp = f"{pi:#0.2f}"
print(type(hp))
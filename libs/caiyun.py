import requests


class Weather:
    api_end = "https://api.caiyunapp.com/v2.6/"
    api_token = ""

    def __init__(self, api_token) -> None:
        self.api_token = api_token

    def get_weather(self, lat, lon):
        url = self.api_end + self.api_token + "/" + str(lon) + "," + str(lat) + "/realtime"
        r = requests.get(url)
        return r.json()


if __name__ == '__main__':
    w = Weather("TAkhjf8d1nlSlspN")
    print(w.get_weather(39.9042, 116.4074))
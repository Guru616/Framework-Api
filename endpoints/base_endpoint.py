import requests


class Endpoint:
    response = None
    response_json = None

    def check_response_is_200(self, url):
        self.response = requests.delete(url)
        assert self.response.status_code == 200



    def check_response_is_404(self, url):
        self.response = requests.get(url)
        assert self.response.status_code == 404
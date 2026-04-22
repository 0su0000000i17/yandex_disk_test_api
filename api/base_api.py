import requests
import json

class BaseAPI:
    def __init__(self, token):
        self.base_url = "https://cloud-api.yandex.net/v1/disk"
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"OAuth {token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })

    def _request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        
        print(f"\n{'='*80}")
        print(f"HTTP REQUEST: {method} {url}")
        
        if kwargs.get("params"):
            params_log = json.dumps(kwargs['params'], indent=4, ensure_ascii=False)
            print(f"Parameters:\n{params_log}")
            
        response = self.session.request(method, url, **kwargs)
        
        print(f"HTTP RESPONSE: Status {response.status_code}")
        
        try:
            if response.text:
                response_data = response.json()
                pretty_json = json.dumps(response_data, indent=4, ensure_ascii=False)
                print(f"Response Body:\n{pretty_json}")
        except Exception:
            if not response.text:
                print("Response Body: [Empty]")
            else:
                print(f"Response Body: {response.text}")
            
        print(f"{'='*80}")
        return response
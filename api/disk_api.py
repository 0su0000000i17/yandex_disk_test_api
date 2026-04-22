from .base_api import BaseAPI

class DiskAPI(BaseAPI):
    def get_disk_info(self):
        return self._request("GET", "/")

    def create_folder(self, path):
        return self._request("PUT", "/resources", params={"path": path})

    def upload_file_by_url(self, path, file_url):
        payload = {"path": path, "url": file_url}
        return self._request("POST", "/resources/upload", params=payload)

    def delete_resource(self, path, permanently="false"):
        params = {"path": path, "permanently": permanently}
        return self._request("DELETE", "/resources", params=params)

    def get_resource_info(self, path):
        return self._request("GET", "/resources", params={"path": path})
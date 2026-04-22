import pytest
import uuid

class TestYandexDisk:
    
    @pytest.fixture(autouse=True)
    def setup_method(self, api_client):
        self.test_path = f"test_{uuid.uuid4().hex}"

    def test_full_resource_lifecycle(self, api_client):
        print("\n[STEP 1] Creating folder (PUT)")
        res_create = api_client.create_folder(self.test_path)
        assert res_create.status_code == 201

        print("\n[STEP 2] Verifying resource info (GET)")
        res_info = api_client.get_resource_info(self.test_path)
        assert res_info.status_code == 200
        assert res_info.json()["name"] == self.test_path

        print("\n[STEP 3] Uploading file via URL (POST)")
        file_url = "https://upload.wikimedia.org/wikipedia/commons/6/61/Starling_%285503763150%29.jpg"
        res_upload = api_client.upload_file_by_url(f"{self.test_path}/file.png", file_url)
        assert res_upload.status_code == 202

        print("\n[STEP 4] Deleting resource (DELETE)")
        res_del = api_client.delete_resource(self.test_path)
        assert res_del.status_code == 204

        print("\n[STEP 5] Final check for 404 (GET)")
        res_final = api_client.get_resource_info(self.test_path)
        assert res_final.status_code == 404
import pytest
from api.disk_api import DiskAPI
from config import Config

@pytest.fixture(scope="session")
def api_client():
    return DiskAPI(Config.TOKEN)
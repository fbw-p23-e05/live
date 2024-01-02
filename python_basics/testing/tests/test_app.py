from app import get_username
import pytest


class TestApp:
    
    @pytest.mark.username
    def test_get_username_returns_username(self):
        username = 'rachelsmith'
        assert get_username(username) is not None
    
    @pytest.mark.username   
    def test_get_username_returns_none_for_wrong_username(self):
        username = 'genie1097'
        assert get_username(username) is None
    
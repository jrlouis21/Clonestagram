import pytest
from django.contrib.auth import get_user_model


class TestCustomUserModel:
    @pytest.mark.django_db
    @pytest.mark.parametrize(
        ("username", "password", "response"),
        [
            pytest.param("testuser", "test1234", None, id="successful-test"),
            pytest.param("", "", TypeError, id="missing-required-values"),
        ],
    )
    def test_user_create(self, username, password, response):
        User = get_user_model()

        user_params = {}
        if username:
            user_params["username"] = username
        if password:
            user_params["password"] = password

        try:
            user = User.objects.create_user(**user_params)

            assert user.username == username
            assert user.is_active == True
            assert user.is_staff == False
            assert user.is_superuser == False

        except Exception as exc:
            assert exc.__class__ == response

    @pytest.mark.django_db
    @pytest.mark.parametrize(
        ("username", "password", "response"),
        [
            pytest.param("testuser", "test1234", None, id="successful-test"),
            pytest.param("", "", TypeError, id="missing-required-values"),
        ],
    )
    def test_superuser_create(self, username, password, response):
        User = get_user_model()

        superuser_params = {}
        if username:
            superuser_params["username"] = username
        if password:
            superuser_params["password"] = password

        try:
            superuser = User.objects.create_superuser(**superuser_params)

            assert superuser.username == username
            assert superuser.is_active == True
            assert superuser.is_staff == True
            assert superuser.is_superuser == True

        except Exception as exc:
            assert exc.__class__ == response

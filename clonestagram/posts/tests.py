import pytest
from .models import Post


class TestPostModel:
    def test_post_create(self):
        post = Post.objects.create()
        pass

    def test_post_update(self):
        pass

    def test_post_delete(self):
        pass

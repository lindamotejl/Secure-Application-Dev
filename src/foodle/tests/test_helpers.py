import pytest

from django.contrib.auth.models import User


@pytest.mark.django_db
def test_user_create():
  User.objects.create_user('rick', 'rsanchez@dumbasarock.com', 'Morty_stinks!')
  assert User.objects.count() == 1
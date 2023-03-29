from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

import pytest

@pytest.fixture
def client():
    return APIClient()

# HeroViewSet Tests


@pytest.mark.django_db
def test_heroes_list_get(client):
    url = reverse('heroes-list')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_heroes_create_post(client):
    url = reverse('heroes-list')
    response = client.post(url, data={})
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_heroes_retrieve_get(client):
    url = reverse('heroes-detail', kwargs={'pk': None})
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_heroes_update_put(client):
    url = reverse('heroes-detail', kwargs={'pk': None})
    response = client.put(url, data={})
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_heroes_partial_update_patch(client):
    url = reverse('heroes-detail', kwargs={'pk': None})
    response = client.patch(url, data={})
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_heroes_destroy_delete(client):
    url = reverse('heroes-detail', kwargs={'pk': None})
    response = client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT

# TeamViewSet Tests


@pytest.mark.django_db
def test_team_list_get(client):
    url = reverse('team-list')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_team_create_post(client):
    url = reverse('team-list')
    response = client.post(url, data={})
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_team_retrieve_get(client):
    url = reverse('team-detail', kwargs={'pk': None})
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_team_update_put(client):
    url = reverse('team-detail', kwargs={'pk': None})
    response = client.put(url, data={})
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_team_partial_update_patch(client):
    url = reverse('team-detail', kwargs={'pk': None})
    response = client.patch(url, data={})
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_team_destroy_delete(client):
    url = reverse('team-detail', kwargs={'pk': None})
    response = client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT

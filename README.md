### Sample project to test the [drf-test-generator](https://pypi.org/project/drf-test-generator/) package.

Runs in Docker container.
###### To install locally:
- docker-compose up --build -d
- docker compose exec web ./manage.py migrate
- docker compose exec web ./manage.py createsuperuser (for any db changes)


###### Package commands (since Django Management Commands):
- docker compose run web ./manage.py generate_viewset_tests -r heroes_app.urls.router --output-file testing.py --variant pytest
- add fixture:

from rest_framework.test import APIClient

@pytest.fixture
def client():
    return APIClient()


###### Most important info about the package:
- works with ViewSets only
- doesnt create own fixtures
- strange behaviour with custom / overriden methods
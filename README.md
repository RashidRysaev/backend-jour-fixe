### Sample project to test the [drf-test-generator](https://pypi.org/project/drf-test-generator/) package.

Runs in Docker container.
###### To install locally:
- docker-compose up --build -d
- be sure all migrations are there via
docker-compose exec web ./manage.py showmigrations

###### Most important info about the package:
- works with ViewSets only
- doesnt create own fixtures
- strange behaviour with custom / overriden methods

###### Package commands (since Django Management Commands):
- docker-compose exec web ./manage.py generate_viewset_tests -r heroes_app.urls.router --output-file testing.py --variant pytest
- docker-compose exec web pytest testing.py
- add fixture:

```
from rest_framework.test import APIClient

@pytest.fixture
def client():
    return APIClient()


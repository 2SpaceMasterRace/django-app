# django-app

[![Build Status](https://api.travis-ci.com/2SpaceMasterRace/django-app.svg?branch=main)](https://app.travis-ci.com/github/2SpaceMasterRace/django-app)
[![Coverage Status](https://coveralls.io/repos/github/2SpaceMasterRace/django-app/badge.svg?branch=main)](https://coveralls.io/github/2SpaceMasterRace/django-app?branch=main)

Django polls application with Travis CI checks and AWS Elastic Beanstalk deployment.

## Assignment links

- GitHub: https://github.com/2SpaceMasterRace/django-app
- Travis dashboard: https://app.travis-ci.com/github/2SpaceMasterRace/django-app
- Deployed app: http://django-app-ci--env.us-west-2.elasticbeanstalk.com/polls/
- Coverage: https://coveralls.io/github/2SpaceMasterRace/django-app

## Run checks locally

Install Python 3.14 and [uv](https://docs.astral.sh/uv/), then run from the repository root:

```sh
uv sync --frozen
uv run black --check .
uv run flake8 .
uv run python djangotutorial/manage.py check
uv run coverage run djangotutorial/manage.py test polls
uv run coverage report --show-missing
```

The initial suite in `djangotutorial/polls/tests.py` checks that the polls index
loads with an empty database. Django creates a separate test database.

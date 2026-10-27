# django-app

[![Build Status](https://app.travis-ci.com/2SpaceMasterRace/django-app.svg?branch=main)](https://app.travis-ci.com/github/2SpaceMasterRace/django-app)
[![Coverage Status](https://coveralls.io/repos/github/2SpaceMasterRace/django-app/badge.svg?branch=main)](https://coveralls.io/github/2SpaceMasterRace/django-app?branch=main)

Django polls application with Travis CI checks and AWS Elastic Beanstalk deployment.

## Assignment links

- GitHub: https://github.com/2SpaceMasterRace/django-app
- Travis dashboard: https://app.travis-ci.com/github/2SpaceMasterRace/django-app
- Deployed app: http://django-app--env.us-west-2.elasticbeanstalk.com/polls/
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

## Activate the hosted integrations

The configuration files alone do not activate Travis CI or Coveralls.

1. Sign in to [Travis CI](https://app.travis-ci.com/) with GitHub and authorize
   the Travis CI GitHub App for `2SpaceMasterRace/django-app`. Activate the
   repository and enable builds for both pushes and pull requests in its settings.
   Confirm your account has build credits available.
2. Sign in to [Coveralls](https://coveralls.io/) with GitHub and enable this
   repository. The Python `coveralls` client detects Travis automatically. If
   Coveralls requests a repository token, add `COVERALLS_REPO_TOKEN` in Travis
   repository settings with its value hidden from logs.
3. In Travis repository settings, add hidden `AWS_ACCESS_KEY_ID` and
   `AWS_SECRET_ACCESS_KEY` variables for an IAM deployment user authorized to
   upload versions to `elasticbeanstalk-us-west-2-793452510245` and update the
   existing `django-app` application and `django-app-env` environment in
   `us-west-2`. Keep credentials out of Git and do not expose them to fork PRs.
4. Push this configuration and open a pull request. Verify that Travis starts
   automatically and reports its result on the PR. In GitHub branch protection
   for `main`, require `Travis CI - Pull Request` to pass before merging.
5. Merge a passing PR to `main`. Travis runs Black, Flake8, Django checks, tests
   under coverage.py, and Coveralls reporting. After those succeed, its
   Elastic Beanstalk provider deploys the application and waits for completion.
   PR builds do not deploy. Verify the build log and deployed app before submitting
   the assignment links above.

Deployment uses the existing EB environment, its configured Django secret key,
and the migration/static-file commands in `.ebextensions/django.config`.
See the [Travis EB deployment documentation](https://docs.travis-ci.com/user/deployment-v2/providers/elasticbeanstalk/)
for provider settings.

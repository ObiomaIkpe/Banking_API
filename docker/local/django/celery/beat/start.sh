#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail

python manage.py migrate django_celery_beat

rm -f './celerybeat.pid'

exec watchfiles --filter python celery.__main__.main --args '-A nextbank.celery_app beat -l INFO'
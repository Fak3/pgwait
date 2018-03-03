#!/usr/bin/env python3
import os
import sys
import time
import psycopg2


def main():
    sys.path.insert(0, os.getcwd())

    if len(sys.argv) == 1 and 'DJANGO_SETTINGS_MODULE' not in os.environ:
        print('Please provide settings path or set DJANGO_SETTINGS_MODULE env variable.')
        sys.exit(1)
    elif len(sys.argv) == 2:
        os.environ['DJANGO_SETTINGS_MODULE'] = sys.argv[1]
    elif len(sys.argv) > 2:
        print('Too many arguments!')
        sys.exit(1)

    from django.conf import settings

    DB = settings.DATABASES['default']
    url = 'postgres://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}'.format(**DB)
    print(f'pgwait: waiting for {url}')

    attempt = 1
    while True:
        args = "user='%(USER)s' password='%(PASSWORD)s' dbname='%(NAME)s' host='%(HOST)s' port='%(PORT)s'"
        try:
            psycopg2.connect(args % DB)
        except Exception as e:
            print('%s Attempt %d failed, retrying in 2 seconds' % (e, attempt))
            attempt += 1
            time.sleep(2)
        else:
            print(f'pgwait: successfully connected to {url}')
            break


if __name__ == '__main__':
    main()

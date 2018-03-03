This command-line tool reads django settings, then tries to connect to configured postgresql server until connection succeeds. It is useful on service startup, when you want to launch migrations right after postgres database gets ready.

## Usage
To wait before migrations:

```bash
pgwait && ./manage.py migrate
```

### Specifying settings path

You can either set `DJANGO_SETTINGS_MODULE` environment variable, or specify settings module path in the first command-line argument.

```bash
pgwait path.to.settings
```

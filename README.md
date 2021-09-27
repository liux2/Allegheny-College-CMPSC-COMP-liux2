# Allegheny College CMPSC COMP-liux2

The COMP project for Allegheny College Computer Science department class of 2020.
This project implemented a system to recommend music tracks based on user-submitted
texts. The text can be the form of diary or video transcribes, which could contain
users’ current emotions. The recommended music can be got by matching the text with
the song lyrics. By using the system, people can fill their emotional needs whenever
they want. The website of the system is [music.xingbangliu.io](http://music.xingbangliu.io).

## Getting Started

### Prerequisite

#### System and Python

This application was built on Linux system, the Python version was 3.7.6.
[Pyenv](https://github.com/pyenv/pyenv) is recommended for Python version management.
Here is a good [tutorial](https://realpython.com/intro-to-pyenv/) on how to install
Pyenv on your system.

[Pipenv](https://github.com/pypa/pipenv) was used to manage the Python dependencies,
here is a good [tutorial](https://realpython.com/pipenv-guide/) on how to install
and use Pipenv.

#### Dependency Installation

To install the dependencies, use `pipenv install` to install from Pipfile. If you
want to install by importing the `requirement.txt`, use
`pipenv install -r path/to/requirements. txt` to install.

The complete dependency list is as follows, please also refer to [Pipfile](music_sug/Pipfile)
and [requirement.txt](music_sug/requirement.txt).

```
lyricsgenius = "==1.8.2"
spacy = "==2.2.4"
networkx = "==2.4"
graphviz = "==0.13.2"
pytextrank = "==2.0.1"
numpy = "==1.18.2"
pip = "*"
six = "==1.14.0"
py-stringmatching = "==0.4.1"
spacy-langdetect = "==0.1.2"
attrs = "==19.3.0"
bcrypt = "==3.1.7"
beautifulsoup4 = "==4.6.0"
blis = "==0.4.1"
catalogue = "==1.0.0"
certifi = "==2019.11.28"
cffi = "==1.14.0"
chardet = "==3.0.4"
click = "==7.1.1"
coverage = "==5.0.4"
cymem = "==2.0.3"
decorator = "==4.4.2"
idna = "==2.9"
importlib-metadata = "==1.5.0"
itsdangerous = "==1.1.0"
langdetect = "==1.0.7"
more-itertools = "==8.2.0"
murmurhash = "==1.0.2"
plac = "==1.1.3"
pluggy = "==0.13.1"
preshed = "==3.0.2"
py = "==1.8.1"
pycparser = "==2.20"
pyparsing = "==2.4.6"
pytest = "==5.4.1"
requests = "==2.23.0"
srsly = "==1.0.2"
thinc = "==7.4.0"
tqdm = "==4.43.0"
urllib3 = "==1.25.8"
wasabi = "==0.6.0"
wcwidth = "==0.1.8"
zipp = "==3.1.0"
Flask = "==1.1.1"
Flask-WTF = "==0.14.3"
Flask-SQLAlchemy = "==2.4.1"
Flask-Bcrypt = "==0.7.1"
Flask-Login = "==0.5.0"
Jinja2 = "==3.0.0a1"
MarkupSafe = "==1.1.1"
SQLAlchemy = "==1.3.15"
Werkzeug = "==1.0.0"
WTForms = "==2.2.1"
gunicorn = "*"
pytest-cov = "*"
```

### Running the Tests

Use `pipenv run test` to test the application. The test files are under `music_sug/test/`
directory. The bash script is `music_sug/scripts/test.sh`.

### Deployment

To deploy the project, first install the dependencies, then use `pipenv run setup`
to install the language model, generate the database, and commit the lyrics model.

The options for the web server could be [Nginx](https://nginx.org/en/docs/) and
[gunicorn](https://gunicorn.org/).

#### Nginx

Install nginx by using `apt install nginx`.
A simple Nginx proxy configuration under `/etc/nginx/sites-enabled` could be:

```
server {
        listen 80;
        server_name Your_IP_adress;
        location / {
                proxy_pass http://localhost:8000;
                include /etc/nginx/proxy_params;
                proxy_redirect off;
        }
}
```

After setting up the configuration file, use `systemctl restart nginx` to restart
the service.

#### Gunicorn

Gunicorn is responsible for handling the Python code, it should be installed with
Pipfile already.
The app can be run with `gunicorn -w number_of_workers name_of_main_program:app`.
The number of worker are defined as (2 * number_of_CPU_cores) + 1. The name of
main program in this project is app, so use `app:app` in the command.

#### Supervisor

Supervisor was used to monitor and manage the processes. To install supervisor,
use `apt install supervisor`.

Under `/etc/supervisor/`, create a configuration file, a simple sample can be:

```
[program:name_of_project]
directory=path/to/name_of_project
command=path/to/project/virtual/environment/bin/gunicorn -w number_of_workers name_of_main_program:app
user=system_user
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
stderr_logfile=/var/log/music_sug/music_sug.err.log
stdout_logfile=/var/log/music_sug/music_sug.out.log
```

Under `/var/log/` create a directory for your project logs. In the example above,
the files `music_sug.err.log` and `music_sug.out.log` should be created.

Reload the configuration by using `supervisorctl reload`, now the application should
be up and running.

# License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE)
file for details.

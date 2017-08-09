# Golos Data

## Features golosdata

* The default is noda golos
* Automatic create database in mongodb GolosDataNew

# Manually setup dev environment (Linux) #

### Installation guide for Ubuntu 16.04

##### 1. Installation package dependencies

##### Ubuntu 16.04

* sudo apt-get install python3-pip memcached libmemcached-dev libpq-dev postgresql-client-9.5

##### 2. MongoDB Installation ([Official documentation](https://docs.mongodb.com/v3.2/tutorial/install-mongodb-on-ubuntu/))

* sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
* echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
* sudo apt-get update
* sudo apt-get install -y mongodb-org

<pre>Useful commands:
        # Ubuntu 16.04 and higher
        Stop/Start/Restart MongoDB service:
        bash:/# systemctl stop/start/restart mongod

        Check status of MongoDB service:
        bash:/# systemctl status mongod
</pre>

##### 3. Configuring virtual environment for python 3.5.x
If you use _virtualenv_:
* sudo pip3 install virtualenv
* virtualenv -p \`which python3.5\` ~/env_steem

If you use _mkvirtualenv_:
* sudo pip3 install virtualenvwrapper
* mkdir ~/virtualenvs
* echo "export VIRTUALENVWRAPPER_PYTHON=\`which python3.5\`" >> ~/.bashrc
* echo "export WORKON_HOME=~/virtualenvs" >> ~/.bashrc
* echo "export PIP_VIRTUALENV_BASE=~/virtualenvs" >> ~/.bashrc
* echo "source \`which virtualenvwrapper.sh\`" >> ~/.bashrc
* mkvirtualenv steepshot -p \`which python3.5\`

##### 4. Setup project
**Activate virtual environment:**

If you use _virtualenv_:
* source ~/env_steem/bin/activate

If you use _mkvirtualenv_:
* workon steepshot

Postactivate:
* export DJANGO_SETTINGS_MODULE=golosdata.prod_settings
* export DJANGO_DEBUG=True
* export DJANGO_LOCAL=True
* alias python=python3.5

_If you are developing in PyCharm you should also export this variable:_
* _export GEVENT_SUPPORT=True_

**Install dependencies: (_Virtual environment has been activated_)**
* python --version (should be Python 3.5)
* pip install -r requirements.txt



##### 5. Run project

```bash
python manage.py migrate
python manage.py runserver
```

# PV SImulator
#### This is a Python Django projects that at interval simulates power usages from the home
![In a single picture](https://raw.githubusercontent.com/Austyns/pvSimulator/master/screen1.png)

## Depeendencies
- Python 3
- Django
- Django rest framework
- Celery 
- RabbitMQ

## Setup
- First intall VirtualEnv to conatinerize app `sudo apt-get install virtualenv`
- Create a python3 virtual env to run the app `virtualenv env --python=python3`
- Active the virtulenv `source env/bin/activate`
- Clone project from git `git clone https://github.com/Austyns/pvSimulator.git`
- cd into the project root and install project dependencies `pip install -r requirements.txt`
- Install rabitMQ if not setup yet to serve as broker for celery
	- ```sudo apt-get install -y erlang```
	- ```sudo apt-get install rabbitmq-server```

- Enable RabbitMQ
	- `sudo systemctl enable rabbitmq-server`
	- `sudo systemctl start rabbitmq-server`

- Run migration to generate models
	`python manage.py migrate`

- Serve the project locally
	`python manage.my runserver`

- Start Celery for async task queue
	From Project root run 
	`celery -A pvSimulator worker -l info -B`

## Previewing
- Once the app is started, go to the browser
http://localhost:8000 to see a realtime chat that plots meter readings againt time.

- You can also preview the task queue by starting the Celery monitoring app ( Flower)
	- `celery -A pvSimulator flower -l info`
	- Then preview from http://localhost:5555

- Outputs are also available from project root outputs/ folder



Thank you 

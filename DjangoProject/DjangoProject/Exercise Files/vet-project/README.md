# Vet Project

Django project for a Vet clinic
https://www.linkedin.com/learning/learning-django-2/

## Dependencies
python 3.8.2

django 3.0.3

venv

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages

```powershell
# https://docs.djangoproject.com/en/4.0/howto/windows/
# This will create a folder called ‘vet-project’ if it does not 
# already exist and set up the virtual environment. 
py -m venv vet-project

# Install Django into the virtual env, while venv is running:
py -m pip install Django

# colored terminal output
py -m pip install colorama

# activate the virtual env
. .\Activate.ps1

```

http://127.0.0.1:8000/

## Usage

```python
# run the webserver
cd 'C:\Users\awilkinson\python\DjangoProject\DjangoProject\Exercise Files\vet-project\Scripts\wisdompets'
python manage.py runserver

# start an app called adoptions
python manage.py startapp adoptions

# to rotate the secret key 
pip install django-rotate-secret-key

# to add environment vars 
pip install django-environ

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
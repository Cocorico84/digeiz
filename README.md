![shield](https://img.shields.io/github/last-commit/Cocorico84/softdesk)
![shield](https://img.shields.io/github/languages/code-size/cocorico84/softdesk) 
![shield](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![shield](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![shield](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)


# Description

The application has 3 endpoints with all CRUD actions :
* /accounts
* /malls
* /units


# Prerequisites

Python 3

# Installation

To clone the repository, you can download the zip or clone either HTTPS or SSH. And when you are in the repository you can activate your virtual environement.

On Linux or Mac
```shell
$ pip install virtualenv
$ virtualenv venv --python=python3
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```

On Windows
```bat
c:\Python38\python -m venv c:\path\to\myenv
C:\\{venv}\\Scripts\\activate.bat
pip install -r requirements.txt
```

# Quickstart

To launch flask :
```console
python app.py
```
When you launch this command, it will start the website on http://127.0.0.1:5000.

If you want to populate the database :

```console
python build_db.py
```
To launch tests :
```console
pytest
```
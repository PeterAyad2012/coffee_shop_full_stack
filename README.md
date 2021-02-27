# Coffee Shop Full Stack

## Full Stack Nano - IAM Final Project

Coffee Shop Full Stack is a cafe application from Udacity for students to order drinks, socialize, and study hard.

The application capabilities:

1) Display graphics representing the ratios of ingredients in each drink.
2) Allow public users to view drink names and graphics.
3) Allow the shop baristas to see the recipe information.
4) Allow the shop managers to create new drinks and edit existing drinks.

## Getting Started

### Installing Dependencies

#### Frontend Dependencies

##### Installing Node and NPM

This project depends on Nodejs and Node Package Manager (NPM). download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).

##### Installing Ionic Cli

The Ionic Command Line Interface is required to serve and build the frontend. 

first, run the CLI as administrator and use the following command to download and install ionic.

```bash
npm install -g @ionic/cli
```

##### Installing project dependencies

for windows users, run the CLI as an administrator and install Visual Studio Build Tools before installing project dependencies using this command:

```bash
npm install --global --production windows-build-tools --vs2017
```

This project uses NPM to manage software dependencies. After cloning, open terminal , change directory to the `frontend` directory and run:

```bash
npm install
```

#### Backend Dependencies

##### Python 3.7.9

Follow instructions to install the latest version of python 3.7 for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

##### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

###### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

### Running server in development mode

##### Run Frontend

Ionic ships with a useful development server which detects changes and transpiles as you work. The application is then accessible through the browser on a localhost port. To run the development server, cd into the `frontend` directory and run:

```bash
ionic serve
```

#### Run Backend 

After installing backend dependencies, To run backend in development mode change directory to the `./src` directory and run:

```bash
export FLASK_APP=api.py
flask run --reload
```
>_tip_: **Windows users replace export keyword with set**



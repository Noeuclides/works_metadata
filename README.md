# Musical Works Metadata

Web application using django framework.

Features:
-   Show a list of the last comics
    
-   Show a detail of the selected comic

## Prerequisites
This app was set with python 3.5, so you have to make sure that you have python3 installed in your machine.

It's better to set a virtual environment. To do that first install virtualenv:

    $ pip install virtualenv
    
 then we are going to create the virtualenv to run the app, please ru the following commands in your terminal:
 
    $ mkdir myvirtualEnvs && cd myvirtualEnvs
    $ virtualenv djangoEnv -p $(which python3)
    $ cd
    

## Getting started

First clone this repository:

    $ git clone https://github.com/Noeuclides/works_metadata.git

then go to the repo's directory:

    $ cd works_metadata
    $ source ../myvirtualEnvs/djangoEnv/bin/activate    

There you can install all the prerequisites to run the app in your computer:

    $ pip install -r requirements.txt


## Run the App

    $ python manage.py runserver






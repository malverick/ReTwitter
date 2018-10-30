To run this app locally

1. Install Python2.7 : https://www.python.org/downloads/
2. Install pip for python
    $sudo apt-get update
    $sudo apt-get install python-pip
3. Install Virtual Environment
    $sudo pip install virtualenv
4. Extract the Zip Folder
    $cd ReTwitter
5. Create Virtual Environment
    $virtualenv venv
6. Activate the Virtual Environment
    $source venv/bin/activate
    $pip install -r requirements.txt
    $python manage.py makemigrations
    $python manage.py migrate
    $python manage.py runserver
Server will start -  127.0.0.1:8000

Test this API on POSTMAN

APP NAME: ACCOUNTS

1. Signup

Url: http://127.0.0.1:8000/accounts/signup/
Method: POST
Request Body Type: RAW, JSON(application/json)
Request Body: {"username":"<username>", "password":"<password>"}
Description: Accepts 2 parameters, username and password. 
If username is unique, registers him in database and logs in the user. Returns JsonResponse, "Note":"User successfully logged in".
If username is not unique, Returns JsonResponse, "Note":"User already exist".

2. Login

Url: http://127.0.0.1:8000/accounts/login/
Method: POST
Request Body Type: RAW, JSON(application/json)
Request Body: {"username":"<username>", "password":"<password>"}
Description: Accepts 2 parameters, username and password. Checks whether the user exists or not.
If the user exists, authenticates the user, do the log in and returns JsonResponse, "Note":"User successfully logged in".
If the user does not exist or password is incorrect, returns JsonResponse, "Error":"Invalid username or password".

3. Logout

Url: http://127.0.0.1:8000/accounts/logout/
Method: GET
Description: Logs out the user and returns JsonResponse, "Note":"Successfully logged out" 

APP NAME: EXTENDED

1. Follow

Url: http://127.0.0.1:8000/extended/follow/
Method: POST
Request Body Type: RAW, JSON(application/json)
Request Body: {"username":"<username>", "password":"<password>"}


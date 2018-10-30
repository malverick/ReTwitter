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
Request Body: {"follow":"<username>"}
Description: Accepts 1 parameter, follow which contains the username of the person to be followed.
Returns JsonResponse mentioning the username of logged in user and username of person whom he just started following.

2. Unfollow

Url: http://127.0.0.1:8000/extended/unfollow/
Method: POST
Request Body Type: RAW, JSON(application/json)
Request Body: {"unfollow":"<username>"}
Description: Accepts 1 parameter, unfollow which contains the username of the person to be unfollowed.
Returns JsonResponse mentioning the username of logged in user and username of person whom he just stopped following.

3. GetUsers

Url: http://127.0.0.1:8000/extended/getUsers/
Method: GET
Description: Return a JsonResponse displaying the list of all the users in the database along with their user ID.

4. CreateTweet

Url: http://127.0.0.1:8000/extended/create/
Method: POST
Request Body Type: RAW, JSON(application/json)
Request Body: {"tweet":"<tweet content>"}
Description: Accepts 1 parameter, tweet which contains the content of the tweet. Store the content of tweet in the database corresponding to the logged in user. Return the JsonResponse mentioning the TweetId of the tweet which is just created.

5. DeleteTweet

Url: http://127.0.0.1:8000/extended/delete/
Method: POST
Request Body Type: RAW, JSON(application/json)
Request Body: {"tweetID":"<tweet id"}
Description: Accepts 1 parameter, tweetID representing the tweet which is to be deleted. Also, checks the basic corner cases like whether tweet exits or not, user is authorised to delete tweet, etc.

6. ReadTweet

Url: http://127.0.0.1:8000/extended/read/
Method: POST
Request Body Type: RAW, JSON(application/json)
Request Body: {"username":"<username>", "tweetID":"<tweet id>"}
Description: Accepts 2 parameters, username of the person whose tweet is to be read and tweetID representing the tweet of the corresponding username. If the tweetID field is left empty, then display all the tweets created by the corresponding username.
Return JsonResponse mentioning the required tweet(s).







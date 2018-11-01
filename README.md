Hello folks !

Recently I started learning Django and tried to implement this project side by side. In this project, I have implemented user login/signup using django rest framework. Then I have implemented some APIs with functionality similar to twitter features like, follow/unfollow a user, create, read and delete a tweet.

I have deployed this project on Heroku which was also a new experience for me. You can test this project on POSTMAN. Follow the instructions below. Hope you like it.

Heroku Link - https://retwitter-django.herokuapp.com (You will get a 404 error page on opeining this because I have not implemented any UI. Kindly follow below instructions for the correct URL of each API)

Test this API on POSTMAN because you need to provide the authorization token while accessing the API which is not possible on browser.

Following is the list of APIs implemented.

1. Signup

Url: https://retwitter-django.herokuapp.com/accounts/signup/

Method: POST

Request Body: "username":"`username`", "password":"`password`"

Description: Accepts 2 parameters, username and password. 
Checks for the uniqueness of the user, registers him in database and logs in the user. Returns the token key generated specific to this user. You have to provide this token key to access other APIs. This will make sure that only logged in user is able to make changes to database corresponding to his account.

2. Login

Url: https://retwitter-django.herokuapp.com/accounts/login/

Method: POST

Request Body: "username":"`username`", "password":"`password`"

Description: Accepts 2 parameters, username and password. Checks whether the user exists or not.
If the user exists, authenticates the user, generates the token and returns the token key generated specific to this user. You have to provide this token key to access other APIs. This will make sure that only logged in user is able to make changes to database corresponding to his account.

3. Logout

Url: https://retwitter-django.herokuapp.com/accounts/logout/

Method: POST

Prerequisites: Make sure under Authorization “No Auth” is selected.

Under “Headers” add the Header key: Content-Type. Make the Header value: application/json

Now, under “Headers” underneath “Content-Type” add the Header key: Authorization and add the Header value: “Token <token key>” (without the quotes).

Description: Deletes the token key generated for this user. A new token key will be generated when the same user will login again.


4. Follow

Url: https://retwitter-django.herokuapp.com/extended/follow/

Method: POST

Request Body: "follow":"`username`"

Prerequisites: Make sure under Authorization “No Auth” is selected.

Under “Headers” add the Header key: Content-Type. Make the Header value: application/json

Now, under “Headers” underneath “Content-Type” add the Header key: Authorization and add the Header value: “Token <token key>” (without the quotes).

Description: Accepts 1 parameter, follow which contains the username of the person to be followed. Follows the user with the username provided in the request body. A user cannot follow himself.

2. Unfollow

Url: https://retwitter-django.herokuapp.com/extended/unfollow/

Method: POST

Request Body: "unfollow":"`username`"

Prerequisites: Make sure under Authorization “No Auth” is selected.

Under “Headers” add the Header key: Content-Type. Make the Header value: application/json

Now, under “Headers” underneath “Content-Type” add the Header key: Authorization and add the Header value: “Token <token key>” (without the quotes).

Description: Accepts 1 parameter, unfollow which contains the username of the person to be unfollowed. Unfollows the user with the username provided.

3. GetUsers

Url: https://retwitter-django.herokuapp.com/extended/getUsers/

Method: GET

Prerequisites: Make sure under Authorization “No Auth” is selected.

Under “Headers” add the Header key: Content-Type. Make the Header value: application/json

Now, under “Headers” underneath “Content-Type” add the Header key: Authorization and add the Header value: “Token <token key>” (without the quotes).

Description: Displays the list of all the registered users in JSON format.

4. CreateTweet

Url: https://retwitter-django.herokuapp.com/extended/create/

Method: POST

Request Body: "tweet":"`content of the tweet`"

Prerequisites: Make sure under Authorization “No Auth” is selected.

Under “Headers” add the Header key: Content-Type. Make the Header value: application/json

Now, under “Headers” underneath “Content-Type” add the Header key: Authorization and add the Header value: “Token <token key>” (without the quotes).

Description: Accepts 1 parameter, tweet which contains the content of the tweet. Store the content of tweet in the database corresponding to the logged in user. Return the tweetID of the tweet just created.

5. DeleteTweet

Url: https://retwitter-django.herokuapp.com/extended/delete/

Method: POST

Request Body: {"tweetID":"`tweet id`"}

Prerequisites: Make sure under Authorization “No Auth” is selected.

Under “Headers” add the Header key: Content-Type. Make the Header value: application/json

Now, under “Headers” underneath “Content-Type” add the Header key: Authorization and add the Header value: “Token <token key>” (without the quotes).

Description: Accepts 1 parameter, tweetID representing the tweet which is to be deleted. Also, checks the basic corner cases like whether tweet exits or not, user is authorised to delete tweet, etc.

6. ReadTweet

Url: https://retwitter-django.herokuapp.com/extended/read/

Method: POST

Request Body: "username":"`username`", "tweetID":"`tweet id`"

Prerequisites: Make sure under Authorization “No Auth” is selected.

Under “Headers” add the Header key: Content-Type. Make the Header value: application/json

Now, under “Headers” underneath “Content-Type” add the Header key: Authorization and add the Header value: “Token <token key>” (without the quotes).

Description: Accepts 2 parameters, username of the person whose tweet is to be read and tweetID representing the tweet of the corresponding username. If username is not provided or field is left empty then by default it assumes the logged in user. If the tweetID is not provided or field is left empty, then by default it displays all the tweets created by the corresponding username.

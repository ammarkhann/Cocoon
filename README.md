# Project Usage

---

To run the project on your machine, you can follow the steps given below:

* Create a virtual environment and activate it

* Clone the project

* Navigate into the src folder

* Run makemigrations using python manage.py makemigrations

* Run migrate using python manage.py migrate

* Create superuser using python manage.py createsuperuser

* Run the project using python manage.py runserver
---

# NEWS API BASE URL

All endpoints generate from the base url given below:

* `url: /api/news/`

---

# AUTHENTICATION 

 JWT Authentication is required to access authenticated endpoints.
 
---

# AUTHENTICATION ENDPOINTS

* Obtain Access and Refresh Token:

       
            URL: /api/token/
            METHOD: POST
            Request Body:{
                "username": <your_username>,
                "password": <your_password>
            }
            Example Response:{
                "refresh": <str>,
                "access": <str>
            }
          
* Refresh Token:

       
            URL: /api/token/refresh/
            METHOD: POST
            Request Body:{
                "refresh": <your_refresh_token>
            }
            Example Response:{
                "access": <str>
            }
           
# AUTHENTICATION HEADER
   As JWT authentication is required to access authenticated endpoints. You should provide 
   authentication header in the following format in your requests:
   ### Authorization: JWT <your_access_token_here>
   


# Supported API Endpoints

- List All Articles:

    *  ```
        URL: news/
        METHOD: GET
        AUTHENTICATED : False
        ```

- Bookmark Article:
    *  ```
        URL: /article/bookmark/add/
        AUTHENTICATED: True
        METHOD: POST

        ```
 
 - Remove Bookmarked Article:
    *  ```
        URL: article/bookmark/remove/
        AUTHENTICATED: True
        METHOD: POST

       ```

---

# ERRORS AND MESSAGES

| RESPONSE   | STATUS CODE | Message |
| ------------- | ------------- | ------------- |
| SUCCESS  | HTTP_200_OK   | Request Processed Successfully  |
| CREATED  | HTTP_201_CREATED  | Object Created Successfully  |
| BAD REQUEST | HTTP_400_BAD_REQUEST | Request was in an invalid format. Check that your params have been properly encoded in the POST body and that your content is UTF8 encoded |
| UNAUTHORIZED | HTTP_401_UNAUTHORIZED | Request made was unauthenticated.Make sure to use your authentication credentials to request the resource |
| NOT FOUND | HTTP_404_NOT_FOUND | Looked up resource could not be found |



If you have any questions or need admin access, kindly email me at the following email address:
ammar88ammar@gmail.com
  

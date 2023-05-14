
# EventApp

This website lets users create events such as exhibition, festival celebration, etc. User can view, like other events.


## API Reference

#### User Registration

```http
  POST /user-register/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `first_name` | `string` | **Required** |
| `last_name` | `string` | **Required** |
| `email` | `email` | **Required** |
| `password` | `string` | **Required** |
| `confirm_password` | `string` | **Required** |

#### User Login

```http
  POST /token/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `email` | `email` | **Required** |
| `password` | `string` | **Required** |

#### Get list of all events

```http
  GET /all-events/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `access_token` | `string` | **Required** User access_token |

#### Get list of all events created by logged in user

```http
  GET /user-events/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `access_token` | `string` | **Required** User access_token |

#### Create an event

```http
  POST /create-event/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `access_token` | `string` | **Required** User access_token |
| `name` | `string` | **Required** Event name |
| `description` | `string` | **Required** Event description |
| `date` | `date` | **Required** Event date |
| `time` | `time` | **Required** Event time |
| `venue` | `string` | **Required** Event venue |
| `image` | `file` |  Event image |

#### Like-Unlike an event

```http
  POST /all-events/${event_id}/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `access_token` | `string` | **Required** User access_token |

#### Delete an event

```http
  DELETE /user-events/${event_id}/delete/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `access_token` | `string` | **Required** User access_token |

#### Update an event

```http
  PUT /edit-event/${event_id}/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `access_token` | `string` | **Required** User access_token |
| `name` | `string` | **Required** Event name |
| `description` | `string` | **Required** Event description |
| `date` | `date` | **Required** Event date |
| `time` | `time` | **Required** Event time |
| `venue` | `string` | **Required** Event venue |
| `image` | `file` |  Event image |


## Deployment

#### To deploy this project install dependancies

```bash
  pip install -r requirements.txt
```
Configure Postgres DB and update environment variables in .env file as per .env-sample file.

#### Migrate the changes in database tables

```bash
  py manage.py makemigrations
```
```bash
  py manage.py migrate
```

#### Run server

```bash
  py manage.py runserver
```

#### To use frontend functionality
Use ModHeader chrom extension and add Request header

    Name: Authorization
    Value: Bearer Token



## Documentation

This project uses Django, Django Rest Framework, Javascript, AJAX.

Django Rest Framework is used for backend functionality. Its API endpoints serves interaction with the data stored in Postgres Database.

Django is used to render HTML pages with Bootstrap and CSS for styling, overall look and feel, Javascript and AJAX for interaction with the rest framework's backend.

Like-Unlike functionality has been used to store the user input in the database and serve the related user interface without reloading the page for smooth and uninterrupted user interaction.

User can register, login, create an event, update an event, delete an event, view all the events, like-unlike any event.

However, User will be able to delete and update only those events which are created by him/her.

To access pages other than login/registration, user will have to provide auth token. Auth token can be added to request header using ModHeader chrome extension. In ModHeader, add request header with name 'Authorization' and your access token string as value with Bearer as suffix.

First, user will need to register an account. Upon successful registration, user will be given an access token which can be added to every request made by user to the DRF endpoints.
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SECRET_KEY`

`DEBUG`

`DB_NAME`

`DB_USER`

`DB_PASSWORD`

`DB_HOST`


## 🔗 Links
[![github](https://img.shields.io/badge/github-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/bhavinpokal)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/bhavinpokal)


## License

[MIT](https://choosealicense.com/licenses/mit/)


## Tech Stack

**Client:** HTML, CSS, BootStrap, JavaScript, AJAX

**Server:** Django Rest Framework

**Database:** Postgres


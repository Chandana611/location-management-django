# Location Details API

A Django REST API application for managing and retrieving location details based on **District, Taluk, and Hobli** master data.

The application uses **Django REST Framework** for API development and **Microsoft SQL Server Stored Procedures** for database operations.

---

## Features

* Fetch all Districts
* Fetch Taluks based on selected District
* Fetch Hoblis based on selected Taluk
* Save location details
* Retrieve saved location details by ID
* Server-side validation for required fields
* SQL Server Stored Procedures for database operations
* Simple responsive web interface for entering location details

---

## Technologies Used

* **Python**
* **Django 4.2**
* **Django REST Framework**
* **Microsoft SQL Server**
* **SQL Server Stored Procedures**
* **HTML5**
* **CSS3**
* **JavaScript**

---

## Application Flow

The application follows a simple layered structure:

```text
Frontend
   │
   ▼
Django REST API
   │
   ▼
Service Layer
   │
   ▼
SQL Server Stored Procedures
   │
   ▼
SQL Server Database
```

The Django application communicates with SQL Server through stored procedures instead of directly writing database queries inside the API views.

---

## Project Structure

```text
location-details-api/
│
├── api/
│   ├── migrations/
│   ├── templates/
│   │   └── api/
│   │       └── index.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── services.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Database

The application uses a Microsoft SQL Server database.

### Database

```text
D00_Jango_Application
```

### Main Tables

#### District_Master

Stores district master information.

```text
district_id
district_lgd_code
district_name
dist_name_kannada
```

#### Taluk_Master

Stores taluk information associated with districts.

```text
taluk_id
taluk_lgd_code
taluk_name
taluk_kannada_name
district_id
```

#### Hobli_Master

Stores hobli information associated with taluks.

```text
district_name
taluk_name
hobli_name
hobli_name_eng
taluk_id
hobli_id
```

#### SaveFormData

Stores the location details submitted through the application.

```text
id
name
address
district_id
district_name
district_lgd_code
taluk_id
taluk_name
taluk_lgd_code
hobli_id
hobli_name
created_date
```

---

## Stored Procedures

The application uses the following SQL Server Stored Procedures:

### Get Districts

```text
GetDistrictsMaster
```

Returns the list of districts.

### Get Taluks

```text
GetTaluksMaster
```

Returns taluks based on the selected district.

### Get Hoblis

```text
GetHobliMaster
```

Returns hoblis based on the selected taluk.

### Save Location Details

```text
SaveFormDataa
```

Saves the submitted location details along with the corresponding district, taluk, and hobli information.

### Get Saved Location Details

```text
GetSaveFormData
```

Returns saved location details based on the record ID.

---

## API Endpoints

### 1. Get Districts

```http
GET /api/districts/
```

Returns all available districts.

Example:

```json
{
    "status": true,
    "districts": [
        {
            "district_id": 1,
            "district_lgd_code": 524,
            "district_name": "BAGALKOT",
            "dist_name_kannada": "ಬಾಗಲಕೋಟೆ"
        }
    ]
}
```

---

### 2. Get Taluks

```http
GET /api/taluks/{district_id}/
```

Returns taluks belonging to the selected district.

Example:

```http
GET /api/taluks/23/
```

---

### 3. Get Hoblis

```http
GET /api/hoblis/{taluk_id}/
```

Returns hoblis belonging to the selected taluk.

Example:

```http
GET /api/hoblis/12/
```

---

### 4. Save Location Details

```http
POST /api/save/
```

Request body:

```json
{
    "name": "Ramesh",
    "address": "Bengaluru",
    "district_id": 23,
    "taluk_id": 1,
    "hobli_id": 180
}
```

Successful response:

```json
{
    "status": true,
    "message": "Data saved successfully"
}
```

---

### 5. Get Saved Location Details

```http
GET /api/save/{id}/
```

Example:

```http
GET /api/save/1/
```

Successful response:

```json
{
    "status": true,
    "message": "Data Found Successfully",
    "id": 1,
    "name": "Ramesh",
    "address": "Bengaluru",
    "district_id": 23,
    "district_name": "RAICHUR",
    "district_lgd_code": 546,
    "taluk_id": 1,
    "taluk_name": "Sindhnur",
    "taluk_lgd_code": 5463,
    "hobli_id": 180,
    "hobli_name": "Turvihal"
}
```

If the record does not exist, the API returns HTTP `404`.

---

## Frontend

The project also contains a simple web interface for entering location details.

The user can:

1. Enter Name
2. Enter Address
3. Select District
4. Select Taluk
5. Select Hobli
6. Submit the form

The dropdowns are dependent on each other:

```text
District
   │
   ▼
Taluk
   │
   ▼
Hobli
```

When a District is selected, the application loads the corresponding Taluks.

When a Taluk is selected, the application loads the corresponding Hoblis.

---

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/location-details-api.git
```

Navigate into the project:

```bash
cd location-details-api
```

---

### 2. Create Virtual Environment

Windows:

```powershell
python -m venv venv
```

Activate it:

```powershell
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Database

Update the database configuration in:

```text
config/settings.py
```

Example:

```python
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'D00_Jango_Application',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'your_sql_server_host',
        'PORT': '1433',
        'OPTIONS': {
            'driver': 'ODBC Driver 18 for SQL Server',
            'extra_params': 'TrustServerCertificate=yes',
        },
    },
}
```

**Do not commit actual database passwords or other credentials to GitHub.**

For a shared or production project, database credentials should be stored using environment variables or another secure configuration mechanism.

---

### 5. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at:

```text
http://127.0.0.1:8000/
```

API endpoints are available under:

```text
http://127.0.0.1:8000/api/
```

---

## API Testing

The APIs can be tested using tools such as:

* Browser
* Postman
* Thunder Client
* curl

Example:

```bash
curl http://127.0.0.1:8000/api/districts/
```

---

## Validation

The Save API validates the required fields before calling the database:

* Name
* Address
* District ID
* Taluk ID
* Hobli ID

If a required field is missing, the API returns a `400 Bad Request`.

Example:

```json
{
    "status": false,
    "message": "Name is required"
}
```

---

## Learning Objectives

This project demonstrates the following concepts:

* Django project and app structure
* Django REST Framework
* API routing
* GET and POST APIs
* Request and response handling
* Service-layer architecture
* Calling SQL Server Stored Procedures from Django
* Working with SQL Server from Python
* Dependent dropdowns
* Form validation
* JSON API responses
* Virtual environments
* Python package management
* Git and GitHub project management

---

## Future Improvements

Possible improvements for future versions:

* Add authentication and authorization
* Add serializers for structured request validation
* Move database credentials to environment variables
* Add automated unit and API tests
* Add API documentation using Swagger/OpenAPI
* Add centralized exception handling
* Add logging
* Add Docker support
* Add CI/CD using GitHub Actions

---

## License

This project is intended for learning and development purposes.

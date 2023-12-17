# Django Project / Garagezone

Garage Zone is a web application built with Django, designed to facilitate the selling of cars. It provides a user-friendly interface with a search field, beautiful design, and integration for registering or logging in with Google and Facebook accounts. Additionally, the project customizes the admin page and includes essential features to ensure a comprehensive website.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [License](#license)

7. ![readme](https://github.com/aminramezanni/django-project-garagezone/assets/111316617/5c26bdcb-ac76-41b5-a0b2-c3f4fadec97a)

## Introduction

Garage Zone is an online platform where users can browse, search for, and list cars for sale. The project aims to simplify the process of selling vehicles by providing an easy-to-use interface and integrating popular social login options for seamless user registration and authentication and use postgresql database.

## Features

The Garage Zone Django project includes the following features:

- **Search Field**: Users can search for specific car models, makes, or other relevant criteria to find the desired vehicles.

- **Beautiful Design**: The project incorporates an aesthetically pleasing and responsive design to enhance user experience across various devices.

- **Social Login**: Users can register or log in using their Google and Facebook accounts, streamlining the onboarding process.

- **Customized Admin Page**: The admin interface has been customized to provide better management of car listings, user accounts, and other relevant data.

- **Essential Website Features**: The project includes all necessary functionalities that any car selling website should have, such as user authentication, car listing creation, user profiles, etc.

## Installation

To set up Garage Zone on your local machine, follow these steps:

1. Ensure you have Python 3.x installed on your system.

2. Clone this repository to your local machine using the following command:
   git clone `https://github.com/aminramezanni/django-project-garagezone`

3. Navigate to the project directory:
   ```cd django-project-garagezone```

4. Create and activate a virtual environment:
   ```python -m venv venv```
   ```source venv/bin/activate``` # On Windows, use: `venv\Scripts\activate`

5. Install the required dependencies:
   ```pip install -r requirements.txt```

6. Set up the database:
   ```python manage.py migrate```

7. Create a superuser to access the admin interface:
   ```python manage.py createsuperuser```

8. Start the development server:
   ```python manage.py runserver```


9. Visit `http://127.0.0.1:8000/` in your web browser to access Garage Zone.

## Usage

After installing and running the project, users can access the website and perform the following actions:

- Browse and search for cars using the search field.

- Register or log in using their Google or Facebook accounts.

- Create listings to sell cars.

- Manage user profiles and listings.

- Admins can access the customized admin page to manage users and listings efficiently.

## Contributing

We welcome contributions to Garage Zone that can improve its functionality, design, or fix any issues. If you would like to contribute, please follow these steps:

1. Fork the repository on GitHub.

2. Create a new branch with a descriptive name for your feature/fix.

3. Make your changes and commit them with a clear message.

4. Push your changes to your forked repository.

5. Submit a pull request, explaining the changes you made.

## License

The Garage Zone project is licensed under the [MIT License](LICENSE). Feel free to use and modify the code according to the terms of this license.

## Contact 

If you have any questions, suggestions, or would like to get in touch, feel free to send an email to aminramezanni@gmail.com. We appreciate your feedback and will do our best to respond as soon as possible.

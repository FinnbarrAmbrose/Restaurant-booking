# Restaurant Booking

![Image Placeholder]

A Django based web application for booking tables at a restaurant

## Project Brief

The Restaurant Booking system is a web based application that allows users to book tables online The system includes authentication booking management and an admin panel for restaurant owners to manage reservations efficiently

## Contents Table

1. [Project Brief](#project-brief)  
2. [Agile](#agile)  
3. [Wireframes](#wireframes)  
4. [Screenshots](#screenshots)  
5. [Features](#features)  
6. [Future Improvements](#future-improvements)  
    - [Planned Enhancements](#planned-enhancements)  
7. [Authentication and Administration](#authentication-and-administration)  
8. [Installation](#installation)  
9. [Usage](#usage)  
10. [Deployment](#deployment)  
11. [Credits](#credits)  
12. [License](#license)  


## Agile

## Wireframes

## Screenshots

## Features

The application includes user registration and login functionality. Users can create, update, and delete bookings. Additionally, users can view a list of their bookings.

## Future Improvements

A list of user stories will be included in the backlog to document planned enhancements.

### Planned Enhancements

- Implement flash messages for user feedback (e.g., successful booking, login, logout confirmations, error messages).
- Redirect users based on roles (e.g., admin users redirected to the admin panel, regular users to their booking dashboard).
- Restrict booking actions to logged-in users to maintain security and privacy.
- Prevent double bookings by checking for existing reservations at the same date and time.
- Improve the navigation menu to dynamically update based on user authentication status.
- Enhance user experience by adding alerts and error messages for failed login attempts or incorrect form submissions.
- Deploy the project on **Hurricane** with proper database configurations.
- Add an email-based password reset feature allowing users to reset their password through an HTML page.

## Authentication and Administration

The application provides secure user authentication with login and registration features. There is an admin interface for managing users and bookings. The application also includes password reset functionality.

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd restaurant_booking
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Set up the database:
    ```sh
    python manage.py migrate
    ```

4. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

5. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Usage

Access the application at `http://127.0.0.1:8000/`. Users can register a new account or log in with an existing account. Once logged in, users can create, update, and delete bookings.

## Deployment

Deployment will be done on **Hurricane**. The application includes a `Procfile` for deployment on Heroku platforms.

## Credits

Note: Video links will be added later.

This project uses templates and code from various sources:

- Bootstrap CSS and HTML templates from [Bootstrap](https://getbootstrap.com/)
- Django tutorials and code snippets from [Django documentation](https://docs.djangoproject.com/) and other online tutorials
- Certain solutions adapted from Stack Overflow and other online tutorials (linked where applicable)
- The website theme is based on a template from [W3Schools](https://www.w3schools.com/bootstrap/tryit.asp?filename=trybs_temp_webpage&stacked=h)
- AI tools were used for research, debugging, and efficiency improvements in this project. All final code was reviewed and implemented by the developer.

## License

Further research on licensing is required. Currently considering the MIT License.
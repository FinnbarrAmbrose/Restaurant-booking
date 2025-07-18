# Restaurant Booking
![Image](https://github.com/user-attachments/assets/8da92841-3953-47bf-a314-9a9a9d220c59)
Welcome to my final Full Stack project - a web application I created to simulate the experience of booking a table at a restaurant online. It's built using Django and includes all the core functionality you'd expect – like user registration, bookings management, and a contact form for special requests.

This app was made as part of my Diploma in Full Stack Software Development. It was a huge learning experience and a lot of fun to put together.

---

![Django](https://img.shields.io/badge/Made%20with-Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Heroku](https://img.shields.io/badge/Deployed%20on-Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Users and Their Needs](#users-and-their-needs)
- [Technology Stack](#technology-stack)
- [Agile Planning](#agile-planning)
- [User Experience and Design](#user-experience-and-design)
- [Database Design](#database-design)
- [Installation](#installation)
- [Deployment](#deployment)
- [Screenshots](#screenshots)
- [Test Plan](#test-plan)
- [User Stories](#user-stories)
- [Lighthouse Audit](#lighthouse-audit)
- [Accreditations](#accreditations)
- [Features Checklist](#features-checklist)
- [Credits](#credits)

---

## Project Overview

This app is designed for restaurants who want to allow customers to easily book tables online. Users can sign up, log in, and manage their own bookings. It keeps things simple – just the essentials. A clean interface, mobile-friendly layout, and useful features make it practical and user-friendly.

**GitHub Repo:** [Restaurant Booking on GitHub](https://github.com/FinnbarrAmbrose/Restaurant-booking/)

**Live Link:** [restaurant-booking-a-d5df88975bf0.herokuapp.com](https://restaurant-booking-a-d5df88975bf0.herokuapp.com/)

---

## Features

- Register and log into your account
- Book a table by choosing a date, time, and number of guests
- See a confirmation message after booking
- View all your upcoming bookings in one place
- Edit or cancel bookings if needed
- Send the restaurant special requests (e.g., allergies, access needs)
- Stay within limits: Max 10 tables per night, 4 guests per table
- Only pick times when the restaurant is open (6–11PM)
- Fully responsive design (works well on phones)
- Social media links open in a new tab

---

## Users and Their Needs

I tried to look at the project from a real user's point of view. Here’s what I focused on solving:

- “I want to make a booking quickly on my phone.”
- “I want to be able to change or cancel it if something comes up.”
- “I want the restaurant to know about allergies or other needs.”
- “I want the site to be clear, easy and not annoying to use.”

And for the restaurant owner:
- “I need to avoid double bookings.”
- “I need control over how many guests we take each night.”

---

## Technology Stack

- **HTML & CSS** – for structure and styling
- **Bootstrap** – responsive layout and UI elements
- **Python** – backend language
- **Django** – the web framework
- **PostgreSQL** – the database
- **Heroku** – for deployment
- **Git & GitHub** – for version control

---

## Agile Planning

I used GitHub Projects to organise my work. I created a Kanban board where each feature became a card. Cards were labelled by priority (must-have, should-have, nice-to-have) and moved through the columns: To Do → In Progress → Done.

It helped keep things on track and made sure nothing essential got missed.

I also opened and closed GitHub issues as I progressed through different parts of the build.

![Image](https://github.com/user-attachments/assets/fdba06a8-4acf-4db1-84e2-72a77987cc27)
---

## User Experience and Design

The homepage has a large image background and clear calls to action. I chose colours that were classy and suitable for a restaurant feel. The layout adapts to small screens and most pages are centered for clarity.

Buttons are bold and labelled clearly. The font is readable. Icons add a nice touch.

Forms use validation to help users avoid mistakes. Flash messages confirm user actions.

---

## Database Design

- Each user can have multiple bookings
- Each booking is linked to one user
- Special requests are tied to individual bookings

Bookings include:
- Date
- Time
- Number of guests

Contact messages include:
- Dietary preferences
- Additional notes

---

## Installation

To run this project locally:

```bash
git clone https://github.com/FinnbarrAmbrose/Restaurant-booking.git
cd restaurant_booking
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Then visit `http://127.0.0.1:8000/` in your browser.

---

## Deployment

This section outlines how to set up the project locally and deploy it to Heroku.

### Prerequisites
- Python 3.11+  
- Git  
- (Optional) PostgreSQL for local testing  
- Heroku CLI ([install guide](https://devcenter.heroku.com/articles/heroku-cli))

### Local Setup

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/restaurant-booking.git
   cd restaurant-booking
   ```

2. **Create and activate a virtual environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate.bat  # Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Generate a Django SECRET_KEY**  
   ```bash
   python - << 'EOF'
   from django.core.management.utils import get_random_secret_key
   print(get_random_secret_key())
   EOF
   ```

5. **Create a `.env` file** (in project root):  
   ```env
   DJANGO_SECRET_KEY=<your-generated-key>
   DJANGO_DEBUG=True
   DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
   DATABASE_URL=               # leave blank to use SQLite fallback
   ```

6. **Apply migrations & collect static files**  
   ```bash
   python manage.py migrate
   python manage.py collectstatic --noinput
   ```

7. **Run the development server**  
   ```bash
   python manage.py runserver
   ```
   Visit `http://localhost:8000` in your browser.

### Deploying to Heroku

1. **Login and create a Heroku app**  
   ```bash
   heroku login
   heroku create your-app-name
   heroku git:remote -a your-app-name
   ```

2. **Provision Heroku Postgres**  
   ```bash
   heroku addons:create heroku-postgresql:hobby-dev
   ```

3. **Set environment variables on Heroku**  
   ```bash
   heroku config:set      DJANGO_SECRET_KEY=<your-prod-secret>      DJANGO_DEBUG=False      DJANGO_ALLOWED_HOSTS=your-app-name.herokuapp.com
   ```

4. **Add `runtime.txt` and `Procfile`**  
   - **runtime.txt**:
     ```txt
     python-3.11.5
     ```
   - **Procfile**:
     ```txt
     web: gunicorn restaurant_booking.wsgi --log-file -
     ```

5. **Commit and push to Heroku**  
   ```bash
   git add runtime.txt Procfile
   git commit -m "Add Heroku runtime and Procfile"
   git push heroku main
   ```

6. **Run migrations and collect static on Heroku**  
   ```bash
   heroku run python manage.py migrate
   heroku run python manage.py collectstatic --noinput
   ```

7. **Open your live app**  
   ```bash
   heroku open
   ```
---

## Screenshots

Here are some views of the app in action.

### Homepage  
![Image](https://github.com/user-attachments/assets/8da92841-3953-47bf-a314-9a9a9d220c59)

### Footer
![Image](https://github.com/user-attachments/assets/96ef3fb8-94f2-4beb-abab-87b55d2a22d6)

### Booking Page  
![Image](https://github.com/user-attachments/assets/a73fbacd-6ddc-4cea-8678-e0db42488d8c)

### My Bookings
![Image](https://github.com/user-attachments/assets/733bff9e-02ed-43ca-8f8c-840e6047e006)

### Mobile View  
![Image](https://github.com/user-attachments/assets/2771feed-63d6-4b11-9981-9a12b0f5ea33)

---

## Test Plan

| Test | Outcome | Screenshot |
|------|---------|------------|
| User can register an account | ✅ | ![Image](https://github.com/user-attachments/assets/3c8712cb-ff38-4c81-8a4d-407bbec44135) |
| Feedback shown after registration | ✅ | ![Image](https://github.com/user-attachments/assets/4a7f55b7-ece2-4d1d-8539-60965455f054) |
| User can log in with valid credentials | ✅ | ![Image](https://github.com/user-attachments/assets/1d3e2693-c69d-4b96-86e2-05b10ab8a205) |
| User cannot log in with invalid credentials | ✅ | ![Image](https://github.com/user-attachments/assets/005b6458-1ab6-4a8d-9c82-3e5a37e35b96) |
| User can log out successfully | ✅ | ![Image](https://github.com/user-attachments/assets/679d7f42-6400-496e-81a2-2a5552057a00) |
| User can view all their bookings | ✅ | ![Image](https://github.com/user-attachments/assets/36338f2a-bf66-4185-8dda-3d5460381fb4) |
| User can create a new booking | ✅ | ![Image](https://github.com/user-attachments/assets/c329242a-769d-4b63-8cd1-b4ddd7029f88) |
| Booking guest limit enforced (1–4) | ✅ | ![Image](https://github.com/user-attachments/assets/771a5d82-2865-4329-b7c6-4ac2be92a004)|
| Booking capped at 10 tables per night | ✅ | ![Image](https://github.com/user-attachments/assets/3d3d26d7-f1bc-4258-838d-414fd1a08eda) |
| Booking edit functionality works | ✅ | ![Image](https://github.com/user-attachments/assets/0df07a0b-5b2a-43ae-a79a-592670ed9753)|
| Booking delete with success message | ✅ | ![Image](https://github.com/user-attachments/assets/78f2c749-5155-43ed-86be-32a0633a3ed9) |
| Contact form tied to a booking | ✅ | ![Image](https://github.com/user-attachments/assets/fce39968-cea6-4683-a5d0-8694f6d75226) |
| Dropdown shows booking info clearly | ✅ | ![Image](https://github.com/user-attachments/assets/cfaa7e60-de80-4220-8a2c-08827d93bad7) |
| Message shown after special request | ✅ | ![Image](https://github.com/user-attachments/assets/b188a60a-5474-4633-8df2-9b56e0e6b378) |
| Layout adapts on mobile | ✅ | ![Image](https://github.com/user-attachments/assets/2771feed-63d6-4b11-9981-9a12b0f5ea33) |
| Footer stays bottom on all screens | ✅ | ![Image](https://github.com/user-attachments/assets/b662a75a-70eb-41b8-89a5-e7b54dbdcecc) |
| Background images render properly | ✅ | ![Image](https://github.com/user-attachments/assets/5987ad9f-2365-448d-b321-3ffaccfafb15) |
| Social icons open in new tab | ✅ | ![Image](https://github.com/user-attachments/assets/c9f785f0-1f12-4ad7-8032-7dbefe832a61) |
| Static files load post deployment | ✅ | ![Image](https://github.com/user-attachments/assets/5987ad9f-2365-448d-b321-3ffaccfafb15) |

---
### Special-Requests Form: Empty Submission
1. Log in as `tester`  
2. Navigate to My Bookings → Special Requests  
3. Leave **Dietary Preferences** and **Additional Notes** blank  
4. Click **Submit**

**Expected:**  
- Inline error “Please enter your dietary preferences.” under the first field  
- Inline error “Please enter additional notes.” under the second field  

**Actual:**  
- Both error messages displayed correctly  
  ![special_requests_empty.png](screenshots/special_requests_empty.png)

---

### Special-Requests Form: Block Repeat Access
1. Log in as `tester`  
2. Submit a valid special-requests form for booking #123  
3. Try to visit `/bookings/123/contact/` again  

**Expected:**  
- Redirect to My Bookings with a warning “You have already submitted a special request for this booking.”  

**Actual:**  
- Redirect works and warning appears  
  ![special_requests_blocked.png](screenshots/special_requests_blocked.png)

---

## User Stories

- As a user, I want to register and log into my account.
- As a user, I want to book a table by picking the date, time, and number of guests.
- As a user, I want to see a message confirming my booking.
- As a user, I want to view all my bookings.
- As a user, I want to edit or cancel a booking if I need to.
- As a user, I want to inform the restaurant of dietary requirements.
- As a user, I want to give additional information like access needs.
- As a user, I only want to see available times that the restaurant is open.
- As the site owner, I want to limit bookings to 10 tables per night.
- As the site owner, I want to make sure no more than 4 guests per table are booked.

---

## Lighthouse Audit

Google Chrome’s Lighthouse audit was used to test performance, accessibility, and SEO.

![Image](https://github.com/user-attachments/assets/64d05705-7df5-4540-877d-2ac9fd46e7c0)

---

## Accreditations

- **Wireframes**: ![Image](https://github.com/user-attachments/assets/185b0c81-a357-41c9-b350-1c7bd836eb95) , ![Image](https://github.com/user-attachments/assets/297af046-07e3-4338-ba67-141f381c6150) , ![Image](https://github.com/user-attachments/assets/858b1e24-49ac-4bb0-aba6-295724728096)
- **Icons**: Font Awesome
- **Badge images**: [Shields.io](https://shields.io/)
- **AI Tools Used**: I wrote and reviewed the whole project however, I made use of the following tools for support:
  - **ChatGPT** – Used to help plan my Agile workflow
  - **GitHub Copilot** – Used during development to Understand why code wasn't working And to explain / clarify methods.
(All final decisions, logic, styling, and functionality were written and controlled by me as the developer.)---
- **Microsoft Windows dictate feature** - As is a Dyslexic I find this feature very useful in writing long sentences and paragraphs. by holding the windows key and pressing H you can enable a dictate software which I have used to write many things in this project in my own words while avoiding spelling errors. 

## Features Checklist

- [x] User registration and login
- [x] Table booking with date, time, and guest count
- [x] Booking confirmation messages
- [x] View, edit, and cancel bookings
- [x] Special requests form
- [x] Booking limits (10 tables per night, 4 guests per table)
- [x] Time limits (6–11PM)
- [x] Mobile responsive layout
- [x] Social links open in new tab
- [x] Deployment to Heroku

---

## Credits

Thanks to the Code Institute Slack community, my mentor, and fellow students for all their feedback and support throughout the build.

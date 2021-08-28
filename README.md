

# NewsAPP


IDE:
- PyCharm 2021.2

Platform:
- Python 3.9
- Django 3.2.6

API:
- Newsapi (https://newsapi.org/)

Windows OS requirements:
- pip install django
- pip install django-crispy-forms
- pip install requests

Usage:
- cd  ./NewsAPP/newsapp/
- python manage.py runserver

Directories overview:
- Application directory: NewsAPP/newsapp/News
- Project directory: NewsAPP/newsapp/NewsApp

Overview:

A website that displays a list of news to users. Registered users can add articles to their favorite list.

Requirements:

User registration information should include:

o Phone number **Done!**

o Email (to login with)  **Done!**

o Name  **Done!**

o Date of birth  **Done!**

o National id - Home page with a list of articles / news (you can use https://newsapi.org/)  **Done!**

o Registration /login pages.  **Done!**

o Details page to display full article.  **Done!**

o Save articles in local database.  **Done!**

o User can add/remove articles to his favorite list.  **Done!**

***Notes***
- To create a superuser account:
  * python manage.py createsuperuser
- To see all features (Favorite, Save Articles,.. ) you need to register.
- To add to favorite, you need to save articles first then go to the "Articles Database".
- To browse your favorite (Add or Remove) go to Favourites.

*This project has been done by Abdullah Almutairi as interview project for Takamol Holding*

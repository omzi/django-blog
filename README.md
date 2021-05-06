<a href="https://thatdevlog.herokuapp.com/" target="_blank"><p>
  <img src="static/images/logo.png" alt="Omzi's Devlog logo">
</p></a>
<blockquote cite="https://thatdevlog.herokuapp.com/">
<i>A slick, minimalist blog powered by Django & PostgreSQL✍.</i>
</blockquote>
<br>
<div>

![](https://img.shields.io/github/stars/omzi/django-blog.svg)
![](https://img.shields.io/github/forks/omzi/django-blog.svg)
![](https://img.shields.io/github/repo-size/omzi/django-blog)
![](https://img.shields.io/github/issues/omzi/django-blog.svg)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-blue.svg?style=flat)](https://github.com/omzi/django-blog/issues)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
![](https://img.shields.io/twitter/follow/o_obioha.svg?style=social&label=@o_obioha)

</div>

<h4><a href="https://thatdevlog.herokuapp.com/"><i>Live Demo</i> 🚀</a></h4>
<br>


## 📷 **Screenshots**
<img loading="lazy" alt="Screenshot #1" src="https://res.cloudinary.com/omzi/image/upload/v1620274341/github/django-blog/screenshot-01-min_xgzoum.png">
<img loading="lazy" alt="Screenshot #2" src="https://res.cloudinary.com/omzi/image/upload/v1620274340/github/django-blog/screenshot-02-min_ujyeo2.png">
<img loading="lazy" alt="Screenshot #3" src="https://res.cloudinary.com/omzi/image/upload/v1620274338/github/django-blog/screenshot-03-min_gvpcpg.png">
<img loading="lazy" alt="Screenshot #4" src="https://res.cloudinary.com/omzi/image/upload/v1620274338/github/django-blog/screenshot-04-min_hvqa9e.png">
<img loading="lazy" alt="Screenshot #5" src="https://res.cloudinary.com/omzi/image/upload/v1620274342/github/django-blog/screenshot-05-min_qeadcr.png">
<img loading="lazy" alt="Screenshot #6" src="https://res.cloudinary.com/omzi/image/upload/v1620274341/github/django-blog/screenshot-06-min_k3oy4g.png">
<img loading="lazy" alt="Screenshot #7" src="https://res.cloudinary.com/omzi/image/upload/v1620274339/github/django-blog/screenshot-07-min_cdiw2f.png">
<img loading="lazy" alt="Screenshot #8" src="https://res.cloudinary.com/omzi/image/upload/v1620274339/github/django-blog/screenshot-08-min_tkzbv7.png">



## ✨ **Features**
**Implemented / Planned:**
- [X] Dynamic blog
- [X] Reverse order post listing
- [X] Comments system
- [X] Category system
- [X] Sign Up & Log In (& log out, obviously)
- [X] Password reset functionality
- [X] Add posts & categories (via the FrontEnd)
- [X] Update posts & delete posts (via the FrontEnd)
- [X] Update Profile (via the FrontEnd)
- [X] Post images stored on Cloudinary
- [X] User generic avatars (on comments)
- [ ] Like/Unlike posts
- [ ] Social sharing buttons
- [ ] Email subscription
- [ ] View Profile
- [ ] User profile avatars
- [ ] 'Deploy to Heroku' button

<br>

## 💻 **Technologies Used**
- HTML + CSS
- [Bootstrap](https://getbootstrap.com)
- [Matter](https://github.com/finnhvman/matter)
- JavaScript
- [Python](https://python.org)
- [Django](https://djangoproject.com)
- [PostgreSQL](https://postgresql.org)
- [Cloudinary](https://cloudinary.com)

<br>

## 🚩 **Prerequisites**
You should have the following installed on your system:
* [Python](https://python.org/) version => 3.8.9
* [PIP](https://pypi.org/project/pip/) version >= 21.0.1
* [virtualenv](https://pypi.org/project/virtualenv/) version >= 20.4.3
<br><br>

## ⚡ **Installation**
Before you proceed, please ensure your system satisfies the prerequisites above. <br><br>
First things first, clone the repo into your desired folder & cd into it:
```shell
$ git clone https://github.com/omzi/django-blog.git && cd django-blog
```
Enter the command to activate the virtual environment for the project:
```shell
blog\scripts\activate
```
After that, install this project's dependencies by entering the command:
```shell
pip install -r requirements.txt
```
## ⚙ **Environment Variables**
This project comes with **required** environment variables that must be setup to avoid errors. First, rename the `.env.example` file in this project's root to `.env`. You should have something like this:
```shell
export DEBUG = # Boolean [True/False]
export SECRET_KEY = # Django secret key
export DATABASE_URL = sqlite:///db.sqlite3 # Or PostgreSQL URL
export EMAIL_HOST = # Email SMTP server
export EMAIL_HOST_USER = # Email account
export EMAIL_HOST_PASSWORD = # Password of email account
export CLOUDINARY_CLOUD_NAME = # Your Cloudinary 'cloud' name
export CLOUDINARY_API_KEY = # Your Cloudinary API key
export CLOUDINARY_API_SECRET = # Your Cloudinary API secret
```
A rundown of available environment variables:
- **`DEBUG`**: Set it to `"True"` if you want errors to be displayed on the site, otherwise set it to `"False"`.
- **`SECRET_KEY`**: To generate a secret key, enter Python's REPL & type the following:
<ul>

```py
from django.core.management.utils import get_random_secret_key

# Print new random secret key
print(get_random_secret_key())
```
Set the value of **`SECRET_KEY`** to the result.
</ul>

- **`DATABASE_URL`**: If you're working locally, you can leave the default as is, though it's preferable (in my opinion) working with a live database from the get-go. During deployment to platforms like Heroku, ensure you set the value to the URL of a live database.
- **`EMAIL_HOST`**: The password reset feature needs an email address to send the password reset mail. I used the SMTP option here, so set the value of this environment variable to the SMTP server hosting mails for **`EMAIL_HOST_USER`**. 
- **`EMAIL_HOST_USER`**: Set it's value to the email address you intend to use for this project. Please ensure the **`EMAIL_HOST`** variable is valid for your email address.
- **`EMAIL_HOST_PASSWORD`**: The password of the email address you intend to use for this project.
- **`CLOUDINARY_CLOUD_NAME`**, **`CLOUDINARY_API_KEY`** and **`CLOUDINARY_API_SECRET`**: You can [sign up for Cloudinary](https://cloudinary.com/users/register/free) for free, if you don't have an account. Once you're logged in, you'll need to retrieve your Cloud name, API key and API secret from the upper left corner of the Cloudinary console. Set their respective values in the `.env` file.
<ul>

<img loading="lazy" alt="Cloudinary console details" src="https://res.cloudinary.com/omzi/image/upload/v1620275315/github/cloudinary-console-details_lwanbj.png">
</ul>

After you're done setting your environment variables, migrate the models to create the necessary database tables:
```shell
python manage.py migrate
```
Also, don't forget to create a superuser account using:
```shell
python manage.py createsuperuser
```
To run the project locally, enter the command:
```shell
python manage.py runserver
```
Open up your browser and visit the URL: `http://127.0.0.1:8000/`.

<br>


## 👥 **Contribution**
If you want to contribute to the project, please [make a pull request](https://help.github.com/en/articles/creating-a-pull-request) or send your files to me via e-mail [obiohaomezibe@gmail.com](mailto:obiohaomezibe@gmail.com) as an attachment.

Your contribution is much appreciated. Thank you.

<br>

## 💬 **Contact**
If you have questions, feedback or anything to share, you can get in touch via:
* Twitter [@o_obioha](https://twitter.com/o_obioha)
* GitHub [@omzi](https://github.com/omzi)
* LinkedIn [/omezibe-obioha/](https://www.linkedin.com/in/omezibe-obioha/)
* or [submit an issue](https://github.com/omzi/django-blog/issues)

<br>

## ❌ **Disclaimer**
This project is my submission to one of the tasks in the [Zuri Internship](https://internship.zuri.team/), '21 cohort. It is **NOT** yet production-ready!

<br>

## 📄 **License**

This project is licensed under the terms of the
[MIT license](/LICENSE).
# Authentication System

## Overview
This project uses Django’s built-in authentication for login/logout, a custom RegistrationForm for signup (with unique email), and a simple Profile model linked One-to-One to User (bio, optional avatar).

## URLs
- `/register/` — Create a new account
- `/login/` — Sign in
- `/logout/` — Sign out
- `/profile/` — View current user’s profile (login required)
- `/profile/edit/` — Edit first/last name, email, bio, avatar (login required)

## Templates
Located in `blog/templates/blog/`:
- `base.html` (nav + messages)
- `home.html`
- `login.html`, `logout.html`, `register.html`
- `profile.html`, `profile_edit.html`

## Settings
- `LOGIN_REDIRECT_URL = "home"`
- `LOGOUT_REDIRECT_URL = "home"`
- `LOGIN_URL = "login"`
- `MEDIA_URL = "/media/"`
- `MEDIA_ROOT = BASE_DIR / "media"`

## How to Test
1. `python manage.py migrate`
2. `python manage.py runserver`
3. Register, login, update profile, upload avatar, logout.

## Security Notes
- CSRF tokens included in all POST forms.
- Passwords stored using Django’s password hashing.
- Profile images saved under `media/avatars/`.

# Social Media API

A Django REST Framework-based **social media API** that allows users to register, log in, manage profiles, create posts, and follow/unfollow other users.  
This project is part of my **ALX back-end web development Capstone**.

---

##  Features
- User authentication (Register, Login, Logout)
- JWT/Token-based authentication
- User profiles (view & update)
- Create, Read, Update, and Delete (CRUD) posts
- Follow/Unfollow users
- Browsable API interface for testing

---

##  Tech Stack
- **Backend:** Django, Django REST Framework
- **Database:** SQLite (default), can be switched to PostgreSQL
- **Authentication:** Django REST Framework Auth Token
- **Deployment Ready:** Production settings configured for WSGI/ASGI

--
🔗 API Endpoints
Endpoint	Method	Description
/	GET	API root (links to all endpoints)
/register/	POST	Register a new user
/login/	POST	Login and retrieve auth token
/logout/	POST	Logout (delete token)
/profile/	GET/PUT	View or update own profile
/users/	GET	List all users
/follow/<id>/	POST	Follow a user
/unfollow/<id>/	POST	Unfollow a user
/posts/	GET/POST	List or create posts
/posts/<id>/	GET/PUT/DELETE	Retrieve, update, or delete a post
🧪 Testing with Browsable API

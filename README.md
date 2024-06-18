## Blog Application
This is a full-stack blog application built using FastAPI for the backend and React for the frontend. The backend uses SQLite as the database and provides endpoints for managing users, posts, comments, categories, tags, and their relationships. The frontend is built with React and fetches data from the backend to display and manage blog content.

### Features
Create, read, update, and delete posts
Create, read, update, and delete users
Manage comments, categories, and tags
Display relationships between posts, categories, and tags
Responsive design with basic CSS styling
## Technologies Used
# Backend

FastAPI
SQLite
Python

# Frontend
React
JavaScript
CSS
Project Structure

# Backend
app.py: Entry point for the FastAPI application
models/: Contains all the database models and their CRUD operations
users.py
posts.py
comments.py
categories.py
tags.py
post_tags.py
post_categories.py
db.py: Database connection and cursor setup

# Frontend
src/
App.jsx: Main React component
UsersComponent.jsx: Component to display and manage users
PostsComponent.jsx: Component to display and manage posts
CommentsComponent.jsx: Component to display and manage comments
CategoriesComponent.jsx: Component to display and manage categories
TagsComponent.jsx: Component to display and manage tags
PostTagsComponent.jsx: Component to display post-tags relationships
PostCategoriesComponent.jsx: Component to display post-categories 

# relationships
index.css: Main CSS file for styling
Getting Started
Prerequisites
Python 3.8 or higher
Node.js and npm
SQLite

# Backend Setup
cd blog-app
Set up a virtual environment and install dependencies:
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install fastapi uvicorn
Create the SQLite database and tables:
bash
Copy code
python -m models.users
python -m models.posts
python -m models.comments
python -m models.categories
python -m models.tags
python -m models.post_tags
python -m models.post_categories
Run the FastAPI server:
bash
Copy code
uvicorn main:app --reload
The backend server will be running at http://localhost:8000.

## Frontend Setup
Navigate to the frontend directory:
bash
Copy code
cd frontend
Install the dependencies:
bash
Copy code
npm install
Start the React development server:
bash
Copy code
npm start
The frontend will be running at http://localhost:3000.

# Usage
Access the frontend at http://localhost:3000 to interact with the application.
Use the provided forms to create new users and posts.
View lists of users, posts, comments, categories, and tags.
The backend API endpoints are available at http://localhost:8000.

# API Endpoints
Users
GET /users/: Retrieve all users
POST /create_user/: Create a new user
Posts
GET /posts/: Retrieve all posts
POST /create_post/: Create a new post
Comments
GET /comments/: Retrieve all comments
Categories
GET /categories/: Retrieve all categories
Tags
GET /tags/: Retrieve all tags
Post Tags
GET /post_tags/: Retrieve all post-tags relationships
Post Categories
GET /post_categories/: Retrieve all post-categories relationships


# License
This project is licensed under the MIT License.

#LIVE LINK
file:///home/samuel/Videos/Screencasts/Screencast%20from%2018-06-2024%2009:05:16%20ASUBUHI.webm


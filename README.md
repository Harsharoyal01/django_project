# Movie Collection Web Application with Django

## Overview

The **Movie Collection Web Application** is a comprehensive project developed using Django that empowers users to create, manage, and personalize their own movie collections. Designed for both casual users and movie enthusiasts, the application provides a user-friendly interface for discovering and organizing movies while integrating seamlessly with external APIs.

## Key Features

1. **User-Centric Design**: 
   - Users can easily register and authenticate using JWT (JSON Web Tokens), ensuring secure access to their personal movie collections.

2. **Dynamic Movie Fetching**:
   - The application fetches movie data from a third-party API in real-time, providing users with up-to-date information on movies, including titles, descriptions, genres, and unique identifiers (UUIDs).

3. **Robust CRUD Functionality**:
   - Users can perform Create, Read, Update, and Delete (CRUD) operations on their movie collections, allowing them to add new movies, modify existing collections, and remove movies as desired.

4. **Request Monitoring**:
   - A custom request counter middleware tracks the total number of API requests made to the application. This feature not only helps in monitoring usage but also ensures that the application can scale effectively to handle high traffic.

5. **Personalized Experience**:
   - The application includes a feature that analyzes user behavior to return their top three favorite genres based on the movies they've added, enhancing user engagement through personalization.

## Technologies Used

- **Django**: Serves as the core framework for building the application and handling server-side logic.
- **Django Rest Framework (DRF)**: Facilitates the creation of RESTful APIs that connect the frontend to the backend.
- **JWT Authentication**: Provides a secure method for user authentication, ensuring that only authorized users can access their collections.
- **Middleware**: Enables the application to efficiently manage and count API requests.
- **Version Control with Git and GitHub**: Maintains a history of code changes, facilitates collaboration, and manages the project lifecycle.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Harsharoyal01/django_project.git
   cd django_project

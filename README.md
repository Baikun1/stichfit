# tailor e-commerce website
## to clone the website
```bash
git clone https://github.com/Baikun1/tailor3.git
```
### to install all modules
```bash
pip install -r reuirements.txt
```
### Go to the project outer folder
```bash
cd tailor
```
### to collect all static file 
```bash
python manage.py collectstatic
```
### to run the project 
```bash
python manage.py runserver
```
### Project Details

#### Functionality

This Django-based e-commerce project includes the following functionalities:

1. **User Authentication and Profiles**:
   - User registration, login, and logout.
   - User profile management, including profile picture upload.

2. **Product Management**:
   - CRUD operations for products (Create, Read, Update, Delete).
   - Product categories and subcategories.
   - Product media management (images and videos).

3. **Shopping Cart**:
   - Add products to the cart.
   - Update product quantities in the cart.
   - Remove products from the cart.
   - View cart contents.

4. **Order Management**:
   - Create and track orders.
   - View order history.
   - Order delivery status updates.

5. **Payment Processing**:
   - Integration with Stripe for payment processing.
   - Payment success and failure handling.
   - View payment history.

6. **Reviews and Ratings**:
   - Add reviews and ratings for products.
   - Upload media (images and videos) with reviews.

7. **Admin Interface**:
   - Manage users, products, orders, and reviews through the Django admin interface.
   - Use Django Debug Toolbar for debugging during development.

#### Tech Stack

1. **Backend**:
   - **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
   - **Django REST Framework** (if applicable): A powerful and flexible toolkit for building Web APIs.
   - **SQLite**: A lightweight, disk-based database used for development and testing.

2. **Frontend**:
   - **HTML/CSS**: For structuring and styling the web pages.
   - **JavaScript**: For client-side scripting and interactivity.
   - **Bootstrap** (if applicable): A popular CSS framework for responsive design.

3. **Authentication**:
   - **Django Allauth**: Integrated set of Django applications addressing authentication, registration, account management, and third-party (social) account authentication.

4. **Media Management**:
   - **Pillow**: A Python Imaging Library (PIL) fork that adds image processing capabilities to your Python interpreter.

5. **Payment Processing**:
   - **Stripe**: A suite of APIs powering online payment processing and commerce solutions for internet businesses.

6. **Environment Management**:
   - **django-environ**: A package for managing environment variables in Django projects.

7. **Debugging**:
   - **Django Debug Toolbar**: A configurable set of panels that display various debug information about the current request/response.

#### Directory Structure

```plaintext
ecommerce2/
├───cart/
│   ├───__init__.py
│   ├───admin.py
│   ├───apps.py
│   ├───migrations/
│   ├───models.py
│   ├───tests.py
│   ├───urls.py
│   └───views.py
├───db.sqlite3
├───ecommerce/
│   ├───__init__.py
│   ├───asgi.py
│   ├───settings.py
│   ├───urls.py
│   └───wsgi.py
├───home/
│   ├───__init__.py
│   ├───admin.py
│   ├───apps.py
│   ├───migrations/
│   ├───models.py
│   ├───tests.py
│   ├───urls.py
│   └───views.py
├───manage.py
├───media/
│   ├───product_media/
│   ├───profile_pics/
│   └───review_media/
├───orders/
│   ├───__init__.py
│   ├───admin.py
│   ├───apps.py
│   ├───forms.py
│   ├───migrations/
│   ├───models.py
│   ├───tests.py
│   ├───urls.py
│   └───views.py
├───payments/
│   ├───__init__.py
│   ├───admin.py
│   ├───apps.py
│   ├───migrations/
│   ├───models.py
│   ├───tests.py
│   ├───urls.py
│   └───views.py
├───products/
│   ├───__init__.py
│   ├───admin.py
│   ├───apps.py
│   ├───forms.py
│   ├───migrations/
│   ├───models.py
│   ├───tests.py
│   ├───urls.py
│   └───views.py
├───reviews/
│   ├───__init__.py
│   ├───admin.py
│   ├───apps.py
│   ├───migrations/
│   ├───models.py
│   ├───tests.py
│   ├───urls.py
│   └───views.py
├───static/
├───templates/
└───users/
    ├───__init__.py
    ├───admin.py
    ├───apps.py
    ├───forms.py
    ├───migrations/
    ├───models.py
    ├───tests.py
    ├───urls.py
    └───views.py
```

### Summary

This Django-based e-commerce project provides a comprehensive set of functionalities for managing users, products, orders, payments, and reviews. It uses a modern tech stack, including Django, SQLite, Stripe, and various Django packages for authentication, media management, and debugging. The project is well-structured, with separate apps for different functionalities, making it easy to manage and extend.

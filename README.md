# Orders Management System
_created with GitHub Copilot_

This project is an Orders Management System built with Django. It allows users to manage orders and order items efficiently. The system includes forms for creating and updating orders, as well as tests to ensure the functionality of the forms and views.

## Features

- **Order Management**: Create, update, and manage orders.
- **Order Items**: Add and manage items within an order.
- **Form Validation**: Ensure data integrity with form validation.
- **Testing**: Comprehensive tests for forms and views.

## Technologies Used

- **Python**: Programming language.
- **Django**: Web framework.
- **pip**: Package installer for Python.

## Project Structure

- `orders/forms.py`: Contains form definitions for orders and order items.
- `orders/tests/test_forms.py`: Contains tests for the order forms.
- `products/tests/test_views.py`: Contains tests for the product views.

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    ```
2. Navigate to the project directory:
    ```sh
    cd <project-directory>
    ```
3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Run the Django development server:
    ```sh
    python manage.py runserver
    ```

## Running Tests

To run the tests, use the following command:
```sh
python manage.py test

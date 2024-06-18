# ATM Interface
 
`By LightxAman`

This is a console-based ATM Interface built using Python and Tkinter for a graphical user interface. The system allows users to perform various banking operations such as viewing transaction history, withdrawing money, depositing money, transferring money, and quitting the application.

## Features

- **User Registration and Login**: Users must register and then log in using their user ID and PIN to access the ATM functionalities.
- **Transaction History**: View a list of past transactions.
- **Withdraw**: Withdraw a specified amount of money.
- **Deposit**: Deposit a specified amount of money.
- **Transfer**: Transfer a specified amount of money to another account.
- **Quit**: Exit the application.

## Project Structure

The application is structured into multiple files for better organization:

- `main.py`: Main application file.
- `registration.py`: Handles user registration and login.
- `transactions.py`: Manages viewing of transaction history.
- `withdraw.py`: Handles withdrawal operations.
- `deposit.py`: Handles deposit operations.
- `transfer.py`: Handles money transfer operations.
- `users.txt`: Stores user data.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.
- Tkinter library for Python.

### Installation

1. Clone the repository to your local machine:


2. Navigate to the project directory:
    ```sh
    cd Task 1
    ```
3. Ensure all required files are in place:
    - `main.py`
    - `registration.py`
    - `transactions.py`
    - `withdraw.py`
    - `deposit.py`
    - `transfer.py`
    - `users.txt` (this file will be created automatically if it doesn't exist)

### Running the Application

Run the main Python file to start the ATM interface:

```sh
python main.py

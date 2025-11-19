PostgreSQL Operations Using Python (psycopg2)
📌 Project Overview

This Python project demonstrates complete PostgreSQL database operations using the psycopg2 library.
The program allows a user to:

Create a PostgreSQL database

Delete a database

Connect to a specific database

Create a table

Insert data (with user input)

Retrieve all records

Delete a specific record

Perform all tasks using a simple interactive menu-driven program

This project is useful for understanding how Python interacts with PostgreSQL.

🛠️ Technologies Used

Python 3.x

psycopg2 (PostgreSQL adapter for Python)

PostgreSQL

📦 Install Dependencies

Install psycopg2 using:

pip install psycopg2

⚙️ How to Run the Program
1. Ensure PostgreSQL Is Installed

Install PostgreSQL and start the service.
Remember your:

Username

Password

Port (default: 5432)

2. Update Credentials Inside Script

In the script, modify:

user="postgres"
password="YOUR_PASSWORD"
host="localhost"

3. Run the Script

Go to your project folder and run:

python main.py


This will open the interactive menu.

🧭 Program Menu Options

When the program runs, you will see:

=== PostgreSQL Operations Menu ===
1. Create Database
2. Delete Database
3. Create Table
4. Insert Data (User Input)
5. Retrieve Data
6. Delete a Record
7. Exit

🧪 Features Explained
✔️ 1. Create Database

Creates a new PostgreSQL database using default connection.

✔️ 2. Delete Database

Safely deletes an existing database.

✔️ 3. Create Table

Creates a students table with fields:

id (Primary Key)

name

marks

✔️ 4. Insert Data

Takes:

Student Name
Marks


Then inserts into the table.

✔️ 5. Retrieve Data

Fetches and displays all rows from the table.

✔️ 6. Delete a Record

Deletes a row based on student ID entered by user.

📂 Project File Structure
PostgreSQL-Project/
│
├── main.py             # Main program with menu-driven PostgreSQL operations
└── README.md           # Documentation

🔐 Important Notes

Usernames and passwords should be updated before running.

Make sure the PostgreSQL server is running.

Only the default database ("postgres") is used for CREATE and DELETE operations.

🧑‍💻 Author

Suhani

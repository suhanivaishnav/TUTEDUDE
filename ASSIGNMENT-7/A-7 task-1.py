import psycopg2

# ---------------------------------------------------
# Function: Connect to PostgreSQL using default database
# ---------------------------------------------------
def connect_default():
    return psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Suhani2004@",
        host="localhost",
        port="5432"
    )

# ---------------------------------------------------
# Create Database studentdb, student
# ---------------------------------------------------
def create_database(db_name):
    conn = connect_default()
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE {db_name};")
    print(f"Database '{db_name}' created successfully!")
    cursor.close()
    conn.close()

# ---------------------------------------------------
# Delete Database student
# ---------------------------------------------------
def delete_database(db_name):
    conn = connect_default()
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(f"DROP DATABASE IF EXISTS {db_name};")
    print(f"Database '{db_name}' deleted successfully!")
    cursor.close()
    conn.close()

# ---------------------------------------------------
# Connect to a specific database studentdb
# ---------------------------------------------------
def connect_to_db(db_name):
    return psycopg2.connect(
        dbname=db_name,
        user="studentdb",
        password="Suhani2004@",
        host="localhost",
        port="5432"
    )

# ---------------------------------------------------
# Create Table
# ---------------------------------------------------
def create_table(db_name):
    conn = connect_to_db(db_name)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            marks INT
        );
    """)
    conn.commit()
    print("Table 'students' created successfully!")
    cursor.close()
    conn.close()

# ---------------------------------------------------
# Insert Data (with user input)
# ---------------------------------------------------
def insert_data(db_name):
    conn = connect_to_db(db_name)
    cursor = conn.cursor()

    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))

    cursor.execute("INSERT INTO students (name, marks) VALUES (%s, %s);", (name, marks))
    conn.commit()

    print("Data inserted successfully!")
    cursor.close()
    conn.close()

# ---------------------------------------------------
# Retrieve Data
# ---------------------------------------------------
def retrieve_data(db_name):
    conn = connect_to_db(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students;")
    records = cursor.fetchall()

    print("\n--- Student Records ---")
    for row in records:
        print(row)

    cursor.close()
    conn.close()

# ---------------------------------------------------
# Delete a row
# ---------------------------------------------------
def delete_data(db_name):
    conn = connect_to_db(db_name)
    cursor = conn.cursor()

    student_id = int(input("Enter ID to delete: "))
    cursor.execute("DELETE FROM students WHERE id = %s;", (student_id,))
    conn.commit()

    print("Record deleted successfully!")
    cursor.close()
    conn.close()


# ---------------------------------------------------
# MAIN MENU
# ---------------------------------------------------
def main():
    while True:
        print("\n=== PostgreSQL Operations Menu ===")
        print("1. Create Database")
        print("2. Delete Database")
        print("3. Create Table")
        print("4. Insert Data (User Input)")
        print("5. Retrieve Data")
        print("6. Delete a Record")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            db = input("Enter database name: ")
            create_database(db)

        elif choice == "2":
            db = input("Enter database name to delete: ")
            delete_database(db)

        elif choice == "3":
            db = input("Enter database name: ")
            create_table(db)

        elif choice == "4":
            db = input("Enter database name: ")
            insert_data(db)

        elif choice == "5":
            db = input("Enter database name: ")
            retrieve_data(db)

        elif choice == "6":
            db = input("Enter database name: ")
            delete_data(db)

        elif choice == "7":
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")


# ---------------------------------------------------
# Run the Program
# ---------------------------------------------------
if __name__ == "__main__":
    main()

import mysql.connector

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="schoolapplication"
)

# Create cursor
cursor = db.cursor()

# Function to insert student data
def insert_student(name, dob, address, gender, parent_name, parent_mobile, parent_occupation, parent_email):
    sql = "INSERT INTO students (name, date_of_birth, home_address, gender, parent_name, parent_mobile, parent_occupation, parent_email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (name, dob, address, gender, parent_name, parent_mobile, parent_occupation, parent_email)
    cursor.execute(sql, val)
    db.commit()
    print("Student data inserted successfully.")

# Example usage:
insert_student("John Doe", "2005-05-20", "123 Main St, City", "Male", "Jane Doe", "1234567890", "Engineer", "jane@example.com")

# Close the connection
cursor.close()
db.close()

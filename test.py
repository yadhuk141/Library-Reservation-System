import mysql.connector

# Establish a connection to the MySQL server
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="yadhuafr141",
    database="test"
)

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table
create_table_query = '''
CREATE TABLE  employees (
    id INT  PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    address VARCHAR(255)
)'''
cursor.execute(create_table_query)

# Insert rows into the table
insert_query = '''INSERT INTO employees (name, age, address) VALUES (%s, %s, %s)'''
data = [
    ("John Doe", 30, "123 Main St"),
    ("Jane Smith", 35, "456 Elm St"),
    ("Bob Johnson", 25, "789 Oak St")
]
cursor.executemany(insert_query, data)
conn.commit()

# Retrieve and display the data from the table
select_query = "SELECT * FROM employees"
cursor.execute(select_query)
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close the cursor and the database connection
cursor.close()
conn.close()

import mysql.connector

# Connect to the MySQL server
mydb = mysql.connector.connect(
    host="localhost", user="root", passwd="root", database="world"
)
print(mydb)

# Create a cursor
mycursor = mydb.cursor()

# Create the 'customerss' table if it doesn't exist
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS customerss (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        address VARCHAR(255),
        phone VARCHAR(20)
    )
""")
# Truncate the 'customerss' table to remove all records
truncate_query = "TRUNCATE TABLE customerss"
mycursor.execute(truncate_query)
mydb.commit()

# Show existing tables
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)

# Insert data into the 'customerss' table
insert_query = "INSERT INTO customerss (name, address, phone) VALUES (%s, %s, %s)"
values = [("LUKE", "HIGHWAY31", "123-436-7890"), ("TIM", "HIGHWAY41", "124-436-7890")]
mycursor.executemany(insert_query, values)
mydb.commit()
print(mycursor.rowcount, "record(s) inserted")

# Fetch and print data from the 'customerss' table ordered by name in ascending order
select_query = "SELECT * FROM customerss ORDER BY name ASC"
mycursor.execute(select_query)
myresult = mycursor.fetchall()
for y in myresult:
    print(y)

# Fetch and print data from the 'customerss' table with address 'HIGHWAY31'
select_query1 = "SELECT * FROM customerss WHERE address='HIGHWAY31'"
mycursor.execute(select_query1)
myresult1 = mycursor.fetchall()
for z in myresult1:
    print(z)

# Close the cursor and database connection
mycursor.close()
mydb.close()

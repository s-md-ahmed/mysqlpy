# Import the mysql.connector library to connect to the MySQL database
import mysql.connector

# Create a connection to the MySQL database server
mydatabase = mysql.connector.connect(
    host="localhost",     # Host where the MySQL server is running
    user="root",          # Username to authenticate with
    password="root",      # Password for authentication
    database="cricket"    # Name of the database to connect to
)

# Create a cursor object to interact with the database
cursor = mydatabase.cursor()

# Display a list of existing databases
cursor.execute("SHOW DATABASES")
for db in cursor:
    print(db)

# Create a table named 'cric_player' if it doesn't exist
create_table_query = "CREATE TABLE IF NOT EXISTS cric_player (name VARCHAR(20), jersey_number INT, age INT, score INT)"
cursor.execute(create_table_query)

# Define a SQL query to insert data into the 'cric_player' table
insert_data_query = "INSERT INTO cric_player (name, jersey_number, age, score) VALUES (%s, %s, %s, %s)"

# Prepare a list of player records to be inserted into the table
players = [("Lara", 10, 25, 100), ("Ponting", 12, 26, 123)]

# Insert multiple records into the table using executemany
cursor.executemany(insert_data_query, players)

# Commit the changes to the database
mydatabase.commit()

# Fetch and print data from the 'cric_player' table
cursor.execute("SELECT * FROM cric_player")
result = cursor.fetchall()
for row in result:
    print(row)

# Update the age of the player named 'Lara'
update_query = "UPDATE cric_player SET age = 46 WHERE name = 'Lara'"
cursor.execute(update_query)

# Commit the changes to the database
mydatabase.commit()

# Close the cursor and the database connection

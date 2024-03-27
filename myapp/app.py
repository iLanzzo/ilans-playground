import mysql.connector
import time

# Wait a few seconds before connecting
time.sleep(10)

try:
    # Connect to MySQL
    mydb = mysql.connector.connect(
        host="mysql",
        user="root",
        password="ilandev",
        database="mydb"
    )

    # Create a cursor object
    cursor = mydb.cursor()
    
    # Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS myapp (
            id INT AUTO_INCREMENT PRIMARY KEY,
            data VARCHAR(255)
        )
    """)

      # Check if the table is empty
    cursor.execute("SELECT COUNT(*) FROM myapp")
    table_count = cursor.fetchone()[0]

    # If table is empty, add text into data column
    if table_count == 0:
        cursor.execute("INSERT INTO myapp (data) VALUES (%s)", ("Welcome to ilandia!",))
        mydb.commit()  # Commit the transaction

    # Specify the ID of the row you want to fetch
    id = 1

    # Execute a query to fetch the specific row by ID
    cursor.execute("SELECT data FROM myapp WHERE id = %s", (id,))

    # Fetch the result
    result = cursor.fetchone()

    # Print the result
    if result:
        print("Message:", result[0])
    else:
        print("No message found for ID:", id)

except mysql.connector.Error as error:
    print("Error:", error)

finally:
    # Close the connection
    if 'mydb' in locals() and mydb.is_connected():
        cursor.close()
        mydb.close()


# import mysql.connector
# #import time

# #time.sleep(5)

# # Connect to MySQL
# mydb = mysql.connector.connect(
#     host="devproj-mysql",
#     user="root",
#     password="ilandev",
#     database="mydb"
# )

# # Create a cursor object
# cursor = mydb.cursor()

# # Specify the ID of the row you want to fetch
# RowID = 1

# # Execute a query to fetch the specific row by ID
# #cursor.execute("SELECT Text FROM myapp WHERE id = %s", (RowID,))
# cursor.execute("SELECT Text FROM myapp WHERE RowID = %s", (RowID,))

# # Fetch the result
# result = cursor.fetchone()

# # Print the result
# if result:
#     print("Message:", result[0])
# else:
#     print("No message found for ID:", RowID)

# # Close the connection
# mydb.close()


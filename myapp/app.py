import mysql.connector
#import time

#time.sleep(5)

# Connect to MySQL
mydb = mysql.connector.connect(
    host="devproj-mysql",
    user="root",
    password="ilandev",
    database="mydb"
)

# Create a cursor object
cursor = mydb.cursor()

# Specify the ID of the row you want to fetch
RowID = 1

# Execute a query to fetch the specific row by ID
cursor.execute("SELECT Text FROM myapp WHERE RowID = %s", (RowID,))

# Fetch the result
result = cursor.fetchone()

# Print the result
if result:
    print("Message:", result[0])
else:
    print("No message found for ID:", RowID)

# Close the connection
mydb.close()
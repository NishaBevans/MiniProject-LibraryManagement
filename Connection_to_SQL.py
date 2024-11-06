import mysql.connector
from mysql.connector import Error

# Database Connection Parameters
db_name = "library_management"
user = "root"
password = "TJChav3z2024!"
host = "localhost"

def connect_database():
    """Connect to the MySQL database and return the connection object"""
    try:
        # Attempting to make a connection
        conn = mysql.connector.connect(
            database=db_name,  # Use the defined db_name variable
            user=user,         # Use the defined user variable
            password=password,  # Use the defined password variable
            host=host,         # Use the defined host variable
            port=3306,
            use_pure=True
        )
        
        # Check if the connection is successful
        if conn.is_connected():
            print("Connected to MySQL database successfully")
            return conn
        else:
            print("Connection failed")
            return None
    
    except Error as e:
        # Handling any connection errors
        print(f"Error: {e}")
        return None

# Example usage
if __name__ == "__main__":
    connection = connect_database()
    if connection:
        # Perform database operations here
        connection.close()  # Remember to close the connection when done
        print("Connection was closed.")

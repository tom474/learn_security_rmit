import sqlite3


def safe_query(user_input):
    # Connect to the database
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    # Use parameterized query to prevent SQL injection
    cursor.execute("SELECT * FROM users WHERE username = ?", (user_input,))

    # Fetch and print the results
    results = cursor.fetchall()
    
    for row in results:
        print(row)
    # Close the connection
    conn.close()
 
 
# Example usage
user_input = 'example_user'
safe_query(user_input)

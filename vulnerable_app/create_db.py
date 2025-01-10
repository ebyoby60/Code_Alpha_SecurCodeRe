import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('example.db')

# Create users table
conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')

# Insert sample data
conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', ('admin', '12345'))

# Save changes and close connection
conn.commit()
conn.close()

print("Database created successfully!")

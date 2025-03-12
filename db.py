import mysql.connector
import time

# Tal + Eddy
def get_db_connection():
    """Create a connection to the MySQL database"""
    # Try to connect multiple times (useful when starting up)
    for _ in range(10):
        try:
            conn = mysql.connector.connect(
                host="chat-mysql",
                user="chatuser",
                password="chatpass",
                database="chatapp"
            )
            return conn
        except mysql.connector.Error:
            # Wait and retry
            time.sleep(3)
    
    raise Exception("Could not connect to MySQL database")

def init_db():
    """Initialize the database schema"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create rooms table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS rooms (
        name VARCHAR(255) PRIMARY KEY
    )
    ''')
    
    # Create messages table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS messages (
        id INT AUTO_INCREMENT PRIMARY KEY,
        room_name VARCHAR(255),
        username VARCHAR(255) NOT NULL,
        message TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (room_name) REFERENCES rooms(name)
    )
    ''')
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Database initialized successfully")

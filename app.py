from flask import Flask, request, current_app, send_from_directory
from datetime import datetime
import os 
from db import get_db_connection, init_db

app = Flask(__name__)


# Initialize the database when the app starts
@app.before_first_request
def initialize():
    init_db()

@app.route('/', methods=['GET'])
def index():
    return current_app.send_static_file('index.html')


@app.route('/<room>', methods=['GET'])
def get_room(room):
    return current_app.send_static_file("index.html")


@app.route('/api/chat/<room>' , methods=['GET'])
def get_room_chat(room):
    # Connect to database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Ensure room exists (create if not)
    cursor.execute("INSERT IGNORE INTO rooms (name) VALUES (%s)", (room,))
    conn.commit()

    # Get messages for room
    cursor.execute("""
        SELECT timestamp, username, message
        FROM messages 
        WHERE room_name = %s 
        ORDER BY timestamp
        """, (room,))

    messages = cursor.fetchall()
    cursor.close()
    conn.close()
    
    # If no messages found, return new room message
    if not messages:
        return 'This is a new room, send the first message!'

    # Format messages as required
    formatted_messages = []
    for timestamp, username, message in messages:
        formatted_time = timestamp.strftime('%Y-%m-%d %H:%M:%S')
        formatted_messages.append(f'[{formatted_time}] {username}: {message}')
    
    return '\n'.join(formatted_messages)


@app.route('/api/chat/<room>' , methods=['POST'])
def add_message(room):
     message_data = request.form.to_dict()

     username = message_data['username']
     message = message_data['msg']

      
    # Connect to database
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Ensure room exists
    cursor.execute("INSERT IGNORE INTO rooms (name) VALUES (%s)", (room,))

    # Insert message
    cursor.execute("""
        INSERT INTO messages (room_name, username, message)
        VALUES (%s, %s, %s)
    """, (room, username, message))
    
    conn.commit()
    cursor.close()
    conn.close()

    return '', 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

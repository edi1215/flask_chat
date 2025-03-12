from flask import Flask, request, current_app, send_from_directory
from datetime import datetime
import os 

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return current_app.send_static_file('index.html')


@app.route('/<room>', methods=['GET'])
def get_room(room):
    return current_app.send_static_file("index.html")


@app.route('/api/chat/<room>' , methods=['GET'])
def get_room_chat(room): 
        if not (os.path.isfile(f'rooms/{room}')):
            return 'This is a new room, send the first message!'
        else :
            return send_from_directory("rooms", f"{room}")


@app.route('/api/chat/<room>' , methods=['POST'])
def add_message(room):
     message_data = request.form.to_dict()

     username = message_data['username']
     message = message_data['msg']
     current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
     with open(f'rooms/{room}', 'a') as room_file:
        room_file.write(f'[{current_datetime}] {username}: {message}\n')

     return ' '


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, current_app, send_from_directory

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return current_app.send_static_file('index.html')


@app.route('/<room>', methods=['GET'])
def get_room(room):
    return current_app.send_static_file("index.html")


@app.route('/api/chat/<room>' , methods=['GET'])
def get_room_chat(room): 
        return send_from_directory("rooms", f"{room}")


@app.route('/api/chat/<room>' , methods=['POST'])
def add_message(room):
     return


if __name__ == '__main__':
    app.run(debug=True)

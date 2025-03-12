from flask import Flask, request, current_app

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return current_app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)

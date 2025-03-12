from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['?'])
def api():
    name = None
    
    if request.method == 'GET':
        return
    elif request.method == 'POST':
        return
    return 


if __name__ == '__main__':
    app.run(debug=True)

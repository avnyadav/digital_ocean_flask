from crypt import methods
from flask import Flask

app = Flask(__name__)


@app.route('/',methods=['GET'])
def index():
    return "This is avnish. Hello World!"



if __name__ == '__main__':
    app.run(debug=True,port=8080)
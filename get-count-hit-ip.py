from flask import Flask, jsonify
from multiprocessing import Value

# Creating the instance of the class Flask
counter = Value('i', 0)
app = Flask(__name__)

@app.route('/')
def index():
    with counter.get_lock():
        counter.value += 1
        out = counter.value

    return jsonify(count=out)


# Run the application
if __name__ == '__main__':
    #init MYSQL
    app.run(host="0.0.0.0",port=80,debug=False)
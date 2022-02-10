from flask import Flask, render_template, request
import time, sys
from loom import *

app = Flask(__name__)
testArray = []
with open('static/numbers.txt') as my_file:
    testArray = my_file.readlines()

index = 0



def loop(next, array):
    if next + 1 > len(array):
        return 1
    else:
        return next + 1


def reverse(next, array):
    target = next - 1
    if target <= 0:
        return len(array)
    else:
        return target


@app.route('/')
def hello_world():  # put application's code here
    return render_template("home.html")


@app.route("/next", methods=["POST", "GET"])
def nextRoute():
    global index
    index = loop(index, testArray)
    lightItUp(index)
    return render_template("index.html", content=testArray, index=index)


@app.route("/previous", methods=["POST", "GET"])
def previousRoute():
    global index
    index = reverse(index, testArray)
    lightItUp(index)
    return render_template("index.html", content=testArray, index=index)

@app.route("/off", methods=["POST", "GET"])
def offRoute():
    off()
    return render_template("home.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)

from flask import Flask
app = Flask(__name__)

@app.route("/",methods=['POST','GET'])
def index():
    return "<h1>This is a Flask Application</h1>"


if __name__=="__main__":
    app.run()


from flask import Flask
app = Flask(__name__)

@app.route("/")
def ola():
    return 'Hello Flask'

if __name__=="__main__":
    app.run()
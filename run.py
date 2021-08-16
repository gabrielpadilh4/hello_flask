from flask import Flask
app = Flask(__name__)

@app.route("/<int:number1>", methods=['GET','POST'])
def hello(number1):
    return 'Hello Flask.{}'.format(number1)

if __name__=="__main__":
    app.run(debug=True) # Only in devlopment mode
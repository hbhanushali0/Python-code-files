
from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World 3"
    
@app.route("/about")
def about():
    return "app by HB"

if __name__ == "__main__":
    app.run(debug = True)
    
    
    


from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    s1 = '''
    
            <center>
            <h1 style="color:red;">
            Hello World HB
            </h1>
            </center>
            
        '''
        
    return s1
    
@app.route("/about")
def about():
    s1 = '''
    
            <center>
            <h1 style="color:blue;">
            App By HB
            </h1>
            </center>
            
            
        '''
        
    return s1
    
    
if __name__ == "__main__":
    app.run(debug = True)
    
    
            

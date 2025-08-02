from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def button1_action():
    # Add the functionality for button 1 here
    # For example, you can perform some action and return a response
    return render_template('compare.html')
    
@app.route('/apple', methods=['POST'])
def applebtn():
    return render_template('apple.html')
    
@app.route('/samsung', methods=['POST'])
def samsungbtn():
    return render_template('samsung.html')

@app.route('/coupon', methods=['POST'])
def button2_action():
    # Add the functionality for button 2 here
    return render_template('coupon.html')
    
@app.route('/search',methods=['GET'])
def searchbtn():
    return "Your Coupon is : A!B@C#D$E%F^G&H*I(J)K_L+"

@app.route('/deals', methods=['POST'])
def button3_action():
    # Add the functionality for button 3 here
    return render_template('deals.html')
    
@app.route('/dealsearch', methods=['GET'])
def dealsearchbtn():
    return redirect("https://www.amazon.com")

if __name__ == '__main__':
    app.run(debug=True)

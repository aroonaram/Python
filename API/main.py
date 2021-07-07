from flask import Flask, request, jsonify, render_template # import

app = Flask(__name__) # # create app



@app.route('/', methods=['GET']) # To render Homepage
def index():
    return render_template('index.html')

@app.route('/math', methods=['POST'])  # This will be called from UI
def math_operation():
    if (request.method=='POST'):
        operation=request.form['operation']
        num1=int(request.form['num1'])
        num2 = int(request.form['num2'])
        if(operation=='add'):
            r=num1+num2
            result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
        if (operation == 'subtract'):
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'multiply'):
            r = num1 * num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'divide'):
            r = num1 / num2
            result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
        return render_template('results.html',result=result)

@app.route('/postman', methods=['POST']) # To call the API from Postman/SOAPUI
def calculator():
    if (request.method == 'POST'):
        operation = request.json['operation']
        val1 = int(request.json['val1'])
        val2 = int(request.json['val2'])
        if (operation == 'add'):
            r = val1+val2
            result= 'the sum of '+str(val1)+' and '+str(val2) +' is '+str(r)
        if(operation == 'Multiply'):

            result = r
        if (operation == 'Substract'):
            result = r
        return jsonify(result)








if __name__ == '__main__' :# keep it running
    print("app is working")
    app.run()


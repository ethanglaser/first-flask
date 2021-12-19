from flask import Flask, render_template, request, Response, send_file


 
app = Flask(__name__)
 
@app.route('/form')
def form():
    return render_template('form.html')
 
@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        return render_template('data.html',form_data = form_data)

@app.route('/')
def hello():
    return 'Hello World!'

# construct your app

@app.route("/get-file")
def get_file():
    return send_file("requirements.txt", as_attachment=True)
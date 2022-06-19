
# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask,render_template,flash, request, redirect, url_for
import urllib.request
import os
from werkzeug.utils import secure_filename
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

#files will be uploaded to server in this folder
UPLOAD_FOLDER = 'static/uploads/'
 
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 #max 16 mb file upload
 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'pdf'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

  
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.

#index
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

#upload endpoint
@app.route('/upload', methods=['POST'])
def upload_image():
    app.logger.info(request.url)
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #print('upload_image filename: ' + filename)
        if filename.rsplit('.', 1)[1].lower() != 'pdf':
            flash('Image successfully uploaded and displayed below')
            return render_template('index.html', filename=filename)
        else:
            flash('Pdf successfully uploaded to server')
            return redirect(request.referrer)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif, pdf')
        return redirect(request.url)
 
#to display uploaded image in frontend if required  
@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

#sample form to demonstrate form upload to server
@app.route('/info')  
def info():  
   return render_template('info.html')  

#sample form posted to this endpoint
#to demo how data sent to server can be processed and sent back to frontend
@app.route('/success',methods = ['POST', 'GET'])  
def print_data():  
   if request.method == 'POST':  
      result = request.form  
      return render_template("result_data.html",result = result) 
  
# main driver function
if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug=True)
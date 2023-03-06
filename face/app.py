import os
from flask import Flask , render_template , request , redirect , url_for , flash , send_from_directory
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from PIL import Image
#pip instal flask-sqlalchemy


app = Flask(__name__ )

@app.route('/')
def index():
   return render_template('index.html')
	
# @app.route('/', methods = ['GET', 'POST'])
# def upload_file():
#    if request.method == 'GET':
#       f = request.files['file']
#       f.save(secure_filename(f.filename))
#       return 'file uploaded successfully'

@app.route('/login')
def login():
   return render_template('login.html')

@app.route('/filee')
def file():
   return render_template('filee.html')

@app.route('/admin' , methods = ['POST'])
def admin():
   if request.method == 'POST':
      return render_template('admin.html')
   else:
      return render_template('admin.html')

# @app.route('/static/index.js')
# def serve_js():
#     return send_from_directory(app.static_folder, 'index.js')


UPLOAD_FOLDER = 'static\\upload_images' 
app.secret_key = os.urandom(24)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload_picture', methods=['GET', 'POST'])
def upload_picture():
   if request.method == 'POST': #GET 
        # check if the post request has the file part
      #   if 'file' not in request.files:
      #       flash('No file part')
      #       return redirect(request.url)
      file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
      #   if file.filename == '':
      #       flash('No selected file')
      #       return redirect(request.url)
      if file and allowed_file(file.filename):
         filename = secure_filename(file.filename)
         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
         print('Filename:', filename)
         print('Upload folder:', app.config['UPLOAD_FOLDER'])
         flash('File uploaded successfully')         
         return redirect(url_for('uploaded_file', filename=filename))
         
                  
      else:
         flash('Invalid file format')
         return redirect(request.url)
  
  

@app.route('/static/upload_images/<filename>')
def uploaded_file(filename):
   #return redirect(UPLOAD_FOLDER, filename)
   #return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
   #return render_template('filee.html')
   # Get the full path to the uploaded file
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    # Open the image file using PIL
    image = Image.open(filepath)

    # Resize the image to the desired size
    image = image.resize((500, 500))

    # Render the upload.html template with the filename and image data
    return render_template('index.html', filename=filename, image=image.tobytes())
#create upload.html and paste chat gpt code there to test if image is displayed


# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
   app.run(debug = True)

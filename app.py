import os
import requests
import json

# NASA API auth
from roti_rot import rot13

from flask import Flask
from flask import render_template

# File upload example
from flask import flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)

# region - authenticate and get image data from NASA
with open('xrl.txt', 'r') as read_handle:
    key = rot13(read_handle.readline())

my_nasa_api_link = f'https://api.nasa.gov/planetary/apod?api_key={key}'
# endregion

# region declare file upload particulars
if os.path.exists('./uploads'):
    print('Upload folder exists')
else:
    os.mkdir('./uploads')
    print('Made upload dir')

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'png', 'gif', 'png', 'jpg', 'jpeg', 'txt'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# function to verify if file extension is allowed
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# endregion

# region define the root resource - NASA image of the day loader
@app.route('/')
def index_page():
    r = requests.get(my_nasa_api_link)
    response = r.json()

    copyright_text = 'Image Credits: '
    if 'copyright' in response:
        copyright_text += response['copyright']
    else:
        copyright_text += 'Public Domain'

    description_text = response.get('explanation', 'No description')
    title_text = response.get('title', 'No title')

    media_type = response['media_type']
    media_url = response['url']

    return render_template('index.html',
                           copyright_text=copyright_text,
                           description_text=description_text,
                           title_text=title_text,
                           media_type=media_type,
                           media_url=media_url)
# endregion


# region define file upload resource
@app.route('/fileUpload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        # if user does not select file, browser can also submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        # valid case
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))

    # Case if method is GET - return HTML page
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
# endregion


# region define file download resource
@app.route('/uploads/<filename>', methods=['GET'])
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
# endregion


# region define file lister resource
@app.route('/uploads')
def get_file_list():
    file_list = os.listdir(UPLOAD_FOLDER)
    return json.dumps(file_list)
# endregion


if __name__ == '__main__':
    app.run()
from flask import Flask, request, make_response
from processing import process
import werkzeug
from config import ALLOWED_EXTENSIONS, HOST, PORT


app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    if 'media' not in request.files:
        return make_response('Send file with image header', 404)
    file = request.files['media']
    file.filename = werkzeug.utils.secure_filename(file.filename)
    if file.filename.split('.')[1] not in ALLOWED_EXTENSIONS:
        return make_response('Send image file with extention *.jpg, *.jpeg, *.png, *.tiff', 404)
    process(file)
    return (' ', 204)


if __name__ == "__main__":
    app.run(HOST, PORT)
from flask import Flask, send_from_directory
import os 


app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(app.root_path, 'media')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def get_media():
    return send_from_directory(app.config['UPLOAD_FOLDER'], "image.png")


if __name__ == "__main__":
    app.run("0.0.0.0", 5566)
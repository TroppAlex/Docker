import os
import json
import datetime
from flask import Flask, render_template

app = Flask(__name__)

BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))
RESOURCE_DIR = os.path.join(BASE_FOLDER, "resources")
PEOPLE_FOLDER = os.path.join(BASE_FOLDER, 'people_photo')



@app.route('/')
def hello_world():
    with open(os.path.join(RESOURCE_DIR, "response.json")) as f:
        return "%s - %s" % (json.loads(f.read()).get("payload"), datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
# @app.route('/index')
# def show_index():
#     full_filename = os.path.join(app.config[PEOPLE_FOLDER], '1.png')
#     return render_template("index.html", user_image = full_filename)
#
#
# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
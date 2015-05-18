import json
from datetime import datetime
from flask import Flask
from flask import render_template

app = Flask(__name__)  # Note the double underscores on each side

def get_json():
	with open("./static/4.5_month.json") as f:
		data = json.loads(f.read())
		quakes = data['features']
	return quakes

get_json()

@app.route("/")
def index():
	template = 'index.html'
	object_list = get_json()
	return render_template(template, object_list=object_list)

@app.route('/<row_id>/')
def detail(row_id):
    template = 'detail.html'
    object_list = get_json()
    for row in object_list:
        if row['id'] == row_id:
            return render_template(template, object=row)


#running a test server
if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)
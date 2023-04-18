import numpy as np
from flask import Flask, render_template, request, redirect
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from image_dict import dog_names 

app = Flask(__name__)

model = load_model('model_120.h5')
def predict_label(img_path):
	img = image.load_img(img_path, target_size=(200, 200))
	img = image.img_to_array(img)
	img = img.reshape(1, 200, 200, 3)
	p = model.predict(img)
	print(p)
	return dog_names[np.argmax(p)]

# Routes
@app.route("/", methods=['GET'])
def homepage():
	return render_template("home.html")

@app.route("/about", methods=['GET'])
def about_page():
	#return "Sneha Seenuvasavarathan - https://www.linkedin.com/in/svsneha/"
	return redirect("https://www.linkedin.com/in/svsneha/", code=302)

@app.route("/submit", methods = ['POST'])
def send_img():
	img = request.files['my_image']
	img_path = "static/uploads/" + img.filename
	img.save(img_path)
	p = predict_label(img_path)
	return render_template("prediction.html", prediction = p, img_path = img_path)

@app.route("/question", methods = ['GET','POST'])
def send_answer():
	# qn = request.json['question']
	# print(qn)
	return 'yagaa'

if __name__ =='__main__':
	app.run(debug = False, port = 8888) #create http server which people can access

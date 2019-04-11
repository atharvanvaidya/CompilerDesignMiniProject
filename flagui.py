from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import miniproject
#app = Flask(__name__)

app = Flask(__name__, static_url_path='/static') 

# class ReusableForm(Form):
# 	name = TextField('Name:', validators=[validators.required()])

# class SentencesDataset(FlaskForm):
# 	test_sentence = StringField('test_sentence' , validators=[DataRequired()])
# 	submit = SubmitField('submit')

sentences = ['अनवर को विंसेट ने रन आउट किया ।','जयसूर्या ने १६ गेंदों का सामना कर तीन चौके लगाये ।' , ' नई दिल्ली ।']

jsonObject = {
	'answer' : [('No Sentence' ,  'Available!')],
	'sentences' : sentences
}

@app.route('/')
def index():
	#return "Hello World!"
	# return app.send_static_file('index.html')
	return render_template('index.html' , jsonObject=jsonObject)
	
@app.route('/' , methods=['POST'])
def index_post():
	text = request.form['sentence'];
	# jsonObject['answer'] = text
	jsonObject['answer'] = miniproject.tagthesentence(text)
	return render_template('index.html' , jsonObject=jsonObject)

if __name__ == '__main__':
   app.run(debug = True)

# @app.route('/tagger' , methods=['GET', 'POST'])
# def tag():
# 	form = ReusableForm(request.form)
# 	myMessage = "Atharva"
# 	if request.method == 'POST':
# 		name=request.form['name']
# 		print(name)
# 	if form.validate():
# 	# Save the comment here.
# 		flash('Hello ' + name)
# 	else:
# 		flash('All the form fields are required. ')
# 	return render_template('index.html', message = myMessage)

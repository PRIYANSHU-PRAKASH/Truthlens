from flask_socketio import SocketIO
from flask import Flask, render_template, request
import fakenews as fr
import PredictionNews as PN
import FetchReal as cd


    
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
	return render_template('main.html')

@app.route('/createdataset',methods=['POST'])			#Create dataset
def createdataset():
	cd.process()
	return render_template('main.html')


@app.route('/main',methods=['POST'])					#Main html file
def main_page():
    	path=request.form['datasetfile']
    	print(path)
    	return render_template('main.html')

@app.route('/countmodel',methods=['POST'])				#Count Model call method
def count_page():
    	path=request.form['datasetfile']
    	print(path)
    	fr.MainProcessCount(path)
    	return render_template('main.html')
   
@app.route('/tfidfmodel',methods=['POST'])				#TFIDF Model call method
def tfidf_page():
    	path=request.form['datasetfile']
    	print(path)
    	fr.MainProcessTfidf(path)
    	return render_template('main.html')

@app.route('/ngrammodel',methods=['POST'])				#Ngram Model Call Method
def ngram_page():
    	path=request.form['datasetfile']
    	print(path)
    	fr.MainProcessNgram(path)
    	return render_template('main.html')


@app.route('/reset',methods=['POST'])					#Reset Button
def reset():
	return render_template('main.html')


@app.route('/prediction',methods=['POST'])				#Prediction Call function
def prediction_page():
    	path=request.form['datasetfile']
    	news=request.form['news']
    	print(path)
    	print(news)
    	res,res1=PN.process(path,news)
    	print(res)
    	return render_template('main.html',message=res,message1=res1,news=news)



# /////////socket io config ///////////////
#when message is recieved from the client    
@socketio.on('message')
def handleMessage(msg):
    print("Message recieved: " + msg)
 
# socket-io error handling
@socketio.on_error()        # Handles the default namespace
def error_handler(e):
    pass


  
  
if __name__ == '__main__':
    socketio.run(app,debug=True,host='127.0.0.1', port=4000)

from flask import Flask, render_template, request
from camera import detectImage
from PIL import Image as im
import io

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ReturnHome')
def ReturnHome():
    return render_template('index.html')

@app.route('/OnImage', methods=['GET', 'POST'])
def OnImage():
    return render_template('onImage.html')

@app.route('/picture', methods=['GET', 'POST'])
def picture():
    file = request.files['file1']
    file.save('static/file.jpg')
    print("="*50)
    print("IMAGE SAVED")

    img_path = 'static/file.jpg'
    

    print("*"*50)
    print("Model is detecting")
    
    detectedBytes = detectImage(img_path)
    detected = im.open(io.BytesIO(detectedBytes))
    detected.save('static/file1.jpg')
    
    stringfile = open('C:/Users/HP/Downloads/OCR/static/stringfile.txt','r')
    data = stringfile.read()
    stringfile.close()
    return render_template('picture.html', string = data)

app.run(debug=True)
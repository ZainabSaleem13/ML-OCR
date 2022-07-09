import numpy as np
from pytesseract import Output
import pytesseract
import cv2


def detectImage(filename):
        img = cv2.imread(filename)
        pytesseract.pytesseract.tesseract_cmd = 'C://Program Files (x86)//Tesseract-OCR//tesseract.exe'
        
        norm_img = np.zeros((img.shape[0], img.shape[1]))
        img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
        img = cv2.GaussianBlur(img, (1, 1), 0)
        img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
        results = pytesseract.image_to_data(img, output_type=Output.DICT)
        string = " ".join([i for i in results['text']])
        text_file = open("C:/Users/HP/Downloads/OCR/static/stringfile.txt", "w")
        text_file.write(string)
        text_file.close()
        
        for i in range(0, len(results['text'])):
            x = results['left'][i]
            y = results['top'][i]
            w = results['width'][i]
            h = results['height'][i]
            text = results['text'][i]
            conf = float(results['conf'][i])
            if conf > 70.0:
                text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 200), 2)
        
        ret,jpg=cv2.imencode('.jpg', img)
        return jpg.tobytes()
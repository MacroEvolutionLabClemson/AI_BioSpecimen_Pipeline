import sys, os
from segmentation.pipeline.training_pipeline import TrainPipeline
from segmentation.utils.main_utils import decodeImage, encodeImageIntoBase64
from flask import Flask, request, jsonify, render_template, Response
from flask_cors import CORS, cross_origin
from segmentation.constant.application import APP_HOST, APP_PORT



app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"



#training route
@app.route("/train")
def trainRoute():
    obj = TrainPipeline()
    obj.run_pipeline()
    return "Training Successfull!"


#home route
@app.route("/")
def home():
    return render_template("index.html")



#prediction route
@app.route("/predict", methods = ['POST', 'GET'])
@cross_origin()
def predictRoute():
    try:
        image = request.json['image']
        decodeImage(image, clApp.filename)

        os.system("yolo task=segment mode=predict model=artifacts/model_trainer/best.pt conf=0.25 source=data/inputImage.jpg save=true")

        opencodedbase64 = encodeImageIntoBase64("runs/segment/predict/inputImage.jpg")
        result = {"image": opencodedbase64.decode('utf-8')}
        os.system("rm -rf runs")

    except ValueError as val:
        print(val)
        return Response("Value not found inside json data")
    except KeyError:
        return Response("Key value error. Incorrect key passed")
    except Exception as e:
        print(e)
        result = "Invalid input"
    
    return jsonify(result)


if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host = APP_HOST, port = APP_PORT)
    
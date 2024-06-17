from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv

from analysis_service import *

load_dotenv()

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/health')
@cross_origin()
def index():
    return 'success'


@app.route('/mediapipe/img', methods=['POST'])
@cross_origin('*')
def analyze_image():
    try:
        params = request.get_json()
        front_image_key = params['frontImgKey']
        side_image_key = params['sideImgKey']

        front_analysis = analysis_front_image(front_image_key)
        side_analysis = analysis_side_image(side_image_key)

        return jsonify({
            'frontShoulderAngle': front_analysis[0],
            'frontPelvisAngle': front_analysis[1],
            'frontKneeAngle': front_analysis[2],
            'frontAnkleAngle': front_analysis[3],
            'sideNeckAngle': side_analysis[0],
            'sideBodyAngle': side_analysis[1],
        }), 201
    except Exception as e:
        e.with_traceback()
        return jsonify({'error': 'Error occurred during prediction'}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6000)

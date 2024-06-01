from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/health')
@cross_origin()
def index():
    return 'success'


@app.route('/mediapipe/img', methods=['POST'])
@cross_origin('*')
def predict():
    try:
        front_image_url = request.form.get('frontImgUrl')
        side_image_url = request.form.get('sideImgUrl')

        print(front_image_url, side_image_url)
        return jsonify({
            'frontShoulderAngle': 100,
            'frontPelvisAngle': 200,
            'frontKneeAngle': 300,
            'frontAnkleAngle': 400,
            'sideNeckAngle': 500,
            'sideBodyAngle': 600,
        }), 200
    except Exception as e:
        print(e)
        return jsonify({'error': 'Error occurred during prediction'}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6000)

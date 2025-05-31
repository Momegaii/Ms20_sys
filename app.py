from flask import Flask,render_template,request,jsonify
from enginehim import *
from ms20models import MS20Models , models
app = Flask(__name__)

@app.route('/stars')
def stars():
    stars = 'stars.html'
    return render_template(stars)

@app.route('/MShim')
def ms_him():
    msh = 'MS_him.html'
    return render_template(msh)

@app.route('/market')
def market():
    mrkt= 'market.html'
    return render_template(mrkt)

@app.route('/MSDL')
def msdl():
    msdl = 'MS20Models.html'
    return render_template(msdl)

@app.route('/Cals_ms')
def mscal():
    mscal = 'pred_cals.html'
    return render_template(mscal)
@app.route('/diabetes')
def diabetes():
    diab = 'diabetes.html'
    return render_template(diab)
@app.route('/lng')
def lng():
    lng = 'lung.html'
    return render_template(lng)

@app.route('/request')
def sndreq():
    sndrq = 'request.html'
    return render_template(sndrq)
@app.route('/Grequest')
def Grequest():
    g = 'gen.html'
    return render_template(g)

@app.route('/api/xcal', methods=["POST"])
def api_xcal():
    data = request.get_json()
    if not data or 'x' not in data:
        return jsonify({"error": "Missing input data"}), 400
    x = data['x']
    pred = models.modelcals100.predict([x])
    return jsonify({"calories": float(pred[0])})

@app.route('/api/xdiab', methods=["POST"])
def api_xdiab():
    data = request.get_json()
    if not data or 'x' not in data:
        return jsonify({"error": "Missing input data"}), 400
    x = data['x']
    pred = models.daib_model.predict([x])
    if pred[0] == 0:
        result = "Diabetes Positive"
    else:
        result = "Diabetes Negative"
    return jsonify({"prediction": result})

@app.route('/api/xlng', methods=["POST"])
def api_xlng():
    data = request.get_json()
    if not data or 'x' not in data:
        return jsonify({"error": "Missing input data"}), 400
    x = data['x']
    pred = models.lng_model.predict([x])
    if pred[0] == 1:
        result = "Lung Cancer Positive"
    else:
        result = "Lung Cancer Negative"
    return jsonify({"prediction": result })

@app.route("/api/request_market", methods=["POST", "GET"])
def wall():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing request data"}), 400
    # Process the market request here
    return jsonify({"wall": data})

@app.route("/api/Grequest", methods=["POST", "GET"])
def generalreq():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing request data"}), 400
    # Process the general request here
    return jsonify({"wall": data})

# === nlp ===
@app.route("/api/ask", methods=["GET"])
def ask():
    user_input = request.args.get('question')
    if not user_input:
        return jsonify({"error": "Missing question parameter."}), 400

    response = chatbot_response(user_input)
    return jsonify({"answer": response})

if __name__ == "__main__":
    app.run(debug=True)
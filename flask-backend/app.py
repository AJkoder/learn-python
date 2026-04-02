from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/test", methods=["POST"])
def test_post():
    data = request.get_json()
    
    return jsonify({
        "received": data
    })
 
if __name__ == "__main__":
    app.run(debug=True)
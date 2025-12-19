from flask import Flask, request, jsonify
from model import recommend_influencers

app = Flask(__name__)

@app.route("/recommend", methods=["GET"])
def recommend():
    niche = request.args.get("niche")
    results = recommend_influencers(niche)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify
from algorithms import find_route
from data import CAMPUS_GRAPH, LOCATIONS

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", locations=LOCATIONS)

@app.route("/api/campus")
def campus():
    return jsonify(CAMPUS_GRAPH)

@app.route("/api/route", methods=["POST"])
def route():
    payload = request.get_json(silent=True) or {}
    start = payload.get("start")
    goal = payload.get("goal")
    algorithm = payload.get("algorithm", "dijkstra")
    accessible = bool(payload.get("accessible", False))

    if start not in CAMPUS_GRAPH["nodes"] or goal not in CAMPUS_GRAPH["nodes"]:
        return jsonify({"error": "Please select valid starting and destination locations."}), 400
    if start == goal:
        return jsonify({"error": "Starting point and destination must be different."}), 400
    if algorithm not in ("dijkstra", "astar"):
        return jsonify({"error": "Unsupported algorithm."}), 400

    result = find_route(CAMPUS_GRAPH, start, goal, algorithm, accessible)
    if not result["path"]:
        return jsonify({"error": "No route found for the selected accessibility settings."}), 404
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)

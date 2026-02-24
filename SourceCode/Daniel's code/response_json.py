from flask import jsonify

def create_response(signal, confidence):
    return jsonify({
        "signal": signal,
        "confidence": confidence
    })

# this file defines helper functions to create JSON responses for the API

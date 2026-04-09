import os
from flask import Flask, jsonify

app = Flask(__name__)

# Security headers configuration
@app.after_request
def set_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    return response

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "message": "Service is operational"}), 200

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"data": "Secure information retrieved successfully."}), 200

if __name__ == "__main__":
    # Ensure development server is only bound to localhost and debug is off by default
    debug_mode = os.environ.get("FLASK_DEBUG", "False").lower() in ["true", "1", "t"]
    app.run(host="127.0.0.1", port=5000, debug=debug_mode)
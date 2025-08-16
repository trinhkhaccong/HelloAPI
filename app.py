import os
import logging
from flask import Flask, jsonify, render_template
from flask_cors import CORS

# Configure logging for debugging
logging.basicConfig(level=logging.DEBUG)

# Create the Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key")

# Enable CORS for cross-origin requests
CORS(app)

@app.route('/')
def index():
    """Serve the main frontend page"""
    return render_template('index.html')

@app.route('/api/hello', methods=['GET'])
def hello_api():
    """API endpoint that returns a hello message"""
    try:
        response_data = {
            "message": "hello",
            "status": "success"
        }
        app.logger.info("Hello API endpoint accessed successfully")
        return jsonify(response_data), 200
    except Exception as e:
        app.logger.error(f"Error in hello API: {str(e)}")
        error_response = {
            "message": "Internal server error",
            "status": "error"
        }
        return jsonify(error_response), 500

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        "message": "Endpoint not found",
        "status": "error"
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        "message": "Internal server error",
        "status": "error"
    }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

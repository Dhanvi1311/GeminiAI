from flask import Flask, request, jsonify
import os
from google.cloud import aiplatform

# Initialize Flask app
app = Flask(__name__)

# Initialize AI Platform
aiplatform.init()

@app.route('/generate', methods=['POST'])
def generate_text():
    prompt = request.json.get('prompt')
    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400

    # Set the API key as an environment variable
    os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

    # Initialize the Gemini model
    model = aiplatform.gapitlm.Model(
        endpoint='https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=AIzaSyD-DjVFxOjc7J6UHDKVAFUh92A8m7qNTUs'
    )

    # Generate text using the model
    response = model.predict(prompt)
    return jsonify({'text': response.text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

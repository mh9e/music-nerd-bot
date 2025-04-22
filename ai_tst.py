from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

# Flask setup
ai_tst = Flask(__name__)
CORS(ai_tst)

# Gemini AI setup
genai.configure(api_key="AIzaSyDrZpS7TEgnVfxoHby8SxivEbm_k3jr6dQ")  # Replace with your real Gemini API key
model = genai.GenerativeModel("gemini-2.0-flash")

@ai_tst.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('prompt')

    if not user_message:
        return jsonify({'error': 'No message received'}), 400

    try:
        response = model.generate_content(user_message)
        return jsonify({'response': response.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    ai_tst.run(host='0.0.0.0', port=5000)

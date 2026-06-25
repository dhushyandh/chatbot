import os
from flask import Flask, request, jsonify
from flask_cors import CORS

from chatbot import get_chat_response


app = Flask(__name__)
CORS(app)


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json() or {}
    message = data.get('message', '')
    if not message:
        return jsonify({"response": "Please send a message."})

    # Use the chatbot module to generate a response
    try:
        response = get_chat_response(message)
    except Exception as e:
        response = "Sorry, an internal error occurred while generating a reply."
        app.logger.exception('Chat handler error')

    return jsonify({"response": response})


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

from flask import Flask, request, jsonify
from flask_cors import CORS
import main as elena_logic # Importing your main.py as a module

# === INITIALIZATION ===
# This creates the web server application
app = Flask(__name__)
# CORS is a security feature that allows your front-end to talk to this back-end
CORS(app) 

# === API ROUTE ===
# This defines the URL that the front-end will send requests to.
# It's set to handle POST requests, which is how the front-end sends the user's command.
@app.route('/process', methods=['POST'])
def process_command():
    """
    This function receives the spoken command from the front-end,
    sends it to your Elena logic for processing, and returns the response.
    """
    # 1. Get the data sent from the front-end
    data = request.get_json()
    
    # 2. Extract the command text. If it's not found, default to an empty string.
    command = data.get('command', '')

    # 3. Check if the command is empty
    if not command:
        print("Received an empty command.")
        return jsonify({'response': 'Sorry, I did not hear anything.'})

    print(f"Received command: '{command}'")

    # 4. Call the processCommand function from your main.py file
    # This is where your assistant's logic is executed.
    response_text = elena_logic.processCommand(command)
    
    print(f"Sending response: '{response_text}'")

    # 5. Return the response back to the front-end in JSON format
    return jsonify({'response': response_text})

# === RUN THE SERVER ===
# This block makes the server run when you execute the script directly.
if __name__ == '__main__':
    # debug=True allows the server to auto-reload when you make code changes.
    # It also provides helpful error messages.
    # The server will be accessible at http://127.0.0.1:5000
    app.run(debug=True, port=5000)

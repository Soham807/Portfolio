from flask import Flask, jsonify
import tyy
# Initialize Flask app
app = Flask(__name__)

# Define a route to return a string
@app.route('/red2', methods=['GET'])
def get_string():
    print("Function executed successfully!")
    tyy.ty()
    print("Function executed successfully!2")

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=5162)

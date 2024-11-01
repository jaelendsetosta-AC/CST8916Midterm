# Import necessary modules from Flask
# Flask: the core framework for the web app
# jsonify: to convert Python dictionaries to JSON responses
# request: to access incoming request data (e.g., POST data)
# abort: to handle errors and send error status codes
from flask import Flask, jsonify, request, abort

# Initialize the Flask app
app = Flask(__name__)

# In-memory "database" of users
# This list holds a set of user dictionaries. 
# In a real-world application, this would be replaced by a database such as MySQL, PostgreSQL, or MongoDB.
students = [
    {"ID": 1, "Name": "Alice", "Grade": "85", "Email": "test2@al.ca"},
    {"ID": 2, "Name": "Bob", "Grade": "80", "Email": "test@al.ca"},
]

# Define route to handle requests to the root URL ('/')
@app.route('/')
def index():
    return "Welcome to Flask REST API Demo! Try accessing /users to see all users."


# Route to retrieve all users (GET request)
# When the client sends a GET request to /users, this function will return a JSON list of all users.
# The @ symbol in Python represents a decorator. 
# In this case, @app.route is a Flask route decorator.
# It is used to map a specific URL (route) to a function in your Flask application.
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students), 200  # 200 is the HTTP status code for 'OK'

# Route to retrieve a single user by their ID (GET request)
# When the client sends a GET request to /users/<id>, this function will return the user with the specified ID.
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    # Using a list comprehension to find the user by ID
    student = next((student for student in students if student['ID'] == student_id), None)
    if student is None:
        abort(404)  # If the user is not found, return a 404 error (Not Found)
    return jsonify(student), 200  # Return the user as a JSON object with a 200 status code (OK)

# Route to create a new user (POST request)
# When the client sends a POST request to /users with user data, this function will add the new user to the list.
@app.route('/students', methods=['POST'])
def create_student():
    # If the request body is not in JSON format or if the 'name' field is missing, return a 400 error (Bad Request)
    if not request.json or not 'Name' in request.json:
        abort(400)
    
    # Create a new user dictionary. Assign the next available ID by incrementing the highest current ID.
    # If no users exist, the new ID will be 1.
    new_student = {
        'ID': students[-1]['ID'] + 1 if students else 1,
        'Name': request.json['Name'],  # The name is provided in the POST request body
        'Grade': request.json.get('Grade', "0"),  # The grade is optional; default is 0 if not provided
        'Email': request.json.get('Email', "0")  # The email is optional; default is 0 if not provided
    }
    # Add the new user to the users list
    students.append(new_student)
    return jsonify(new_student), 201  # 201 is the HTTP status code for 'Created'

# Route to update an existing user (PUT request)
# When the client sends a PUT request to /users/<id> with updated user data, this function will update the user.
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    # Find the user by their ID
    student = next((student for student in students if student['ID'] == student_id), None)
    if student is None:
        abort(404)  # If the user is not found, return a 404 error (Not Found)
    
    # If the request body is missing or not in JSON format, return a 400 error (Bad Request)
    if not request.json:
        abort(400)
    
    # Update the user's data based on the request body
    # If a field is not provided in the request, keep the existing value
    student['Name'] = request.json.get('Name', student['Name'])
    student['Grade'] = request.json.get('Grade', student['Grade'])
    student['Email'] = request.json.get('Email', student['Email'])
    return jsonify(student), 200  # Return the updated user data with a 200 status code (OK)

# Route to delete a user (DELETE request)
# When the client sends a DELETE request to /users/<id>, this function will remove the user with that ID.
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students  # Reference the global users list
    # Rebuild the users list, excluding the user with the specified ID
    students = [student for student in students if student['ID'] != student_id]
    return '', 204  # 204 is the HTTP status code for 'No Content', indicating the deletion was successful

# Entry point for running the Flask app
# The app will run on host 0.0.0.0 (accessible on all network interfaces) and port 8000.
# Debug mode is disabled (set to False).
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)
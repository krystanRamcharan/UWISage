from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
CORS(app)

def get_connection():
    return mysql.connector.connect(
        host='localhost',
        database='uwi_sage',
        user='root',
        password='root'
    )

@app.route('/api/hello', methods=['GET'])
def hello():
    return "hello"

@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data['uwiEmail']
    username = data['username']
    password = data['password']

    hashed_pw = generate_password_hash(password)

    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO users (uwi_email, username, password_hash) VALUES (%s, %s, %s)"
        cursor.execute(query, (email, username, hashed_pw))
        conn.commit()
        return jsonify({'message': 'User registered successfully'}), 201
    except mysql.connector.IntegrityError:
        return jsonify({'error': 'Email or username already exists'}), 400
    except Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

@app.route('/api/signin', methods=['POST'])
def signin():
    data = request.get_json()
    email = data['uwiEmail']
    password = data['password']

    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM users WHERE uwi_email = %s"
        cursor.execute(query, (email,))
        user = cursor.fetchone()

        if user and check_password_hash(user['password_hash'], password):
            return jsonify({'message': 'Login successful', 'username': user['username']}), 200
        else:
            return jsonify({'error': 'Invalid credentials'}), 401
    except Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)

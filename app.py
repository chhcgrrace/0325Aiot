import os
from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime
import pytz

app = Flask(__name__)
DB_NAME = 'aiotdb.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    # Create sensors table as requested: id (INTEGER) temp (FLOAT) humid (FLOAT) time (TIMESTAMP)
    c.execute('''
        CREATE TABLE IF NOT EXISTS sensors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            temp FLOAT,
            humid FLOAT,
            time TIMESTAMP,
            metadata TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/sensor', methods=['POST'])
def receive_data():
    data = request.json
    if not data or 'temp' not in data or 'humid' not in data:
        return jsonify({"error": "Invalid data format"}), 400

    temp = data['temp']
    humid = data['humid']
    metadata = str(data.get('metadata', ''))

    # Store time as Taiwan time
    tw_tz = pytz.timezone('Asia/Taipei')
    current_time = datetime.now(tw_tz).strftime('%Y-%m-%d %H:%M:%S')

    try:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute('INSERT INTO sensors (temp, humid, time, metadata) VALUES (?, ?, ?, ?)',
                  (temp, humid, current_time, metadata))
        conn.commit()
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

    return jsonify({"message": "Data stored successfully", "time": current_time}), 201

if __name__ == '__main__':
    # Try to initialize the database before running
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=False)

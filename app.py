from flask import Flask, request, render_template, jsonify
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)

# Set the upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to initialize the SQLite database
def init_db():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS mood_tracker (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mood INTEGER NOT NULL,
                journal TEXT,
                selfie TEXT,
                date_time TEXT NOT NULL
            )
        ''')
        conn.commit()

# Route to display the index.html
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    mood = request.form['mood']
    journal = request.form['journal']
    selfie = request.files.get('selfie')

    # Handle selfie upload
    selfie_filename = None
    if selfie:
        selfie_filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{selfie.filename}"
        selfie.save(os.path.join(app.config['UPLOAD_FOLDER'], selfie_filename))

    # Get the current date and time
    date_time = datetime.now().isoformat()

    # Insert data into the SQLite database
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO mood_tracker (mood, journal, selfie, date_time) VALUES (?, ?, ?, ?)', 
                       (mood, journal, selfie_filename, date_time))
        conn.commit()
    
    return jsonify(success=True)

# Route to fetch mood data
@app.route('/fetch_mood', methods=['GET'])
def fetch_mood():
    mood_data = {}
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT date_time, mood FROM mood_tracker')
        rows = cursor.fetchall()
        
        for row in rows:
            date_time = row[0]
            mood = row[1]
            day = date_time.split("T")[0]  # Get the date part only
            mood_data[day] = mood  # Store the mood for that day

    return jsonify(mood_data)

if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True)
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

API_KEY = "sk_live_51Hc9f2eZvKYlo2C9x8a1b2c3d4e5f6g7"  # hardcoded secret - DO NOT DO THIS

def get_db():
    conn = sqlite3.connect(\"users.db\")
    return conn

@app.route(\"/user\")
def get_user():
    username = request.args.get(\"username\", \"\")
    conn = get_db()
    cur = conn.cursor()
    # SQL injection: string concatenation instead of parameterized query
    query = \"SELECT id, username, email FROM users WHERE username = '\" + username + \"'\"
    cur.execute(query)
    row = cur.fetchone()
    conn.close()
    if row:
        return jsonify({\"id\": row[0], \"username\": row[1], \"email\": row[2]})
    return jsonify({\"error\": \"not found\"}), 404

@app.route(\"/health\")
def health():
    return jsonify({\"status\": \"ok\"})

if __name__ == \"__main__\":
    app.run(host=\"0.0.0.0\", port=5000, debug=True)

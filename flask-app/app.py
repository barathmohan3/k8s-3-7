import os
import psycopg2
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    try:
        conn = psycopg2.connect(
            dbname=os.environ.get("DB_NAME").strip(),
            user=os.environ.get("DB_USER").strip(),
            password=os.environ.get("DB_PASSWORD").strip(),
            host=os.environ.get("DB_HOST").strip(),
            port=os.environ.get("DB_PORT").strip()
        )
        cur = conn.cursor()
        cur.execute("SELECT NOW();")
        result = cur.fetchone()
        cur.close()
        conn.close()
        return f"Hello! DB Time: {result[0]}"
    except Exception as e:
        return f"Error: {e}"

# Ensure the app runs and binds to 0.0.0.0
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
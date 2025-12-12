from flask import Flask, render_template, request
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# MySQL config (XAMPP defaults)
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',        # XAMPP default
    'password': '',        # XAMPP default: empty string
    'database': 'code_converter'
}


def get_db_connection():
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except Error as e:
        print(f"DB Error: {e}")
        return None


def py_to_java(code: str) -> str:
    if not code:
        return ""
    # 70% rules: def/print + basic if/else
    converted = code.replace("def ", "public static void ")
    converted = converted.replace("print(", "System.out.println(")
    converted = converted.replace("if ", "if (")
    converted = converted.replace("else:", "} else {")
    converted = converted.replace(":", ") {")
    converted = converted + "\n}"
    return converted


@app.route('/', methods=['GET', 'POST'])
def index():
    python_code = ""
    java_code = ""

    if request.method == 'POST':
        python_code = request.form.get('code', '')
        java_code = py_to_java(python_code)

        # SAVE to DB (CREATE)
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO conversions (python_code, java_code) VALUES (%s, %s)",
                (python_code, java_code)
            )
            conn.commit()
            cursor.close()
            conn.close()

    return render_template('index.html',
                           python_code=python_code,
                           java_code=java_code)


@app.route('/list')
def list_conversions():
    # READ last 10 conversions
    conversions = []
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM conversions ORDER BY created_at DESC LIMIT 10"
        )
        conversions = cursor.fetchall()
        cursor.close()
        conn.close()
    return render_template('list.html', conversions=conversions)

<<<<<<< HEAD
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

=======

if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> dc06aba (70% done)

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# very simple placeholder converter
def py_to_java(code: str) -> str:
    if not code:
        return ""
    # demo rules: def -> public static void, print() -> System.out.println()
    converted = code.replace("def ", "public static void ")
    converted = converted.replace("print(", "System.out.println(")
    return converted

@app.route("/", methods=["GET", "POST"])
def index():
    java_code = None
    py_code = None
    if request.method == "POST":
        py_code = request.form.get("python", "")
        java_code = py_to_java(py_code)
    return render_template("index.html", py_code=py_code, java_code=java_code)

# simple REST API endpoint
@app.route("/api/convert", methods=["POST"])
def api_convert():
    data = request.get_json(force=True)
    py_code = data.get("code", "")
    java_code = py_to_java(py_code)
    return jsonify({"java": java_code})

@app.route("/list")
def list_conversions():
    # DB not yet connected – placeholder page
    return render_template("list.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


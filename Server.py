from flask import Flask, jsonify, render_template
app = Flask(__name__)


@app.route("/login")
def server_info():
    return jsonify(
        {
            "nombre":"Jose luis",
            "usuario":"jose@gmail.com",
            "clave":"12345"
        }
    )


if __name__ == "__main__":
    app.run(port=8000, host="0.0.0.0", debug=True)
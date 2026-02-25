from flask import Flask

from api.routes.markup import markup_bp

app = Flask(__name__)
app.register_blueprint(markup_bp)

host = "localhost"
port = "8000"


if __name__ == "__main__":
    app.run(debug=True, host=host, port=port)

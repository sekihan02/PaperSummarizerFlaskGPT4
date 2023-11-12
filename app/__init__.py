from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'  # ここでシークレットキーを設定

    # Routes
    from .routes import chat
    app.register_blueprint(chat.bp)

    return app

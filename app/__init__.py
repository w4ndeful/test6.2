from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Реєстрація блюпринтів
    from .posts import posts_bp
    app.register_blueprint(posts_bp)

    # Обробник 404
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("404.html"), 404

    return app

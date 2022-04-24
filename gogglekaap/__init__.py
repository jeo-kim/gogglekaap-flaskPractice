from flask import Flask, render_template

def create_app():
    print('run: create_app()')
    app = Flask(__name__)

    @app.route('/')
    def index():
        app.logger.info('RUN HELLO WORLD')
        return render_template('index.html')

    @app.errorhandler(404)
    def page_404(error):
        return render_template('/404.html'), 404


    return app

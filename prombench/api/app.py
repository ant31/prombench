from flask import Flask, request
from flask_cors import CORS
from prombench.config import GCONFIG
from prombench.exception import PrombenchException
from prombench.api.handlers.errors import render_error
from prombench.api.handlers.request_logging import before_request_log, after_request_log
from prombench.api.flaskapp import FlaskApp


def getvalues():
    jsonbody = request.get_json(force=True, silent=True)
    values = request.values.to_dict()
    if jsonbody:
        values.update(jsonbody)
    return values


class PrombenchApp(FlaskApp):
    from prombench.api.info import info_app

    blueprints = [(info_app, "")]
    before_request_funcs = [before_request_log]
    after_request_funcs = [after_request_log]
    error_handler_funcs = [(PrombenchException, render_error)]


def create_app():
    app = Flask(__name__)
    CORS(app)
    ffapp = PrombenchApp(app)
    # app.logger.addHandler(logging.StreamHandler(sys.stdout))
    # app.logger.setLevel(logging.INFO)
    if GCONFIG.prombench['env'] != 'production':
        ffapp.app.config.from_object('prombench.api.config.DevelopmentConfig')
    else:
        ffapp.app.config.from_object('prombench.api.config.ProductionConfig')

    ffapp.app.logger.info("Start service")
    return ffapp


if __name__ == "__main__":
    application = create_app().app
    application.run(host='0.0.0.0')

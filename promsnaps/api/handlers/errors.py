from flask import jsonify, Response
from promsnaps.exception import PrometheusSnapsException


def errorhandler(context_app):
    def decorator(func):
        @context_app.errorhandler(PrometheusSnapsException)
        def func_wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return func_wrapper

    return decorator


def render_error(error: Exception) -> Response:
    if isinstance(error, PrometheusSnapsException):
        response = jsonify({"error": error.to_dict()})
        response.status_code = error.status_code
    else:
        response = jsonify({"error": str(error)})
        response.status_code = 500
    return response

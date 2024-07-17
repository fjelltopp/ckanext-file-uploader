from flask import Blueprint

file_uploader_js = Blueprint("file_uploader_js", __name__)


def page():
    return "Hello, file_uploader_js!"


file_uploader_js.add_url_rule("/file_uploader_js/page", view_func=page)


def get_blueprints():
    return [file_uploader_js]

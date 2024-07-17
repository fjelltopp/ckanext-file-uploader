import ckan.plugins.toolkit as tk


def file_uploader_js_required(value):
    if not value or value is tk.missing:
        raise tk.Invalid(tk._("Required"))
    return value


def get_validators():
    return {
        "file_uploader_js_required": file_uploader_js_required,
    }

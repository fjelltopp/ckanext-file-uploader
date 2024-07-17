"""Tests for views.py."""

import ckan.plugins.toolkit as tk
import pytest


@pytest.mark.ckan_config("ckan.plugins", "file_uploader_js")
@pytest.mark.usefixtures("with_plugins")
def test_file_uploader_js_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("file_uploader_js.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, file_uploader_js!"

"""Tests for helpers.py."""

import ckanext.file_uploader_js.helpers as helpers


def test_file_uploader_js_hello():
    assert helpers.file_uploader_js_hello() == "Hello, file_uploader_js!"

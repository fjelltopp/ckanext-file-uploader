"""Tests for validators.py."""

import ckan.plugins.toolkit as tk
import pytest

from ckanext.file_uploader_js.logic import validators


def test_file_uploader_js_reauired_with_valid_value():
    assert validators.file_uploader_js_required("value") == "value"


def test_file_uploader_js_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.file_uploader_js_required(None)

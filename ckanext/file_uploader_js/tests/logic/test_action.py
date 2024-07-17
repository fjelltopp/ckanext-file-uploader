"""Tests for action.py."""

import ckan.tests.helpers as test_helpers
import pytest


@pytest.mark.ckan_config("ckan.plugins", "file_uploader_js")
@pytest.mark.usefixtures("with_plugins")
def test_file_uploader_js_get_sum():
    result = test_helpers.call_action("file_uploader_js_get_sum", left=10, right=30)
    assert result["sum"] == 40

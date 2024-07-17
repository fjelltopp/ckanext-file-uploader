"""Tests for auth.py."""

import ckan.model as model
import ckan.tests.factories as factories
import ckan.tests.helpers as test_helpers
import pytest


@pytest.mark.ckan_config("ckan.plugins", "file_uploader_js")
@pytest.mark.usefixtures("with_request_context", "with_plugins", "clean_db")
def test_file_uploader_js_get_sum():
    user = factories.User()
    context = {"user": user["name"], "model": model}
    assert test_helpers.call_auth("file_uploader_js_get_sum", context=context)

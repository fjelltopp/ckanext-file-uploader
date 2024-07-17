import ckan.plugins.toolkit as tk

import ckanext.file_uploader_js.logic.schema as schema


@tk.side_effect_free
def file_uploader_js_get_sum(context, data_dict):
    tk.check_access("file_uploader_js_get_sum", context, data_dict)
    data, errors = tk.navl_validate(data_dict, schema.file_uploader_js_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"],
    }


def get_actions():
    return {
        "file_uploader_js_get_sum": file_uploader_js_get_sum,
    }

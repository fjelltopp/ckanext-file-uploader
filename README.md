[![Tests](https://github.com/fjelltopp/ckanext-file-uploader/actions/workflows/test.yml/badge.svg)](https://github.com/fjelltopp/ckanext-file-uploader/actions/workflows/test.yml)

# ckanext-file-uploader

This CKAN extension provides a javascript enhanced file upload widget for improved UI/X when uploading files to create or update resources.

![visual_readme](visual_readme.gif)

## Compatibility with core CKAN versions

| CKAN version       | Compatible? |
| ------------------ | ----------- |
| v1.0.1 and earlier | not tested  |
| v1.0.2             | v1.0.0      |

## Compatibility with ckanext-fjelltopp-theme versions

| CKAN version    | Compatible?   |
| --------------- | ------------- |
| 2.8 and earlier | not tested    |
| 2.9             | <= v1.0.0     |
| 2.10            | not tested    |
| 2.11            | not tested    |

## Installation

To install ckanext-file-uploader:

1. Activate your CKAN virtual environment, for example:

    ```sh
    . /usr/lib/ckan/default/bin/activate
    ```

2. Clone the source and install it on the virtualenv

    ```sh
    git clone https://github.com/fjelltopp/ckanext-file-uploader.git
    cd ckanext-file-uploader
    pip install -e .
    pip install -r requirements.txt
    ```

3. Install the javascript dependencies (you may need to [install `nvm`](https://github.com/nvm-sh/nvm?tab=readme-ov-file#installing-and-updating) first)

    ```sh
    cd react
    nvm use
    npm clean-install
    npm run build
    ```

4. Add `file_uploader` to the `ckan.plugins` setting in your CKAN config file (by default the config file is located at `/etc/ckan/default/ckan.ini`).
    If you are using `ckanext-fjelltopp-theme` make sure that this extension is rightwards in the list of extensions.

5. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

    ```sh
    sudo service apache2 reload
    ```

## Config settings

None at present


## Developer installation

To install ckanext-file-uploader for development, activate your CKAN virtualenv and
do:

```sh
git clone https://github.com/fjelltopp/ckanext-file-uploader.git
cd ckanext-file-uploader
python setup.py develop
pip install -r dev-requirements.txt
cd react
nvm use
npm install --include=dev
npm run dev
```

## Tests

To run the python tests, do:

```sh
pytest --ckan-ini=test.ini
```

And for the javascript tests:

```sh
cd react
npm run test
```

## License

[AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html)

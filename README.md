# BasicContainerizedAPI

Exposing a basic webapi through its docker container.<br>

This project is an experiment with docker, however it's also worth providing non-docker instructions too, so I will split them into two separate categories.<br>
If you'd like to install and run via a docker container, following the Docker-specific Instructions. If you'd like to install, run, modify, or generate api documentation then follow the General Instructions.


## Docker-specific Instructions ##

These instructions are for running the API within a docker container accessible via port 25005.

1. Install Docker
2. Open a command-line shell and point it at this directory
3. Type `docker-compose up`
4. The API is now accessible via `http://127.0.0.1:25005/`.
5. Refer to documentation on available endpoints, expected arguments, and response format
6. If you made changes run `docker-compose build` and start over from step 1

## General Instructions ##

These instructions are for running the API in flask's built-in development server on port 5000 (by default), as well as general instructions for other tasks.
### Installation ###

1. Install Python and add it to your PATH variable so you can invoke it from a command-line shell
2. Open a command-line shell and point it at this directory
3. (optional) Create a new virtual environment:
    | Windows (cmd prompt) | Mac/Linux |
    | --- | --- |
    | `py -3 -m venv venv` (only once) | `python3 -m venv venv` (only once) |
    | `venv\Scripts\activate` (per shell instance) | `. venv/bin/activate` (per shell instance) |
4. Type `pip install -r requirements.txt`

### Invocation ###

These instructions will start the Flask internal webserver. This is good for development. For deploying to production, refer to Flask's website. This project is not meant to be deployed to production, so you are on your own.

1. Follow the instructions in the 'Installation' section of this README if you haven't already
2. Invoke flask after setting up environment variables:
    <table>
    <tr>
    <td> Windows (cmd prompt) </td> <td> Mac/Linux (bash) </td>
    </tr>
    <tr>
    <td>

    ```
    set FLASK_APP=basicwebapi
    set FLASK_ENV=development
    flask run
    ```

    </td>
    <td>

    ```
    export FLASK_APP=basicwebapi
    export FLASK_ENV=development
    flask run
    ```

    </td>
    </tr>
    </table>
3. The API is now accessible via `http://localhost:5000/`.
4. Refer to documentation on available endpoints, expected arguments, and response format.

### Re-Generating Documentation ###

The provided documentation is generated with [pdoc](https://pdoc.dev/). pdoc looks at python's built-in docstrings to generate most of its documentation. These are special comments that follow module, class, or function definitions:
```py
"""Documentation here"""
```
pdoc also provides a way of documenting variables / fields using the same format. pdoc will interpret these docstrings as markdown (along with some common markdown extensions). Refer to their website for more details. This is not a pdoc tutorial and I am not associated with pdoc in any way.

1. Install pdoc via `pip install pdoc`
2. Generate the documentation via `pdoc basicwebapi`

The above invocation will automatically open your web browser and point it at pdoc's internal webserver. This is good for active development. When finished, export the HTML to the docs folder like this:
1. `pdoc basicwebapi -o ./docs`

### Running Tests ###

This project uses pytest. Each test is contained in a file that begins with `test_` and each test function begins with `test_` as well. Refer to pytest documentation for more info. This is not a pytest tutorial and I am not affiliated with pytest in any way.

1. Install pytest and coverage via `pip install pytest coverage`
2. Run pytest via `pytest`
3. Run coverage via `coverage run -m pytest`
4. See the coverage report via `coverage report` or output to htmlconv/index.html via `coverage html`
# BasicContainerizedAPI
 Exposing a basic webapi through its docker container.

## Installation ##

1. Install Python and add it to your PATH variable so you can invoke it from a command-line shell
2. Open a command-line shell and point it at this directory
3. (optional) Create a new virtual environment:
    | Windows | Mac/Linux |
    | --- | --- |
    | `py -3 -m venv venv` (only once) | `python3 -m venv venv` (only once) |
    | `venv\Scripts\activate` (per shell instance) | `. venv/bin/activate` (per shell instance) |
4. Type `pip install -r requirements.txt`

## Invocation ##

These instructions will start the Flask internal webserver. This is good for development. For deploying to production, refer to Flask's website. This project is not meant to be deployed to production, so you are on your own.

1. Follow the instructions in the 'Installation' section of this README if you haven't already
2. Setup Flask environment variables:
    <table>
    <tr>
    <td> Windows (cmd prompt) </td> <td> Mac/Linux (bash) </td>
    </tr>
    <tr>
    <td>

    ```
    set FLASK_APP=hello
    set FLASK_ENV=development
    flask run
    ```

    </td>
    <td>

    ```
    export FLASK_APP=main.py
    export FLASK_ENV=development
    flask run
    ```

    </td>
    </tr>
    </table>
3. The API is now accessible via `http://localhost:5000/`.
4. Refer to documentation on available endpoints, expected arguments, and response format.

## Re-Generating Documentation ##

The provided documentation is generated with [pdoc](https://pdoc.dev/). pdoc looks at python's built-in docstrings to generate most of its documentation. These are special comments that follow module, class, or function definitions:
```py
"""Documentation here"""
```
pdoc also provides a way of documenting variables / fields using the same format. pdoc will interpret these docstrings as markdown (along with some common markdown extensions). Refer to their website for more details. This is not a pdoc tutorial and I am not associated with pdoc in any way.

1. Install pdoc via `pip install pdoc`
2. Generate the documentation via `pdoc ./main.py`

The above invocation will automatically open your web browser and point it at pdoc's internal webserver. This is good for active development. When finished, export the HTML to the docs folder like this:
1. `pdoc ./main.py -o ./docs`
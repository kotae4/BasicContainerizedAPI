# BasicContainerizedAPI

Exposing a basic webapi through its docker container.<br>

This project is an experiment with docker and so requires running it through docker. Instructions for this as well as other general tasks like re-generating documentation or running unit tests are provided below.
## How-To Run ##

These instructions are for running the API within a docker container accessible via port 25005 along with a MariaDB server in a separate container that the API must communicate with.

1. Install Docker
2. Open a command-line shell and point it at this directory
3. Type `docker-compose up`
4. The API is now accessible via `http://127.0.0.1:25005/`.
5. Refer to documentation on available endpoints, expected arguments, and response format

Note: The entire project directory is mounted via a bind mount so if a change is made on the host system it will be reflected within the api container as well. Still, once you're happy with whatever changes you've made it would make sense to shut the containers down and rebuild the basicwebapi image.
Anoter note: The MariaDB container exposes port 3306 so you can connect to it from your host machine using whatever mysql client you want. The basicwebapi itself uses docker's internal networking to connect, so if you don't want it exposed you can remove the port mapping from the docker-compose file.

## How-To Deploy ##

This isn't meant for production. Dev-mode features are pretty built-in. You're on your own.

## How-To Re-Generate Documentation ##

The provided documentation is generated with [pdoc](https://pdoc.dev/). pdoc looks at python's built-in docstrings to generate most of its documentation. These are special comments that follow module, class, or function definitions:
```py
"""Documentation here"""
```
pdoc also provides a way of documenting variables / fields using the same format. pdoc will interpret these docstrings as markdown (along with some common markdown extensions). Refer to their website for more details. This is not a pdoc tutorial and I am not associated with pdoc in any way.

1. Install pdoc via `pip install pdoc`
2. Generate the documentation via `pdoc basicwebapi !basicwebapi.db`

The above invocation will automatically open your web browser and point it at pdoc's internal webserver. This is good for active development. When finished, export the HTML to the docs folder like this:
1. `pdoc basicwebapi !basicwebapi.db -o ./docs`

## How-To Re-Generate requirements.txt ##

1. Install pipreqs via `pip install pipreqs`
2. Generate requirements.txt via `pipreqs . --force`
3. (optional) Add the coverage dependency manually: `coverage==6.4.1` at the end of the requirements.txt file

At some point it'd make sense to shut your containers down and re-build the basicwebapi image, but because of the bind mount this isn't entirely necessary.

## How-To Run Tests ##

This project uses pytest. Each test is contained in a file that begins with `test_` and each test function begins with `test_` as well. Refer to pytest documentation for more info. This is not a pytest tutorial and I am not affiliated with pytest in any way.

1. Open a shell in the webapi container and type `bash`
2. Run pytest via `pytest`
3. Run coverage via `coverage run -m pytest`
4. See the coverage report via `coverage report` or output to htmlconv/index.html via `coverage html`

## How-To Install locally (without docker) ##

This isn't meant to run outside of docker. You may have to change some things in the code. I have not tested it locally so I do not know.<br>
In general, here's what I would expect needs to be done:
1. Install a MariaDB Server locally (or provision one on a remote server) and create a database named `basicwebapi`
2. Install MariaDB C connectors for the MariaDB python lib
3. Install Python and add it to your PATH variable so you can invoke it from a command-line shell
4. Open a command-line shell and point it at this directory
5. (optional) Create a new virtual environment:
    | Windows (cmd prompt) | Mac/Linux |
    | --- | --- |
    | `py -3 -m venv venv` (only once) | `python3 -m venv venv` (only once) |
    | `venv\Scripts\activate` (per shell instance) | `. venv/bin/activate` (per shell instance) |
6. Type `pip install -r requirements.txt`

## How-To Run locally (without docker) ##

Again, this isn't meant to run outisde of docker. Some changes to the code may be necessary, but here's what I'd expect:<br>
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
    set BASICWEBAPI-SETTINGS=basicwebapi-settings.cfg
    flask init-db
    flask run
    ```

    </td>
    <td>

    ```
    export FLASK_APP=basicwebapi
    export FLASK_ENV=development
    export BASICWEBAPI-SETTINGS=basicwebapi-settings.cfg
    flask init-db
    flask run
    ```

    </td>
    </tr>
    </table>
3. The API is now accessible via `http://localhost:5000/`.
4. Refer to documentation on available endpoints, expected arguments, and response format.

Note: these instructions will start the Flask internal webserver. This is good for development. For deploying to production, refer to Flask's website. This project is not meant to be deployed to production, so you are on your own.
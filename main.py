"""A basic WebAPI for experimenting with docker containers"""
from flask import Flask
from flask import request

app = Flask(__name__);

class _ResponseObject:
    status = -1;
    body = "Unknown Error";

    def __init__(self, _status = -1, _body = "Unknown Error"):
        self.status = _status;
        self.body = _body;

    def ToObject(self):
        return { "status": self.status, "body": self.body};

@app.route('/math')
def math():
    """**/math?leftOperand={integer}&rightOperand={integer}&operation={add|subtract|multiply|divide}**<br>
    *Expects integers to be whole numbers.*<br>
    **Response Schema (JSON):** { "status": {integer}, "body": {integer|string} }<br>
    **Status codes:**<br>
    **400** - indiciates an error. The "body" field is a string containing the detailed error message.<br>
    **200** - indicates a success. The "body" field is an integer containing the result of the operation.<br>
    """
    try:
        leftOperand = request.args.get("leftOperand", type=int);
        rightOperand = request.args.get("rightOperand", type=int);
    except ValueError:
        return _ResponseObject(400, "Bad operands. Expected to be a whole integer.").ToObject();

    operation = request.args.get("operation", type=str);

    if ((leftOperand == None) or (rightOperand == None) or (operation == None)):
        return _ResponseObject(400, "Missing arguments. Expected 'leftOperand', 'rightOperand', and 'operation'. Refer to documentation.").ToObject();

    # now just check the operation arg and perform the associated calculation
    # or error if it does not match any supported operations
    result = 0;
    try:
        if (operation == 'add'):
            result = leftOperand + rightOperand;
        elif (operation == 'subtract'):
            result = leftOperand - rightOperand;
        elif (operation == 'multiply'):
            result = leftOperand * rightOperand;
        elif (operation == 'divide'):
            result = leftOperand / rightOperand;
        else:
            return _ResponseObject(400, "Bad operation. Expected 'add', 'subtract', 'multiply', or 'divide'.").ToObject();
    except (ArithmeticError, MemoryError):
        return _ResponseObject(400, "Calculation impossible with provided operands.").ToObject();

    return _ResponseObject(200, result).ToObject();
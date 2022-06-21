"""Tests the math API endpoint"""
from basicwebapi import create_app

def test_math(client):
    # missing operand
    response = client.get("/math");
    respJSON = response.get_json();
    assert respJSON is not None;
    assert respJSON["status"] == 400;

    # missing operand
    response = client.get("/math?leftOperand=3");
    respJSON = response.get_json();
    assert respJSON is not None;
    assert respJSON["status"] == 400;

    # missing operand
    response = client.get("/math?leftOperand=3&operation=add");
    respJSON = response.get_json();
    assert respJSON is not None;
    assert respJSON["status"] == 400;

    # the good case
    response = client.get("/math?leftOperand=3&operation=add&rightOperand=1");
    respJSON = response.get_json();
    assert respJSON is not None;
    assert respJSON["status"] == 200;
    assert respJSON["body"] == 4;

    # division by zero
    response = client.get("/math?leftOperand=3&operation=divide&rightOperand=0");
    respJSON = response.get_json();
    assert respJSON is not None;
    assert respJSON["status"] == 400;

    # unsupported operation
    response = client.get("/math?leftOperand=3&operation=unsupported&rightOperand=1");
    respJSON = response.get_json();
    assert respJSON is not None;
    assert respJSON["status"] == 400;

    # bad format for operand (float, expects int)
    response = client.get("/math?leftOperand=3.14159&operation=add&rightOperand=1");
    respJSON = response.get_json();
    assert respJSON is not None;
    assert respJSON["status"] == 400;

    # bad format for operand (string, expects int)
    response = client.get("/math?leftOperand=3&operation=add&rightOperand=hello");
    respJSON = response.get_json();
    assert respJSON is not None;
    assert respJSON["status"] == 400;

    # bad format for operand (empty, expects int)
    response = client.get("/math?leftOperand=3&operation=add&rightOperand=");
    respJSON = response.get_json();
    assert respJSON is not None;
    assert respJSON["status"] == 400;
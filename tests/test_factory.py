"""Tests the __init__ module"""
from basicwebapi import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing
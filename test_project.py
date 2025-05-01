import pytest
from project import get_response, is_greeting, is_farewell

def test_greetings():
    assert get_response("hi") in ["Hello!", "Hi there!", "Hey, how can I help you?"]
    assert get_response("hello") in ["Hello!", "Hi there!", "Hey, how can I help you?"]

def test_farewells():
    assert get_response("bye") in ["Goodbye!", "See you later!", "Take care!"]
    assert get_response("goodbye") in ["Goodbye!", "See you later!", "Take care!"]

def test_how_are_you():
    assert get_response("how are you") in [
        "I'm doing well, thank you!",
        "I'm great, how about you?",
        "Doing fine, how can I assist you?"
    ]

def test_chatbot_name():
    assert get_response("what is your name") == "I am Chatbot, your virtual assistant!"

def test_help():
    assert get_response("help") == "I can chat with you, answer your basic questions, and more. Try asking about my name or how I'm doing!"

def test_unknown_input():
    assert get_response("blah blah") == "Sorry, I didn't understand that. Can you ask something else?"

def test_is_greeting():
    assert is_greeting("hi") is True
    assert is_greeting("howdy friend") is True
    assert is_greeting("bye") is False

def test_is_farewell():
    assert is_farewell("goodbye") is True
    assert is_farewell("see you soon") is True
    assert is_farewell("hello") is False

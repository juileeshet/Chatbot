import pytest
from project import get_response

def test_greetings():
    assert get_response("hi") in ["Hello!", "Hi there!", "Hey, how can I help you?"]
    assert get_response("hello") in ["Hello!", "Hi there!", "Hey, how can I help you?"]

def test_farewells():
    assert get_response("bye") in ["Goodbye!", "See you later!", "Take care!"]
    assert get_response("goodbye") in ["Goodbye!", "See you later!", "Take care!"]

def test_how_are_you():
    assert get_response("how are you") in ["I'm doing well, thank you!", "I'm great, how about you?", "Doing fine, how can I assist you?"]

def test_chatbot_name():
    assert get_response("what is your name") == "I am Chatbot, your virtual assistant!"

def test_help():
    assert get_response("help") == "I can chat with you, answer your basic questions, and more. Try asking about my name or how I'm doing!"

def test_unknown_input():
    assert get_response("blah blah") == "Sorry, I didn't understand that. Can you ask something else?"

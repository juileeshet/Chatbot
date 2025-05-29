Have you ever wanted to create your own personal assistant—something simple, fun, and interactive? That’s exactly what this project is about. I built a basic chatbot using Python that you can talk to through the command line. While it’s not Siri or Alexa, it’s a small step into the world of conversational AI.

The chatbot responds to simple user inputs like “hi,” “bye,” “how are you,” or even “what’s your name?” It’s friendly, polite, and always ready to chat. If it doesn’t understand something, it politely lets you know and encourages you to try asking something else. The main purpose here was to learn how to process user input and give meaningful responses using Python’s logic and structure.

The core of the project revolves around two main components: the main() function, which handles the interaction loop, and the get_response() function, which checks the user’s input and picks an appropriate reply. To keep things lively, the chatbot doesn’t just repeat the same thing every time—it randomly chooses a response from a small list, making each conversation feel a bit more dynamic.

To make sure everything works as expected, I also wrote a few unit tests using pytest. These tests check whether the chatbot replies correctly to various types of inputs like greetings, farewells, and general questions. It was a great way to learn more about writing clean, testable code.

While this chatbot doesn’t use machine learning or understand natural language deeply, it’s a fun and educational project that taught me a lot about basic programming, user interaction, and program structure. In the future, I’d love to expand on this by giving the chatbot a memory, connecting it to a web interface using Flask, or even trying out simple AI techniques.

In short, this project is my way of exploring how computers can “talk” to us, even in a very basic form. It’s a small but exciting step into the world of interactive programming and AI.

FEATURES

Responds to greetings like "hi", "hello", etc.
Responds to farewells like "bye", "see you", etc.
Answers simple questions like "how are you?" or "what is your name?"
Provides help information
Responds with a default message for unknown inputs

TECHNOLOGIES

Python 3

pytest for unit testing

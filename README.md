# AI API Comparison
This project is intended to act as a framework for evaluating the quality of AI-powered API's, with simple code designed to automate such a task written in python. \
A full writeup document with more detail (including evaluaiton criteria) is included in this repository as well. \
The findings will be incorporated into [my discord bot](https://github.com/REALBRICKD/discord-gemini-bot), though the findings can easily be applied elsewhere. \
When run, the program adds every API to be tested to a list, and has them respond to the list of prompts found in prompts.txt. Additional methods for continuous conversation have also been programmed. \

# Production and Design
This project's heart includes Main.py and the test implementation (testImplementation.py). \
There is a parent class for all the openrouter APIs as they are all attached to one API key and initialized the same way, as well as using the same logic. \
A separate helper has been made for Google Gemini, as it has a separate key and different configuration. \
A range of example prompts can be found in prompts.txt. 

# Running the program
This project is not designed to be run in its current state, though assuming you have an openrouter key and a Google Gemini key...\
* Clone the repo as normal.
* Create a .env file
* Within that .env file, insert:
  * > GEMINI_API_KEY = "Your key here"
  * > OPENROUTER_API_KEY = "Your key here"
* Once authenticated, the program should run all the prompts through all the included APIs.

# Roadmap
The design of this project allows easy addition of more APIs and prompts, with the ability to hold continuous conversation or responding to a list of prompts. I plan to test more APIs such as OpenAI's ChatGPT and Anthropic's Claude. \
The test results can influence development of any project involving any such APIs, or even if one wanted to make their own custom API. 

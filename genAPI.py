#Imports
import os
import pip
import requests

from google import genai
from google.genai import types

#API Keys
API_KEY = ""

# General API superclass
class GenAPI:
    key = ""
    headers = None
    client = None
    prompt = ""
    history = []

    def __init__(self, API_KEY):
        self.key = API_KEY
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }
        self.headers = headers

    def respond(self, prompt):
        pass
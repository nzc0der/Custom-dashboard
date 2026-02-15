import random

class QuoteService:
    def __init__(self):
        self.quotes = [
            {"text": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
            {"text": "Innovation distinguishes between a leader and a follower.", "author": "Steve Jobs"},
            {"text": "Your time is limited, so don't waste it living someone else's life.", "author": "Steve Jobs"},
            {"text": "Stay hungry, stay foolish.", "author": "Steve Jobs"},
            {"text": "Make it simple, but significant.", "author": "Don Draper"},
            {"text": "Design is not just what it looks like and feels like. Design is how it works.", "author": "Steve Jobs"}
        ]

    def get_random_quote(self):
        return random.choice(self.quotes)

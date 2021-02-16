import pandas as pd

class DataHistory:

    def __init__(self, data):
        self.data = data
        self.history = {}

    def add(self, commit):
        self.history[commit.name] = self.data.copy()

    def checkout(self, name):
        return(self.history[name])

    def log(self):
        return(self.history.keys())

    
class Commit:

    def __init__(self, name):
        self.name = name
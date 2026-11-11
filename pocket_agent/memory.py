
class Memory:
    def __init__(self):
        self.data = {}

    def remember(self, key, value):
        """Store information in memory."""
        self.data[key] = value

    def recall(self, key):
        """Retrieve information from memory."""
        return self.data.get(key, "I don't remember that.")

    def show_all(self):
        """Display everything stored in memory."""
        return self.data

    


print("Hello")

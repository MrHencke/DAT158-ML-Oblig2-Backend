class prediction:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        
    def serialize(self):
        return {
            "key": self.key,
            "data": self.data
        }
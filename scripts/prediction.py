class Prediction:
    """
    Constructor for the Prediction class.
    """
    def __init__(self, key, data):
        self.key = key
        self.data = data
        
    def serialize(self):
        """
        Serializes input to JSON-compatible key-value pairs.
        
        Returns:
            (Dict): A dict of key (label) and data (value) from input.
        """
        return {
            "key": self.key,
            "data": self.data
        }
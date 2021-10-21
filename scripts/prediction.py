class prediction:
    def __init__(self, item, score):
        self.item = item
        self.score = score
        
    def serialize(self):
        return {
            "item": self.label,
            "score": self.score
        }
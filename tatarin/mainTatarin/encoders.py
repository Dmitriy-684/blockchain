import json


class TheoryEncoder(json.JSONEncoder):
    def default(self, obj):
        return {"Topic": obj.topic,
                "Content": obj.content,
                "Bonus": obj.bonus}
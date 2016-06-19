from json_serializer import JsonSerializer

test_object = [
    {
        'a': 5,
        'b': [1, 2]
    },
    {
        'smth': {
            "true": True,
            "nothing": None
        },
        'any_number': 12.78
    }
]


with open('result.json', 'w+') as f:
    f.write(JsonSerializer().to_json(test_object))

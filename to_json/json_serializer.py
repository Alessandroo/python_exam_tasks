class JsonSerializer(object):
    def __init__(self, indent_size=4):
        self.TAB = ' ' * indent_size

    def to_json(self, obj, indentation=0):
        indent_string = self.TAB * indentation
        if isinstance(obj, bool):
            return str(obj).lower()
        elif isinstance(obj, (int, float)):
            return str(obj)
        elif isinstance(obj, str):
            return '"{}"'.format(obj)
        elif obj is None:
            return 'null'
        elif isinstance(obj, (list, set)):
            obj_string = ',\n'.join(['{indent}{content}'
                .format(indent=self.TAB * (indentation + 1),
                        content=self.to_json(item, indentation + 1))
                 for item in obj])

            return ('[\n{content}\n{indent}]'
                .format(indent=self.TAB * indentation, content = obj_string))
        elif isinstance(obj, dict):
            obj_string = ',\n'.join(['{indent}"{key}": {value}'
                .format(indent=self.TAB * (indentation + 1),
                        key=key,
                        value=self.to_json(obj[key], indentation + 1))
                for key in obj])

            return ('{{\n{content}\n{indent}}}'
                .format(indent=self.TAB * indentation, content = obj_string))
        else:
            raise TypeError()

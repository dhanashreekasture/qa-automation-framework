from jsonschema import validate, ValidationError


class Validator:

    SCHEMA = {
        "type": "object",
        "properties": {
            "medicine": {"type": "string"},
            "price": {"type": "number"},
            "quantity": {"type": "number", "minimum": 1}
        },
        "required": ["medicine", "price", "quantity"]
    }

    @staticmethod
    def validate(data):
        errors = []

        try:
            validate(instance=data, schema=Validator.SCHEMA)
        except ValidationError as e:
            errors.append(e.message)

        return errors
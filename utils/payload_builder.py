import json


class PayloadBuilder:

    META_FIELDS = {"scenario_id", "test_case_id"}

    @staticmethod
    def build(data: dict) -> dict:
        payload = {
            k: PayloadBuilder._convert_type(v)
            for k, v in data.items()
            if k not in PayloadBuilder.META_FIELDS and not k.startswith("expected")
            and k != "payload_override"
        }
        override = data.get("payload_override")

        if override:
            try:
                override_dict = json.loads(override)
                payload.update(override_dict)
            except Exception as e:
                raise Exception(f"Invalid payload_override JSON: {e}")

        return payload

    @staticmethod
    def _convert_type(value):
        if value is None:
            return None
        try:
            return int(value)
        except:
            pass
        try:
            return float(value)
        except:
            pass
        return value
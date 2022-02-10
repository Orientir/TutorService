from django.core.serializers.json import DjangoJSONEncoder, Serializer as JsonSerializer

class Serializer(JsonSerializer):
    def _init_options(self):
        super()._init_options()
        self.json_kwargs["cls"] = CustomJsonEncoder


class CustomJsonEncoder(DjangoJSONEncoder):
    def default(self, obj):
        return super().default(obj)
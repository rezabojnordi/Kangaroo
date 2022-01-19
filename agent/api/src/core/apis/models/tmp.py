from flask_restx import fields
from flask_restx import Api
import flask_restx

api = Api(
    version="1.0.1",
    title="Baloot Turbo Wordpress Middleware API",
    description="The infrastructure's middleware API list which WUI backend can interact with",
    validate=True,
)

class Modes():
    """
    TBA
    """

    # Modes values
    MODE_REQ = 1
    MODE_RES = 2
    MODE_ADMIN = 4
    MODE_DB = 8

    @staticmethod
    def validMode(value):
        maxAllowed = 0
        try:
            for k, v in Modes.__dict__.items():
                if "MODE_" in k:
                    maxAllowed |= v
            return (value > 0 and value <= maxAllowed)
        except:
            return False


class ExpandedField():
    """
    TBA
    """

    def __init__(self, name, field_type=fields.Raw, model_mode=Modes.MODE_REQ, required=False, description="", example="", pattern=None) -> None:
        """TBA"""
        self.name = name
        self.type = field_type
        self.modelMode = model_mode
        self.required = required
        self.description = description
        self.example = example
        self.pattern = pattern
        if not Modes.validMode(model_mode):
            raise Exception(f"Mode '{model_mode}' is not valid!")

    def getModelFieldObject():
        pass

a = ExpandedField('username', fields.Integer)

def foo(name, field_type=fields.String, mode=Modes.MODE_REQ):
    if (mode & Modes.MODE_REQ):
        pass
    if (mode & Modes.MODE_ADMIN):
        pass
    return {name: field_type()}


fields_list = []
fields_list.append(foo('name'))
fields_list.append(foo('pass'))
fields_list.append(foo('yoyo'))


def bar(field_list):
    if not isinstance(field_list, list):
        return None
    result = {}
    for f in field_list:
        for k, v in f.items():
            result[k] = v
    if len(result.keys()) != len(field_list):
        return None
    return result


a = {'a': 1, "b": 2}
t = api.model('test', bar(fields_list))
# print (t)


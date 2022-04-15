import strawberry

from mysk_utils.schema import Person


@strawberry.experimental.pydantic.type(model=Person, all_fields=True)
class People:
    pass

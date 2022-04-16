import strawberry

from mysk_utils.schema import Person, Contact
from mysk_utils.schema.people.contacts import _ContactType
from mysk_utils.schema.people.person import _ThaiPrefix, _EnglishPrefix


@strawberry.experimental.pydantic.type(model=Contact)
class ContactType:
    type: strawberry.enum(_ContactType)
    value: strawberry.auto
    name: strawberry.auto


@strawberry.experimental.pydantic.type(model=Person)
class PersonType:
    id: strawberry.auto
    first_name_th: strawberry.auto
    middle_name_th: strawberry.auto
    last_name_th: strawberry.auto
    first_name_en: strawberry.auto
    middle_name_en: strawberry.auto
    last_name_en: strawberry.auto
    birthdate: strawberry.auto
    citizen_id: strawberry.auto
    contact: strawberry.auto
    prefix_th: strawberry.enum(_ThaiPrefix)
    prefix_en: strawberry.enum(_EnglishPrefix)

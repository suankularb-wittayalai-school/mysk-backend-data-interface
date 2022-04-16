import strawberry
from .people import PersonType


@strawberry.type
class Query:
    @strawberry.field
    def health_check(self, info) -> bool:
        return True

    @strawberry.field
    def get_person(self, info, id: int) -> PersonType:
        person = PersonType(
            id=id,
            first_name_th="สมชาย",
            last_name_th="สมหญิง",
            first_name_en="Somchai",
            last_name_en="Somchai",
            prefix_th="นาง",
            prefix_en="Ms.",
            birthdate="2000-01-01",
            citizen_id="1234567890123",
        )
        return person

import strawberry


@strawberry.type
class Query:
    @strawberry.field
    def health_check(self, info) -> bool:
        return True

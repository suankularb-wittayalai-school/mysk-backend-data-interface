from fastapi import FastAPI, Response, status
import strawberry
from strawberry.fastapi import GraphQLRouter


# from starlette.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import uvicorn
import os

from mysk_utils.response import InternalCode
from schema.query import Query

load_dotenv()

app = FastAPI()

schema = strawberry.Schema(query=Query)
graphql_router = GraphQLRouter(schema)

app.include_router(graphql_router, prefix="/graphql")


@app.get(
    "/", status_code=status.HTTP_200_OK, response_description="Welcome to MySK API"
)
def health_check(response: Response):
    response.headers["X-Internal-Code"] = str(InternalCode.IC_GENERIC_SUCCESS.value)
    return {"status": True}


if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host=os.environ.get("HOST"),
        port=int(os.environ.get("PORT")),
        log_level="info",
        reload=True,  # reload on code changes
    )

from fastapi import FastAPI
from salesforce_sdk import IntegrationAsgiMiddleware, client_context

app = FastAPI()
app.add_middleware(IntegrationAsgiMiddleware)

@app.get("/helloworld")
async def hello(input: str):
        cctx = client_context.get()
        print("DataAPI:", cctx.data_api)
        print("Org:", cctx.org)
        return "hello, world!"
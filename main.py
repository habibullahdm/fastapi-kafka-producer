import uvicorn
from dotenv import dotenv_values
from fastapi import FastAPI

from api.router import api_router as api_router_v1
from consumer.kafka_consumer import init_kafka_consumer, run_consumer
from producer.kafka_producer import init_kafka_producer

app = FastAPI()
app.include_router(api_router_v1, prefix="/v1")
config = dotenv_values(".env")

init_kafka_producer()
init_kafka_consumer()
run_consumer()

if __name__ == "__main__":
    uvicorn.run("main:app", host=config["HOST_URL"], port=int(config["HOST_PORT"]))

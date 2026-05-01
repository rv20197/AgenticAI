from fastapi import FastAPI, Query
from .client.rq_client import queue
from .queues.worker import process_query

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/chat")
async def chat(query: str = Query(..., description="The chat query of user")):
    job = queue.enqueue(process_query, query)
    return {"status": "queued", "job_id": job.id}

async def get_result(jobId: str = Query(...,description="Job Id")):
    job = queue.fetch_job(job_id=jobId)

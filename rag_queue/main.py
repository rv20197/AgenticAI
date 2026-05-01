from .server import app
import uvicorn
from dotenv import load_dotenv

load_dotenv()

def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)

main()

# {
#   "status": "queued",
#   "job_id": "2c957829-0b2a-49ac-85ab-5b9f9544a3f1"
# }
from server import app
import uvicorn
from dotenv import load_dotenv

load_dotenv()

def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)

main()

# {
#   "status": "queued",
#   "job_id": "cd1f413b-167a-49b6-ac45-189234efe99e"
# }
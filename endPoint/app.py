from fastapi import FastAPI, Query
from datetime import datetime
import pytz

app = FastAPI()

@app.get("/info")
async def get_info(
    slack_name: str = Query(None),
    track: str = Query(None)
):

    current_day = datetime.now(pytz.utc).strftime("%A")
    utc_time = datetime.utcnow().isoformat() + 'Z'

    github_file_url = "https://github.com/username/repo/blob/main/main.py"
    github_repo_url = "https://github.com/username/repo"

    return {
        "slack_name": slack_name,
        "current_day": current_day, 
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }
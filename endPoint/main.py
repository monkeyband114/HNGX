from fastapi import FastAPI
from datetime import datetime
import pytz

app = FastAPI()

@app.get("/api")
async def get_info(
    slack_name: str = "michaelvoke",
    track: str = "backend"
):

    current_day = datetime.now(pytz.utc).strftime("%A")
    utc_time = datetime.utcnow().isoformat() + 'Z'

    github_file_url = "https://github.com/monkeyband114/HNGX/blob/1ea309610467cfb46447c752a617bd5e5fd2c6cc/endPoint/app.py"
    github_repo_url = "https://github.com/monkeyband114/HNGX.git"

    return {
        "slack_name": slack_name,
        "current_day": current_day, 
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }
    
    
    
"""App Python main file that runs FastAPI"""

from datetime import datetime

from pytz import timezone

from fastapi import FastAPI

from app_python.src import config


app = FastAPI()


@app.get("/")
async def get_time():
    """Provides current Moscow time on main route"""
    time = datetime.now(timezone(config.TIMEZONE))
    return {"current_time": time.strftime(config.TIME_FORMAT)}

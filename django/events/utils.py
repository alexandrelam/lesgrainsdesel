def formatTime(db_time: str) -> str:
    return str(db_time)[:10] + "T" + str(db_time)[11:16]

from fastapi import FastAPI

app = FastAPI()
tasks = list()


@app.get("/")
def index() -> dict[str, str]:
    return {"message": "Hello, World"}

@app.get("/task")
def get_all_task() -> dict:
    if len(tasks) == 0:
        return {"Message": "No task available"}
    return {"Task": tasks}
""" main project file """
from fastapi import FastAPI

app = FastAPI()
tasks = list()


@app.get("/")
def index() -> dict[str, str]:
    """ Display a message to test that everything is correct

    Returns:
        dict[str, str]: Dictionary with values ​​(key and value) of type strings
    """
    return {"message": "Hello, World"}

@app.get("/task")
def get_all_task() -> list:
    """list all stored tasks

    Returns:
        list: list of stored tasks
    """
    if len(tasks) == 0:
        return {"Message": "No task available"}
    return tasks
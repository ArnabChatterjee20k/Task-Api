from flask import Blueprint, request, abort , make_response , jsonify
task = Blueprint("task",__name__)
from api.Models.Task import Task

@task.get("/")
def get_task():
    return Task.read_all_task()

@task.post("/")
def create_task():
    data = request.json
    if not data:
        abort(403)
    task_name = data.get("name")
    Task.create_task(task_name)
    
    response = jsonify({"status":"Successfull"})
    return make_response(response,200)

@task.get("/<id>")
def get_single_task(id):
    task = Task.query.get_or_404(id)
    response = jsonify({
        "id":task.id,
        "name":task.name,
        "status":task.status
    })
    return make_response(response,200)

@task.put("/<id>")
def update_task(id):
    data = request.json
    if not data:
        abort(403)

    task = Task.query.get_or_404(id)
    print([data.get("status")])
    Task.update_task(task,data)

    response = jsonify({
        "status":"successful"
    })
    return make_response(response,200)

@task.delete("/<id>")
def delete_task(id):
    previous_task = Task.query.get_or_404(id)
    Task.delete(previous_task)

    response = jsonify({"status":"Task Deleted"})
    return make_response(response,200)

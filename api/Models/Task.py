from api import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    status = db.Column(db.Boolean, default=False)

    @staticmethod
    def update_task(previous_task,new_task):
        """
            previous_task - task object
            new_task - the new task dictionary
        """
        if(new_task.get("name")):
            previous_task.name = new_task.get("name")
        
        # since the status is bool so if false appeared and we do .get() the if statement will not execute so using membership
        if("status" in new_task):
            previous_task.status = new_task.get("status")

        db.session.commit()
    
    @staticmethod
    def delete(task):
        """
            task - task object
        """
        db.session.delete(task)
        db.session.commit()
    
    @staticmethod
    def _add_to_db(object):
        """
            An abstracted method
            object - the object which needs to be inserted to db
        """
        db.session.add(object)
        db.session.commit()

    @staticmethod
    def read_all_task():
        """
            a serialiser function to converts every sqlalchemy object to json equivalent
        """
        def to_json(unserialised_object):
            return {
                'id':unserialised_object.id,
                'name': unserialised_object.name,
                'status': unserialised_object.status,
            }
        
        return {'tasks': list(map(lambda x: to_json(x), Task.query.all()))}
    
    @staticmethod
    def create_task(task_name):
        """
            task_name - the name of the task
        """
        task = Task(name = task_name)
        Task._add_to_db(task)
from app import db


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    completed_at = db.Column(db.DateTime, nullable = True, default = None)
    goal_id = db.Column(db.Integer, db.ForeignKey("goal.goal_id"), nullable = True)
    goal = db.relationship("Goal", back_populates = "tasks")

    @classmethod
    def from_dict(cls, task_data):
        new_task = Task(title = task_data["title"], description = task_data["description"], completed_at = None)
        return new_task

    def to_dict(self):
        task_dict = {}
        task_dict["id"] = self.task_id
        task_dict["title"] = self.title
        task_dict["description"] = self.description
        task_dict["is_complete"] = bool(self.completed_at)
        task_dict["goal_id"] = self.goal_id

        return task_dict
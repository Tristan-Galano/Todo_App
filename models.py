import app
from datetime import datetime

class Task(app.db.Model):
    id = app.db.Column(app.db.Integer(), primary_key=True)
    name = app.db.Column(app.db.String(140))
    date = app.db.Column(app.db.DateTime(), default=datetime.now())
    completed = app.db.Column(app.db.Boolean(), default=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f'<Task id:{self.id} - {self.name}'

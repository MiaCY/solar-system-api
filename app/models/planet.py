from app import db


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    color = db.Column(db.String)

    def to_dict(self):
        return dict(
            id= self.id,
            name = self.name,
            description = self.description,
            color = self.color)


# planets = [
#     Planet(1,"Earth","big","blue/green"),
#     Planet(2,"Mars","smaller","red"),
#     Planet(3,"Venus","a little bigger","gold")]
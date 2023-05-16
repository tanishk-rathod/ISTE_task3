from __main__ import db

class Register(db.Model):
    S_no = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80), primary_key=False, nullable=False)
    Email = db.Column(db.String(50), nullable=False)
    Phone = db.Column(db.Integer, primary_key=False, nullable=False)
    College = db.Column(db.String(50), primary_key=False, nullable=True)
    City = db.Column(db.String(50), primary_key=False, nullable=False)
    State = db.Column(db.String(50), primary_key=False, nullable=False)
    No_of_members = db.Column(db.Integer, primary_key=False, nullable=False)
    # DateTime = db.Column(db.String(12),primary_key=False,nullable=True)

class Contact(db.Model):
    S_no = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(50), nullable=False)
    Email = db.Column(db.String(50), nullable=False)
    Phone = db.Column(db.String(50), nullable=False)
    Subject = db.Column(db.String(50), nullable=False)
    Message = db.Column(db.String(200), nullable=False)
    # DateTime = db.Column(db.String(12),primary_key=False,nullable=True)
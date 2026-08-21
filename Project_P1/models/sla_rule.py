from extensions import db


class SlaRule(db.Model):
    __tablename__ = "sla_rules"

    id = db.Column(db.Integer, primary_key=True)
    priority = db.Column(db.String(20), unique=True, nullable=False)
    response_time_hours = db.Column(db.Integer, nullable=False)
    resolution_time_hours = db.Column(db.Integer, nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)

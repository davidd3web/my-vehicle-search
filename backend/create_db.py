from app import db, app  # Importing app as well

with app.app_context():
    db.create_all()

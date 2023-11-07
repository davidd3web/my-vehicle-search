from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, UserInput 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db.init_app(app)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    all_data = UserInput.query.all()
    return jsonify({'data': [{ 'make': item.make, 'model': item.model, 'price': item.price, 'email': item.email, 'anyModel': item.anyModel } for item in all_data]})

@app.route('/api/save', methods=['POST'])
def save_data():
    data = request.json
    print(data)
    make = data.get('make', '')
    model = data.get('model', '')
    price = data.get('price')
    email = data.get('email')
    anyModel = data.get('anyModel', False)

    if anyModel:
        model = None

    new_input = UserInput(make=make, model=model, price=price, email=email, anyModel=anyModel)
    db.session.add(new_input)
    db.session.commit()
    return jsonify({'message': 'Data saved.'})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Blueprint, jsonify,request,render_template
from models import User,Order,db,Image
import base64
join_routes = Blueprint('join', __name__)

@join_routes.route('/users/orders', methods=['GET'])
def get_users_orders():
    query = db.session.query(User,Order).join(Order, User.id == Order.user_id).all()

    # Convert the join query results to a list of dictionaries
    result = []
    for User_row,Order_row in query:
        binary_data =User_row.data
        base64_image =base64.b64encode(binary_data).decode('utf-8')
        results={
            'name': User_row.username,
            'contact': User_row.email,
            'age':User_row.age,
            'amount': Order_row.amount,
            'id':User_row.id,
            'location':User_row.location,
            'phone':User_row.phone,
            'image':base64_image 
        }
        result.append(results)
        
    # return jsonify(result)
    return render_template('details.html',result=result)


@join_routes.route('/getall')
def get_users():
    users = db.session.query(User,Order).all()
    result = []
    for user1,Order_row in users:
        binary_data =user1.data
        base64_image =base64.b64encode(binary_data).decode('utf-8')
        result.append({
            'name': user1.username,
            'contact':user1.email,
            'id':user1.id,
            # 'user_id':Order_row.user_id,
            'amount':Order_row.amount,
            'age':user1.age,
            'image':base64_image
        })
    # return jsonify(result)
    return render_template('index.html',result=result)


@join_routes.route('/users/<id>', methods=['GET'])
def get_user(id):   
    user = db.session.query(User).get(id)
    result=[]
    if user:
        result.append({
            'id': user.id,
            'name': user.username,
            'contact': user.email,
            'age':user.age,
            
        })
        # return jsonify(result)
    return render_template('id.html',result=result)



@join_routes.route('/adduser', methods=['POST'])
def create_user():
    data = request.get_json()
    # Create a new user
    new_user = User(username=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}),201


@join_routes.route('/update/<id>', methods=['PUT'])
def update_user(id):
    user = db.session.query(User).get(id)
    if user:
        data = request.get_json()
        user.username = data['name']
        user.email = data['email']
        db.session.commit()
        return jsonify({'message': 'User updated successfully'}),200
    return jsonify({'message': 'User not found'}), 404

@join_routes.route('/delete/<id>', methods=['DELETE'])
def delete_user(id):
    user = db.session.query(User).get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'}), 200
    return jsonify({'message': 'User not found'}), 404


@join_routes.route('/complexquery',methods=['GET'])
def complex_query():
    query=db.session.query(User,Order).join(Order,User.id ==Order.user_id).filter(User.username == 'dhinesh kumar', Order.amount > 100).all()
    result=[]
    for User_row,Order_row in query:
        result.append({
            'username':User_row.username,
            'email':User_row.email,
            'amount':Order_row.amount,
            'id':User_row.id,
            'age':User_row.age
        })
    return jsonify (result)


@join_routes.route('/complexquery2',methods=['GET'])
def complex_query2():
    query=db.session.query(User,Order).join(Order,User.id ==Order.user_id).filter(User.email=="dhinesh@imcrinox.com",Order.amount.between(1, 100000)).all()
    result=[]
    for User_row,Order_row in query:
        result.append({
            'username':User_row.username,
            'email':User_row.email,
            'amount':Order_row.amount,
            'id':User_row.id
        })
    return jsonify (result)

@join_routes.route('/complexquery3',methods=['GET'])
def complex_query3():
    query=db.session.query(User,Order).join(Order,User.id ==Order.user_id).filter(User.age>=20).order_by(User.age).all()
    result = []
    for user_row,order in query:
        result.append({
            'username':user_row.username,
            'age':user_row.age
        })
    return jsonify(result)

@join_routes.route('/orderdetails',methods=['GET'])
def orderdetails():
    query = db.session.query(User,Order).join(Order, User.id == Order.user_id).all()
    result=[]
    for user_row,order_row in query:
        result.append({
            'id':order_row.id,
            'amount':order_row.amount
        })
    return jsonify(result)

@join_routes.route('/image',methods=['GET'])
def Imagedetails():
    query=db.session.query(Image).all()
    result=[]
    for image_row in query:
        binary_data =image_row.data
        base64_image =base64.b64encode(binary_data).decode('utf-8')
        result.append({
            'id':image_row.id,
            'name':image_row.name,
            'image':base64_image
        })
    # return jsonify(result)
    return render_template('image.html',result=result)

@join_routes.route('/registered_users', methods=['GET'])
def get_registered_users():
    subquery = db.session.query(User.id).filter(User.registration_status == 1).subquery()

    query = db.session.query(User).filter(User.id.in_(subquery))

    result = []
    for user in query:
        result.append({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'registration_status': user.registration_status
        })

    return jsonify(result)
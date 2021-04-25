from flask import Flask, render_template, jsonify, request, session, redirect, url_for
import pymongo
from bson import ObjectId
from bson.json_util import dumps, loads
import os
from werkzeug.utils import secure_filename

#se crea copnexion a base datos
myClient = pymongo.MongoClient("mongodb://admin-rentapp:rentapp12345@rentapp-shard-00-00.iqoc1.mongodb.net:27017,rentapp-shard-00-01.iqoc1.mongodb.net:27017,rentapp-shard-00-02.iqoc1.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-viqn5b-shard-0&authSource=admin&retryWrites=true&w=majority")
#se crea base de datos
myDB = myClient["rentApp"]
#se crean colecciones
apartmentsCollection = myDB["apartments"]
onwerCollection = myDB["onwer"]
userCollection = myDB["user"]

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './static/img/uploads'
app.secret_key = 'werwetwryteurturtrtyrtyrtyQQy4613874'


@app.route('/user', methods=['GET'])
def user():
    result = userCollection.find()
    if result:
        list_data = list(result)
        json_data = dumps(list_data)
        return json_data
    else:
        return jsonify({'status':'404'})

@app.route('/user/<id>',methods=['GET'])
def user_by_id(id):
            query = {"_id": ObjectId(id)}
            result = userCollection.find_one(query)
            if result:
                json_data = dumps(result)
                return json_data
            else:
                return jsonify({'status':'404'})

@app.route('/user/<id>',methods=['DELETE'])
def delete_user(id):
        query = {"_id": ObjectId(id)}
        delete = userCollection.delete_one(query)
        if delete:
            return jsonify({'status':'200'})
        else:
            return jsonify({'status':'400'})


@app.route('/user', methods=['POST'])
def send_user():
    
    name = request.json['name']
    ident =request.json['identification']
    email = request.json['email']
    country = request.json['country']
    city = request.json['city']
    password = request.json['password']
    user = {"name": name, "ident":ident, "email": email , "country": country, "city": city, "password":password}
    save = userCollection.insert_one(user)
    if save:
        return jsonify({"status": "200"})
    else:
        return jsonify({"status": "400"})

@app.route('/user/<id>', methods=['PUT'])
def up_user(id):
        query = {"_id": ObjectId(id)}
        name = request.json['name']
        ident =request.json['identification']
        email = request.json['email']
        country = request.json['country']
        city = request.json['city']
        password = request.json['password']
        user = {"$set":{"name": name, "ident":ident, "email": email,"country": country, "city": city, "password":password}}
        update = userCollection.update_one(query, user)
        if update:
            return jsonify({"status": "200"})
        else:
            return jsonify({"status": "400"})
     
# # #esquema y rutas de propietarios



@app.route('/onwer/', methods=['GET'])
def onwer():
    result = onwerCollection.find()
    if result:
        list_data = list(result)
        json_data = dumps(list_data)
        return json_data
    else:
        return jsonify({'status':'404'})


@app.route('/onwer/<id>',methods=['GET'])
def onwer_by_id(id):
        query = {"_id": ObjectId(id)}
        result = onwerCollection.find_one(query)
        if result:
            json_data = dumps(result)
            return json_data
        else:
            return jsonify({'status':'404'})


@app.route('/onwer/<id>',methods=['DELETE'])
def delete_onwer(id):
        query = {"_id": ObjectId(id)}
        delete = onwerCollection.delete_one(query)
        if delete:
            return jsonify({'status':'200'})
        else:
            return jsonify({'status':'400'})

@app.route('/onwer', methods=['POST'])
def send_onwer():
    name = request.json['name']
    ident =request.json['identification']
    email = request.json['email']
    country = request.json['country']
    city = request.json['city']
    password = request.json['password']
    user = {"name": name, "ident":ident, "email": email , "country": country, "city": city, "password":password}
    save = onwerCollection.insert_one(user)
    if save:
        return jsonify({"status": "200"})
    else:
        return jsonify({"status": "400"})



@app.route('/onwer/<id>', methods=['PUT'])
def up_onwer(id):
        query = {"_id": ObjectId(id)}
        name = request.json['name']
        ident =request.json['identification']
        email = request.json['email']
        country = request.json['country']
        city = request.json['city']
        password = request.json['password']
        user = {"$set":{"name": name, "ident":ident, "email": email,"country": country, "city": city, "password":password}}
        update = onwerCollection.update_one(query, user)
        if update:
            return jsonify({"status": "200"})
        else:
            return jsonify({"status": "400"})




# @app.route('/onwer-apartment/<id>',methods=['GET'])
# def onwer_apartment(id):
#         query = {"_id": ObjectId(id)}
#         result = apartmentsCollection.find_one(query)
#         if result:
#             return render_template("onwer-apartment.html", data = result)
#         else: 
#             return render_template("404.html")

# # #esquema y rutas de apartamentos


@app.route('/apartment/', methods=['GET'])
def apartment():
    result = apartmentsCollection.find()
    if result:
        list_data = list(result)
        json_data = dumps(list_data)
        return json_data
    else:
        return jsonify({'status':'404'})   


@app.route('/apartment/<id>',methods=['GET'])
def apartment_by_id(id):
        query = {"_id": ObjectId(id)}
        result = apartmentsCollection.find_one(query)
        if result:
            json_data = dumps(result)
            return json_data
        else:
            return jsonify({'status':'404'})


@app.route('/delete-apartment/<id>',methods=['DELETE'])
def delete_apartment(id):
        query = {"_id": ObjectId(id)}
        delete = apartmentsCollection.delete_one(query)
        if delete:
            return jsonify({'status':'200'})
        else:
            return jsonify({'status':'400'})



@app.route('/apartment', methods=['POST'])
def send_apartment():
    name = request.json['title']
    idonwer = request.json['idonwer']
    location = request.json['location']
    assessment = 1
    country = request.json['country']
    city = request.json['city']
    address = request.json['address']
    nigth_value = request.json['nigth_value']
    review = request.json['review']
    apartment = {"idonwer": idonwer, "name":name, "address": address, "assessment": assessment, "location": location, "country": country, "city": city, "nigth_value":nigth_value, "review":review}
    save = apartmentsCollection.insert_one(apartment)
    if save:
        return jsonify({"status": "200"})
    else:
        return jsonify({"status": "400"})



@app.route('/apartment/<id>', methods=['PUT'])
def up_apartment(id):
    query = {"_id": ObjectId(id)}
    name = request.json['title']
    idonwer = request.json['idonwer']
    location = request.json['location']
    assessment = 1
    country = request.json['country']
    city = request.json['city']
    address = request.json['address']
    nigth_value = request.json['nigth_value']
    review = request.json['review']
    apartment = {"$set":{"idonwer": idonwer, "name":name, "address": address, "assessment": assessment, "location": location, "country": country, "city": city, "nigth_value":nigth_value, "review":review}}
    update = apartmentsCollection.update_one(query, apartment)
    if update:
        return jsonify({"status": "200"})
    else:
        return jsonify({"status": "400"})


# @app.route('/signinuser', methods=['POST'])
# def signinuser():
#     user = request.form.get('email')
#     status = "E"
#     password = request.form.get('password')
#     query = {"email":user, "password": password}
#     result = userCollection.find_one(query)
#     if result:
#         session['user'] = str(result['_id']) 
#         session['name'] = result['name']
#         session['type'] = "user"
#         return redirect(url_for("homeuser"))
#     else:
#         return render_template("signin.html", status = status)

# @app.route('/signinonwer', methods=['POST'])
# def signinonwer():
#     user = request.form.get('emailPrio')
#     status = "E"
#     password = request.form.get('passwordPrio')
#     query = {"email":user, "password": password}
#     result = onwerCollection.find_one(query)
#     if result:
#         session['user'] = str(result['_id']) 
#         session['name'] = result['name']
#         session['type'] = "onwer"
#         return redirect(url_for('homeonwer'))
#     else:
#         return render_template("signin.html", status = status)


if __name__ == '__main__':
    app.run(debug=True, port=8001)

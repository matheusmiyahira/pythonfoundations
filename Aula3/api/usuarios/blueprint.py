from flask import Blueprint, request, Response
from config import db
from bson.json_util import dumps

usuarios_route = Blueprint('usuarios_route',__name__, url_prefix='/usuarios')

@usuarios_route.route('/',methods=['POST'])
def insert_user():
    try:
        user = request.get_json()
        db.user.insert_one(
            {
                'name' : user['name'],
                'email' : user['email'],
                'messages' : []
            }
        )
        response = {'messages':f'Usuario {user["name"]}, criado com sucesso!'}
        return Response(dumps(user), status=200)
    except Exception as e:
        error = {'error':e}
        return Response(dumps(error), status=500)

@usuarios_route.route('/', methods=['GET'])
def get_user():
    try:
        user = db.user.find()
        return Response(dumps(user), status=200)
    except Exception as e:
        error = {'error':e}
        return Response(dumps(error), status=500)


@usuarios_route.route('/',methods=['PATCH'])
def update_user():
    try:
        user = request.get_json()
        update = db.user.updat_one(
            {
                'email' : user['email'],
                '$set' : user
            }
        )
        if update.modified_count:
            response = {'message':f'Usuario {user["name"]}, atualizado com sucesso'}
            return Response(dumps(response), status=200)
        if update.matched_count:
            response = {'message':f'Usuario {user["name"]}, econtrado, porem nao modificado.'}
            return Response(dumps(response), status=304)
        else:
            response = {'message':f'Usuario {user["name"]}, nao econtrado.'}
            return Response(dumps(response), status=503)
    except Exception as e:
        error = {'error':e}
        return Response(dumps(error), status=500)

@usuarios_route.route('/',methods=['DEETE'])
def delete_user():
    try:
        user = request.get_json()
        update = db.user.delete_one(
            {
                'email':user['email']
            }
        )
        if update.deleted_count:
            response = {'message':f'Usuario {user["name"]}, deletado com sucesso.'}
            return Response(dumps(response), status=200)
        else:
            response = {'message':f'Usuario {user["name"]}, nao econtrado.'}
            return Response(dumps(response), status=503)
    except Exception as e:
        error = {'error':e}
        return Response(dumps(error), status=500)






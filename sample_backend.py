from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)

users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}

@app.route('/')
def hello_world():
   return "Hello, world!"

@app.route('/users', methods=['GET', 'POST'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get("name")
      search_job = request.args.get("job")
      if search_username and search_job:
         subdict = {"users_list" : []}
         for user in users["users_list"]:
            if user["name"] == search_username and user["job"] == search_job:
               subdict["users_list"].append(user)
         return subdict
      elif search_username:
         subdict = {"users_list" : []}
         for user in users["users_list"]:
            if user["name"] == search_username:
               subdict["users_list"].append(user)
         return subdict
      return users
   elif request.method == 'POST':
      userToAdd = request.get_json()
      users['users_list'].append(userToAdd)
      resp = jsonify(success=True)
      resp.status_code = 200
      return resp

@app.route('/users/<id>', methods=['GET', 'DELETE'])
def get_user(id):
   if id:
      for user in users['users_list']:
         if user["id"] == id:
            if request.method == 'GET':
               return user
            elif request.method == 'DELETE':
               users['users_list'].remove(user)
      return ({})
   return users
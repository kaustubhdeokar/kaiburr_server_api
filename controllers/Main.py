from controllers.modules import *

class ServerHandler(RequestHandler):
    """
    Creates a new server
    """

    def set_default_headers(self):
        print("setting headers!!!")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers",
                        "*")
        self.set_header('Access-Control-Allow-Methods', ' PUT, DELETE, GET, OPTIONS')

    def put(self):
        body = json.loads(self.request.body)
        db['servers'].insert_one({
            'name': body['name'],
            'id': body['id'],
            'language': body['language'],
            'framework': body['framework']
        })
        self.write(json.dumps({
            'status': 201,
            'message': 'server id '+body['id'] + ' successfully'
        }))

    def delete(self):
        id = self.get_argument('id')
        message = "successfully deleted"
        status = 202
        try:
            db['servers'].delete_one({
                'id': id
            })
        except:
            status = 503
            message = "id not registered"
        self.write(json.dumps({
            'status': status,
            'message': message
        }))

    @coroutine
    def get(self):
        id = self.get_query_arguments('id')
        if len(id)==0:

            servs = db['servers'].find({}, {'_id':0}).to_list(None)
        else:
            print("here")
            servs = db['servers'].find_one({'id': id[0]}, {'_id': 0})
        servs = yield servs
        if(servs==None):
            status = 404
            message = "no servers"

            self.write(json.dumps({
                'status': status,
                'message': message
            }))
            return
        status = 200
        message = "success"
        self.write(json.dumps({
            'status': status,
            'message': message,
            'servers': servs
        }))


    def options(self):
        self.set_status(204)

    def write_error(self, status_code, **kwargs):
        jsonData = {
            'status': int(status_code),
            'message': "Internal server error"
        }
        self.write(json.dumps(jsonData))


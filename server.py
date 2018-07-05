from bottle import post, put, route, run, request, response, Bottle, static_file
import json
logCollection = []
app = Bottle()

@app.hook('after_request')
def enable_cors():
    """
    You need to add some headers to each request.
    Don't use the wildcard '*' for Access-Control-Allow-Origin in production.
    """
    print("enable_cors")
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
    return response

# @app.route('/')
# def index():
#     return "no response"
#
@app.route('/logview', method=["GET"]) 
def logview():
    print(request.headers)
    print( { key : value for key,value in request.headers.items()})
    return static_file("index.html",root="./")


@app.route('/log', method=["GET"])
def logget():
    print( { key : value for key,value in request.headers.items()})
    return json.dumps(logCollection)
#
#
# @app.post('/log')
# def logpost():
#     eho = { key:value for (key,value) in request.params.items() }
#     return {'echo':eho} 
#
# @app.route('/log',method=["POST"])
# def logput():
#     eho = json.loads(list(request.params.keys())[0] )
#     if eho['log'] :
#         logCollection.append(eho['log'])
#     return {'echo':eho, 'logCollection':len(logCollection)} 

@app.route('/log', method=["POST","OPTIONS"])
def logoptions():
    print( { key : value for key,value in request.headers.items()})
    if request.method == "OPTIONS":
        return 'h'
    if request.method == "POST":
        # eho = json.loads(list(request.params.keys())[0] )
        # if eho['log'] :
        #     logCollection.append(eho['log'])
        # return {'echo':eho, 'logCollection':len(logCollection)} 
        return 'o'
    return ''

run(app, port=8881, debug=False)

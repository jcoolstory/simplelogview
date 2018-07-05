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

@app.route('/log', method=["GET"]) 
def logview():
    return static_file("index.html",root="./")


@app.route('/log', method=["POST"])
def logget():
    return json.dumps(logCollection)

@app.route('/log', method=["POST","OPTIONS"])
def logoptions():
    if request.method == "OPTIONS":
        return 'h'
    if request.method == "POST":
        eho = json.loads(list(request.params.keys())[0] )
        if eho['log'] :
            logCollection.append(eho['log'])
        return {'echo':eho, 'logCollection':len(logCollection)} 
        # return 'o'
    return ''

run(app, port=8881, debug=False)

#!flask/bin/python
from flask import Flask, jsonify, request, abort, make_response

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

sendPinResp = [{'resultCode':0, 'resultDesc':1}]

@app.route('/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})



@app.route('/api/hubmx/sendPIN', methods=['POST'])
def send_pin_json():
   
    print request.data 
    return jsonify({'result': True})
    '''
    if request.json:
	return jsonify({sendPinREsp})
    else: 
	abort(404)
'''
	

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)

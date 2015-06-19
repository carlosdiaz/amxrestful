#!flask/bin/python
from flask import Flask, jsonify, request, abort, make_response, Response
from xml.etree import ElementTree as ET

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

sendPinRespXML = """<?xml version="1.0" ?>
<!DOCTYPE message SYSTEM "/home/jinny/bin/ems.dtd">
<resultCode>1</resultCode>
<resultDesc>None</resultDesc>
"""


@app.route('/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})



@app.route('/api/hubmx/sendPIN', methods=['POST'])
def send_pin_json():
   
    #print request.data 
    root = ET.fromstring(request.data)
    #root = tree.getroot()
    for child in root:
    	print child.tag, child.attrib

    element = root.find('msisdn')

    if element is None:
    	print "element not found"

    else:
    	print element.text

    return Response(sendPinRespXML, mimetype='text/xml')
    
	

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0', debug=True)

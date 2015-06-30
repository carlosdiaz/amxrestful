#!flask/bin/python
from flask import Flask, jsonify, request, abort, make_response, Response
from xml.etree import ElementTree as ET

app = Flask(__name__)

sendPinResp = [{'resultCode':0, 'resultDesc':1}]


sendPinRespXML = """<?xml version="1.0" encoding="ISO-8859-1"?><soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><soapenv:Body>
<sendPINResponse xmlns="http://www.csapi.org/schema/parlayx/sendpin/v1_0/local">
<resultCode>0</resultCode>
<resultDesc>Success.</resultDesc>
</sendPINResponse>
</soapenv:Body>
</soapenv:Envelope"""





@app.route('/api/hubmx/sendPIN', methods=['POST'])
def send_pin_json():
   
    #print request.data 
    #root = ET.fromstring(request.data)

    if validateRequestSendPin(request.data):
    #element = tree.findall('msisdn')
    	return Response(send_pin_response(True), mimetype='text/xml')
    else:
	return Response(send_pin_response(False), mimetype='text/xml')

    	


def validateRequestSendPin(xml):
    
    root = ET.fromstring(xml)
    for child in root:
        #print child.tag, child.attrib, child.text
        for child1 in child:
                #print child1.tag, child1.attrib, child1.text
                for child2 in child1:
                        #print child2.tag
			if child2.tag == "{http://www.csapi.org/schema/parlayx/sendpin/v1_0/local}msisdn":
				#print "Msisdn found"
				return True
    #print "Msisdn Not found"
    return False


@app.route('/api/hubmx/confirmPIN', methods=['POST'])
def confirm_pin_json():
    return "<resultCode>0</resultCode>"


def send_pin_response(success): 
    if success:
    	return """<?xml version="1.0" encoding="ISO-8859-1"?><soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><soapenv:Body>
<sendPINResponse xmlns="http://www.csapi.org/schema/parlayx/sendpin/v1_0/local">
<resultCode>0</resultCode>
<resultDesc>Success.</resultDesc>
</sendPINResponse>
</soapenv:Body>
</soapenv:Envelope"""
    else:
    	return """<?xml version="1.0" encoding="ISO-8859-1"?><soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><soapenv:Body>
<sendPINResponse xmlns="http://www.csapi.org/schema/parlayx/sendpin/v1_0/local">
<resultCode>1</resultCode>
<resultDesc>Failure.</resultDesc>
</sendPINResponse>
</soapenv:Body>
</soapenv:Envelope"""




@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0', debug=True)

import sys
import httplib
from datetime import datetime


#Request for SendPin method

hostname = "127.0.0.1"
uri = "api/hubmx/sendPIN"
port = 5000

starttime = datetime.now()

print "Start Time: " + str(starttime)


request_xml = """<?xml version="1.0" encoding="ISO-8859-1"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" 
xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:ns8156="http://tempuri.org">
<SOAP-ENV:Header>
<tns:RequestSOAPHeader xmlns:tns="http://www.huawei.com/schema/osg/common/v2_1"><tns:AppId>N</tns:AppId>
<tns:TransId>2015062300100779801</tns:TransId><tns:OA></tns:OA><tns:FA></tns:FA></tns:RequestSOAPHeader>
<wsse:Security xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
<wsse:UsernameToken xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">
<wsse:Username>XXX</wsse:Username>
<wsse:Password Type="...#PasswordDigest">XXX</wsse:Password>
<wsse:Nonce>XXX</wsse:Nonce><wsse:Created>2015-06-23T00:10:07Z</wsse:Created></wsse:UsernameToken></wsse:Security>
</SOAP-ENV:Header>
<SOAP-ENV:Body>
<sendPIN xmlns="http://www.csapi.org/schema/parlayx/sendpin/v1_0/local">
<msisdn>12345678</msisdn>
<productID>123456</productID>
</sendPIN>
</SOAP-ENV:Body>
</SOAP-ENV:Envelope>"""



print "Request: "+request_xml

webservice = httplib.HTTP(hostname + ":" + str(port))
webservice.putrequest("POST", uri)
webservice.putheader("Content-type", 'text/xml; charset="ISO-8859-1"')
webservice.putheader("Content-length", str(len(request_xml)))
webservice.endheaders()
webservice.send(request_xml)

statuscode, statusmessage, header = webservice.getreply()

responsetime = datetime.now()

total_time = responsetime - starttime

print "Response: ", statuscode, statusmessage
print "headers: ", header
print webservice.getfile().read()

print "Response Time: "+str(responsetime)

print "Total Time: "+str(total_time.microseconds)


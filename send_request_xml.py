import sys
import httplib
from datetime import datetime


hostname = "127.0.0.1"
uri = "api/hubmx/sendPIN"
port = 5000

starttime = datetime.now()

print "Start Time: " + str(starttime)


request_xml =  """<?xml version="1.0" ?>
<!DOCTYPE message SYSTEM "/home/jinny/bin/ems.dtd">
<sendpin>
<msisdn>123456</msisdn>
<productid>9876543</productid>
</sendpin>"""

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


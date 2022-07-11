# XML and JSON are two most common ways to send data over the internet?
# XML - eXtensible Markup Language : Tags, Attributes, Serialize & De-Serialize
# XML Schema - Description of the legal format of an XML document.
# XSD is the W3C Schema specification(W3c Spec) for XML
# XSD data-type
# xs:string
# xs:date
# xs:dateTime
# xs:decimal
import xml.etree.ElementTree as ET
data = '''<person>
<name>Check</name>
<phone type="intl"> +1 734 303 4456
</phone>
<email hide="yes"/>
</person>'''

tree = ET.fromstring(data)

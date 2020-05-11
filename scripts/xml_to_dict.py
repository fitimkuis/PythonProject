#!/usr/bin/python3
import xmltodict

from datetime import date

epoch_year = date.today().year
year_start = date(epoch_year, 1, 1)
year_end = date(epoch_year, 12, 31)
print(year_start)
print(year_end)
print(year_start.strftime('%m/%d/%Y'))

xmlsource = '''<dns:ManageSPResourceRequest
        xmlns:dns="http://www.adventure-works.com">
    <SPResource>
        <ID>ORD690432</ID>
        <orderDate>2020-04-17T13:30:00Z</orderDate>
        <orderType>Ship</orderType>
        <SPResourceComprisedOf>
            <DescribedBy>
                <value>EMP00432</value>
                <Characteristic>
                    <ID>EmployeeID</ID>
                </Characteristic>
            </DescribedBy>
            <DescribedBy>
                <value>Howard_Snyder</value>
                <Characteristic>
                    <ID>contactName</ID>
                </Characteristic>
            </DescribedBy>
            <DescribedBy>
                <value>CUST00432</value>
                <Characteristic>
                    <ID>customerId</ID>
                </Characteristic>
            </DescribedBy>
        </SPResourceComprisedOf>
    </SPResource>
</dns:ManageSPResourceRequest>'''


my_dict = xmltodict.parse(xmlsource)
print(my_dict['dns:ManageSPResourceRequest']['SPResource']['ID'])
#ORD690432
print(my_dict['dns:ManageSPResourceRequest']['SPResource']['orderDate'])
#2020-04-17T13:30:00Z
print(my_dict['dns:ManageSPResourceRequest']['SPResource']['orderType'])
#Ship
print(my_dict['dns:ManageSPResourceRequest']['SPResource']['SPResourceComprisedOf']['DescribedBy'])
#[OrderedDict([('value', 'EMP00432'), ('Characteristic', OrderedDict([('ID', 'EmployeeID')]))]), OrderedDict([('value', 'Howard_Snyder'), ('Characteristic', OrderedDict([('ID', 'contactName')]))]), OrderedDict([('value', 'CUST00432'), ('Characteristic', OrderedDict([('ID', 'customerId')]))])]
print("****************")
print("request my_dict['dns:ManageSPResourceRequest']['SPResource']['SPResourceComprisedOf']['DescribedBy'][0]")
print(my_dict['dns:ManageSPResourceRequest']['SPResource']['SPResourceComprisedOf']['DescribedBy'][0])
#OrderedDict([('value', 'EMP00432'), ('Characteristic', OrderedDict([('ID', 'EmployeeID')]))])
print("****************")
print("request my_dict['dns:ManageSPResourceRequest']['SPResource']['SPResourceComprisedOf']['DescribedBy'][1]")
print(my_dict['dns:ManageSPResourceRequest']['SPResource']['SPResourceComprisedOf']['DescribedBy'][1])
#OrderedDict([('value', 'Howard_Snyder'), ('Characteristic', OrderedDict([('ID', 'contactName')]))])
print("****************")
print("request my_dict['dns:ManageSPResourceRequest']['SPResource']['SPResourceComprisedOf']['DescribedBy'][2]")
print(my_dict['dns:ManageSPResourceRequest']['SPResource']['SPResourceComprisedOf']['DescribedBy'][2])
#OrderedDict([('value', 'CUST00432'), ('Characteristic', OrderedDict([('ID', 'customerId')]))])
print("****************")
#print(my_dict['dns:ManageSPResourceRequest']['SPResource']['SPResourceComprisedOf']['DescribedBy'][0]['value'])
#print(my_dict['dns:ManageSPResourceRequest']['SPResource']['SPResourceComprisedOf']['DescribedBy'][1]['value'])
#print(my_dict['dns:ManageSPResourceRequest']['SPResource']['SPResourceComprisedOf']['DescribedBy'][2]['value'])
#EMP00432
#Howard_Snyder
#CUST00432
#print("****************")

#print("****************")
#print(my_dict['dns:ManageSPResourceRequest']['SPResource']['SPResourceComprisedOf']['DescribedBy'][0]['Characteristic']['ID'])
#print(my_dict['dns:ManageSPResourceRequest']['SPResource']['SPResourceComprisedOf']['DescribedBy'][1]['Characteristic']['ID'])
#print(my_dict['dns:ManageSPResourceRequest']['SPResource']['SPResourceComprisedOf']['DescribedBy'][2]['Characteristic']['ID'])
#EmployeeID
#contactName
#customerId
print("****************")

l = len(my_dict['dns:ManageSPResourceRequest']['SPResource']['SPResourceComprisedOf']['DescribedBy'])

for i in range (l):
    print(my_dict['dns:ManageSPResourceRequest']['SPResource']['SPResourceComprisedOf']['DescribedBy'][i]['value'])
#EMP00432
#Howard_Snyder
#CUST00432
print("****************")
for i in range (l):
    print(my_dict['dns:ManageSPResourceRequest']['SPResource']['SPResourceComprisedOf']['DescribedBy'][i]['Characteristic']['ID'])
#EmployeeID
#contactName
#customerId
print("****************")

codes = []
for articel in my_dict['dns:ManageSPResourceRequest']['SPResource']['SPResourceComprisedOf']['DescribedBy']:
    codes.append(articel['value'])
print(codes)
#['EMP00432', 'Howard_Snyder', 'CUST00432']

codes = []
for item in my_dict['dns:ManageSPResourceRequest']['SPResource']['SPResourceComprisedOf']['DescribedBy'][0]:
    codes.append(item)
print(codes)
#['value', 'Characteristic']

with open('demo.xml') as fd:
    doc = xmltodict.parse(fd.read())
#print(doc)
xmltodict.parse(xmlsource)
#print(xmltodict.parse(xmlsource)['dns:ManageSPResourceRequest']['SPResource']['SPResourceComprisedOf']['DescribedBy'][0])

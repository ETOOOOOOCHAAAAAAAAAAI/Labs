import json

file_path = 'C:/Users/ASUS TUF Gaming F15/Downloads/sample-data.json'

with open(file_path, "r") as file:
    data = json.load(file)
print(data.keys())

interfaces = data['imdata']
print("Interface Status")
print("="*86)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
for item in interfaces:
    interface = item.get('l1PhysIf', {})
    dn = interface.get('attributes', {}).get('dn', '')
    descr = interface.get('attributes', {}).get('descr', '')
    speed = interface.get('attributes', {}).get('speed', '')
    mtu = interface.get('attributes', {}).get('mtu', '')
    print("{:<50} {:<20} {:<8} {:<6}".format(dn, descr, speed, mtu))

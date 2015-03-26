from sys import argv

ITEMCODE_FILE = "itemcodes.txt"
LOCATION_FILE = "locations.txt"

itemcodes = {}
for line in open(ITEMCODE_FILE):
    line = line.strip().split()
    code, name = tuple(line)
    code = int(code, 0x10)
    itemcodes[name] = code
    itemcodes[code] = name

locations = {}
for line in open(LOCATION_FILE):
    line = line.strip().split()
    address, name = line[0], " ".join(line[1:])
    address = int(address, 0x10)
    locations[name] = address
    locations[address] = name

if __name__ == "__main__":
    filename = argv[1]
    f = open(filename, 'r+b')
    for address in locations:
        if type(address) is not int:
            continue
        f.seek(address)
        code = f.read(2)
        code = (ord(code[0]) << 8) | ord(code[1])
        item = itemcodes[code].lower().replace('_', ' ')
        location = locations[address]
        print "{0:50} {1}".format(location + ':', item)

import xmltodict

filename = "pe10_1.xml"

with open(filename) as XML_file:
    line = XML_file.read()
    XML_dict = xmltodict.parse(line)

    for x in XML_dict["artikelen"]["artikel"]:
        print(x["naam"])

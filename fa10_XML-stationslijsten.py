import xmltodict

file = "fa10.xml"

with open(file) as XML:
    line = XML.read()
    XML_dict = xmltodict.parse(line)
    print("Dit zijn de codes en types van de 4 stations:")
    for x in XML_dict["Stations"]["Station"]:
        print("{0:4} - {1}".format(x["Code"], x["Type"]))

    print("\nDit zijn alle stations met één of meer synoniemen:")
    for y in XML_dict["Stations"]["Station"]:
        if y["Synoniemen"] is not None:
            print("{0:4} - {1}".format(y["Code"], y["Synoniemen"]))

    print("\nDit is de lange naam van elk station:")
    for z in XML_dict["Stations"]["Station"]:
        print("{0:4} - {1}".format(z["Code"], z["Namen"]["Lang"]))

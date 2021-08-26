import PySimpleGUI as sg
from os import path
import csv
import zipfile
import xml.etree.ElementTree as ET
from xml.dom import minidom
from xml.etree import ElementTree
import pprint
import webbrowser

def prettify(elem):
    """Return a pretty-printed XML string for the Element."""
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def readCSV(fPath):
    with open(fPath, newline='', encoding='utf8') as csvfile:
#    with open("C:/Users/John/github/testpygui/syrinscape_remote_control_links_mattekure.csv", newline='', encoding='utf8') as csvfile:
        fDialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        reader = csv.DictReader(csvfile, dialect=fDialect, doublequote=True)

        for row in reader:
            tDict = {
                "id": row['id'].replace(":", ""),
                "status": row['status'],
                "subcategory": row['subcategory'],
                "product_or_pack": row['product_or_pack'],
                "soundset": row['soundset'],
                "name": row['name'],
                "type": row['type'],
                "sub_type": row['sub_type'],
                "genre_players_play_url": row['genre_players_play_url'],
                "genre_players_stop_url": row['genre_players_stop_url'],
                "online_player_play_url": row['online_player_play_url'].replace("https", "syrinscape-online") + '?auth_token=',
                "online_player_stop_url": row['online_player_stop_url'].replace("https", "syrinscape-online") + '?auth_token=',
            }
            addToDict(tDict)


def addToDict(tDict):
    if tDict["subcategory"] in sDict:
        x = sDict[tDict["subcategory"]]
        x[tDict["id"]] = tDict
        sDict[tDict["subcategory"]] = x
    else:
        sDict[tDict["subcategory"]] = { tDict["id"]: tDict}

def genXML():
    root = ET.Element('root', attrib={'version': '3.3'})
    sosoundElement = ET.SubElement(root, 'sosounds')
    stopall = ET.SubElement(sosoundElement, 'stopall')
    stopalllocked = ET.SubElement(stopall, 'locked', attrib={'type': 'number'})
    stopalllocked.text = '1'
    stopallname = ET.SubElement(stopall, 'name', attrib={'type': 'string'})
    stopallname.text = "Stop All (Syrinscape Online)"
    stopallppack = ET.SubElement(stopall, 'productPack', attrib={'type': 'string'})
    stopallppack.text = "Global"
    stopallsset = ET.SubElement(stopall, 'soundset', attrib={'type': 'string'})
    stopallsset.text = "Global"
    stopallsType = ET.SubElement(stopall, 'soundType', attrib={'type': 'string'})
    stopallsType.text = "Global"
    stopallsoPlay = ET.SubElement(stopall, 'SOPlayURL', attrib={'type': 'string'})
    stopallsoPlay.text = "syrinscape-online://www.syrinscape.com/online/frontend-api/stop-all/?auth_token="
    stopallsoStop = ET.SubElement(stopall, 'SOStopURL', attrib={'type': 'string'})
    stopallsoStop.text = "syrinscape-online://www.syrinscape.com/online/frontend-api/stop-all/?auth_token="
    stopallgPlay = ET.SubElement(stopall, 'GPlayURL', attrib={'type': 'string'})
    stopallgPlay.text =""
    stopallgStop = ET.SubElement(stopall, 'GStopURL', attrib={'type': 'string'})
    stopallgStop.text = ""

    stopallfantasy = ET.SubElement(sosoundElement, 'stopallfantasy')
    stopallfantasylocked = ET.SubElement(stopallfantasy, 'locked', attrib={'type': 'number'})
    stopallfantasylocked.text = '1'
    stopallfantasyname = ET.SubElement(stopallfantasy, 'name', attrib={'type': 'string'})
    stopallfantasyname.text = "Stop All (Fantasy Player)"
    stopallfantasyppack = ET.SubElement(stopallfantasy, 'productPack', attrib={'type': 'string'})
    stopallfantasyppack.text = "Global"
    stopallfantasysset = ET.SubElement(stopallfantasy, 'soundset', attrib={'type': 'string'})
    stopallfantasysset.text = "Global"
    stopallfantasysType = ET.SubElement(stopallfantasy, 'soundType', attrib={'type': 'string'})
    stopallfantasysType.text = "Global"
    stopallfantasysoPlay = ET.SubElement(stopallfantasy, 'SOPlayURL', attrib={'type': 'string'})
    stopallfantasysoPlay.text = ""
    stopallfantasysoStop = ET.SubElement(stopallfantasy, 'SOStopURL', attrib={'type': 'string'})
    stopallfantasysoStop.text = ""
    stopallfantasygPlay = ET.SubElement(stopallfantasy, 'GPlayURL', attrib={'type': 'string'})
    stopallfantasygPlay.text ="syrinscape-fantasy:stop-all/"
    stopallfantasygStop = ET.SubElement(stopallfantasy, 'GStopURL', attrib={'type': 'string'})
    stopallfantasygStop.text = "syrinscape-fantasy:stop-all/"

    stopallscifi = ET.SubElement(sosoundElement, 'stopallscifi')
    stopallscifilocked = ET.SubElement(stopallscifi, 'locked', attrib={'type': 'number'})
    stopallscifilocked.text = '1'
    stopallscifiname = ET.SubElement(stopallscifi, 'name', attrib={'type': 'string'})
    stopallscifiname.text = "Stop All (Sci-Fi Player)"
    stopallscifippack = ET.SubElement(stopallscifi, 'productPack', attrib={'type': 'string'})
    stopallscifippack.text = "Global"
    stopallscifisset = ET.SubElement(stopallscifi, 'soundset', attrib={'type': 'string'})
    stopallscifisset.text = "Global"
    stopallscifisType = ET.SubElement(stopallscifi, 'soundType', attrib={'type': 'string'})
    stopallscifisType.text = "Global"
    stopallscifisoPlay = ET.SubElement(stopallscifi, 'SOPlayURL', attrib={'type': 'string'})
    stopallscifisoPlay.text = ""
    stopallscifisoStop = ET.SubElement(stopallscifi, 'SOStopURL', attrib={'type': 'string'})
    stopallscifisoStop.text = ""
    stopallscifigPlay = ET.SubElement(stopallscifi, 'GPlayURL', attrib={'type': 'string'})
    stopallscifigPlay.text ="syrinscape-sci-fi:stop-all/"
    stopallscifigStop = ET.SubElement(stopallscifi, 'GStopURL', attrib={'type': 'string'})
    stopallscifigStop.text = "syrinscape-sci-fi:stop-all/"



    for category in sDict:
        xCategory = ET.SubElement(sosoundElement, 'category', attrib={'name': catLookup[category], 'baseicon': "0", 'decalicon': "0"})
        soundCategory = sDict[category]
        for soundID in soundCategory:
            tDict = soundCategory[soundID]
            xSound = ET.SubElement(xCategory, soundID)

            locked = ET.SubElement(xSound, 'locked', attrib={'type': 'number'})
            locked.text = '1'
            name = ET.SubElement(xSound, 'name', attrib={'type': 'string'})
            name.text = tDict['name']
            ppack = ET.SubElement(xSound, 'productPack', attrib={'type': 'string'})
            ppack.text = tDict['product_or_pack']
            sset = ET.SubElement(xSound, 'soundset', attrib={'type': 'string'})
            sset.text = tDict['soundset']
            sType = ET.SubElement(xSound, 'soundType', attrib={'type': 'string'})
            sType.text = getSoundType(tDict['type'], tDict['sub_type'])
            soPlay = ET.SubElement(xSound, 'SOPlayURL', attrib={'type': 'string'})
            soPlay.text = tDict['online_player_play_url']
            soStop = ET.SubElement(xSound, 'SOStopURL', attrib={'type': 'string'})
            soStop.text = tDict['online_player_stop_url']
            gPlay = ET.SubElement(xSound, 'GPlayURL', attrib={'type': 'string'})
            gPlay.text = tDict['genre_players_play_url']
            gStop = ET.SubElement(xSound, 'GStopURL', attrib={'type': 'string'})
            gStop.text = tDict['genre_players_stop_url']

    return prettify(root)


def getSoundType(type, subtype):
    if type == "element":
        return subtypeLookup[subtype]
    else:
        return subtypeLookup[type]

catLookup = {
    "boardgame": "Sounds: Boardgame",
    "dungeons-and-dragons": "Sounds: Dungeons & Dragons",
    "fantasy": "Sounds: Fantasy",
    "general-fantasy": "Sounds: General Fantasy",
    "pathfinder": "Sounds: Pathfinder",
    "sci-fi": "Sounds: Sci-Fi"
}

subtypeLookup = {
    "oneshot": "Element: One-Shot",
    "music": "Element: Music",
    "sfx": "Element: Sound Effect",
    "mood": "Mood"
}



defxml = '''<?xml version="1.0" encoding="UTF-8"?>
<root version="3.3">
	<name>Syrinscape Soundlinks</name>
	<category>Supplement</category>
	<author>John Waite (mattekure), Rob Twohy (rob2e)</author>
	<ruleset>Any</ruleset>
</root>
'''


layout = [
    [
        sg.Button("Download Syrinscape CSV"),
    ],
    [
        sg.Text("Select your downloaded Syrisncape CSV File"),
        sg.In(size=(25, 1), enable_events=True, key="-CSVFILE-"),
        sg.FileBrowse(file_types=(("CSV Files", "*.csv"),)),
    ],
    [
        sg.Button("CONVERT"),
        sg.Button("EXIT")
    ],
]

# Create the window
window = sg.Window("Syrinscape CSV to FG Module converter", layout)
sDict = {}

# Create an event loop
while True:
    event, values = window.read()
    if event == "CONVERT":
        if values["-CSVFILE-"] == "": continue
        readCSV(values["-CSVFILE-"])
        xmlText = genXML()
        zf = zipfile.ZipFile('Fantasy_Grounds_Syrinscape_Sound_Links.mod', mode='w', compression=zipfile.ZIP_DEFLATED,)
        thumbpath = path.abspath(path.join(path.dirname(__file__), 'thumbnail.png'))
        with open(thumbpath, mode='rb') as file:
            fileContent = file.read()
        try:
            zf.writestr('thumbnail.png', fileContent)
            zf.writestr('client.xml', xmlText)
            zf.writestr('definition.xml', defxml)
        finally:
            zf.close()
    elif event == "Download Syrinscape CSV":
        webbrowser.open('https://www.syrinscape.com/account/remote-control-links-csv/', new=2)
    elif event == "EXIT" or event == sg.WIN_CLOSED:
        break

window.close()

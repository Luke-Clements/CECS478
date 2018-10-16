import json

from base64 import b64decode, b64encode

def loadMessageFromJSON(filepath):

    with open(filepath, 'r') as json_file:
        data = json.load(json_file)
    
    key = b64decode(data["Key"])
    text = b64decode(data["Text"])
    tag = b64decode(data["Tag"])
    json_file.close()
    return (key, text, tag)

def saveMessageAsJSON(saveFilePath, key, text, tag):

    data = {
        'Key': b64encode(key).decode('utf-8'),
        'Text': b64encode(text).decode('utf-8'),
        'Tag': b64encode(tag).decode('utf-8')
        }

    with open(saveFilePath, 'w+') as outFile:
        json.dump(data, outFile)
    outFile.close()

def loadFileFromJSON(filepath):
    with open(filepath, 'r') as json_file:
        data = json.load(json_file)

    key = b64decode(data["Key"])
    text = b64decode(data["Text"])
    ext = data["Extension"]
    tag = b64decode(data["Tag"])
    json_file.close()
    return (text, key, tag, ext)

def saveFileAsJSON (saveFilePath, text, key, tag, ext):
    data = {
        'Key': b64encode(key).decode('utf-8'),
        'Text': b64encode(text).decode('utf-8'),
        'Extension': ext,
        'Tag': b64encode(tag).decode('utf-8')
        }

    with open(saveFilePath, 'w+') as outFile:
        json.dump(data, outFile)
    outFile.close()

def saveFile(filename, plaintext, ext):
    with open(filename + ext, "wb") as sFile:
        sFile.write(plaintext)
    sFile.close()


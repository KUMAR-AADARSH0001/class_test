# Link to the dev app, https://ubm-nodejs.onrender.com/

# Read Json file using Python, https://www.geeksforgeeks.org/read-json-file-using-python/
import json

exampleDictData = (
    {
        # The value can be anything
        "qualifierName": "regex",
        # The value can be Include or Exclude
        "type": "Exclude",
        # The value can be Mails or Buckets
        "source": "Mails",
        # The value can be anything here
        "filter": "Sumit",
    },
)
# Opening a JSON file
f = open("test.json")

# Returns a jsong object as a dictionary
data = json.load(f)


def myFunc(x):
    if x < 18:
        return False
    else:
        return True


def convertFormat(dict_data):
    result = {}

    for x in dict_data:
        print(f"x value is {x}")
        # 1. Create the exclusions_inclusions keys e.g. mails_exclusion
        exclusions_inclusions = x["type"] == "Exclude" and "exclusion" or "inclusion"
        source = x["source"].lower()
        key = f"{source}_{exclusions_inclusions}"
        # 2. Create initial index
        listKeyIndex = 1
        qualifire = x["qualifierName"]
        qualifierNameKey = f"{qualifire}_{listKeyIndex}"

        dictToAdd = {qualifierNameKey: {qualifire: x["filter"]}}
        if key in result:
            # filter(, result[key])
            result[key].append(dictToAdd)
        else:
            result[key] = [dictToAdd]

        print(result)


convertFormat(data)
print(data)

# Closing file
f.close()

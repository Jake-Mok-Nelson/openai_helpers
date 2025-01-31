
import json
import logging
import os



def saveOutput(filename, data):
    extension = filename.split(".")[-1]
    if extension == "json":
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
    else:
        with open(filename, "w") as f:
            f.write(data)
    return "Output saved to " + filename
            

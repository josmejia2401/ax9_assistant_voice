#!/usr/bin/python3
import json
import os
from pathlib import Path
import json


class File:
    @staticmethod
    def getSRCResource():
        current_dir = Path(__file__).parent
        file_path = os.path.join(current_dir, 'src', 'resources')
        contBreak = 0
        while os.path.exists(file_path) == False:
            if contBreak > 5:
                break
            current_dir = Path(current_dir).parent
            file_path = os.path.join(current_dir, 'src', 'resources')
            contBreak += 1
        return file_path

    @staticmethod
    def saveJson(data, name):
        current_dir = File.getSRCResource()
        # with open('config.json', 'w') as f:
        #    json.dump(data, f)
        new_file = os.path.join(current_dir, name)
        with open(new_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    
    @staticmethod
    def loadFileFromResourcesAsJson(name=None):
        current_dir = File.getSRCResource()
        print("current_dir", current_dir, name)
        file_path = os.path.join(current_dir, name)
        contents = None
        with open(file_path) as dataFile:
            contents = json.load(dataFile)
        return contents
import json
import os
import shlex
import shutil
import subprocess
import sys
import time
from threading import Thread


class FileTransfer(Thread):

    def __init__(self):
        super(FileTransfer, self).__init__()

        self.current_directory = os.getcwd()

    def run(self):

        while True:

            with open(self.current_directory + '/config.json', 'r') as config_file:
                reading = config_file.read()
                data = json.loads(reading)

            source_path = data['config'][0]['source']
            destiny_path = data['config'][0]['destiny']
            time_to_wait = data['config'][0]['timer']
            filter_type = data['config'][0]['filter_type']
            filter_value = data['config'][0]['filter_value']

            print('Your source path is: ')
            print(source_path)

            print('Your destiny path is: ')
            print(destiny_path)

            print('os listdir')
            print(os.listdir(source_path))

            time.sleep(time_to_wait)

            for file in os.listdir(source_path):

                if filter_type == 'prefix':
                    if file.startswith(filter_value):
                        # Command to effectively transfer the file
                        try:
                            shutil.move(source_path + '/' + file, destiny_path + '/' + file)
                            print("File "+file+" transferred successfully")
                        except:
                            "Error"

                if filter_type == 'sufix':
                    if file.endswith(filter_value):
                        try:
                            shutil.move(source_path + '/' + file, destiny_path + '/' + file)
                            print("File " + file + " transferred successfully")
                        except:
                            "Error"

                if filter_type == 'infix':
                    if filter_value in file:
                        try:
                            shutil.move(source_path + '/' + file, destiny_path + '/' + file)
                            print("File " + file + " transferred successfully")
                        except:
                            "Error"

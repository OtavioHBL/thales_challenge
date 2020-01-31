import json
import os
import shutil
import time
import datetime
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


class FileTransferExtra(Thread):

    def __init__(self):
        super(FileTransferExtra, self).__init__()

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
            mode = data['config'][0]['operation_mode']

            print('Your source path is: ')
            print(source_path)

            print('Your destiny path is: ')
            print(destiny_path)

            print('os listdir')
            print(os.listdir(source_path))

            file_list = []
            for i in os.listdir(source_path):
                x = os.stat(os.path.join(source_path, i))
                file_list.append([i, x.st_ctime])

            file_list.sort(key=lambda g: g[1])

            #Transfer oldest file first
            if mode == '1':
                for file in file_list:

                    time.sleep(time_to_wait)

                    if filter_type == 'prefix':
                        if file[0].startswith(filter_value):
                            # Command to effectively transfer the file
                            try:
                                shutil.move(source_path + '/' + file[0], destiny_path + '/' + file[0])
                                print("File "+file[0]+" transferred successfully")
                            except:
                                "Error"

                    if filter_type == 'sufix':
                        if file[0].endswith(filter_value):
                            try:
                                shutil.move(source_path + '/' + file[0], destiny_path + '/' + file[0])
                                print("File " + file[0] + " transferred successfully")
                            except:
                                "Error"

                    if filter_type == 'infix':
                        if filter_value in file[0]:
                            try:
                                shutil.move(source_path + '/' + file[0], destiny_path + '/' + file[0])
                                print("File " + file[0] + " transferred successfully")
                            except:
                                "Error"

            #Transfer newest file first
            if mode == '2':
                for file in reversed(file_list):

                    time.sleep(time_to_wait)

                    if filter_type == 'prefix':
                        if file[0].startswith(filter_value):
                            # Command to effectively transfer the file
                            try:
                                shutil.move(source_path + '/' + file[0], destiny_path + '/' + file[0])
                                print("File "+file[0]+" transferred successfully")
                            except:
                                "Error"

                    if filter_type == 'sufix':
                        if file[0].endswith(filter_value):
                            try:
                                shutil.move(source_path + '/' + file[0], destiny_path + '/' + file[0])
                                print("File " + file[0] + " transferred successfully")
                            except:
                                "Error"

                    if filter_type == 'infix':
                        if filter_value in file[0]:
                            try:
                                shutil.move(source_path + '/' + file[0], destiny_path + '/' + file[0])
                                print("File " + file[0] + " transferred successfully")
                            except:
                                "Error"



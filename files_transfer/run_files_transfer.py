from files_transfer import FileTransfer, FileTransferExtra
import json
import os



if __name__ == '__main__':

    with open(os.getcwd() + '/config.json', 'r') as config_file:

        reading = config_file.read()
        data = json.loads(reading)

        if data['config'][0]['operation'] == '1':
            transfer = FileTransfer()
            transfer.start()

        if data['config'][0]['operation'] == '2':
            transfer = FileTransferExtra()
            transfer.start()


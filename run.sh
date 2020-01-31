echo "Activating virtual environment"
source mypython/bin/activate
echo "Navigating to file directory"
cd files_transfer
echo "Executing python file"
python run_files_transfer.py
cd /..
echo "Deactivating virtual environment"
source mypython/bin/deactivate

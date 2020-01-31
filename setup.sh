echo "Initializing install process"
sudo apt update
sudo apt upgrade
echo "Installing Python 2.7 and pip, please wait"
sudo apt install python2.7 python-pip
echo "Installing virtual environment"
pip install virtualenv
echo "Creating virtual environment"
virtualenv mypython



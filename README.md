# hackrx
Provider Invoice Text Curation

Project uses python 3.8 and gitbash as terminal (windows 10)

Using virtualenv to isolate python packages.
If you have a different version of python installed, install python 3.8 from Microsoft store.


Use these commands to know your python executable installation location if needed \
import os \
import sys \
os.path.dirname(sys.executable) \
'C:\\Python25' 

Commands to set up environment - 
(make sure you are in Environments folder in terminal)- \
python -m virtualenv -p <path to python 3.8 executable> hackrx_env 

Use these commands to know your python executable installation location if needed - \
import os \
import sys \
os.path.dirname(sys.executable) \
'C:\\Python25' 

In my case command is - \
python -m virtualenv -p  C:\\Users\\Lenovo\\AppData\\Local\\Microsoft\\WindowsApps\\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\\python3.8.exe hackrx_env 

Then - \
source hackrx_env/Scripts/activate #to activate the environment 

Then - \
pip install Flask \
pip install virtualenv 

Then - \
python app.py #to run the app 



#run command 'deactivate'
#to deactivate the environment if ever needed

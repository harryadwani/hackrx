# hackrx 3.0 Hackathon!
Problem statement - Implement a provider invoice text extraction to identify provider (hospital/Dr./laboratory) names & other critical information tags (AI,ML, Computer Vision, Python-Flask for backend. 

Provider Invoice Text Curation

Project uses python 3.8 and gitbash as terminal (windows 10)

Using virtualenv to isolate python packages.
Short and nice tutorial to virtualenv - https://www.youtube.com/watch?v=N5vscPTWKOk&ab_channel=CoreySchafer \
If you have a different version of python installed, install python 3.8 from Microsoft store.

------------------------------------------------------------

Commands to set up environment - 
(make sure you are in Environments folder in terminal)- 
### `pip install virtualenv`
### `python -m virtualenv -p <path to python 3.8 executable> hackrx_env`

------------------------------------------------------------

Use these commands to know your python executable installation location if needed - 
### `import os` 
### `import sys`
### `os.path.dirname(sys.executable)` 

------------------------------------------------------------

In my case command is - 
### `python -m virtualenv -p  C:\\Users\\Lenovo\\AppData\\Local\\Microsoft\\WindowsApps\\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\\python3.8.exe hackrx_env `

Then - 
### `source hackrx_env/Scripts/activate #to activate the environment`

Then - 
### `pip install -r requirements.txt #to install required dependencies`


Then - 
### `python app.py` 
to run the app 

------------------------------------------------------------


run command 
### `deactivate`
to deactivate the environment if ever needed

------------------------------------------------------------

MAKE SURE TO UPDATE PYTHON PACKAGES DEPENDENCIES FILE WHEN YOU ADD A NEW PACKAGE using 
### `pip freeze --local > requirements.txt `


------------------------------------------------------------

When setup is done and starting the project at a later time, make sure to cd into Environments folder and activate environment using- 

### `source hackrx_env/Scripts/activate`

# NoteMaker
* <b>Information</b><br>
This backend of the program is built using flask framework. 

* <b>Environment setup:</b><br>
This project is based on python 3.6. Have added requirements.txt file to install the dependencies.<br>
I would suggest creating new virtual environment either using virtual_env or conda (I myself used virtual_env).
Use the following command: `virtualenv -p /usr/bin/python3.6 <env_name>`. 
<br>Then activate this env using:`source <env_name>/bin/activate`.
<br>After that install all requirements in the requirements.txt file `pip install -r requirements.txt`

* <b>Database: </b><br>
I have added MySQl database to the github repo under name `albanero.sql`. You can import this whatever application you are using(I user phpmyadmin) and accordingly change the username and password to your account on the database configuration in `notes_webpage_handlers.py` file.

* <b>Run the server</b><br>
Now after doing environment setup, we are going to start the server by running the following command `python notes_webpage_handlers.py`. This would show a link `localhost:5000`. Visit the link to find the running website.

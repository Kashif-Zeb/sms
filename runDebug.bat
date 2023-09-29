@ECHO OFF
set FLASK_APP=project.api
set FLASK_ENV=development
set DEBUG=true

CMD /k "python runDebug.py"

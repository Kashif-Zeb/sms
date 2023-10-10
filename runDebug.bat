@ECHO OFF
@REM set FLASK_APP=project.api
@REM set FLASK_ENV=development
@REM set DEBUG=true

SET DB_NAME=sms
SET DB_URL=localhost
SET DB_USER=root
SET DB_PWD=kashif
SET DB_PORT=3306

CMD /k "python runDebug.py"

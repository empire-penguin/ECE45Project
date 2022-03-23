python --version 3>NUL
if errorlevel 1 goto errorNoPython

pip install virtualenv
python -m venv venv
source venv\bin\activate
pip install -r requirements.txt

echo "Setup completed successfully."

goto:eof

:errorNoPython
echo.
echo Error^: Python not installed
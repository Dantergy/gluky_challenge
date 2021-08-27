@echo Installing libraries and virtual environment
python -m venv env
call .\env\Scripts\activate 
pip install firebase_admin
pip install pandas
pip install openpyxl
@echo.
@echo All libraries installed, you can close this window.





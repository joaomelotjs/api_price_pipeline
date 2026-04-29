@echo off

cd /d "C:\Users\paulo\OneDrive\Área de Trabalho\api_price_pipeline"

call venv\Scripts\activate.bat

python -m src.pipeline

pause
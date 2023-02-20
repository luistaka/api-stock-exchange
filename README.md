# aws sam
sam build
sam deploy --no-fail-on-empty-changeset --no-confirm-changeset --config-env production
 
# api-stock-exchange
Ingestor from API to S3

# Python Version
python 3.9.16

# Create VENV 
python3 -m venv /Users/luis.takahashi/Desktop/Tools/Git/api-stock-exchange

# Create requirement
pip freeze > requirements.txt

# Activate VENV
source /Users/luis.takahashi/Desktop/Tools/Git/api-stock-exchange/bin/activate

# Install requirements
pip install -r requirements.txt
pip install --upgrade --force-reinstall -r requirements.txt

# See list of libraries installed
pip list

# Deactivate VENV
deactivate

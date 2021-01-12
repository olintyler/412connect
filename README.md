# 412connect
git clone https://github.com/CAASI-G2A/412connect.git

# Windows virtual env
py -m venv env
.\env\Scripts\activate

# macOS and Linux virtual env
python3 -m venv env
source env/bin/activate

# install software
pip install -r requirements.txt

# run locally
python manage.py runserver

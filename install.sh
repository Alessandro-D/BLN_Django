# Create virtual env
python -m virtualenv env

# Activate env
./env/Scripts/activate

# Install pip requirements
pip install -r requirements.txt

# Make Django Migrations
python ./bln/manage.py migrate
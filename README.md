# Overview
This is a web application with **wiki** functions. 
It features markdown input and the ability to specify the slug (end of URL) for each page.
Django is used as framework.

# Settings
The following is an example of local startup. 
It is assumed that a Python environment (including pip) has already been built on Linux or Mac.
```
# In any hierarchy
git clone https://github.com/h-akira/Wiki_Project.git
cd Wiki_Project
pip3 install -r requirements.txt
```
In the `settings.py`, Read `settings_local.py` by `import` to set `SECRET_KEY` and other individual settings. 
You can copy and edit `Wiki_Project/settings_local_sample.py`, 
or automatically generate `settings_local.py` with `SECRET_KEY` by using `bin/add_secret_key.py`. 
Because Symbolic links are placed in the hierarchy `Wiki_Project/Wiki_Project`, 
Plese execute it. 
```
cd Wiki_Project
./add_secret_key.py
```
After that, go to the hierarchy where `manage.py` is located and do database migrations.
```
cd ..
python3 manage.py makemigrations
python3 manage.py migrate
```
This completes the preparation, and you can run the server.
```
python3 manage.py runserver
```


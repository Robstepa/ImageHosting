# ImageHosting

# Requirements
-python 3.6<br/>
-django 2.0.1<br/>
-google-cloud-vision<br/>
-pip 10.0.1

# You need get your own Google Vision API key
This might be helpful: https://support.google.com/cloud/answer/6158862?hl=en <br/>
Choose Service Account Key as JSON file<br/>
Remeber to enable your Google Vision API

# Running project
1. From project folder run install.py(as admin)<br/>
2. When you got your key as JSON file, rename it as key.json and put in project folder(dont worry its in .gitignore)<br/>
3. Then type in your terminal(go to project folder) `python manage.py migrate`<br/>
4. Then type in your terminal(go to project folder) `python manage.py runserver`<br/>
5. Go to http://127.0.0.1:8000/hosting/

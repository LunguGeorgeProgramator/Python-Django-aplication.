# GLS_test_project
The front end part made in a simply html file and javascript, using jQuery. Just upload the files guide_v.json, index.html, player.js in any server and open index.html.

The back end part made in python Django:

This project is a simple DJango app, I am ussing bitnami-djangostack-2.2.2-0,
for windows. It can be downloaded from link:

https://bitnami.com/stack/django/installer

bitnami-djangostack-2.2.2-0-windows-x64-installer

1: It is a simple install, easy next .. next .. buttons. Also the project files need to be added in windows path:

C:\Users\USER_NAME_FROM_YOUR_PC\Bitnami Django Stack projects

I use host:

http://127.0.0.1:90/GuidedLearningSolution/

2: If there are problem with localhost please set in 

 C:\Users\USER_NAME_FROM_YOUR_PC\Documents\GitHub\GLS_test_project\GuidedLearningSolution\GuidedLearningSolution\settings.py

Line 27: ALLOWED_HOSTS = ['127.0.0.1']

3: set the DataBase user, password and host as:
    host_mysql = "127.0.0.1"
    user_mysql = "root"
    pass_mysql = "secret"
    
   Note this aplication dose not need to import a database one is created automated on first site load in:
   C:\Users\USER_NAME_FROM_YOUR_PC\Documents\GitHub\GLS_test_project\GuidedLearningSolution\guide\database\DataBaseClass.py

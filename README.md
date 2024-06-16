#### Thanks to [chai aur code](https://www.youtube.com/@chaiaurcode)
- [playlist](https://www.youtube.com/playlist?list=PLu71SKxNbfoDOf-6vAcKmazT92uLnWAgy)
- [documentation & snippet](https://chaicode.com/blogs/getting-started-with-django)


##### prerequisites: python, html, css

### Instructions:
1. virtual environment setup
    - python -m vevn .venv
        - not being tracked by Git | .gitignore
        - as like .git file

    - but for more fast python installer and resolver --> uv
        
        - [official-documentation](https://pypi.org/project/uv)
        - pip install uv  -->  cmd
        - uv venv  -->  Create a virtual environment at .venv
        - .venv\Scripts\activate

    - to deactivate
        - deactivate
<br>

2. django setup
    - uv pip install Django
        - using uv | so, have to use uv before pip
<br>

3. project setup
    - django-admin startproject chaiAurDjango
    - cd chaiAurDjango
    - python manage.py runserver
    - python manage.py runserver 8001 --> any port can be
<br>

4. file structure
    - pycache  -->  store caches
    - __init__  -->  make it package
    - settings  -->  write down all the configuraiton
    - urls  -->  routes
    - views  -->  write down business logic then render or response
    - models  -->  database table structure
    - templates  -->  frontend | html
    - ##### urls --> views --> templates
<br>

5. django architechture
    - User  --request--->  urls.py  -----> views.py  --render/response--->  User
<br>

6. {{}} vs {% %} --> inside html
    - {{}}  ---->  variable interpolation
    - {% %}  ---->  template tags
        - template logic, loops, conditional statements, and other control structures
        - define a block or load and csrf
<br>

7. create a app
    - python manage.py startapp chai
    - add 'chai' into the INSTALLED_APPS in the settings
<br>

8. django-html emmet
    - ctrl + ,  ===>  search 'emmet'  ===>  go to Include language  ===>  add Item: django-html , value: html
#### Thanks to [chai aur code](https://www.youtube.com/@chaiaurcode)
- [playlist](https://www.youtube.com/playlist?list=PLu71SKxNbfoDOf-6vAcKmazT92uLnWAgy)
- [documentation & snippet](https://chaicode.com/blogs/)


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
<br>


9. template inheritance
    - make a base/layout html file
    - make block_unnamed and give a name
        - {% block block-name %} default value {% endblock %}
    - then extends that file | write your code within block
<br>


10. How to add tailwind
    - [documentation](https://django-tailwind.readthedocs.io/en/latest/installation.html)
    - uv pip install django-tailwind
        - using uv | so, have to use uv before pip
    - uv pip install 'django-tailwind[reload]'
        - uv will not work on this, so
            - install pip: 
                - 1. python -m pip install --upgrade pip
                - 2. python -m ensurepip --upgrade
                    - if 1st one does not work

        - now do not need to use 'uv' anymore
    - pip install 'django-tailwind[reload]'
        - if any error happend --> use double quote
    - other instruction followed from documentation

    - ##### uv is very pathetic
        - I'm going to follow:
            - python -m venv .venv
            - add .gitignore file --> *
        - again follows upper steps
        - if any error occurs then go to chatGPT
    - ##### for hot reloading
        - python manage.py tailwind start
            - but it is on live
    
    - python manage.py tailwind build
        - it's just build | production grade
<br>


11. super user
    - before create super user | occurs error in the /admin
    - python manage.py createsuperuser
        - username: admin
        - password: admin
    - before creating superuser  -->  migrate
<br>


12. A guide on Django models
    - [chai aur code](https://chaicode.com/blogs/a-guide-on-django-models)
    - python manage.py makemigrations chai
        - only for chai.models
<br>


13. customized url
    - url name used at html href
        - {% url 'path_name' chai.id %}
            - chai.id --> custom value
    
    - chai.image
        - return the static file path
        - <img scr="{{chai.image.url}}" alt="">

    - ##### random:
        - /../ if '/' exist at starting  --->  that path replace the url
        - ../ if '/' not exist at starting  -->  add that path with existing url
<br>


14. django authentication system
    - [official documentation](https://docs.djangoproject.com/en/5.0/topics/auth/default/)


<br>



15. model relationship
    - one to one  -->  ek review er cha ektai
    - one to many  -->  ek cha er multiple review thakte pare
        - Or many to one

    - many to many  -->  ek cha multiple store a thakte pare, abar ek store a multiple cha thakte pare

    - [official documentation](https://docs.djangoproject.com/en/5.0/topics/db/examples/)
    - make sure you migrate and register your models
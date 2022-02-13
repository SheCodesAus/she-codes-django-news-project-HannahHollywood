# Plus Resources: Django Project Starter

Starter code for the Plus Django project.

Create a virtual environment inside your folder:
"virtualenv"

Activate the virtual environment:
Mac/Linux: ". venv/bin/activate"
Windows: "venv/Scripts/activate"

Install Django to the file:
(Ensure you've saved the .txt file "Django==4.0.1")
"pip3 install -r requirements.txt"

Check Django version:
"django-admin --version"

To exit Django:
"deactivate"
Then Re-Enter Django:
". venv/bin/activate"

> > > https://docs.djangoproject.com/en/4.0/intro/tutorial01/

---

> > > https://docs.djangoproject.com/en/4.0/ref/models/fields/

---

IMPORTANT > Check server >>

1. open powershell/terminal
2. navigate to your project
3. start your virtual environment
4. run your server "python3 manage.py runserver"

---

Everytime you make changes to the 'models' you need to run:
1."python3 manage.py makemigrations"
2. Run "python manage.py migrate" to apply them.


--------------
Ideas to Improve Website:
1. Complete Step 9 (DONE)

2. Create User Profile (DONE)
First step: User will fill out the "Sign Up" form and then:
    Need to redirect them to a page that will allow them to fill out the following:
    (HTML files: editProfile.html >> userProfileHome.html)
    (Create EditUserProfileForm class)
        - Add a profile photo
        - Location
        - Link to Social Media
        - Bio

3. Link to User Profile from Home (DONE)

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

Fix this error!:
"You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run "python manage.py migrate" to apply them."

---

Everytime you make changes to the 'models' you need to run:
"python3 manage.py makemigrations" (enter eg. polls)

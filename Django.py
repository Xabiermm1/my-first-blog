#COMO CREAR UN NUEVO ENTORNO CON VIRTUAL ENV (CODIGO EN CONSOLA DE COMANDO)
CD C:\Users\ESTELA Y XABI\Desktop\DjangoProyect
C:\Python27\python -m virtualenv myvenv
myvenv\Scripts\activate
#generando entorno de carpetas de django para mi site
python "C:\Users\ESTELA Y XABI\Desktop\DjangoProyect\myvenv\Scripts\django-admin.py" startproject projectname

#para general la base de datos de sqlite3, estando en el directoirio de manage.py
python manage.py migrate

#Iniciamos el servidor estando en la carpeta de manage.py
python manage.py runserver

#Para preparar el archibo de migracion del blog
python manage.py makemigrations blog
#Para migrarlo
python manage.py migrate blog

#Para crear un superusuario para tener acceso a toda la pagina
python manage.py createsuperuser

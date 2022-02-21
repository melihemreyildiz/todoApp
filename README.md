    Python kurulmalı (Python 3.8). Dokumantasyon:
            https://www.python.org/downloads/

    Nodejs kurulmalı (Node 14).
        https://nodejs.org/en/download/

    Python projesi için virtual environement kurulmalıdır. Dokumantasyon:
        https://docs.python.org/3/library/venv.html

    Python proje bağımlılıkları kurulmalı:

      $ cd djangoProject
      $ source venv/bin/activate
      $pip install -r requirements.txt

    API projesini ayağa kaldırmak için aşağıdaki adımları izleyiniz.
        Veritabanı yoksa oluşturulmalı


        Veritabanı migrationları yoksa onlar oluşturulmalı.

      $ python manage.py makemigrations          
      $ python manage.py migrate   


        En son olarak giriş yapabilmek için user oluşturulmalı.

      $ python manage.py createsuperuser
      > Username (leave blank to use <'yourusername'>): arge
      > Email address: isim@gmail.com
      > Password: <'yourpassword'>
      > Password (again): <'yourpassword'>

    Frontend kısmını ayağa kaldırmak için aşağıdaki adımları izleyiniz.

      $ cd frontend/project
      $ npm install
      $ npm run dev

    Proje http://localhost:8080 linkinden ulaşılabilir halde başlamıştır.

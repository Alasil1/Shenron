# Shenron
Shenron :
Your one-stop site for movies lovers, by any stretch of the imagination.

Shenron is a dynamic website for film enthusiasts to discover, share, and review their movies and shows.open discussion forums,and favourite list, Shenron also aspires to be an IMDb alternative with fairness at its heart and a truly community-oriented approach.

Current Status :
System Integration: The backend, frontend, and database are fully integrated and functional, meeting the required implementation percentage.
Documentation: Comprehensive documentation provided for backend and frontend.

Features :
Search Movies: Find detailed information about your favorite movies usig their titles.
Discussion Forums: Engage in lively debates and share your opinions in topic-driven forums.
Personal favourites list: Have your own list of the movies you love.

Tech Stack:
Backend: Django with Django REST Framework (APIs for data handling and user interaction).
Frontend: HTML, CSS (ensuring a sleek and user-friendly experience).
Database: MySQL (robust storage for movies, reviews, and user data).

Installation & Setup :
Prerequisites:
    Python: version 3.11 (preferably)
    django: version 5.1
    MySQL: version 8.0 or higher
Steps
    1.Clone the repository: 
    -git clone https://github.com/omaryasser3/Shenron.git     
    -cd Shenron 
    2.Install dependencies:

    -pip install django
    -pip install mysqlclient
    -pip install requests

    3.Set up the database:

    -Configure your settings.py to match your MySQL database credentials.
    -Run migrations:
        python manage.py makemigrations (py manege.py makemigrations for windows)
        python manage.py migrate        (py manage.py migrate for windows)
    4.Run the server:
        -python manage.py runserver     (py manage.py runserver for windows)
    5.Access Shenron:
    -Open your browser and navigate to http://127.0.0.1:8000/
    
PS: 
    - It is recommended to use pycharm as the IDE.
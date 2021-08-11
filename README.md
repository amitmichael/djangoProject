# matchFinderProject

Please clone the repository and run the following commands: <br>
1.```python manage.py runserver ```<br>
2.```python manage.py migrate```<br>
2. go to http://127.0.0.1:8000/matchFinder/ *to load the sample data* (index function calls load_sample_data.py that writes to the database). <br>
3. on http://127.0.0.1:8000/matchFinder/<job_id> You'll find the matching candidate list: 
  - ids 1-6 are valid at the moment. you can add your own on http://127.0.0.1:8000/admin 

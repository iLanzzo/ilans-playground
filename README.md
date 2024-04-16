Welcome to my first DevOps project.

.

This project holds two containers, one for MySQL the other for myapp.

Using docker compose it builds myapp image using python apline and creates another container for the database using MySQL.

The code builds everything up including the database itself.

Once it's up, the app connects to MySQL's database via the network and prints the data from the DB.

To run the app - follow the steps:

.

1 - Download the contnent (including: myapp folder, compose.yml).

2 - Save everything as is in a folder.

3 - Run "docker compose up -d" from the main folder.

4 - Connect to 'devproj-app' container that runs the code using - 'docker exec -it devproj-app bash'.

  4.1 - You can run a script to see the current data in the database using - 'python display_table.py' (if it's empty, the app will create database).
  
5 - Run the app container using - 'docker exec -it devproj-app bash' then run 'python app.py', it will print the data from the database.

.

Thanks, 

Ilan G.

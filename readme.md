# Heading RESTful API for user registration in the database for the login panel of the mobile application using the Python programming language and the Flask library.

---

## Startup guide:

1. The command line user (CMD console, Git Bash, etc.) must start the Python virtual runtime with "source env/Script/activate".
2. After entering the above command, user should use python run.py or py run.py command to run Flask server.
3. The next step is to launch the selected API platform, in which the user must enter registration data in a file with the json extension to be able to connect to the address http://127.0.0.1:5000/api/register and transfer the entered data to the database .
4. After creating the user, the option to login to the application is required. To do this, the user must restart the selected API platform and then enter the login details into the application. This action must be performed at the address http://127.0.0.1:5000/api/login. The login details are also entered in the json file. Logging in is possible via a username and password, but the password entered during registration is automatically encrypted, so when logging in, the user must already enter the generated token with the encrypted password.
5. To be able to check the entered data, the user can use the "GET" command at the address http://127.0.0.1:5000/api/register.
6. Another option is to use the database command console to check the entered data or possibly remove the data from the database.
7. The user who wants to access the database via a dedicated command console (psql) must call it from the system and then enter the required access data.

## App Description:

The "crypto_reader" application is a project created for engineering work, which mainly focuses on Blockchain technology. The application uses digital currencies, therefore it was necessary to secure the application with the option of logging in to resources. To create the logical layer of the application, I used the connect_db.py file, which connects to the database created in PostgreSQL, the file contains login data to the database. The endpoints file contains endpoint addresses. The migrate.py file in the file has been created code that allows you to modify and migrate the database template. The template.py file contains the necessary code to create a database model into which data will be implemented by users. The files directory contains two files named Register.py and Login.py. The first file is created for user registration in the database, the file has options to register the user in the system, an additional option is password encryption with the SHA256 algorithm.
The second Login.py file forces the user to enter the data, i.e. username and encrypted password.
All user data is stored in a database created in PostgreSQL.
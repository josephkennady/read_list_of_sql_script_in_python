# -read_list_of_sql_script_in_python

The script imports the following libraries:

* os: This library is used to retrieve the name of the SQL script file from the path.
* glob: This library is used to get a list of all the SQL script files in a given folder.
* create_engine: This function from the sqlalchemy library is used to create a connection to the MySQL database.
* pymysql: This library is used as the MySQL connector for sqlalchemy.
* pandas: This library is used to store the result of the SQL script in a DataFrame and write it to a CSV file.

The script then defines the following constants with the MySQL database connection details:

* DB_USER: The username to connect to the MySQL database.
* DB_PASSWORD: The password for the MySQL user.
* DB_HOST: The hostname or IP address of the MySQL server.
* DB_PORT: The port number of the MySQL server.
* DB_NAME: The name of the database to connect to.

Next, the script creates a connection string for sqlalchemy using the above constants and uses it to create a connection to the MySQL database using the create_engine function.

The script then defines the following constants:

* folder_path: The path to the folder containing the SQL scripts.
* sql_scripts: A list of the paths to all the SQL script files in the folder specified by folder_path.

The script then loops through the list of sql_scripts, reads each script into a string, and executes it using pd.read_sql_query. The result is stored in a DataFrame.

The script then gets the name of the SQL script file (without the path or the '.sql' extension) using `os.path

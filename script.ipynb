!pip install sqlalchemy
!pip install PyMySQL
!pip install pandas

import os
import glob

from sqlalchemy import create_engine
import pymysql
import pandas as pd

# Replace with your MySQL database connection details
DB_USER = 'username'
DB_PASSWORD = 'password'
DB_HOST = 'localhost'
DB_PORT = 3306
DB_NAME = 'database_name'

# Set the connection string for SQLAlchemy
conn_str = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
engine = create_engine(conn_str)

# Set the path to the folder containing the SQL scripts
folder_path = '/path/to/folder/'

# Get a list of all the SQL scripts in the folder
sql_scripts = glob.glob(folder_path + '*.sql')

# Loop through the list of SQL scripts
for script_path in sql_scripts:
    # Read the SQL script into a string
    with open(script_path, 'r') as script_file:
        sql_script = script_file.read()

    # Execute the SQL script and store the result in a Pandas DataFrame
    df = pd.read_sql_query(sql_script, engine)

    # Get the name of the SQL script (without the path or the '.sql' extension)
    script_name = os.path.basename(script_path).replace('.sql', '')

    # Save the DataFrame to a CSV file with the same name as the SQL script
    df.to_csv(f'{folder_path}{script_name}.csv', index=False)

print('All scripts have been executed and the results have been saved to CSV files')

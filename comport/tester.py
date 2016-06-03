import cx_Oracle

class Tester:

    def __init__(self, config_values):
        # save required values into a config object
        self.config = dict()
        self.config['oracle_host'] = config_values['oracle_host']
        self.config['oracle_port'] = int(config_values['oracle_port'])
        self.config['oracle_database'] = config_values['oracle_database']
        self.config['oracle_username'] = config_values['oracle_username']
        self.config['oracle_password'] = config_values['oracle_password']

    def get_database_connection(self):
        ''' Connect to the database, return the cursor.
        '''
        # Connect to the database server.
        # iapro-oracle.cr87k6k55djc.us-east-1.rds.amazonaws.com:1521/IAPRODB
        dsn_tns = cx_Oracle.makedsn(self.config['oracle_host'], self.config['oracle_port'], self.config['oracle_database'])
        conn = cx_Oracle.connect(self.config['oracle_username'], self.config['oracle_password'], dsn_tns)
        return conn

    def check_connection(self):
        ''' Try to make a connection to the Oracle database.
        '''
        print("* Trying to connect to Oracle database: {host}:{port}/{db} as {username}".format(host=self.config['oracle_host'], port=self.config['oracle_port'], db=self.config['oracle_database'], username=self.config['oracle_username']))

        # make a connection to the database
        conn = self.get_database_connection()

        print("* Successful connection to database with version {}!".format(conn.version))

        # Close the database connection.
        conn.close()
        print("* Closed connection to Oracle database.")
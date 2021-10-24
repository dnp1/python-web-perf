from os import environ

PG_DATABASE = environ['PGDATABASE']
PG_USER = environ['PGUSER']
PG_PASSWORD = environ['PGPASSWORD']
PG_HOST = environ['PGHOST']
PG_PORT = int(environ.get('PGPORT', '5432'))
PG_POOL_SIZE = int(environ.get('POOL_SIZE', '10'))

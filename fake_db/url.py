from envparse import env

env.read_envfile('.env')
db_config = {
    "host": env('HOST_'),
    "user": env('USER_'),
    "password": env('PASSWORD_'),
    "database": env('DB_')
}


# # use library psycopg2-binary to connect to a Database

# # CREATE USER psycopg_test_user WITH CREATEDB PASSWORD 'password';
# # CREATE DATABASE psycopg_test_db WITH OWNER psycopg_test_user;
# # -- This is really bad security and should not be done in real-world
# # -- application programming.

# # CREATE TABLE owners (
# #   id SERIAL PRIMARY KEY,
# #   first_name VARCHAR(255) NOT NULL,
# #   last_name VARCHAR(255) NOT NULL,
# #   email VARCHAR(255) NOT NULL
# # );

# # # -- Make and model should have their own tables
# # # -- Simplified for now
# # CREATE TABLE cars (
# #   id SERIAL PRIMARY KEY,
# #   manu_year INTEGER NOT NULL,
# #   make VARCHAR(255),
# #   model VARCHAR(255),
# #   owner_id INTEGER NOT NULL,
# #   FOREIGN KEY (owner_id) REFERENCES owners(id)
# # );

# # INSERT INTO owners (first_name, last_name, email)
# # VALUES
# # ('Tim', 'Petrol', 'rotary@fast.com'),
# # ('Ryan', 'Runner', '10sec@jdm.com'),
# # ('Tia', 'Petrol', 'typer@wtec.com');

# # INSERT INTO cars (manu_year, make, model, owner_id)
# # VALUES
# # (1993, 'Mazda', 'Rx7', 1),
# # (1995, 'Mitsubishi', 'Eclipse', 2),
# # (1994, 'Acura', 'Integra', 3);

# import psycopg2

# CONNECTION_PARAMETERS = {
#     'dbname': 'psycopg_test_db',
#     'user': 'psycopg_test_user',
#     'password': 'password',
# }

# with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
#     print(conn.get_dsn_parameters())
#     # Output: {'user': 'psycopg_test_user', 'dbname': 'psycopg_test_db', ...}

# # cursor objects are iterable
# with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
#     with conn.cursor() as curs:
#         curs.execute('SELECT * FROM cars;')
#         cars = curs.fetchall()
#         for car in cars:
#             print(car) # (1993, 'Mazda', 'Rx7')


# def print_all_cars():
#     with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
#         with conn.cursor() as curs:
#             curs.execute('SELECT manu_year, make, model, owner_id FROM cars;')
#             cars = curs.fetchall()
#             for car in cars:
#                 print(car)  

# print_all_cars()

# # Parameterizing 
# # Fetch and return all cars in the cars table :param owner_id: <int> the id of 
# # the owner who's cars to return :return: <list> the results of the query
# def get_owners_cars(owner_id):
#     with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
#         with conn.cursor() as curs:
#             curs.execute("""
#                          SELECT manu_year, make, model FROM cars
#                          WHERE owner_id = %(owner_id)s
#                          """,
#                          {'owner_id': owner_id})
#             results = curs.fetchall()
#             return results

# print(get_owners_cars(1)) # [(1993, 'Mazda', 'Rx7')]
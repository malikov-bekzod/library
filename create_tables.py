from connection import postgres_conn
cursor = postgres_conn.cursor()

def create_tables():

    cursor.execute("""CREATE TABLE author(
                   author_id SERIAL NOT NULL PRIMARY KEY,
                   first_name VARCHAR(20) NOT NULL,
                   last_name VARCHAR(20) NOT NULL,
                   birth_date DATE NOT NULL,
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")

    cursor.execute("""CREATE TABLE book(
                   book_id SERIAL NOT NULL PRIMARY KEY,
                   name VARCHAR(50) NOT NULL,
                   description TEXT,
                   cost NUMERIC(8,2) NOT NULL,
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")


    cursor.execute("""CREATE TABLE book_author(
                   book_id INT NOT NULL REFERENCES book(book_id),
                   author_id INT NOT NULL REFERENCES author(author_id),
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")



    cursor.execute("""CREATE TABLE "region"(
                   region_id SERIAL NOT NULL PRIMARY KEY,
                   name VARCHAR(50) NOT NULL,
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")


    cursor.execute("""CREATE TABLE "address"(
                   address_id SERIAL NOT NULL PRIMARY KEY,
                   address VARCHAR(50) NOT NULL,
                   district VARCHAR(40) NOT NULL,
                   region_id INT NOT NULL REFERENCES region(region_id),
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")



    cursor.execute("""CREATE TABLE staff(
                   staff_id SERIAL NOT NULL PRIMARY KEY,
                   first_name VARCHAR(20) NOT NULL,
                   last_name VARCHAR(20) NOT NULL,
                   address_id INT NOT NULL REFERENCES address(address_id),
                   phone_number VARCHAR(20) NOT NULL,
                   email VARCHAR(60) NOT NULL,
                   username VARCHAR(20) NOT NULL,
                   password VARCHAR(20) NOT NULL,
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")


    cursor.execute("""CREATE TABLE customer(
                   customer_id SERIAL NOT NULL PRIMARY KEY,
                   first_name VARCHAR(20) NOT NULL,
                   last_name VARCHAR(20) NOT NULL,
                   address_id INT NOT NULL REFERENCES address(address_id),
                   phone_number VARCHAR(20) NOT NULL,
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")





    cursor.execute("""CREATE TABLE rental(
                   rental_id SERIAL NOT NULL PRIMARY KEY,
                   customer_id INT NOT NULL REFERENCES customer(customer_id),
                   book_id INT NOT NULL REFERENCES book(book_id),
                   create_date DATE NOT NULL,
                   return_date DATE NOT NULL,
                   staff_id INT NOT NULL REFERENCES staff(staff_id),
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")
    



    cursor.execute("""CREATE TABLE payment(
                   payment_id SERIAL NOT NULL PRIMARY KEY,
                   rental_id INT NOT NULL REFERENCES rental(rental_id),
                   payment_date DATE NOT NULL,
                   amount NUMERIC(8,2) NOT NULL,
                   staff_id INT NOT NULL REFERENCES staff(staff_id),
                   customer_id INT NOT NULL REFERENCES customer(customer_id),
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")



    postgres_conn.commit()
    print("CREATE TABLE")

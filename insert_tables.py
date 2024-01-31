from connection import postgres_conn

cursor = postgres_conn.cursor()

def insert_tables():

    cursor.execute(f"INSERT INTO author(first_name,last_name,birth_date) VALUES('alisher','navoiy','1441-02-09')")


    cursor.execute(f"INSERT INTO book(name,description,cost) VALUES('xamsa','bu asar doston shaklida yozilgan bolib 5 ta qismdan iborat',34_000.145)")


    cursor.execute(f"INSERT INTO book_author(book_id,author_id) VALUES(1,1)")


    cursor.execute(f"INSERT INTO region(name) VALUES('toshkent')")


    cursor.execute(f"INSERT INTO address(address,district,region_id) VALUES('171 oltariq','olmaliq',1)")


    cursor.execute(f"INSERT INTO staff(first_name,last_name,address_id,phone_number, email, username,password) VALUES('qahhor','abdulatipov',1,'+998-94-343-45-23','sjfssdfjsdjfsj@gmail.com','staff123','passwrd123')")



    cursor.execute(f"INSERT INTO customer(first_name,last_name,address_id,phone_number) VALUES('polat','ravshanov',1,'+998-91-123-45-67')")


    cursor.execute(f"INSERT INTO rental(customer_id,book_id,create_date,return_date,staff_id) VALUES(1,1,'22-01-2023','22-02-2023',1)")


    cursor.execute(f"INSERT INTO payment(rental_id,payment_date,amount,staff_id,customer_id) VALUES(1,'02-09-2023',34_000.145,1,1)")


    postgres_conn.commit()
    print("INSERT 0 1")

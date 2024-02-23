from base import Database

def createTable():
    country_table = f"""
        CREATE TABLE country(
            country_id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            last_update TIMESTAMP DEFAULT now());"""

    city_table = f"""
        CREATE TABLE city(
            city_id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            country_id INT REFERENCES country(country_id),
            last_update TIMESTAMP DEFAULT now());"""
    
    address = f"""
        CREATE TABLE address(
            address_id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            city_id INT REFERENCES city(city_id),
            last_update TIMESTAMP DEFAULT now());"""
    
    customer = f"""
        CREATE TABLE customer(
            customer_id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50),
            phone_number VARCHAR(10) NOT NULL,
            password VARCHAR(10),
            birth_date DATE NOT NULL,
            address_id INT REFERENCES address(address_id),
            last_update TIMESTAMP DEFAULT now());"""

    product = f"""
        CREATE TABLE product(
            product_id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            description TEXT,
            rating FLOAT,
            create_date DATE,
            last_update TIMESTAMP DEFAULT now());"""
    
    product_type = f"""
        CREATE TABLE product_type(
            product_type_id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            price FLOAT NOT NULL,
            color VARCHAR(20),
            product_id INT REFERENCES product(product_id),
            last_update TIMESTAMP DEFAULT now());"""
    
    category = f"""
        CREATE TABLE category(
            category_id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            description TEXT,
            last_update TIMESTAMP DEFAULT now(),
            create_date DATE);"""
    
    product_category = f"""
        CREATE TABLE product_category(
            product_category_id SERIAL PRIMARY KEY,
            product_id INT REFERENCES product(product_id),
            category_id INT REFERENCES category(category_id),
            last_update TIMESTAMP DEFAULT now());"""
    
    payment_type = f"""
        CREATE TABLE payment_type(
            payment_type_id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            last_update TIMESTAMP DEFAULT now());"""
    
    payment = f"""
        CREATE TABLE payment(
            payment_id SERIAL PRIMARY KEY,
            amount FLOAT,
            payment_type_id INT REFERENCES payment_type(payment_type_id),
            last_update TIMESTAMP DEFAULT now());"""
    
    product_customer = f"""
        CREATE TABLE product_customer(
            product_customer_id SERIAL PRIMARY KEY,
            product_id INT REFERENCES product(product_id),
            customer_id INT REFERENCES customer(customer_id),
            last_update TIMESTAMP DEFAULT now());"""
    
    branch = f"""
        CREATE TABLE branch(
            store_id SERIAL PRIMARY KEY,
            name VARCHAR(20),
            description TEXT,
            address_id INT REFERENCES address(address_id),
            create_date DATE,
            last_update TIMESTAMP DEFAULT now());"""
    
    dataTable = {
        "country_table": country_table,
        "city_table": city_table,
        "address": address,
        "customer": customer,
        "product": product,
        "product_type": product_type,
        "category": category,
        "product_category": product_category,
        "payment_type": payment_type,
        "payment" : payment,
        "product_customer": product_customer,
        "branch": branch    
    }

#     for i in dataTable:
#         print(f"{i} {Database.connect(dataTable[i], "create")}")
#
#
# if __name__ == "__main__":
#     createTable()
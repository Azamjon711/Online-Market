from base import Database


class Country:
    def __init__(self, name: str):
        self.name = name

    def insert(self, table="country"):
        query = f"""INSERT INTO {table}(name) 
        VALUES('{self.name}');"""
        return Database.connect(query, "insert")

    @staticmethod
    def select(table="country"):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")

    @staticmethod
    def delete(column, data, table="country"):
        query = f"""DELETE FROM {table} WHERE {column} = '{data}';"""
        return Database.connect(query, "delete")

    @staticmethod
    def deleteID(column, data, table="country"):
        query = f"""DELETE FROM {table} WHERE {column} = {data};"""
        return Database.connect(query, "delete")

    @staticmethod
    def update(column, data, idColumn, id, table="country"):
        # faqat ID bo'yicha UPDATE qilish
        query = f"""UPDATE {table} SET {column} = '{data}' WHERE {idColumn} = {id};"""
        return Database.connect(query, "update")


class City(Country):
    def __init__(self, name: str, country_id: int):
        super().__init__(name)
        self.country_id = country_id

    def insert(self, table="city"):
        query = f"""INSERT INTO {table}(name, country_id) 
        VALUES('{self.name}', {self.country_id});"""
        return Database.connect(query, "insert")


class Address(Country):
    def __init__(self, name: str, city_id: int):
        super().__init__(name)
        self.city_id = city_id

    def insert(self, table="address"):
        query = f"""INSERT INTO {table}(name, city_id) 
        VALUES('{self.name}', {self.city_id});"""
        return Database.connect(query, "insert")


class Customer:
    def __init__(self, first_name: str, last_name: str, phone_number: str, password: str, birth_date: str, address_id: int):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.password = password
        self.birth_date = birth_date
        self.address_id = address_id

    def insert(self, table="customer"):
        query = f"""INSERT INTO {table}(name) 
        VALUES('{self.first_name}', '{self.last_name}', '{self.phone_number}', '{self.password}', '{self.birth_date}', {self.address_id});"""
        return Database.connect(query, "insert")

    @staticmethod
    def select(table="customer"):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")

    @staticmethod
    def delete(column, data, table="customer"):
        query = f"""DELETE FROM {table} WHERE {column} = '{data}';"""
        return Database.connect(query, "delete")

    @staticmethod
    def deleteID(column, data, table="customer"):
        query = f"""DELETE FROM {table} WHERE {column} = {data};"""
        return Database.connect(query, "delete")

    @staticmethod
    def update(column, data, idColumn, id, table="customer"):
        # faqat ID bo'yicha UPDATE qilish
        query = f"""UPDATE {table} SET {column} = '{data}' WHERE {idColumn} = {id};"""
        return Database.connect(query, "update")


class Product:
    def __init__(self, name: str, description: str, rating: float, create_date: str):
        self.name = name
        self.description = description
        self.rating = rating
        self.create_date = create_date

    @staticmethod
    def select(table="product"):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")

    def insert(self, table="product"):
        query = f"""INSERT INTO {table}(title, description, rating, create_date) 
        VALUES('{self.name}', '{self.description}', {self.rating}, '{self.create_date}');"""
        return Database.connect(query, "insert")

    @staticmethod
    def delete(column, data, table="product"):
        query = f"""DELETE FROM {table} WHERE {column} = '{data};'"""
        return Database.connect(query, "delete")

    @staticmethod
    def deleteID(column, data, table="product"):
        query = f"""DELETE FROM {table} WHERE {column} = {data};"""
        return Database.connect(query, "delete")

    @staticmethod
    def update(column, data, idColumn, id, table="product"):
        # faqat ID bo'yicha UPDATE qilish
        query = f"""UPDATE {table} SET {column} = '{data}' WHERE {idColumn} = {id};"""
        return Database.connect(query, "update")


class ProductType:
    def __init__(self, name:str, color:str, price:float, product_id:int):
        self.name = name
        self.color = color
        self.price = price
        self.product_id = product_id

    @staticmethod
    def select(table = "product_type"):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")
    
    def insert(self, table = "product_type"):
        query = f"""INSERT INTO {table}(name, color, price, product_id) 
        VALUES('{self.name}', '{self.color}', {self.price}, {self.product_id});"""
        return Database.connect(query, "insert")
    
    @staticmethod
    def delete(column, data, table = "product_type"):
        query = f"""DELETE FROM {table} WHERE {column} = '{data}';"""
        return Database.connect(query, "delete")
    
    @staticmethod
    def deleteID(column, data, table = "product_type"):
        query = f"""DELETE FROM {table} WHERE {column} = {data};"""
        return Database.connect(query, "delete")
    
    @staticmethod
    def update(column, data, idColumn, id, table="product_type"):
        # faqat ID bo'yicha UPDATE qilish
        query = f"""UPDATE {table} SET {column} = '{data}' WHERE {idColumn} = {id};"""
        return Database.connect(query, "update")

class Category:
    def __init__(self, name:str, description:str, create_date:str):
        self.name = name
        self.description = description
        self.create_date = create_date
    
    @staticmethod
    def select(table = "category"):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")
    
    def insert(self, table = "category"):
        query = f"""INSERT INTO {table}(name, description, create_date) 
        VALUES('{self.name}', '{self.description}', '{self.create_date}');"""
        return Database.connect(query, "insert")
    
    @staticmethod
    def delete(column, data, table = "category"):
        query = f"""DELETE FROM {table} WHERE {column} = '{data}';"""
        return Database.connect(query, "delete")
    
    @staticmethod
    def deleteID(column, data, table = "category"):
        query = f"""DELETE FROM {table} WHERE {column} = {data};"""
        return Database.connect(query, "delete")

    @staticmethod
    def update(column, data, idColumn, id, table="category"):
        # faqat ID bo'yicha UPDATE qilish
        query = f"""UPDATE {table} SET {column} = '{data}' WHERE {idColumn} = {id};"""
        return Database.connect(query, "update")


class ProductCategory:
    def __init__(self, product_id:int, category_id:int):
        self.product_id = product_id
        self.category_id = category_id

    @staticmethod
    def select(table = "product_category"):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")
    
    def insert(self, table = "product_category"):
        query = f"""INSERT INTO {table}(product_id, category_id) 
        VALUES({self.product_id}, {self.category_id});"""
        return Database.connect(query, "insert")
    
    @staticmethod
    def delete(column, data, table = "product_category"):
        query = f"""DELETE FROM {table} WHERE {column} = '{data}';"""
        return Database.connect(query, "delete")
    
    @staticmethod
    def deleteID(column, data, table = "product_category"):
        query = f"""DELETE FROM {table} WHERE {column} = {data};"""
        return Database.connect(query, "delete")
    
    @staticmethod
    def update(column, data, idColumn, id, table="product_category"):
        # faqat ID bo'yicha UPDATE qilish
        query = f"""UPDATE {table} SET {column} = '{data}' WHERE {idColumn} = {id};"""
        return Database.connect(query, "update")


class PaymentType:
    def __init__(self, name:str):
        self.name = name

    @staticmethod
    def select(table = "payment_type"):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")
    
    def insert(self, table = "payment_type"):
        query = f"""INSERT INTO {table}(name) 
        VALUES('{self.name}');"""
        return Database.connect(query, "insert")
    
    @staticmethod
    def delete(column, data, table = "payment_type"):
        query = f"""DELETE FROM {table} WHERE {column} = '{data}';"""
        return Database.connect(query, "delete")
    
    @staticmethod
    def deleteID(column, data, table = "payment_type"):
        query = f"""DELETE FROM {table} WHERE {column} = {data};"""
        return Database.connect(query, "delete")

    @staticmethod
    def update(column, data, idColumn, id, table="payment_type"):
        # faqat ID bo'yicha UPDATE qilish
        query = f"""UPDATE {table} SET {column} = '{data}' WHERE {idColumn} = {id};"""
        return Database.connect(query, "update")

class Payment:
    def __init__(self, amount:float, payment_type_id:int):
        self.amount = amount
        self.payment_type_id = payment_type_id

    @staticmethod
    def select(table = "payment"):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")
    
    def insert(self, table = "payment"):
        query = f"""INSERT INTO {table}(name, payment_type_id) 
        VALUES('{self.name}', {self.payment_type_id});"""
        return Database.connect(query, "insert")
    
    @staticmethod
    def delete(column, data, table = "payment"):
        query = f"""DELETE FROM {table} WHERE {column} = '{data}';"""
        return Database.connect(query, "delete")
    
    @staticmethod
    def deleteID(column, data, table = "payment"):
        query = f"""DELETE FROM {table} WHERE {column} = {data};"""
        return Database.connect(query, "delete")

    @staticmethod
    def update(column, data, idColumn, id, table="payment"):
        # faqat ID bo'yicha UPDATE qilish
        query = f"""UPDATE {table} SET {column} = '{data}' WHERE {idColumn} = {id};"""
        return Database.connect(query, "update")

class ProductCustomer:
    def __init__(self, product_id:int, customer_id:int):
        self.product_id = product_id
        self.customer_id = customer_id

    @staticmethod
    def select(table = "product_customer"):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")
    
    def insert(self, table = "product_customer"):
        query = f"""INSERT INTO {table}(product_id, customer_id) 
        VALUES({self.product_id}, {self.customer_id});"""
        return Database.connect(query, "insert")
    
    @staticmethod
    def delete(column, data, table = "product_customer"):
        query = f"""DELETE FROM {table} WHERE {column} = '{data};'"""
        return Database.connect(query, "delete")
    
    @staticmethod
    def delete_id(column, data, table = "product_customer"):
        query = f"""DELETE FROM {table} WHERE {column} = {data};"""
        return Database.connect(query, "delete")

    @staticmethod
    def update(column, data, idColumn, id, table="product_customer"):
        # faqat ID bo'yicha UPDATE qilish
        query = f"""UPDATE {table} SET {column} = '{data}' WHERE {idColumn} = {id};"""
        return Database.connect(query, "update")


class Branch:
    def __init__(self, name:str, description:str, address_id:int, create_date:str):
        self.name = name
        self.description = description
        self.address_id = address_id
        self.create_date = create_date

    @staticmethod
    def select(table = "branch"):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")
    
    def insert(self, table = "branch"):
        query = f"""INSERT INTO {table}(name, description, address_id, create_date) 
        VALUES('{self.name}', '{self.description}', {self.address_id}, '{self.create_date}');"""
        return Database.connect(query, "insert")
    
    @staticmethod
    def delete(column, data, table = "branch"):
        query = f"""DELETE FROM {table} WHERE {column} = '{data}';"""
        return Database.connect(query, "delete")
    
    @staticmethod
    def deleteID(column, data, table = "branch"):
        query = f"""DELETE FROM {table} WHERE {column} = {data};"""
        return Database.connect(query, "delete")

    @staticmethod
    def update(column, data, idColumn, id, table="branch"):
        # faqat ID bo'yicha UPDATE qilish
        query = f"""UPDATE {table} SET {column} = '{data}' WHERE {idColumn} = {id};"""
        return Database.connect(query, "update")



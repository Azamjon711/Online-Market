import mainDb
import classes


def countryTable():
    move = input("""
        1.Insert
        2.Select
        3.Delete
        4.Update
        0.Back
>>> """)

    if move == "1":
        name = input("Name: ")
        country = classes.Country(name)
        print(country.insert())
        return countryTable()

    elif move == "2":
        for i in classes.Country.select("country"):
            print(i)
        return countryTable()

    elif move == "3":
        column = input("Column: ")
        data = input("Data: ")
        if column != "country_id":
            print(classes.Country.delete(column, data))
        else:
            print(classes.Country.deleteID(column, data))
        return countryTable()

    elif move == "4":
        column = input("Column name: ")
        data = input("New data: ")
        idColumn = input("ID Column name: ")
        id = input("ID: ")
        print(classes.Country.update(column, data, idColumn, id))
        return countryTable()

    elif move == "0":
        return mainDb.main()

    else:
        print("ERROR!!!")
        return countryTable()


def cityTable():
    move = input("""
            1.Insert
            2.Select
            3.Delete
            4.Update
            0.Back
    >>> """)

    if move == "1":
        name = input("Name: ")
        countryId = input("Country ID: ")
        city = classes.City(name, countryId)
        print(city.insert())
        return cityTable()

    elif move == "2":
        for i in classes.City.select("city"):
            print(i)
        return cityTable()

    elif move == "3":
        column = input("Column: ")
        data = input("Data: ")
        if column != "city_id":
            print(classes.Country.delete(column, data, "city"))
        else:
            print(classes.Country.deleteID(column, data, "city"))
        return cityTable()

    elif move == "4":
        column = input("Column name: ")
        data = input("New data: ")
        idColumn = input("ID Column name: ")
        id = input("ID: ")
        print(classes.Country.update(column, data, idColumn, id, "city"))
        return cityTable()

    elif move == "0":
        return mainDb.main()

    else:
        print("ERROR!!!")
        return cityTable()


def addressTable():
    move = input("""
            1.Insert
            2.Select
            3.Delete
            4.Update
            0.Back
    >>> """)

    if move == "1":
        name = input("Name: ")
        cityId = input("City ID: ")
        address = classes.Address(name, cityId)
        print(address.insert())
        return addressTable()

    elif move == "2":
        for i in classes.Address.select("address"):
            print(i)
        return addressTable()

    elif move == "3":
        column = input("Column: ")
        data = input("Data: ")
        if column != "address_id":
            print(classes.Address.delete(column, data, "address"))
        else:
            print(classes.Address.deleteID(column, data, "address"))
        return addressTable()

    elif move == "4":
        column = input("Column name: ")
        data = input("New data: ")
        idColumn = input("ID Column name: ")
        id = input("ID: ")
        print(classes.Address.update(column, data, idColumn, id, "address"))
        return addressTable()

    elif move == "0":
        return mainDb.main()

    else:
        print("ERROR!!!")
        return addressTable()


def customerTable():
    move = input("""
            1.Insert
            2.Select
            3.Delete
            4.Update
            0.Back
    >>> """)

    if move == "1":
        firstName = input("First Name: ")
        lastName = input("Last Name: ")
        phoneNumber = input("Phone Number: ")
        password = input("Password: ")
        birthDate = input("Birth Date: ")
        addressId = input("Address ID: ")
        customer = classes.Customer(firstName, lastName, phoneNumber, password, birthDate, addressId)
        print(customer.insert())
        return customerTable()

    elif move == "2":
        for i in classes.Customer.select():
            print(i)
        return customerTable()

    elif move == "3":
        column = input("Column: ")
        data = input("Data: ")
        if column != "customer_id":
            print(classes.Customer.delete(column, data))
        else:
            print(classes.Customer.deleteID(column, data))
        return customerTable()

    elif move == "4":
        column = input("Column name: ")
        data = input("New data: ")
        idColumn = input("ID Column name: ")
        id = input("ID: ")
        print(classes.Customer.update(column, data, idColumn, id))
        return customerTable()

    elif move == "0":
        return mainDb.main()

    else:
        print("ERROR!!!")
        return customerTable()


def productTable():
    move = input("""
            1.Insert
            2.Select
            3.Delete
            4.Update
            0.Back
    >>> """)

    if move == "1":
        name = input("Name: ")
        description = input("Description: ")
        rating = input("Rating: ")
        createDate = input("Create Date: ")
        product = classes.Product(name, description, rating, createDate)
        print(product.insert())
        return productTable()

    elif move == "2":
        for i in classes.Product.select():
            print(i)
        return productTable()

    elif move == "3":
        column = input("Column: ")
        data = input("Data: ")
        if column != "product_id":
            print(classes.Product.delete(column, data))
        else:
            print(classes.Product.deleteID(column, data))
        return productTable()

    elif move == "4":
        column = input("Column name: ")
        data = input("New data: ")
        idColumn = input("ID Column name: ")
        id = input("ID: ")
        print(classes.Product.update(column, data, idColumn, id))
        return productTable()

    elif move == "0":
        return mainDb.main()

    else:
        print("ERROR!!!")
        return productTable()


def productTypeTable():
    move = input("""
            1.Insert
            2.Select
            3.Delete
            4.Update
            0.Back
    >>> """)

    if move == "1":
        name = input("Name: ")
        price = input("Price: ")
        color = input("Color: ")
        productId = input("Product ID: ")
        productType = classes.ProductType(name, color, price, productId)
        print(productType.insert())
        return productTypeTable()

    elif move == "2":
        for i in classes.ProductType.select():
            print(i)
        return productTypeTable()

    elif move == "3":
        column = input("Column: ")
        data = input("Data: ")
        if column != "product_type_id":
            print(classes.ProductType.delete(column, data))
        else:
            print(classes.ProductType.deleteID(column, data))
        return productTypeTable()

    elif move == "4":
        column = input("Column name: ")
        data = input("New data: ")
        idColumn = input("ID Column name: ")
        id = input("ID: ")
        print(classes.ProductType.update(column, data, idColumn, id))
        return productTypeTable()

    elif move == "0":
        return mainDb.main()

    else:
        print("ERROR!!!")
        return productTypeTable()


def categoryTable():
    move = input("""
            1.Insert
            2.Select
            3.Delete
            4.Update
            0.Back
    >>> """)

    if move == "1":
        name = input("Name: ")
        description = input("Description: ")
        createDate = input("Create Date: ")
        category = classes.Category(name, description, createDate)
        print(category.insert())
        return categoryTable()

    elif move == "2":
        for i in classes.Category.select():
            print(i)
        return categoryTable()

    elif move == "3":
        column = input("Column: ")
        data = input("Data: ")
        if column != "category_id":
            print(classes.Category.delete(column, data))
        else:
            print(classes.Category.deleteID(column, data))
        return categoryTable()

    elif move == "4":
        column = input("Column name: ")
        data = input("New data: ")
        idColumn = input("ID Column name: ")
        id = input("ID: ")
        print(classes.Course.update(column, data, idColumn, id))
        return categoryTable()

    elif move == "0":
        return mainDb.main()

    else:
        print("ERROR!!!")
        return categoryTable()


def productCategoryTable():
    move = input("""
            1.Insert
            2.Select
            3.Delete
            4.Update
            0.Back
    >>> """)

    if move == "1":
        productId = input("Product ID: ")
        categoryId = input("Category ID: ")
        prodCat = classes.ProductCategory(productId, categoryId)
        print(prodCat.insert())
        return productCategoryTable()

    elif move == "2":
        for i in classes.ProductCategory.select():
            print(i)
        return productCategoryTable()

    elif move == "3":
        column = input("Column: ")
        data = input("Data: ")
        if column != "product_category_id":
            print(classes.ProductCategory.delete(column, data))
        else:
            print(classes.ProductCategory.deleteID(column, data))
        return productCategoryTable()

    elif move == "4":
        column = input("Column name: ")
        data = input("New data: ")
        idColumn = input("ID Column name: ")
        id = input("ID: ")
        print(classes.ProductCategory.update(column, data, idColumn, id))
        return productCategoryTable()

    elif move == "0":
        return mainDb.main()

    else:
        print("ERROR!!!")
        return productCategoryTable()


def paymentTypeTable():
    move = input("""
            1.Insert
            2.Select
            3.Delete
            4.Update
            0.Back
    >>> """)

    if move == "1":
        name = input("Name: ")
        paymentType = classes.PaymentType(name)
        print(paymentType.insert())
        return paymentTypeTable()

    elif move == "2":
        for i in classes.PaymentType.select():
            print(i)
        return paymentTypeTable()

    elif move == "3":
        column = input("Column: ")
        data = input("Data: ")
        if column != "payment_type_id":
            print(classes.PaymentType.delete(column, data))
        else:
            print(classes.PaymentType.deleteID(column, data))
        return paymentTypeTable()

    elif move == "4":
        column = input("Column name: ")
        data = input("New data: ")
        idColumn = input("ID Column name: ")
        id = input("ID: ")
        print(classes.PaymentType.update(column, data, idColumn, id))
        return paymentTypeTable()

    elif move == "0":
        return mainDb.main()

    else:
        print("ERROR!!!")
        return paymentTypeTable()


def paymentTable():
    move = input("""
            1.Insert
            2.Select
            3.Delete
            4.Update
            0.Back
    >>> """)

    if move == "1":
        name = input("Name: ")
        paymentTypeId = input("Payment Type ID: ")
        payment = classes.Payment(name, paymentTypeId)
        print(payment.insert())
        return paymentTable()

    elif move == "2":
        for i in classes.Payment.select():
            print(i)
        return paymentTable()

    elif move == "3":
        column = input("Column: ")
        data = input("Data: ")
        if column != "payment_type_id":
            print(classes.Payment.delete(column, data))
        else:
            print(classes.Payment.deleteID(column, data))
        return paymentTable()

    elif move == "4":
        column = input("Column name: ")
        data = input("New data: ")
        idColumn = input("ID Column name: ")
        id = input("ID: ")
        print(classes.Payment.update(column, data, idColumn, id))
        return paymentTable()

    elif move == "0":
        return mainDb.main()

    else:
        print("ERROR!!!")
        return paymentTable()
    


def productCustomerTable():
    move = input("""
            1.Insert
            2.Select
            3.Delete
            4.Update
            0.Back
    >>> """)

    if move == "1":
        productId = input("Product ID: ")
        customerId = input("Customer ID: ")
        prodCust = classes.ProductCustomer(productId, customerId)
        print(prodCust.insert())
        return productCustomerTable()

    elif move == "2":
        for i in classes.ProductCustomer.select():
            print(i)
        return productCustomerTable()

    elif move == "3":
        column = input("Column: ")
        data = input("Data: ")
        if column != "product_customer_id":
            print(classes.ProductCustomer.delete(column, data))
        else:
            print(classes.ProductCustomer.deleteID(column, data))
        return productCustomerTable()

    elif move == "4":
        column = input("Column name: ")
        data = input("New data: ")
        idColumn = input("ID Column name: ")
        id = input("ID: ")
        print(classes.ProductCustomer.update(column, data, idColumn, id))
        return productCustomerTable()

    elif move == "0":
        return mainDb.main()

    else:
        print("ERROR!!!")
        return productCustomerTable()


def branchTable():
    move = input("""
                1.Insert
                2.Select
                3.Delete
                4.Update
                0.Back
        >>> """)

    if move == "1":
        name = input("Name: ")
        description = input("Description: ")
        addressId = input("Address ID: ")
        createDate = input("Create Date: ")
        branch = classes.Branch(name, description, addressId, createDate)
        print(branch.insert())
        return branchTable()

    elif move == "2":
        for i in classes.Branch.select():
            print(i)
        return branchTable()

    elif move == "3":
        column = input("Column: ")
        data = input("Data: ")
        if column != "branch_id":
            print(classes.Branch.delete(column, data))
        else:
            print(classes.Branch.deleteID(column, data))
        return branchTable()

    elif move == "4":
        column = input("Column name: ")
        data = input("New data: ")
        idColumn = input("ID Column name: ")
        id = input("ID: ")
        print(classes.Branch.update(column, data, idColumn, id))
        return branchTable()

    elif move == "0":
        return mainDb.main()

    else:
        print("ERROR!!!")
        return branchTable()



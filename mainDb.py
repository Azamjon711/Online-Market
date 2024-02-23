import tables


def main():
    print(" JADVALLAR ROYXATI: ")
    move = input(""""
                1.Country Table
                2.City Table
                3.Address Table
                4.Customer Table
                5.Product Table
                6.Product_Type Table
                7.Category Table
                8.Product_Category Table
                9.Payment_Type Table
                10.Payment Table
                11.Product_Customer Table
                12.Branch Table

>>> """)

    if move == "1":
        return tables.countryTable()
    elif move == "2":
        return tables.cityTable()
    elif move == "3":
        return tables.addressTable()
    elif move == "4":
        return tables.customerTable()
    elif move == "5":
        return tables.productTable()
    elif move == "6":
        return tables.productTypeTable()
    elif move == "7":
        return tables.categoryTable()
    elif move == "8":
        return tables.productCategoryTable()
    elif move == "9":
        return tables.paymentTypeTable()
    elif move == "10":
        return tables.paymentTable()
    elif move == "11":
        return tables.productCustomerTable()
    elif move == "12":
        return tables.branchTable()
    else:
        print("ERROR!!!")
        return main()


if __name__ == "__main__":
    main()

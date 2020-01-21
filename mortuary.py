class Queries:
    def sort_by_name(func):
        def append_sort_to_func(self):
            return f"{func(self)} ORDER BY last_name ASC, first_name ASC"

        return append_sort_to_func

    @sort_by_name
    def customers(self):
        return "SELECT * FROM Customer"

    def coffins(self):
        return "SELECT * FROM Coffin"

    @sort_by_name
    def employees(self):
        return "SELECT * FROM Employee"

    def gravestones(self):
        return "SELECT * FROM GraveStones"

    @sort_by_name
    def deceased(self):
        return "SELECT * FROM Deceased"

    def obelisks(self):
        return "SELECT * FROM Obelisk"

    @sort_by_name
    def vendors(self):
        return "SELECT * FROM Vendor"


queries = Queries()

print(queries.customers())
print(queries.coffins())
print(queries.employees())
print(queries.gravestones())
print(queries.deceased())
print(queries.obelisks())
print(queries.vendors())

#classand objects

class employee:
    def __init__(self):
        self.employee={}
    def addemployee(self,employeeid,name,department,salary):
        if employeeid in self.employee:
            print(f"{employeeid} already exists")
        else:
            self.employee[employeeid]={"name":name,"department":department,"salary":salary}
    def displayemployee(self):
        print(self.employee)
    
    def highestsalary(self):
        list=[]
        for i,data in self.employee.items():
            list.append(data["salary"])
        maximum_salary=max(list)
        for i,data in self.employee.items():
            if data["salary"]==maximum_salary:
                print(i,":",data)
    def calhighcondition(self, condition):
        result = [
            {
            "emp_id": emp_id,
            "name": data["name"],
            "department": data["department"],
            "salary": data["salary"]
            }
            for emp_id, data in self.employee.items()
            if data["salary"] > condition
            ]
        print(result)

em = employee()
empdata= [
    {"emp_id": 101, "name": "Alice", "department": "HR", "salary": 50000},
    {"emp_id": 102, "name": "Bob", "department": "IT", "salary": 75000},
    {"emp_id": 103, "name": "Charlie", "department": "Finance", "salary": 60000},
    {"emp_id": 104, "name": "Diana", "department": "IT", "salary": 82000}
]
for i in empdata:
    em.addemployee(i["emp_id"],i["name"],i["department"],i["salary"])
em.displayemployee()
em.highestsalary()
em.calhighcondition(60000)


# Inventory management

class inventory:
    def __init__(self):
        self.product={}
        
    def addproducts(self,pro_id,name,quantity,price):
        self.product[pro_id]={"name":name,"quantity":quantity,"price":price}
        
    def displayproduct(self):
        for i,j in self.product.items():
            print(i,":",j)
        
    #updating the quantity in the product
    
    def updatequantity(self, quantity, product_id):
        if product_id in self.product:
            self.product[product_id]["quantity"] += quantity
            print(f"Quantity updated. New quantity: {self.product[product_id]['quantity']}")
        else:
            print("No such product ID exists.")
    
    def getspecificpro(self,pro_id):
        if pro_id in self.product:
            print(self.product[pro_id])
        else:
            print("No such product ID exists.")
        
    def getlowstock(self,quantity):
        list=[{"pro_id":pro_id,"name":data["name"],"quantity":data["quantity"],"price":data["price"] }
              for pro_id,data in self.product.items() if data["quantity"]<quantity]
        for i in list:
            print(i)
        


inn=inventory()
product_data = [
    {"pro_id": 201, "name": "Laptop", "quantity": 10, "price": 55000},
    {"pro_id": 202, "name": "Smartphone", "quantity": 25, "price": 20000},
    {"pro_id": 203, "name": "Headphones", "quantity": 50, "price": 1500},
    {"pro_id": 204, "name": "Monitor", "quantity": 15, "price": 12000},
    
]
for i in product_data:
    inn.addproducts(i["pro_id"],i["name"],i["quantity"],i["price"])
inn.updatequantity(55,203)
inn.displayproduct()
inn.getspecificpro(204)
inn.getlowstock(20)

class Library:
    def __init__(self):
        self.books = []

    def addbook(self, title, author):
        self.books.append({"title": title, "author": author, "available": True})
        print(f"Book '{title}' by {author} added to the library.")

    def borrowbook(self, title):
        for book in self.books:
            if book["title"] == title:
                if book["available"]:
                    book["available"] = False
                    print(f"You borrowed '{title}'.")
                    return
                else:
                    print(f"'{title}' is currently unavailable.")
                    return
        print(f"Book '{title}' not found in the library.")

    def getavailablebooks(self):
        return [book for book in self.books if book["available"]]

    def displayavailablebooks(self):
        available = self.getavailablebooks()
        if not available:
            print("No books are currently available.")
        else:
            print("Available books:")
            for book in available:
                print(f"- {book['title']} by {book['author']}")

library=Library()
library.addbook("The Alchemist", "Paulo Coelho")
library.addbook("Clean Code", "Robert C. Martin")
library.addbook("Introduction to Algorithms", "Cormen")
library.addbook("The Psychology of Money", "Morgan Housel")
library.addbook("To Kill a Mockingbird", "Harper Lee")

print()
library.borrowbook("Clean Code")
library.borrowbook("The Alchemist")
library.borrowbook("To Kill a Mockingbird")

print()

# library.displayavailablebooks()

class product1:
    def __init__(self,product_id,name,price):
        self.product_id=product_id
        self.name=name
        self.price=price
    def display(self):
        print(f"{self.product_id},{self.name},{self.price}")
class sales:
    def __init__(self):
        self.sale=[]
    def addsale(self,product1,quantity):
        price=quantity* product1.price
        self.sale.append({"product_id":product1.product_id,"name":product1.name,"total_price":price})
        print(self.sale)
    def totalsale(self):
        print("Total_sum = ",sum(data["total_price"] for data in self.sale))
    def report(self):
        for i in self.sale:
            print(i)
if __name__ == "__main__":
    
    prod1=product1(101,"mobile",70000)
    prod2=product1(102,"airpods",60000)
    
    sale1=sales()
    sale1.addsale(prod1,25)
    sale1.addsale(prod2,40)
    
    prod1.display()
    sale1.totalsale()
    sale1.report()
            


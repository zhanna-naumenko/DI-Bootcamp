
# Exercise 1 : Student Grade Summary
student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}

student_averages = {key: round(sum(val) / len(val))for key, val in student_grades.items()}
print(student_averages)

grade_list = {"A": range(90,101), "B": range(80,90), "C":range(70, 80), "D":range(60, 70), "F":range(0,60)}

student_letter_grades = {}

for student, average in student_averages.items():
    for letter, grade_range in grade_list.items():
        if average in grade_range:
            student_letter_grades[student] = letter


for student, grade in student_letter_grades.items():
    print(f"The student {student} has grade {grade}.")

# Exercise 2 : Advanced Data Manipulation and Analysis
sales_data = [
    {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
    {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
    {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
    {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
    {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
    {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
    {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
]
# Total Sales Calculation
products = []
for num in range(0, len(sales_data)):
    products.append(sales_data[num]["product"])

name_of_products = list(set(products))
print(name_of_products)

product_dict = {}

for num in range(0, len(sales_data)):
    for key,value in sales_data[num].items():
        if key == "product":
            if value in product_dict:
                product_dict[value] += sales_data[num]["price"] * sales_data[num]["quantity"]
            else:
                product_dict[value] = sales_data[num]["price"] * sales_data[num]["quantity"]
print(product_dict)

# Customer Spending Profile
customer = []
for num in range(0, len(sales_data)):
    customer.append(sales_data[num]["customer_id"])

customer = list(set(customer))
print(customer)

customer_dict = {}

for num in range(0, len(sales_data)):
    for key,value in sales_data[num].items():
        if key == "customer_id":
            if value in customer_dict:
                customer_dict[value] += sales_data[num]["price"] * sales_data[num]["quantity"]
            else:
                customer_dict[value] = sales_data[num]["price"] * sales_data[num]["quantity"]
print(customer_dict)

# Sales Data Enhancement
for num in range(0, len(sales_data)):
    sales_data[num]["total_price"] = sales_data[num]["price"] * sales_data[num]["quantity"]

print(sales_data)

# High-Value Transactions
high_value_transaction = [sales_data[num]["total_price"] for num in range(0, len(sales_data)) if sales_data[num]["total_price"] > 500]
high_value_transaction.sort()
print(high_value_transaction)

# Customer Loyalty Identification:
customer = []
for num in range(0, len(sales_data)):
    customer.append(sales_data[num]["customer_id"])

customer_id = list(set(customer))
print(customer_id)

customer_loyalty = {}

for num in range(0, len(sales_data)):
    for key,value in sales_data[num].items():
        if key == "customer_id":
            if value in customer_loyalty:
                customer_loyalty[value] += 1
            else:
                customer_loyalty[value] = 1
print(customer_loyalty)

most_loyal = max(customer_loyalty, key=customer_loyalty.get)
print(f"The most loyal customer is {most_loyal}.")

# Bonus:
product_totals = {}
product_counts = {}

for sale in sales_data:
    product = sale["product"]
    transaction_value = sale["price"] * sale["quantity"]

    product_totals[product] = product_totals.get(product, 0) + transaction_value
    product_counts[product] = product_counts.get(product, 0) + 1

average_transaction_value = {
    product: round(product_totals[product] / product_counts[product], 2)
    for product in product_totals
}

print(average_transaction_value)
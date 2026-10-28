FILE_NAME = "expenses.txt"

def add_expense(date,category,amount,note):
    file = open(FILE_NAME,"a")
    record = date + "," + category + "," + str(amount) + "," + note + "\n"
    file.write(record)
    file.close()

def get_expenses():
    expenses = []
    try :
        file = open(FILE_NAME,"r")
        
        for line in file :
            data = line.strip().split(",")
            expense = {
                    "date" : data[0],
                    "category" : data[1] ,
                    "amount" : data[2],
                    "note" : data[3]
                }
            expenses.append(expense)
        
        file.close()
    

    except:
        pass
    return expenses



def total_expense():
    expenses = get_expenses()

    total = 0

    for e in expenses :
        total = total + float(e["amount"])
    return total


def category_expense():

    expenses = get_expenses()

    category_data = {}

    for e in expenses:

        category = e["category"]
        amount = float(e["amount"])

        if category in category_data:
            category_data[category] = category_data[category] += amount
        else :
            category_data[category] = amount
    return category_data
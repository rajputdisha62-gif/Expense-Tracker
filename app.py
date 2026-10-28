import streamlit as st
import expense_manager as em

st.title("Personal Expense Tracker")

menu = st.sidebar.selectbox(
    "Menu",
    ["Add Expense", "View Expenses", "Total Expense", "Category Wise"]
)

# ADD EXPENSE 

if menu == "Add Expense":

    st.header("Add New Expense")

    date = st.text_input("Date")
    category = st.selectbox(
        "Category",
        ["Food", "Travel", "Shopping", "Bills", "Other"]
    )

    amount = st.number_input("Amount")

    note = st.text_input("Note")

    if st.button("Add Expense"):

        em.add_expense(date, category, amount, note)

        st.success("Expense Added Successfully!")



# VIEW EXPENSES 

elif menu == "View Expenses":

    st.header("All Expenses")

    expenses = em.get_expenses()

    for e in expenses:

        st.write(
            e["date"],
            "|",
            e["category"],
            "| Rupee",
            e["amount"],
            "|",
            e["note"]
        )



# TOTAL EXPENSE 

elif menu == "Total Expense":

    st.header("Total Spending")

    total = em.total_expense()

    st.subheader("Total Expense = Rupee " + str(total))



# CATEGORY WISE 

elif menu == "Category Wise":

    st.header("Category Wise Expense")

    data = em.category_expense()

    for cat in data:

        st.write(cat, " : Rupee", data[cat])
        
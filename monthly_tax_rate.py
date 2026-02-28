monthly_sales = float(input("Enter total sales for the month: "))

state_rate = 0.05
county_rate = 0.025

state_tax = monthly_sales * state_rate
county_tax = monthly_sales * county_rate
total_tax = state_tax + county_tax

print("County Tax:", county_tax)
print("State Tax:", state_tax)
print("Total Sales Tax:", total_tax)

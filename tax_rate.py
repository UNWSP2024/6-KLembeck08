def calc_tax(amount, rate):
    return amount * rate

# Main program
total_sales = float(input("Enter total sales for the month: "))

state_rate = 0.05
county_rate = 0.025

state_tax = calc_tax(total_sales, state_rate)
county_tax = calc_tax(total_sales, county_rate)
total_tax = state_tax + county_tax

print("County Sales Tax:", county_tax)
print("State Sales Tax:", state_tax)
print("Total Sales Tax:", total_tax)

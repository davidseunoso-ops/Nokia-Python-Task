amount_invested = 1000
rate_of_return = 0.07

year_one = 10
year_two = 20
year_three = 30

amount_on_deposit_for_first_year = amount_invested * (1 + rate_of_return) ** year_one
amount_on_deposit_for_second_year = amount_invested * (1 + rate_of_return) ** year_two
amount_on_deposit_for_third_year = amount_invested * (1 + rate_of_return) ** year_three

print('Amount on deposit for the first year is ', '$',amount_on_deposit_for_first_year)
print('Amount on deposit for the second year is ', '$',amount_on_deposit_for_second_year)
print('Amount on deposit for the third year is ', '$',amount_on_deposit_for_third_year)



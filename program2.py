#An App for Mobile hosting provider charges- $0.51 per hour how much does it cost to operator per day, per week, per month? how many days can i operate one server with$918?
cost_hour = 0.51


cost_day = cost_hour * 24
cost_week = cost_day * 7
cost_month = cost_day * 30  

budget = 918
days_possible = budget / cost_day


print("Cost per day: $", round(cost_day, 2))
print("Cost per week: $", round(cost_week, 2))
print("Cost per month: $", round(cost_month, 2))
print("Days you can operate with $918:", round(days_possible, 2))

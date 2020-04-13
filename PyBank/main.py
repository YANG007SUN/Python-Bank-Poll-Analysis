# importing package
import pathlib
import csv
import statistics as stat



# read the data
budget_filepath = pathlib.Path("../Resources/budget_data.csv")

# ======================================== open file and calculate statistics =========================================
with open(budget_filepath, "r") as budgetfile:
    budget_data = csv.reader(budgetfile, delimiter = ",")

    # skip header
    next(budget_data)

    total_months = 0
    net_total = 0

    # initialize a list for average profit/loss and a list for period
    profit_loss= []
    pl_list = []
    period_month = []

    # loop through the dataset
    for row in budget_data:
        total_months = total_months+1 # total months
        net_total = int(row[1]) +net_total # net total 
        period_month.append(row[0])
        profit_loss.append(row[1])

    # pop out the first element in period_month
    period_month.pop(0)
    
    # get period change list by using current period value - previous period value
    for i in range(len(profit_loss)):
        if i >0:
            pl_list.append(int(profit_loss[i])-int(profit_loss[i-1]))

    # average periodic profit change
    average_change = round(stat.mean(pl_list),3)

    # create a dict to hold period and periodic profit change
    my_dict = {period:change for period, change in zip(period_month, pl_list)}
    
    # store some value
    greatest_increase_profit_period = max(my_dict, key = my_dict.get)
    greatest_decrease_profit_period = min(my_dict, key = my_dict.get)
    greatest_increase_value = my_dict[greatest_increase_profit_period]
    greatest_decrease_value = my_dict[greatest_decrease_profit_period]

# ================================================ print final analysis ================================================
print("Financial Analysis")
print("==============================")
print(f"Total Months: {total_months}")
print(f"Net Total Amount: ${net_total}")
print(f"Aveage Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_profit_period} ${greatest_increase_value}")
print(f"Greatest Decrease in Profits: {greatest_decrease_profit_period} -${greatest_decrease_value*-1}")


# =================================== create and text file and export with analysis ====================================
analysis_text = open("Financial_Analysis.txt","w")
analysis_text.write(f"Financial Analysis\n==============================\nTotal Months: {total_months}\nNet Total Amount: ${net_total}\nAveage Change: ${average_change}\nGreatest Increase in Profits: {greatest_increase_profit_period} ${greatest_increase_value}\nGreatest Decrease in Profits: {greatest_decrease_profit_period} -${greatest_decrease_value*-1}")
import os
import csv

# Set CSV file path
PyBank = os.path.join('/Users/Blob/OneDrive/Desktop/PyBank/python-challenge/PyBank_BudgetData.csv')
Output = os.path.join('/Users/Blob/OneDrive/Desktop/PyBank/python-challenge/Output.txt')

# Read mode
with open(PyBank, 'r') as csvfile:
    # Read file
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Initialize Variables
    total_months = 0
    total_profits = 0
    previous_profit_loss = 0
    total_change = 0
    counter = 0

    max_profit_loss = 0
    max_profit_loss_date = ''

    min_profit_loss = 0
    min_profit_loss_date = ''

    # Loop through rows to get data points
    for row in csvreader:
        total_months += 1
        total_profits += int(row[1])
        current_profit_loss = int(row[1])

        if counter > 0:
            profit_loss_change = current_profit_loss - previous_profit_loss
            total_change += profit_loss_change

            if profit_loss_change > max_profit_loss:
                max_profit_loss = profit_loss_change
                max_profit_loss_date = row[0]

            if profit_loss_change < min_profit_loss:
                min_profit_loss = profit_loss_change
                min_profit_loss_date = row[0]

        previous_profit_loss = current_profit_loss
        counter += 1

    average = total_change / (total_months - 1)

    # Print data points
    # print("Financial Analysis")
    # print("----------------------------")
    # print('Total Months: ' + str(total_months))
    # print('Total: ' + '$' + str(total_profits))
    # print('Average Change: $' + str(round(average, 2)))
    # print('Greatest Increase in Profits: ' + max_profit_loss_date + ' ($' + str(max_profit_loss) + ')')
    # print('Greatest Decrease in Profits: ' + min_profit_loss_date + ' ($' + str(min_profit_loss) + ')')

    lines = []

    lines.append("Financial Analysis")
    lines.append("----------------------------")
    lines.append('Total Months: ' + str(total_months))
    lines.append('Total: ' + '$' + str(total_profits))
    lines.append('Average Change: $' + str(round(average, 2)))
    lines.append('Greatest Increase in Profits: ' + max_profit_loss_date + ' ($' + str(max_profit_loss) + ')')
    lines.append('Greatest Decrease in Profits: ' + min_profit_loss_date + ' ($' + str(min_profit_loss) + ')')

    f = open(Output, "w")

    for line in lines:
        print(line)
        f.write(line + '\n')

    f.close()
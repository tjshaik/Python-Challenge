import os
import csv
# set path
data_csv = os.path.join ("Resources","budget_data.csv")
output = "analysis/bank_analysis.txt"
# setting variables 
total_months = 0
net_total = 0
previous_profit_loss = 1088983
rev_change = 0
change_list = []
greatest_increase = ["",0]
greatest_decrease = ["", 99999999]
tot_change = 0

# Open and read csv and 
# Read the header row first 
with open(data_csv) as data:
    csv_reader = csv.reader(data, delimiter= ",")
    csv_header = next(data)
    print(f"Header: {csv_header}")
    
    #loop through file
    for row in csv_reader:
        date = row[0]
        profit_loss = int(row[1])
            #cal total 
        total_months = total_months + 1
        net_total = net_total + int(row[1])
        #if total_months==1:
        # cal change
        rev_change = int(row[1]) - previous_profit_loss
        previous_profit_loss = int(row[1])

        tot_change = tot_change + rev_change

     #find greatest increase and decrease 
        if rev_change > greatest_increase[1]:
            greatest_increase = [date,rev_change]

        if rev_change < greatest_decrease[1]:
            greatest_decrease = [date,rev_change]
            #previous_profit_loss = profit_loss


         # change in profit and losses
    avg_change = tot_change/(total_months - 1)
   
with open(output, 'w') as txt_file:
##print
    results_pybank = (

    f"\n\n Financial Analysis\n"
    f"---------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change{avg_change}\n"
    f"Greatest Increase: {greatest_increase}\n"
    f"Greatest Decrease: {greatest_decrease}\n"

    )
    print(results_pybank)
        # save text file 
    txt_file.write(results_pybank)

import random
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
import csv
import statistics

# dice1 = random.randint(1,6)
# dice2 = random.randint(1,6)
# print(dice1, dice2)

# count = []
# dice_result = []
# for i in range(0,100):
#     dice1 = random.randint(1,6)
#     dice2 = random.randint(1,6)
#     dice_result.append(dice1 + dice2)
#     count.append(i)

# fig = px.bar(x = dice_result, y = count)
# fig.show()    

# fig = ff.create_distplot([dice_result],["Result"])
# fig.show() 

df = pd.read_csv("data.csv")

# fig1 = ff.create_distplot([df["Height(Inches)"].tolist()], ["Height"], show_hist= False )
# fig2 = ff.create_distplot([df["Weight(Pounds)"].tolist()], ["Weight"], show_hist= False)
# fig1.show() 
# fig2.show()

dice_result = []
for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1 + dice2)

# Caculating the mean and the standard deviation
mean = sum(dice_result)/len(dice_result)
std_deviation = statistics.stdev(dice_result)
median = statistics.median(dice_result)
mode = statistics.mode(dice_result)

fig = ff.create_distplot([dice_result],["Result"],show_hist = False)
fig.show()

first_std_deviation_start, first_std_deviation_end = mean - std_deviation, mean + std_deviation
second_std_deviation_start, second_std_deviation_end = mean - (2 * std_deviation), mean + (2 * std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)
# print("{}% of data lies within 1 std_deviation". format(len((list_of_data_within_1_std_deviation)* 100.0 / len(dice_result))))

height_list = df["Height(Inches)"]._list()
weight_list = df["Weight(Pounds)"]._list()

# Calculating mean
height_mean = statistics.mean(height_list)
weight_mean = statistics.mean(weight_list)

# Calculating mode
height_mode = statistics.mode(height_list)
weight_mode = statistics.mode(weight_list)

# Caculating median
height_median = statistics.median(height_list)
weight_median = statistics.median(weight_list)

# 
height_first_std_deviation_start, height_first_std_deviation_end = height_mean - height_std_deviation, height_mean + height_std_deviation
height_second_std_deviation_start, height_second_std_deviation_end = height_mean - (2 * height_std_deviation), height_mean + (2 * height_std_deviation)
height_third_std_deviation_start, height_third_std_deviation_end = height_mean-(3* height_std_deviation), height_mean+(3* height_std_deviation)

height_list_of_data_within_1_std_deviation = [result for result in height_list if result > height_first_std_deviation_start and result < height_first_std_deviation_end]
height_list_of_data_within_2_std_deviation = [result for result in height_list if result > height_second_std_deviation_start and result < height_second_std_deviation_end]
height_list_of_data_within_3_std_deviation = [result for result in height_list if result > height_third_std_deviation_start and result < height_third_std_deviation_end]

weight_list_of_data_within_1_std_deviation = [result for result in dice_result if result > weight_first_std_deviation_start and result < weight_first_std_deviation_end] 
weight_list_of_data_within_2_std_deviation = [result for result in dice_result if result > weight_second_std_deviation_start and result < weight_second_std_deviation_end] 
weight_list_of_data_within_3_std_deviation = [result for result in dice_result if result > weight_third_std_deviation_start and result < weight_third_std_deviation_end]

# height print
print("{}% of data lies within 1 standard deviation".format(len(height_list_of_data_within_1_std_deviation)*100.0/len(height_list))) 
print("{}% of data lies within 2 standard deviations".format(len(height_list_of_data_within_2_std_deviation)*100.0/len(height_list))) 
print("{}% of data lies within 3 standard deviations".format(len(height_list_of_data_within_3_std_deviation)*100.0/len(height_list)))

# weight print
print("{}% of data lies within 1 standard deviation".format(len(weight_list_of_data_within_1_std_deviation)*100.0/len(weight_list))) 
print("{}% of data lies within 2 standard deviations".format(len(weight_list_of_data_within_2_std_deviation)*100.0/len(weight_list))) 
print("{}% of data lies within 3 standard deviations".format(len(weight_list_of_data_within_3_std_deviation)*100.0/len(weight_list)))
import pandas as pd
import statistics as st
import csv
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")
math_list = df["math score"].to_list()
reading_list = df["reading score"].to_list()
writing_list = df["writing score"].to_list()

math_mean = st.mean(math_list)
reading_mean = st.mean(reading_list)
writing_mean = st.mean(writing_list)

math_mode = st.mode(math_list)
reading_mode = st.mode(reading_list)
writing_mode = st.mode(writing_list)

math_median = st.median(math_list)
reading_median = st.median(reading_list)
writing_median = st.median(writing_list)

reading_stdev = st.stdev(reading_list)

reading_first_stdev_start, reading_first_stdev_end = reading_mean-reading_stdev, reading_mean+reading_stdev
reading_second_stdev_start, reading_second_stdev_end = reading_mean-(2*reading_stdev), reading_mean+(2*reading_stdev)
reading_third_stdev_start, reading_third_stdev_end = reading_mean-(3*reading_stdev), reading_mean+(3*reading_stdev)

reading_list_of_data_within_1_stdev = [result for result in reading_list if result > reading_first_stdev_start and result < reading_first_stdev_end]
reading_list_of_data_within_2_stdev = [result for result in reading_list if result > reading_second_stdev_start and result < reading_second_stdev_end]
reading_list_of_data_within_3_stdev = [result for result in reading_list if result > reading_third_stdev_start and result < reading_third_stdev_end]

print("{}% of data for height lies within 1 standard deviation".format(len(reading_list_of_data_within_1_stdev)*100.0/len(reading_list)))
print("{}% of data for height lies within 2 standard deviations".format(len(reading_list_of_data_within_2_stdev)*100.0/len(reading_list)))
print("{}% of data for height lies within 3 standard deviations".format(len(reading_list_of_data_within_3_stdev)*100.0/len(reading_list)))

fig = ff.create_distplot([reading_list], [reading_mean])

fig.show()
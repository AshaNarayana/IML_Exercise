
# One Reference to learn about numpy, there are many on the web
# https://www.tutorialspoint.com/numpy/numpy_pdf_version.htm
#
#
# GOAL: To start with the numpy library and to know what to do with it
#
# In this exercise you have to follow the steps and complete them with some code
# Include the Example1.py in one project in PyCharm 


print ("Using  Numpy ")

import numpy as np


# 2. Create an array (standard python array), called height, with this values
#
height = [1.73, 1.68, 1.71, 1.89, 1.79]


# 3. Create an array (standard python array), called weight, with this values
#
weight = [65.4, 59.2, 63.6, 88.4, 68.7]


# 4. print the two arrays (height and weight) on the console
print(f'height: {height}')
print(f'weight: {weight}')


# 4. Uncomment the code and answer: What happens with this line?
# Answer : If uncommented below line gives TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'
# bmi = weight / height ** 2


# 5. Convert height and weight into two numpy arrays,
#  called np_height and np_weight, respectively
np_height = np.array(height)
np_weight = np.array(weight)

# 6. Compute bmi again with the two numpy arrays
# bmi is the weight / height^2
# Answer : above line gives TypeError: ufunc 'bitwise_xor' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''
bmi = np_weight / np_height ** 2

# 7. print bmi array on the console
print(f'bmi: {bmi}')
# 8. Compute the mean of the bmi and print on the console
bmi_mean = np.mean(bmi)
print(f'bmi_mean: {bmi_mean}')
# 9. Compute the median  of the bmi and print on the console
bmi_median = np.median(bmi)
print(f'bmi_median: {bmi_median}')

# 10. Compute the correlation between height and weight
correlation_matrix = np.corrcoef(height, weight)
print(f'correlation_matrix: {correlation_matrix}')
# 11. Compute the standard deviation of bmi
std_deviation = np.std(bmi)
print(f'std_deviation: {std_deviation}')

# 12. Show on console the dimension of bmi, height and weight
print(f'Dimensions of bmi: {bmi.ndim} or shape of bmi: {bmi.shape}')
print(f'Dimensions of weight: {np_weight.ndim} or shape of weight: {np_weight.shape}')
print(f'Dimensions of height: {np_height.ndim} or shape of height: {np_height.shape}')
# 13a. Compute the sum of bmi and sort the values too, show bmi on the console
bmi_sum = np.sum(bmi)
bmi_sort = np.sort(bmi)
print(f'Sum of bmi: {bmi_sum}')
print(f'Sorted bmi: {bmi_sort}')

# 13b. The result for these sentences is the same?
# Think about it before uncomment the code and run it to look at the results


print(f'(height + weight): {height + weight}')
print(f'(np_height + np_weight): {np_height + np_weight}')


# 14. Create a 2 dimensional array, called np_table,
# in one dimension the values of the height and
# in the second dimension the values of the weight

np_table = np.array([height, weight])

print(f'np_table: {np_table}')
# 15. Print on the console the first dimension of np_table
print(f'first dimension of np_table: {np_table[0]}')
# 16. Print on the console the second dimension of np_table
print(f'second dimension of np_table: {np_table[1]}')

# 17. Print on the console all the dimension of the np_table

print(f'all dimension of the np_table: {np_table.shape}')
# 18. Print on the console the second column of np_table
second_column = np_table[:, 1]
print(f'second column of np_table: {second_column}')
# 19. Print on the console the third column of np_table
third_column = np_table[:, 2]
print(f'third_column of np_table: {third_column}')
#  20 Create and print an array, called np_tableshort,  with the second and third columns of np_table
np_tableshort = np_table[:, 1:3]

print(f'np_tableshort: {np_tableshort}')
# end of the  numpy code

import matplotlib.pyplot as plt
#
#
# x = np.linspace(0, 3, 1000)
# plt.plot(x, x, label='linear')
# .plot(x, x**2, label='quadratic')
# plt.plot(x, x**3, label='cubic')
# plt.xlabel('x label')
# plt.ylabel('y label')
# plt.title("Simple Plot")
# plt.legend()
# plt.show()

# x = np.arange(0, 10, 0.2)
# y = np.sin(x)
# fig, ax = plt.subplots()
# ax.plot(x, y)
# plt.show()

#
#
# names = ['group_a', 'group_b', 'group_c']
# values = [1, 10, 100]
# plt.figure(1, figsize=(9, 5))
# plt.subplot(131)
# plt.bar(names, values)
# plt.subplot(132)
# plt.scatter(names, values)
# plt.subplot(133)
# plt.plot(names, values)
# plt.suptitle('Categorical Plotting')
# plt.show()

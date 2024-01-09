import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

# Read data from the file
salary_data = pd.read_csv('data9-1.csv')

# Extract salary data
Salary = salary_data.iloc[:, 0]

# Calculate mean annual salary
mean_salary = np.mean(Salary)

# Set up the figure size and dpi
plt.figure(figsize=(14, 9), dpi=300)

# Create a histogram
plt.hist(Salary, bins=30, density=True, alpha=0.7,
         label='Salary Distribution', color='#45B39D', edgecolor='black')

# Calculate the probability density function using a kernel density estimate
salary_range = np.linspace(Salary.min(), Salary.max(), 1000)
kde = gaussian_kde(Salary)
plt.plot(salary_range, kde(salary_range),
         label='Probability Density Function', color='#34495E')

# Calculate the fraction of population with salaries between mean and 1.2 times the mean
lower_bound = 0.8 * mean_salary
upper_bound = 1.2 * mean_salary
fraction_between = np.sum((Salary >= lower_bound) & (
    Salary <= upper_bound)) / len(Salary)

# Plot mean and fraction on the graph
plt.axvline(mean_salary, color='#34495E', linestyle='--', label='Mean Salary')
plt.text(mean_salary, plt.ylim()[
         1]*0.9, f'  Mean Salary: {mean_salary:.2f}', color='#34495E', fontfamily='rockwell', fontsize='15')
plt.text(upper_bound, plt.ylim()[
         1]*0.65, f'      Fraction(X): {fraction_between:.2f}', color='#34495E', fontfamily='rockwell', fontsize='15', ha='left')

# Set x and y limits
plt.xlim(0, plt.xlim()[1])
plt.ylim(0, plt.ylim()[1])

# Set labels, title, and legend
plt.xlabel('Salary', fontfamily='rockwell', fontsize='8')
plt.ylabel('Probability Density', fontfamily='rockwell', fontsize='8')
plt.title('Salary Distribution and Probability Density Function',
          fontfamily='rockwell', fontsize='20')
plt.legend(loc='upper right', fontsize='15',
           frameon=False, bbox_to_anchor=(1, 0.95))

# Customize legend text color and style
legend = plt.gca().get_legend()
for text in legend.get_texts():
    text.set_color('black')
    text.set_fontfamily('rockwell')
    text.set_fontsize('15')

# Calculate Statistical Properties


def statisticalProperties(salary_data):
    kurtosis = salary_data.kurtosis()
    skewness = salary_data.skew()
    median = np.median(salary_data)
    mode = salary_data.mode()
    return mode, median, kurtosis, skewness


mode, median, kurtosis, skewness = statisticalProperties(Salary)
print(
    f"mode is : {mode}\nmedian : {median}\nkurtosis : {kurtosis}\nskewness : {skewness}")

# Customize tick parameters
plt.tick_params(axis='x', labelsize=10, colors='black')
plt.tick_params(axis='y', labelsize=10, colors='black')

# Show the plot
plt.show()

import numpy as np
import matplotlib.pyplot as plt
age_groups = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
males = [30, 45, 40, 20, 15, 10]
females = [35, 50, 38, 25, 18, 12]
x = np.arange(len(age_groups))
bar_width = 0.35
plt.figure(figsize=(12, 7))
bars1 = plt.bar(x - bar_width/2, males, bar_width, label='Males', color='skyblue')
bars2 = plt.bar(x + bar_width/2, females, bar_width, label='Females', color='lightcoral')
plt.title('Distribution of Ages and Genders in a Population')
plt.xlabel('Age Groups')
plt.ylabel('Number of People')
plt.xticks(x, age_groups)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

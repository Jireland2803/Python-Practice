import pandas as pd
import matplotlib.pyplot as plt


file = pd.read_csv('tlevel_results_core.csv')
data = pd.DataFrame(file)
print(data)

file = pd.read_csv('tlevel_results_core.csv')
filtered_file = file[file['percent'] != 'z']
convert_percent = {'grade': str, 'percent': float}
filtered_file = filtered_file.astype(convert_percent)
avg_percent = filtered_file.groupby('grade')['percent'].mean()  # Compute average speed per generation
avg_percent.plot(kind='bar', color='skyblue')  # Plot as a bar chart
plt.title('Average achievement rate per grade')
plt.xlabel('Grade')
plt.ylabel('Percentage(%)')
plt.show()


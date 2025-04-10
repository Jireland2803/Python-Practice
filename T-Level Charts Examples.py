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
plt.savefig('Graphs/Average Achievement Rate Per Grade.png')
plt.show()


file = pd.read_csv('tlevel_results_core.csv')
filtered_file = file[file['percent'] != 'z']
convert_percent = {'grade': str, 'percent': float}
filtered_file = filtered_file.astype(convert_percent)
filtered_file = filtered_file[filtered_file['sex'] == 'Male']
avg = filtered_file.groupby('grade')['percent'].mean()
avg_percent.plot(kind='bar', color='red')
plt.title('Average achievement rate per grade for males')
plt.xlabel('Grade')
plt.ylabel('Percentage(%)')
plt.savefig('Graphs/Male Average Achievement Rates.png')
plt.show()


file = pd.read_csv('tlevel_results_core.csv')
filtered_file = file[file['count'] != 'z']
filtered_file = filtered_file[filtered_file['grade'] != 'Number of students']
convert_count = {'grade': str, 'count': int}
filtered_file = filtered_file.astype(convert_count)
count_graph = filtered_file.groupby('grade')['count'].mean()
count_graph.plot(kind='line', color='green')
plt.title('Average number of students that achieved each grade')
plt.xlabel('Grade')
plt.ylabel('Number of Students')
plt.savefig('Graphs/Average Number of Students Per Grade.png')
plt.show()


file = pd.read_csv('tlevel_results_core.csv')
filtered_file = file[file['core_component'] == 'Digital Production, Design and Development']
filtered_file = filtered_file[filtered_file['sex'] == 'All']
filtered_file = filtered_file[filtered_file['grade'] != 'Number of students']
filtered_file = filtered_file[filtered_file['grade'] != 'D']
filtered_file = filtered_file[filtered_file['grade'] != 'E']
filtered_file = filtered_file[filtered_file['grade'] != 'Unclassified']
graph = filtered_file.groupby('time_period')['count'].sum()
graph.plot(kind='line', color='purple')
plt.title('Filtering by component')
plt.xlabel('Grade')
plt.ylabel('Number of Students')
print(graph)
plt.show()
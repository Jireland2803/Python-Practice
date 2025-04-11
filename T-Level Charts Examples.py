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
dpdd_filter = file[file['core_component'] == 'Digital Production, Design and Development']
dpdd_sex = dpdd_filter[dpdd_filter['sex'] == 'All']
dpdd_grade = dpdd_sex[dpdd_sex['grade'] != 'Number of students']
dpdd_grade_filter = dpdd_grade[dpdd_grade['grade'] != 'D']
dpdd_grade_filter = dpdd_grade[dpdd_grade['grade'] != 'E']
dpdd_grade_filter = dpdd_grade[dpdd_grade['grade'] != 'Unclassified']
dpdd_graph = dpdd_grade_filter.groupby('time_period')['count'].sum()
dpdd_graph.plot(kind='line', color='purple')
plt.title('Number of Students That Achieved a C or Higher: Digital Production, Design and Development')
plt.xlabel('Grade')
plt.ylabel('Number of Students')
print(dpdd_graph)
plt.savefig('Graphs/Digital Production, Design and Development.png')
plt.show()

file = pd.read_csv('tlevel_results_core.csv')
dsp_filter = file[file['core_component'] == 'Design, Surveying and Planning']
dsp_sex = dsp_filter[dsp_filter['sex'] == 'All']
dsp_grade = dsp_sex[dsp_sex['grade'] != 'Number of students']
dsp_grade_filter = dsp_grade[dsp_grade['grade'] != 'D']
dsp_grade_filter = dsp_grade[dsp_grade['grade'] != 'E']
dsp_grade_filter = dsp_grade[dsp_grade['grade'] != 'Unclassified']
dsp_graph = dsp_grade_filter.groupby('time_period')['count'].sum()
dsp_graph.plot(kind='line', color='blue')
plt.title('Number of Students That Achieved a C or Higher: Design, Surveying and Planning')
plt.xlabel('Grade')
plt.ylabel('Number of Students')
print(dsp_graph)
plt.savefig('Graphs/Design, Surveying and Planning.png')
plt.show()

file = pd.read_csv('tlevel_results_core.csv')
eey_filter = file[file['core_component'] == 'Education and Early Years']
eey_sex = eey_filter[eey_filter['sex'] == 'All']
eey_grade = eey_sex[eey_sex['grade'] != 'Number of students']
eey_grade_filter = eey_grade[eey_grade['grade'] != 'D']
eey_grade_filter = eey_grade[eey_grade['grade'] != 'E']
eey_grade_filter = eey_grade[eey_grade['grade'] != 'Unclassified']
eey_graph = dpdd_grade_filter.groupby('time_period')['count'].sum()
eey_graph.plot(kind='line', color='lime')
plt.title('Number of Students That Achieved a C or Higher: Education and Early Years')
plt.xlabel('Grade')
plt.ylabel('Number of Students')
plt.savefig('Graphs/Education and Early Years')
print(eey_graph)
plt.show()

file = pd.read_csv('tlevel_results_core.csv')
bse_filter = file[file['core_component'] == 'Building Services Engineering']
bse_sex = bse_filter[bse_filter['sex'] == 'All']
bse_grade = bse_sex[bse_sex['grade'] != 'Number of students']
bse_grade_filter = bse_grade[bse_grade['grade'] != 'D']
bse_grade_filter = bse_grade[bse_grade['grade'] != 'E']
bse_grade_filter = bse_grade[bse_grade['grade'] != 'Unclassified']
bse_graph = bse_grade_filter.groupby('time_period')['count'].sum()
bse_graph.plot(kind='line', color='black')
plt.title('Number of Students That Achieved a C or Higher: Building Services Engineering')
plt.xlabel('Grade')
plt.ylabel('Number of Students')
print(bse_graph)
plt.savefig('Graphs/Building Services Engineering')
plt.show()

file = pd.read_csv('tlevel_results_core.csv')
dbs_filter = file[file['core_component'] == 'Digital Business Services']
dbs_sex = dbs_filter[dbs_filter['sex'] == 'All']
dbs_grade = dbs_sex[dbs_sex['grade'] != 'Number of students']
dbs_grade_filter = dbs_grade[dbs_grade['grade'] != 'D']
dbs_grade_filter = dbs_grade[dbs_grade['grade'] != 'E']
dbs_grade_filter = dbs_grade[dbs_grade['grade'] != 'Unclassified']
dbs_graph = dbs_grade_filter.groupby('time_period')['count'].sum()
dbs_graph.plot(kind='line', color='slateblue')
plt.title('Number of Students That Achieved a C or Higher: Digital Business Services')
plt.xlabel('Grade')
plt.ylabel('Number of Students')
print(dbs_graph)
plt.savefig('Graphs/Digital Business Services')
plt.show()

file = pd.read_csv('tlevel_results_core.csv')
dss_filter = file[file['core_component'] == 'Digital Support Services']
dss_sex = dss_filter[dss_filter['sex'] == 'All']
dss_grade = dss_sex[dss_sex['grade'] != 'Number of students']
dss_grade_filter = dss_grade[dss_grade['grade'] != 'D']
dss_grade_filter = dss_grade[dss_grade['grade'] != 'E']
dss_grade_filter = dss_grade[dss_grade['grade'] != 'Unclassified']
dss_graph = dss_grade_filter.groupby('time_period')['count'].sum()
dss_graph.plot(kind='line', color='slateblue')
plt.title('Number of Students That Achieved a C or Higher: Digital Support Services')
plt.xlabel('Grade')
plt.ylabel('Number of Students')
print(dss_graph)
plt.savefig('Graphs/Digital Support Services')
plt.show()


fig, axes = plt.subplots(nrows= 2, ncols= 3)
dpdd_graph.plot(ax=axes[0,0])
dsp_graph.plot(ax=axes[0,1])
eey_graph.plot(ax=axes[0,2])
bse_graph.plot(ax=axes[1,0])
dbs_graph.plot(ax=axes[1,1])
dss_graph.plot(ax=axes[1,2])
plt.savefig('Graphs/All Six Graphs on the Same Plot')


plt.show()

fig, axes = plt.subplots()
dpdd_graph.plot(ax=axes, label = 'DPDD')
dsp_graph.plot(ax=axes, label = 'DSP')
eey_graph.plot(ax=axes, label = 'EEY')
bse_graph.plot(ax=axes, label = 'BSE')
dbs_graph.plot(ax=axes, label = 'DBS')
dss_graph.plot(ax=axes, label = 'DSS')
plt.legend()
plt.savefig('Graphs/All Six Graphs on a single axis')

plt.show()

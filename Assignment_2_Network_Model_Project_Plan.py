#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from cheche_pm import Project
import networkx as nx


# In[2]:


p = Project() # create empty project instance

p.add_activity(activity_name='A',activity_duration = 2, activity_precedence= [None], a_desc= 'Describe product')
p.add_activity(activity_name='B',activity_duration = 4, activity_precedence= [None], a_desc= 'Develop marketing strategy')
p.add_activity(activity_name='C',activity_duration = 6, activity_precedence= ['A'], a_desc= 'Design brochure')
p.add_activity(activity_name='D1',activity_duration = 80, activity_precedence= ['A'], a_desc= 'Requirements analysis')
p.add_activity(activity_name='D2',activity_duration = 120, activity_precedence= ['D1'], a_desc= 'Software design')
p.add_activity(activity_name='D3',activity_duration = 120, activity_precedence= ['D1'], a_desc= 'System design')
p.add_activity(activity_name='D4',activity_duration = 720, activity_precedence= ['D2', 'D3'], a_desc= 'Coding')
p.add_activity(activity_name='D5',activity_duration = 80, activity_precedence= ['D4'], a_desc= 'Write documentation')
p.add_activity(activity_name='D6',activity_duration = 160, activity_precedence= ['D4'], a_desc= 'Unit testing')
p.add_activity(activity_name='D7',activity_duration = 160, activity_precedence= ['D6'], a_desc= 'System testing')
p.add_activity(activity_name='D8',activity_duration = 80, activity_precedence= ['D5', 'D7'], a_desc= 'Package deliverables')
p.add_activity(activity_name='E',activity_duration = 40, activity_precedence= ['B','C'], a_desc= 'Survey potential market')
p.add_activity(activity_name='F',activity_duration = 32, activity_precedence= ['D8','E'], a_desc= 'Develop pricing plan')
p.add_activity(activity_name='G',activity_duration = 16, activity_precedence= ['A','D8'], a_desc= 'Develop implementation plan')
p.add_activity(activity_name='H',activity_duration = 24, activity_precedence= ['F','G'], a_desc= 'Write client proposal')


# In[3]:


p = Project.from_excel(filename='project-plan-v003_Python.xlsx',
                      rcpsp_format=True)


# In[4]:


p.plot_network_diagram(plot_type = 'nx')


# In[5]:


p.create_project_dict()
out_df = pd.DataFrame(p.PROJECT).T


# In[6]:


out_df


# In[7]:


p.CPM(verbose=True)


# In[8]:


pd.DataFrame(p.cpm_schedule).T


# In[9]:


p.get_critical_path()


# In[10]:


from pulp import LpProblem, LpMinimize, LpVariable, LpStatus
import matplotlib.pyplot as plt


# In[11]:


file_path = 'project-plan-v003.xlsx'
df = pd.read_excel(file_path, sheet_name='Sheet1')


# In[12]:


# Task information
tasks = df['taskID'].dropna().tolist()
expected_hours = df.set_index('taskID')['expectedHours'].fillna(0).to_dict()  # Replace NaN with 0 (due to the "D" task of develop product prototype)
predecessors = df.set_index('taskID')['predecessorTaskIDs'].dropna().to_dict()


# In[13]:


# Linear programming model
model = LpProblem('Project_Scheduling', LpMinimize)


# In[14]:


# Decision variables: Start times for each task
start_times = {task: LpVariable(f"start_{task}", lowBound=0) for task in tasks}


# In[15]:


# Completion time variable
completion_time = LpVariable('completion_time', lowBound=0)


# In[16]:


# Objective function: Minimize total project duration
model += completion_time, 'Minimize_Project_Completion_Time'


# In[17]:


# Constraints: task predecessors
for task, preds in predecessors.items():
    if isinstance(preds, str):  # Handling multiple dependencies within the predecessors
        preds = preds.split(', ')
    else:
        preds = [preds]
    for pred in preds:
        if pred in tasks:  # Ensure predecessor is a valid task
            model += start_times[task] >= start_times[pred] + expected_hours.get(pred, 0)


# In[18]:


# Constraint: Completion time must be at least as large as the latest finish time
for task in tasks:
    model += completion_time >= start_times[task] + expected_hours.get(task, 0)


# In[19]:


# Solve the model
model.solve()


# In[20]:


# Extract results
schedule_results = {task: start_times[task].varValue for task in tasks}
completion_time_value = completion_time.varValue


# In[21]:


# Convert results into a DataFrame for visualization
schedule_df = pd.DataFrame(list(schedule_results.items()), columns=['Task', 'Start Time'])
schedule_df['Duration'] = schedule_df['Task'].map(expected_hours)
schedule_df['Completion Time'] = schedule_df['Start Time'] + schedule_df['Duration']


# In[22]:


# Display results
print('\nOptimal Project Schedule:')
print(schedule_df)
print(f'\nTotal Project Completion Time: {completion_time_value} hours')
print(f'Solver Status: {LpStatus[model.status]}')


# In[23]:


file_path = 'project-plan-v003.xlsx'
df = pd.read_excel(file_path, sheet_name='Sheet1')


# In[24]:


# Function to solve LP model for different time estimates
def solve_project_scheduling(time_column):
    tasks = df['taskID'].dropna().tolist()
    task_times = df.set_index('taskID')[time_column].fillna(0).to_dict()  # Use given time estimates
    predecessors = df.set_index('taskID')['predecessorTaskIDs'].dropna().to_dict()

    # Linear programming model
    model = LpProblem(f"Project_Scheduling_{time_column}", LpMinimize)

    # Decision variables: Start times for each task
    start_times = {task: LpVariable(f"start_{task}", lowBound=0) for task in tasks}

    # Completion time variable
    completion_time = LpVariable('completion_time', lowBound=0)

    # Objective function: Minimize total project duration
    model += completion_time, 'Minimize_Project_Completion_Time'

    # Constraints: Task dependencies
    for task, preds in predecessors.items():
        if isinstance(preds, str):   # Handling multiple dependencies within the predecessors
            preds = preds.split(', ')
        else:
            preds = [preds]
        for pred in preds:
            if pred in tasks:  # Ensure predecessor is a valid task
                model += start_times[task] >= start_times[pred] + task_times[pred]

    # Constraint: Completion time must be at least as large as the latest finish time
    for task in tasks:
        model += completion_time >= start_times[task] + task_times[task]

    # Solve the model
    model.solve()

    # Extract results
    schedule_results = {task: start_times[task].varValue for task in tasks}
    completion_time_value = completion_time.varValue

    # Convert results into a DataFrame
    schedule_df = pd.DataFrame(list(schedule_results.items()), columns=['Task', 'Start Time'])
    schedule_df['Duration'] = schedule_df['Task'].map(task_times)
    schedule_df['Completion Time'] = schedule_df['Start Time'] + schedule_df['Duration']

    return schedule_df, completion_time_value, model.status


# In[25]:


# Solve for Best-Case, Expected-Case, and Worst-Case Scenarios
best_case_schedule, best_case_time, best_status = solve_project_scheduling('bestCaseHours')
expected_case_schedule, expected_case_time, expected_status = solve_project_scheduling('expectedHours')
worst_case_schedule, worst_case_time, worst_status = solve_project_scheduling('worstCaseHours')


# In[26]:


# Display results
print('\nBest-Case Scenario:')
print(best_case_schedule)
print(f'Total Completion Time: {best_case_time} hours')

print('\nExpected-Case Scenario:')
print(expected_case_schedule)
print(f'Total Completion Time: {expected_case_time} hours')

print('\nWorst-Case Scenario:')
print(worst_case_schedule)
print(f'Total Completion Time: {worst_case_time} hours')


# In[27]:


# Critical path using a directed graph approach.
def compute_critical_path(schedule_df, predecessors, total_project_time):

    # Create a directed graph
    G = nx.DiGraph()

    # Add tasks as nodes
    for _, row in schedule_df.iterrows():
        G.add_node(row['Task'], duration=row['Duration'])

    # Add edges based on dependencies
    for task, preds in predecessors.items():
        if isinstance(preds, str):
            preds = preds.split(', ')  # Handling multiple dependencies
        else:
            preds = [preds]
        for pred in preds:
            if pred in schedule_df['Task'].values:  # Ensure the predecessor exists
                G.add_edge(pred, task, weight=schedule_df[schedule_df['Task'] == pred]['Duration'].values[0])

    # Compute the longest path (Critical Path)
    longest_path = nx.dag_longest_path(G, weight='weight')

    return longest_path


# In[28]:


# Compute the critical path for each scenario
best_case_critical_path = compute_critical_path(best_case_schedule, predecessors, best_case_time)
expected_case_critical_path = compute_critical_path(expected_case_schedule, predecessors, expected_case_time)
worst_case_critical_path = compute_critical_path(worst_case_schedule, predecessors, worst_case_time)


# In[29]:


# Display corrected critical paths
print('\nCritical Path (Best Case):', ' → '.join(best_case_critical_path))
print('\nCritical Path (Expected Case):', ' → '.join(expected_case_critical_path))
print('\nCritical Path (Worst Case):', ' → '.join(worst_case_critical_path))


# In[30]:


# Gantt chart for the project schedule
def plot_gantt_chart(schedule_df, title):

    fig, ax = plt.subplots(figsize=(12, 6))

    # Convert task start times and durations into bars
    y_positions = range(len(schedule_df))
    start_times = schedule_df['Start Time']
    durations = schedule_df['Duration']

    ax.barh(y_positions, durations, left=start_times, color='skyblue', edgecolor='black')

    # Annotate task names
    for i, (task, start, duration) in enumerate(zip(schedule_df['Task'], start_times, durations)):
        ax.text(start + duration / 2, i, task, ha='center', va='center', fontsize=10, color='black', weight='bold')

    # Formatting
    ax.set_yticks(y_positions)
    ax.set_yticklabels(schedule_df['Task'])
    ax.set_xlabel("Time (Hours)")
    ax.set_title(title)
    ax.invert_yaxis()  # Highest priority task at the top

    plt.grid(axis='x', linestyle='--', alpha=0.6)
    plt.show()


# In[31]:


plot_gantt_chart(best_case_schedule, "Gantt Chart - Best Case Scenario")
plot_gantt_chart(expected_case_schedule, "Gantt Chart - Expected Case Scenario")
plot_gantt_chart(worst_case_schedule, "Gantt Chart - Worst Case Scenario")


# In[ ]:





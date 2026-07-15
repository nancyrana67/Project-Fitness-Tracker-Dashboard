# 🏋️ Personal Fitness Tracker Dashboard

## 📖 Project Overview

The **Personal Fitness Tracker Dashboard** is a Python-based application developed to help fitness enthusiasts **record, analyze, and visualize** their daily fitness activities. The system allows users to log activities such as walking, running, cycling, gym workouts, yoga, and swimming while automatically calculating useful fitness metrics.

The project demonstrates the practical implementation of **Python Programming**, **Object-Oriented Programming (OOP)**, **Control Structures**, **NumPy**, **Pandas**, **Matplotlib**, and **Seaborn**.

---

# 🎯 Project Objective

The main objective of this project is to develop a Python-based fitness tracker dashboard that can:

- Record daily fitness activities.
- Validate user input using control structures.
- Store activity records in a CSV dataset.
- Perform numerical analysis using NumPy.
- Analyze activity data using Pandas.
- Generate fitness reports.
- Visualize fitness progress using charts and graphs.
- Help users understand their workout trends and health performance.

---

# ❓ Problem Statement

Fitness enthusiasts often find it difficult to maintain and analyze their workout history manually.

This project solves that problem by providing an easy-to-use dashboard where users can:

- Log daily fitness activities.
- Calculate health metrics.
- Track calories burned.
- Monitor workout duration.
- View activity trends through graphical visualization.

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Pandas | Data Loading & Data Analysis |
| NumPy | Numerical Calculations |
| Matplotlib | Graph Visualization |
| Seaborn | Heatmap Visualization |
| CSV File | Data Storage |
| OOP | Modular Program Design |

---

# 📂 Project Structure

```
Personal_Fitness_Tracker/
│
├── fitness_tracker.py
├── Fitness_Activities.csv
├── README.md
```

---

# 📋 Dataset Information

Dataset File:

```
Fitness_Activities.csv
```

Columns:

| Column | Description |
|---------|-------------|
| Date | Date of Activity |
| Activity_Type | Type of Exercise |
| Duration | Workout Duration (Minutes) |
| Calories_Burned | Calories Burned |

Example:

| Date | Activity_Type | Duration | Calories_Burned |
|------|---------------|----------|-----------------|
|2026-06-01|Walking|30|120|
|2026-06-02|Running|45|420|
|2026-06-03|Cycling|60|500|

---

# 🚀 Features

## 1. User Activity Logging

Users can enter:

- Date
- Activity Type
- Duration
- Calories Burned

The system validates all inputs before saving.

Example:

```
Enter Date :
2026-06-22

Activity Type :
Running

Duration :
45

Calories Burned :
450
```

---

## 2. Data Validation

The program validates:

- Duration must be greater than zero.
- Calories must be greater than zero.
- Invalid numeric values are rejected.
- Uses loops and conditional statements for validation.

Example:

```
Duration : -10

Output:

Duration must be greater than 0.
```

---

## 3. Object-Oriented Programming

The project follows Object-Oriented Programming principles.

Main Class:

```
FitnessTracker
```

Methods:

```
__init__()

load_data()

save_data()

display_data()

log_activity()

calculate_metrics()

filter_activities()

generate_report()

bar_chart()

line_graph()

pie_chart()

heat_map()

visualize_data()
```

Advantages:

- Encapsulation
- Reusability
- Modular Design
- Easy Maintenance

---

# 📊 Fitness Metrics

The project calculates:

- Total Activities
- Total Duration
- Total Calories Burned
- Average Duration
- Average Calories Burned
- Daily Average Calories
- Activity Frequency
- Percentage Improvement

Example Output

```
Total Activities : 20

Total Calories Burned : 8340

Average Duration : 49.25

Average Calories : 417.00

Daily Average Calories : 417.00

Percentage Improvement : 250%
```

---

# 📈 Data Analysis Using NumPy

NumPy is used for numerical operations.

Examples:

- Sum
- Mean
- Percentage Improvement
- Average Calories
- Average Duration

Functions Used:

```
np.sum()

np.mean()

numpy arrays
```

---

# 📑 Data Handling Using Pandas

Pandas is used for:

- Loading CSV
- Cleaning Data
- Removing Duplicates
- Removing Missing Values
- Creating New Columns
- Grouping Data
- Filtering Records
- Weekly Analysis

New Column Created:

```
Calories_Per_Minute
```

Formula

```
Calories Burned / Duration
```

Example

| Duration | Calories | Calories/Minute |
|-----------|-----------|-----------------|
|40|200|5.0|

---

# 🔍 Filtering Activities

Users can filter records by:

### Activity Type

Example:

```
Running
```

Output:

Only Running activities are displayed.

---

### Date Range

Example:

```
Start Date:
2026-06-01

End Date:
2026-06-10
```

Output:

Displays all activities between selected dates.

---

# 📄 Report Generation

The system generates a summary report including:

- Total Activities
- Calories Burned
- Maximum Calories
- Minimum Calories
- Average Duration
- Activity Summary
- Weekly Trends

---

# 📉 Data Visualization

The project generates four different graphs.

---

## 1. Bar Chart

Displays:

Time spent on each activity.

X-axis

```
Activity Type
```

Y-axis

```
Duration
```

---

## 2. Line Graph

Displays:

Calories burned over time.

X-axis

```
Date
```

Y-axis

```
Calories Burned
```

---

## 3. Pie Chart

Displays:

Percentage distribution of activities.

Example:

Walking - 25%

Running - 20%

Cycling - 15%

etc.

---

## 4. Heat Map

Displays the correlation between:

- Duration
- Calories Burned
- Calories Per Minute

Generated using Seaborn.

---

# 🔄 Program Workflow

```
Start Program

↓

Load CSV Dataset

↓

Display Main Menu

↓

User Selects Option

↓

Perform Requested Operation

↓

Update Dataset

↓

Generate Analysis

↓

Display Graphs

↓

Exit
```

---

# 📜 Main Menu

```
============================================

PERSONAL FITNESS TRACKER DASHBOARD

============================================

1. Display All Activities

2. Log New Activity

3. Calculate Fitness Metrics

4. Filter Activities

5. Generate Report

6. Visualize Data

7. Exit
```

---

# 📦 Required Python Libraries

Install the required libraries using pip.

```
pip install pandas

pip install numpy

pip install matplotlib

pip install seaborn
```

Or install everything together.

```
pip install pandas numpy matplotlib seaborn
```

---

# ▶️ How to Run

Step 1

Download the project.

Step 2

Open the project folder in VS Code.

Step 3

Install required libraries.

Step 4

Ensure the dataset

```
Fitness_Activities.csv
```

is present.

Step 5

Run the project.

```
python fitness_tracker.py
```

---

# 💡 Concepts Used

✅ Python Programming

✅ Functions

✅ Control Structures

✅ Loops

✅ Exception Handling

✅ Object-Oriented Programming

✅ Classes and Objects

✅ Encapsulation

✅ NumPy

✅ Pandas

✅ CSV Handling

✅ Data Cleaning

✅ Data Analysis

✅ Data Visualization

✅ Matplotlib

✅ Seaborn

---

# 📚 Learning Outcomes

After completing this project, students will understand:

- Python project development
- Working with CSV datasets
- Object-Oriented Programming
- Data preprocessing
- Numerical analysis
- Data visualization
- User input validation
- File handling
- Report generation

---

# 🔮 Future Enhancements

The project can be extended by adding:

- Login and Authentication
- BMI Calculator
- Heart Rate Tracking
- Water Intake Tracker
- Sleep Monitoring
- Monthly Reports
- PDF Report Export
- Database Integration (MySQL/SQLite)
- GUI using Tkinter
- Web Dashboard using Flask or Django

---

# 👨‍💻 Author

**Project Name**

Personal Fitness Tracker Dashboard

**Developed Using**

Python, NumPy, Pandas, Matplotlib, Seaborn

**Project Type**

Mini Project (BCA)

---

# 📄 Conclusion

The Personal Fitness Tracker Dashboard successfully demonstrates the implementation of Python programming concepts with real-world data analysis. It enables users to record fitness activities, calculate important health metrics, generate reports, and visualize workout progress through interactive charts.

The project integrates Object-Oriented Programming, NumPy, Pandas, Matplotlib, and Seaborn, making it an excellent example of data analysis and visualization in Python.

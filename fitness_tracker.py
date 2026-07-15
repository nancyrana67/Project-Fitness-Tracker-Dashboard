# ==========================================================
# Personal Fitness Tracker Dashboard
# File Name : fitness_tracker.py
# Part - 1
# ==========================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


class FitnessTracker:

    def __init__(self, filename="D:\\csvfiles\\Fitness_Activities.csv"):
        self.filename = filename

        # Create CSV if it doesn't exist
        if not os.path.exists(self.filename):
            df = pd.DataFrame(columns=[
                "Date",
                "Activity_Type",
                "Duration",
                "Calories_Burned"
            ])
            df.to_csv(self.filename, index=False)

        self.load_data()

    # ---------------------------------------------
    # Load Dataset
    # ---------------------------------------------
    def load_data(self):
        self.df = pd.read_csv(self.filename)

        if not self.df.empty:

            # Remove duplicate rows
            self.df.drop_duplicates(inplace=True)

            # Remove missing values
            self.df.dropna(inplace=True)

            # Convert Date column
            self.df["Date"] = pd.to_datetime(self.df["Date"])

            # Create New Column
            self.df["Calories_Per_Minute"] = (
                self.df["Calories_Burned"] /
                self.df["Duration"]
            ).round(2)

    # ---------------------------------------------
    # Save Dataset
    # ---------------------------------------------
    def save_data(self):
        self_df = self.df.copy()

        if "Calories_Per_Minute" in self_df.columns:
            self_df.drop(columns=["Calories_Per_Minute"], inplace=True)

        self_df.to_csv(self.filename, index=False)

    # ---------------------------------------------
    # Log New Activity
    # ---------------------------------------------
    def log_activity(self):

        print("\n========= Add New Activity =========")
        while True:
            try:   
                date = input("Date (YYYY-MM-DD): ")
                pd.to_datetime(date)  # Validate date format
                break
            except:
                print("Invalid date format. Please enter in YYYY-MM-DD format.")

        activity = input("Activity Type: ").title()

        # Validation using control structure

        while True:
            try:
                duration = int(input("Duration (Minutes): "))

                if duration <= 0:
                    print("Duration must be greater than 0.")
                else:
                    break

            except ValueError:
                print("Please enter a valid number.")

        while True:
            try:
                calories = float(input("Calories Burned: "))

                if calories <= 0:
                    print("Calories must be positive.")
                else:
                    break

            except ValueError:
                print("Please enter a valid number.")

        new_data = pd.DataFrame({

            "Date": [date],
            "Activity_Type": [activity],
            "Duration": [duration],
            "Calories_Burned": [calories]

        })

        self.df = pd.concat([self.df, new_data], ignore_index=True)

        #convert Date column
        self.df["Date"] = pd.to_datetime(self.df["Date"])

        #create calories per minutes column 
        self.df["Calories_Per_Minute"] = (
            self.df["Calories_Burned"] /
            self.df["Duration"]
        ).round(2)

        #save the updated data 
        self.save_data()

        print("\nActivity Added Successfully!")

    # ---------------------------------------------
    # Calculate Fitness Metrics
    # ---------------------------------------------
    def calculate_metrics(self):

        if self.df.empty:
            print("\nNo Data Available.")
            return

        print("\n========= FITNESS METRICS =========")

        total_calories = np.sum(self.df["Calories_Burned"])

        total_duration = np.sum(self.df["Duration"])

        average_duration = np.mean(self.df["Duration"])

        average_calories = np.mean(self.df["Calories_Burned"])

        total_activities = len(self.df)

        activity_frequency = (
            self.df["Activity_Type"]
            .value_counts()
        )

        daily_average = (
            self.df.groupby("Date")["Calories_Burned"]
            .sum()
            .mean()
        )

        # Percentage Improvement
        calories = self.df["Calories_Burned"].values

        if len(calories) > 1:
            improvement = (
                ((calories[-1] - calories[0]) /
                 calories[0]) * 100
            )
        else:
            improvement = 0

        print(f"Total Activities : {total_activities}")

        print(f"Total Duration : {total_duration:.0f} Minutes")

        print(f"Total Calories Burned : {total_calories:.0f}")

        print(f"Average Duration : {average_duration:.2f} Minutes")

        print(f"Average Calories : {average_calories:.2f}")

        print(f"Daily Average Calories : {daily_average:.2f}")

        print(f"Percentage Improvement : {improvement:.2f}%")

        print("\nActivity Frequency")

        print(activity_frequency)

    # ---------------------------------------------
    # Display Dataset
    # ---------------------------------------------
    def display_data(self):

        if self.df.empty:
            print("\nNo Data Found.")

        else:
            print("\n========== FITNESS DATA ==========\n")
            print(self.df)
    
        # ---------------------------------------------
    # Filter Activities
    # ---------------------------------------------
    def filter_activities(self):

        if self.df.empty:
            print("\nNo Data Available.")
            return

        print("\n========= FILTER OPTIONS =========")
        print("1. Filter by Activity Type")
        print("2. Filter by Date Range")

        choice = input("Enter your choice: ")

        if choice == "1":

            activity = input("Enter Activity Type: ").title()

            filtered = self.df[
                self.df["Activity_Type"] == activity
            ]

            if filtered.empty:
                print("\nNo records found.")
            else:
                print(filtered)

        elif choice == "2":

            start = input("Start Date (YYYY-MM-DD): ")
            end = input("End Date (YYYY-MM-DD): ")

            start = pd.to_datetime(start)
            end = pd.to_datetime(end)

            filtered = self.df[
                (self.df["Date"] >= start) &
                (self.df["Date"] <= end)
            ]

            if filtered.empty:
                print("\nNo records found.")
            else:
                print(filtered)

        else:
            print("Invalid Choice.")

    # ---------------------------------------------
    # Generate Report
    # ---------------------------------------------
    def generate_report(self):

        if self.df.empty:
            print("\nNo Data Available.")
            return

        print("\n============= FITNESS REPORT =============")

        print("\nTotal Activities :",
              len(self.df))

        print("Total Calories Burned :",
              self.df["Calories_Burned"].sum())

        print("Average Duration :",
              round(self.df["Duration"].mean(), 2))

        print("Maximum Calories Burned :",
              self.df["Calories_Burned"].max())

        print("Minimum Calories Burned :",
              self.df["Calories_Burned"].min())

        print("\nActivity Summary")

        summary = self.df.groupby(
            "Activity_Type"
        ).agg({

            "Duration": "sum",
            "Calories_Burned": "sum"

        })

        print(summary)

        print("\nWeekly Trends")

        weekly = self.df.copy()

        weekly["Week"] = weekly["Date"].dt.isocalendar().week

        weekly_summary = weekly.groupby("Week").agg({

            "Duration": "sum",
            "Calories_Burned": "sum"

        })

        print(weekly_summary)

    # ---------------------------------------------
    # Bar Chart
    # ---------------------------------------------
    def bar_chart(self):

        if self.df.empty:
            print("No Data Available.")
            return

        activity_time = self.df.groupby(
            "Activity_Type"
        )["Duration"].sum()

        plt.figure(figsize=(8,5))

        plt.bar(activity_time.index,
                activity_time.values)

        plt.title("Time Spent On Each Activity")

        plt.xlabel("Activity Type")

        plt.ylabel("Duration (Minutes)")

        plt.grid(axis="y")

        plt.show()

    # ---------------------------------------------
    # Line Graph
    # ---------------------------------------------
    def line_graph(self):

        if self.df.empty:
            print("No Data Available.")
            return

        daily = self.df.groupby(
            "Date"
        )["Calories_Burned"].sum()

        plt.figure(figsize=(10,5))

        plt.plot(
            daily.index,
            daily.values,
            marker="o"
        )

        plt.title("Calories Burned Over Time")

        plt.xlabel("Date")

        plt.ylabel("Calories Burned")

        plt.xticks(rotation=45)

        plt.grid(True)

        plt.show()

    # ---------------------------------------------
    # Pie Chart
    # ---------------------------------------------
    def pie_chart(self):

        if self.df.empty:
            print("No Data Available.")
            return

        activity = self.df[
            "Activity_Type"
        ].value_counts()

        plt.figure(figsize=(7,7))

        plt.pie(
            activity.values,
            labels=activity.index,
            autopct="%1.1f%%",
            startangle=90
        )

        plt.title("Activity Distribution")

        plt.show()

    # ---------------------------------------------
    # Heat Map
    # ---------------------------------------------
    def heat_map(self):

        if self.df.empty:
            print("No Data Available.")
            return

        correlation = self.df[
            ["Duration",
             "Calories_Burned",
             "Calories_Per_Minute"]
        ].corr()

        plt.figure(figsize=(6,5))

        sns.heatmap(
            correlation,
            annot=True,
            cmap="YlGnBu"
        )

        plt.title(
            "Correlation Between Fitness Metrics"
        )

        plt.show()

    # ---------------------------------------------
    # Show All Graphs
    # ---------------------------------------------
    def visualize_data(self):

        self.bar_chart()

        self.line_graph()

        self.pie_chart()

        self.heat_map()


    
# ==========================================================
# Main Program
# ==========================================================

def main():

    tracker = FitnessTracker()

    while True:

        print("\n" + "=" * 50)
        print("      PERSONAL FITNESS TRACKER DASHBOARD")
        print("=" * 50)

        print("1. Display All Activities")
        print("2. Log New Activity")
        print("3. Calculate Fitness Metrics")
        print("4. Filter Activities")
        print("5. Generate Fitness Report")
        print("6. Visualize Fitness Data")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ")

        if choice == "1":
            tracker.display_data()

        elif choice == "2":
            tracker.log_activity()

        elif choice == "3":
            tracker.calculate_metrics()

        elif choice == "4":
            tracker.filter_activities()

        elif choice == "5":
            tracker.generate_report()

        elif choice == "6":

            print("\nGenerating Charts...")

            tracker.visualize_data()

        elif choice == "7":

            print("\n========================================")
            print(" Thank You for using Fitness Tracker!")
            print(" Stay Healthy and Keep Exercising!")
            print("========================================")

            break

        else:
            print("\nInvalid choice! Please enter a number between 1 and 7.")


# ==========================================================
# Program Entry Point
# ==========================================================

if __name__ == "__main__":
    main()
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
@st.cache
def load_data():
    return pd.read_csv("data_science_salaries.csv")

df = load_data()

# Title and introduction
st.title("Data Science Salary Analysis")
st.write("""
This app provides an in-depth analysis of salaries for data science roles across various factors like experience, company size, job title, and more. 
Explore the visualizations below to gain insights.
""")

# Sidebar for navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Choose a section", [
    "Average Salary Trend by Year",
    "Top 10 Highest and Lowest Paying Job Titles",
    "Salary by Experience Level",
    "Top 7 Highest Paying Locations",
    "Salary by Work Model",
    "Salary by Employment Type",
    "Salary by Company Size and Job Title"
])

# Function to add data labels on the bar charts
def add_data_labels(ax, data):
    for p in ax.patches:
        height = p.get_height()
        ax.annotate(
            f"${height:,.0f}",  # Format the salary value
            (p.get_x() + p.get_width() / 2., height),  # Position at the top of the bar
            ha="center", 
            va="bottom",  # Position above the bar
            fontsize=10, 
            color="black",
            fontweight="bold"  # Make the labels more prominent
        )

# Section 1: Average Salary Trend by Year
if selection == "Average Salary Trend by Year":
    st.header("Average Salary Trend (2020-2024)")
    average_salary_per_year = df.groupby("work_year")["salary_in_usd"].mean()
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=average_salary_per_year.index, y=average_salary_per_year.values, marker='o', color='b')
    plt.title("Average Salary Trend (2020–2024)", fontsize=16)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Average Salary (USD)", fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot()

# Section 2: Top 10 Highest and Lowest Paying Job Titles
elif selection == "Top 10 Highest and Lowest Paying Job Titles":
    st.header("Top 10 Highest and Lowest Paying Job Titles")
    average_salary_by_job = df.groupby("job_title")["salary_in_usd"].mean().sort_values(ascending=False)
    top_10_highest = average_salary_by_job.head(10)
    top_10_lowest = average_salary_by_job.tail(10)
    
    # Highest-paying job titles
    st.subheader("Top 10 Highest Paying Job Titles")
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x=top_10_highest.values, y=top_10_highest.index, palette="Blues_r")
    add_data_labels(ax, top_10_highest)
    plt.title("Top 10 Highest-Paying Job Titles", fontsize=16)
    plt.xlabel("Average Salary (USD)", fontsize=10)
    plt.ylabel("Job Titles", fontsize=10)
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    st.pyplot()

    # Lowest-paying job titles
    st.subheader("Top 10 Lowest Paying Job Titles")
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x=top_10_lowest.values, y=top_10_lowest.index, palette="Reds_r")
    add_data_labels(ax, top_10_lowest)
    plt.title("Top 10 Lowest-Paying Job Titles", fontsize=16)
    plt.xlabel("Average Salary (USD)", fontsize=10)
    plt.ylabel("Job Titles", fontsize=10)
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    st.pyplot()

# Section 3: Salary by Experience Level
elif selection == "Salary by Experience Level":
    st.header("Salary by Experience Level")
    average_salary_by_experience = df.groupby("experience_level")["salary_in_usd"].mean()
    plt.figure(figsize=(8, 6))
    ax = sns.barplot(x=average_salary_by_experience.index, y=average_salary_by_experience.values, palette="viridis")
    add_data_labels(ax, average_salary_by_experience)
    plt.title("Average Salary by Experience Level", fontsize=16)
    plt.xlabel("Experience Level", fontsize=12)
    plt.ylabel("Average Salary (USD)", fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot()

# Section 4: Top 7 Highest Paying Locations
elif selection == "Top 7 Highest Paying Locations":
    st.header("Top 7 Highest Paying Locations")
    average_salary_by_location = df.groupby("company_location")["salary_in_usd"].mean().sort_values(ascending=False)
    top_7_highest_location = average_salary_by_location.head(7)
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x=top_7_highest_location.values, y=top_7_highest_location.index, palette="Blues_r")
    add_data_labels(ax, top_7_highest_location)
    plt.title("Top 7 Highest-Paying Company Locations", fontsize=16)
    plt.xlabel("Average Salary (USD)", fontsize=12)
    plt.ylabel("Company Locations", fontsize=12)
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    st.pyplot()

# Section 5: Salary by Work Model
elif selection == "Salary by Work Model":
    st.header("Salary by Work Model")
    average_salary_by_work_model = df.groupby("work_models")["salary_in_usd"].mean()
    plt.figure(figsize=(8, 6))
    ax = sns.barplot(x=average_salary_by_work_model.index, y=average_salary_by_work_model.values, palette="viridis")
    add_data_labels(ax, average_salary_by_work_model)
    plt.title("Average Salary by Work Model", fontsize=16)
    plt.xlabel("Work Model", fontsize=12)
    plt.ylabel("Average Salary (USD)", fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot()

# Section 6: Salary by Employment Type
elif selection == "Salary by Employment Type":
    st.header("Salary by Employment Type")
    average_salary_by_employment_type = df.groupby("employment_type")["salary_in_usd"].mean()
    plt.figure(figsize=(8, 6))
    ax = sns.barplot(x=average_salary_by_employment_type.index, y=average_salary_by_employment_type.values, palette="coolwarm")
    add_data_labels(ax, average_salary_by_employment_type)
    plt.title("Average Salary by Employment Type", fontsize=16)
    plt.xlabel("Employment Type", fontsize=12)
    plt.ylabel("Average Salary (USD)", fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot()

# Section 7: Salary by Company Size and Job Title
elif selection == "Salary by Company Size and Job Title":
    st.header("Average Salary by Company Size and Job Title")
    average_salary_by_company_size_job = df.groupby(["company_size", "job_title"])["salary_in_usd"].mean().unstack()
    ax = average_salary_by_company_size_job.plot(kind="bar", figsize=(12, 8), colormap="viridis")
    add_data_labels(ax, average_salary_by_company_size_job)
    plt.title("Average Salary by Company Size and Job Title", fontsize=16)
    plt.xlabel("Company Size", fontsize=12)
    plt.ylabel("Average Salary (USD)", fontsize=12)
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend(title="Job Titles", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    st.pyplot()

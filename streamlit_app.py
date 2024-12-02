import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to load data
@st.cache
def load_data(uploaded_file):
    return pd.read_csv(uploaded_file)

# Streamlit layout
st.title('Data Science Salary Analysis')

# Upload CSV file
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Load the data
    df = load_data(uploaded_file)

    # Show the first few rows of the dataframe
    st.subheader("Data Preview")
    st.write(df.head())

    # Dropdown for graph selection
    chart_type = st.selectbox(
        "Select the chart to display",
        [
            "Average Salary Trend (2020–2024)",
            "Top 10 Highest-Paying Job Titles",
            "Top 10 Lowest-Paying Job Titles",
            "Top 7 Highest-Paying Company Locations",
            "Average Salary by Work Model",
            "Average Salary by Employment Type",
            "Average Salary by Experience Level",
            "Average Salary by Company Size and Job Title"
        ]
    )

    # Graph rendering logic
    if chart_type == "Average Salary Trend (2020–2024)":
        st.subheader("Average Salary Trend (2020–2024)")
        average_salary_per_year = df.groupby("work_year")["salary_in_usd"].mean()
        plt.figure(figsize=(10, 6))
        sns.lineplot(x=average_salary_per_year.index, y=average_salary_per_year.values, marker='o', color='b')
        plt.title("Average Salary Trend (2020–2024)", fontsize=16)
        plt.xlabel("Year", fontsize=12)
        plt.ylabel("Average Salary (USD)", fontsize=12)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        st.pyplot(plt)

    elif chart_type == "Top 10 Highest-Paying Job Titles":
        st.subheader("Top 10 Highest-Paying Job Titles")
        average_salary_by_job = df.groupby("job_title")["salary_in_usd"].mean().sort_values(ascending=False)
        top_10_highest = average_salary_by_job.head(10)
        plt.figure(figsize=(10, 6))
        sns.barplot(x=top_10_highest.values, y=top_10_highest.index, palette="Blues_r")
        for i, value in enumerate(top_10_highest.values):
            plt.text(value, i, f"${value:,.0f}", fontsize=10, color="black", va="center")
        plt.title("Top 10 Highest-Paying Job Titles", fontsize=16)
        plt.xlabel("Average Salary (USD)", fontsize=10)
        plt.ylabel("Job Titles", fontsize=10)
        plt.grid(axis='x', linestyle='--', alpha=0.7)
        st.pyplot(plt)

    elif chart_type == "Top 10 Lowest-Paying Job Titles":
        st.subheader("Top 10 Lowest-Paying Job Titles")
        average_salary_by_job = df.groupby("job_title")["salary_in_usd"].mean().sort_values(ascending=True)
        top_10_lowest = average_salary_by_job.head(10)
        plt.figure(figsize=(10, 6))
        sns.barplot(x=top_10_lowest.values, y=top_10_lowest.index, palette="Reds_r")
        for i, value in enumerate(top_10_lowest.values):
            plt.text(value, i, f"${value:,.0f}", fontsize=10, color="black", va="center")
        plt.title("Top 10 Lowest-Paying Job Titles", fontsize=16)
        plt.xlabel("Average Salary (USD)", fontsize=10)
        plt.ylabel("Job Titles", fontsize=10)
        plt.grid(axis='x', linestyle='--', alpha=0.7)
        st.pyplot(plt)

    elif chart_type == "Top 7 Highest-Paying Company Locations":
        st.subheader("Top 7 Highest-Paying Company Locations")
        average_salary_by_location = df.groupby("company_location")["salary_in_usd"].mean().sort_values(ascending=False)
        top_7_highest_location = average_salary_by_location.head(7)
        plt.figure(figsize=(10, 6))
        sns.barplot(x=top_7_highest_location.values, y=top_7_highest_location.index, palette="Blues_r")
        for i, value in enumerate(top_7_highest_location.values):
            plt.text(value, i, f"${value:,.0f}", fontsize=10, color="black", va="center")
        plt.title("Top 7 Highest-Paying Company Locations", fontsize=16)
        plt.xlabel("Average Salary (USD)", fontsize=12)
        plt.ylabel("Company Locations", fontsize=12)
        plt.grid(axis="x", linestyle="--", alpha=0.5)
        st.pyplot(plt)

    elif chart_type == "Average Salary by Work Model":
        st.subheader("Average Salary by Work Model")
        average_salary_by_work_model = df.groupby("work_models")["salary_in_usd"].mean()
        plt.figure(figsize=(8, 6))
        sns.barplot(x=average_salary_by_work_model.index, y=average_salary_by_work_model.values, palette="viridis")
        plt.title("Average Salary by Work Model", fontsize=16)
        plt.xlabel("Work Model", fontsize=12)
        plt.ylabel("Average Salary (USD)", fontsize=12)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        st.pyplot(plt)

    elif chart_type == "Average Salary by Employment Type":
        st.subheader("Average Salary by Employment Type")
        average_salary_by_employment_type = df.groupby("employment_type")["salary_in_usd"].mean()
        plt.figure(figsize=(8, 6))
        sns.barplot(x=average_salary_by_employment_type.index, y=average_salary_by_employment_type.values, palette="coolwarm")
        plt.title("Average Salary by Employment Type", fontsize=16)
        plt.xlabel("Employment Type", fontsize=12)
        plt.ylabel("Average Salary (USD)", fontsize=12)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        st.pyplot(plt)

    elif chart_type == "Average Salary by Experience Level":
        st.subheader("Average Salary by Experience Level")
        average_salary_by_experience = df.groupby("experience_level")["salary_in_usd"].mean()
        plt.figure(figsize=(8, 6))
        sns.barplot(x=average_salary_by_experience.index, y=average_salary_by_experience.values, palette="viridis")
        plt.title("Average Salary by Experience Level", fontsize=16)
        plt.xlabel("Experience Level", fontsize=12)
        plt.ylabel("Average Salary (USD)", fontsize=12)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        st.pyplot(plt)

    elif chart_type == "Average Salary by Company Size and Job Title":
        st.subheader("Average Salary by Company Size and Job Title")
        average_salary_by_company_size_job = df.groupby(["company_size", "job_title"])["salary_in_usd"].mean().unstack()
        fig, ax = plt.subplots(figsize=(12, 8))
        average_salary_by_company_size_job.plot(kind="bar", ax=ax, colormap="viridis")
        ax.set_title("Average Salary by Company Size and Job Title", fontsize=16)
        ax.set_xlabel("Company Size", fontsize=12)
        ax.set_ylabel("Average Salary (USD)", fontsize=12)
        ax.legend(title="Job Titles", bbox_to_anchor=(1.05, 1), loc="upper left")
        ax.grid(axis="y", linestyle="--", alpha=0.7)
        st.pyplot(fig)

else:
    st.write("Please upload a CSV file to get started.")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to load data
@st.cache
def load_data(uploaded_file):
    return pd.read_csv(uploaded_file)

# Streamlit layout
st.title('Data Science Salary Analysis', fontsize=24)

# Upload CSV file
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Load the data
    df = load_data(uploaded_file)

    # Move the dropdown to the left sidebar
    chart_type = st.sidebar.selectbox(
        "Select the chart to display",
        [
            "Average Salary Trend (2020–2024)",
            "Top 10 Highest-Paying Job Titles",
            "Top 10 Lowest-Paying Job Titles",
            "Top 7 Highest-Paying Company Locations",
            "Average Salary by Work Model",
            "Average Salary by Employment Type",
            "Average Salary by Experience Level"
        ],
        index=0
    )

    # Graph rendering logic
    if chart_type == "Average Salary Trend (2020–2024)":
        st.subheader("Average Salary Trend (2020–2024)", fontsize=20)
        average_salary_per_year = df.groupby("work_year")["salary_in_usd"].mean()
        plt.figure(figsize=(18, 12))  # Large figure size
        sns.lineplot(x=average_salary_per_year.index, y=average_salary_per_year.values, marker='o', color='b')
        for i, value in enumerate(average_salary_per_year.values):
            plt.text(average_salary_per_year.index[i], value, f"${value:,.0f}", color='black', fontsize=14, ha='center')
        plt.title("Average Salary Trend (2020–2024)", fontsize=22)
        plt.xlabel("Year", fontsize=18)
        plt.ylabel("Average Salary (USD)", fontsize=18)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        st.pyplot(plt)

    elif chart_type == "Top 10 Highest-Paying Job Titles":
        st.subheader("Top 10 Highest-Paying Job Titles", fontsize=20)
        average_salary_by_job = df.groupby("job_title")["salary_in_usd"].mean().sort_values(ascending=False)
        top_10_highest = average_salary_by_job.head(10)
        plt.figure(figsize=(18, 12))  # Large figure size
        sns.barplot(x=top_10_highest.values, y=top_10_highest.index, palette="Blues_r")
        for i, value in enumerate(top_10_highest.values):
            plt.text(value, i, f"${value:,.0f}", fontsize=14, color="black", va="center")
        plt.title("Top 10 Highest-Paying Job Titles", fontsize=22)
        plt.xlabel("Average Salary (USD)", fontsize=18)
        plt.ylabel("Job Titles", fontsize=18)
        plt.grid(axis='x', linestyle='--', alpha=0.7)
        st.pyplot(plt)

    elif chart_type == "Top 10 Lowest-Paying Job Titles":
        st.subheader("Top 10 Lowest-Paying Job Titles", fontsize=20)
        average_salary_by_job = df.groupby("job_title")["salary_in_usd"].mean().sort_values(ascending=True)
        top_10_lowest = average_salary_by_job.head(10)
        plt.figure(figsize=(18, 12))  # Large figure size
        sns.barplot(x=top_10_lowest.values, y=top_10_lowest.index, palette="Reds_r")
        for i, value in enumerate(top_10_lowest.values):
            plt.text(value, i, f"${value:,.0f}", fontsize=14, color="black", va="center")
        plt.title("Top 10 Lowest-Paying Job Titles", fontsize=22)
        plt.xlabel("Average Salary (USD)", fontsize=18)
        plt.ylabel("Job Titles", fontsize=18)
        plt.grid(axis='x', linestyle='--', alpha=0.7)
        st.pyplot(plt)

    elif chart_type == "Top 7 Highest-Paying Company Locations":
        st.subheader("Top 7 Highest-Paying Company Locations", fontsize=20)
        average_salary_by_location = df.groupby("company_location")["salary_in_usd"].mean().sort_values(ascending=False)
        top_7_highest_location = average_salary_by_location.head(7)
        plt.figure(figsize=(18, 12))  # Large figure size
        sns.barplot(x=top_7_highest_location.values, y=top_7_highest_location.index, palette="Blues_r")
        for i, value in enumerate(top_7_highest_location.values):
            plt.text(value, i, f"${value:,.0f}", fontsize=14, color="black", va="center")
        plt.title("Top 7 Highest-Paying Company Locations", fontsize=22)
        plt.xlabel("Average Salary (USD)", fontsize=18)
        plt.ylabel("Company Locations", fontsize=18)
        plt.grid(axis="x", linestyle="--", alpha=0.5)
        st.pyplot(plt)

    elif chart_type == "Average Salary by Work Model":
        st.subheader("Average Salary by Work Model", fontsize=20)
        average_salary_by_work_model = df.groupby("work_models")["salary_in_usd"].mean()
        plt.figure(figsize=(18, 12))  # Large figure size
        sns.barplot(x=average_salary_by_work_model.index, y=average_salary_by_work_model.values, palette="viridis")
        for i, value in enumerate(average_salary_by_work_model.values):
            plt.text(i, value, f"${value:,.0f}", fontsize=14, color="black", va="center", ha="center")
        plt.title("Average Salary by Work Model", fontsize=22)
        plt.xlabel("Work Model", fontsize=18)
        plt.ylabel("Average Salary (USD)", fontsize=18)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        st.pyplot(plt)

    elif chart_type == "Average Salary by Employment Type":
        st.subheader("Average Salary by Employment Type", fontsize=20)
        average_salary_by_employment_type = df.groupby("employment_type")["salary_in_usd"].mean()
        plt.figure(figsize=(18, 12))  # Large figure size
        sns.barplot(x=average_salary_by_employment_type.index, y=average_salary_by_employment_type.values, palette="coolwarm")
        for i, value in enumerate(average_salary_by_employment_type.values):
            plt.text(i, value, f"${value:,.0f}", fontsize=14, color="black", va="center", ha="center")
        plt.title("Average Salary by Employment Type", fontsize=22)
        plt.xlabel("Employment Type", fontsize=18)
        plt.ylabel("Average Salary (USD)", fontsize=18)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        st.pyplot(plt)

    elif chart_type == "Average Salary by Experience Level":
        st.subheader("Average Salary by Experience Level", fontsize=20)
        average_salary_by_experience = df.groupby("experience_level")["salary_in_usd"].mean()
        plt.figure(figsize=(18, 12))  # Large figure size
        sns.barplot(x=average_salary_by_experience.index, y=average_salary_by_experience.values, palette="viridis")
        for i, value in enumerate(average_salary_by_experience.values):
            plt.text(i, value, f"${value:,.0f}", fontsize=14, color="black", va="center", ha="center")
        plt.title("Average Salary by Experience Level", fontsize=22)
        plt.xlabel("Experience Level", fontsize=18)
        plt.ylabel("Average Salary (USD)", fontsize=18)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        st.pyplot(plt)

else:
    st.write("Please upload a CSV file to get started.")

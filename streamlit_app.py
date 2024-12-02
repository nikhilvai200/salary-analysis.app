import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to load data
@st.cache
def load_data(uploaded_file):
    return pd.read_csv(uploaded_file)

# Streamlit layout
st.markdown('<h1 style="font-size:36px;">Data Science Salary Analysis</h1>', unsafe_allow_html=True)

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
        ]
    )

    # Define function for adding data labels
    def add_data_labels(ax, orientation='v'):
        for p in ax.patches:
            if orientation == 'v':  # Vertical bars (e.g., column chart)
                ax.annotate(f"${p.get_height():,.0f}",
                            (p.get_x() + p.get_width() / 2., p.get_height()),
                            ha='center', va='bottom', fontsize=10, color="black")
            elif orientation == 'h':  # Horizontal bars (e.g., bar chart)
                ax.annotate(f"${p.get_width():,.0f}",
                            (p.get_width(), p.get_y() + p.get_height() / 2.),
                            ha='left', va='center', fontsize=10, color="black")

    # Graph rendering logic
    if chart_type == "Average Salary Trend (2020–2024)":
        st.markdown('<h2 style="font-size:28px;">Average Salary Trend (2020–2024)</h2>', unsafe_allow_html=True)
        average_salary_per_year = df.groupby("work_year")["salary_in_usd"].mean()
        plt.figure(figsize=(14, 8))
        sns.lineplot(x=average_salary_per_year.index, y=average_salary_per_year.values, marker='o', color='b')
        for i, value in enumerate(average_salary_per_year.values):
            plt.text(average_salary_per_year.index[i], value, f"${value:,.0f}", color='black', fontsize=10, ha='center')
        plt.title("Average Salary Trend (2020–2024)", fontsize=18)
        plt.xlabel("Year", fontsize=14)
        plt.ylabel("Average Salary (USD)", fontsize=14)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        st.pyplot(plt)

    elif chart_type == "Top 10 Highest-Paying Job Titles":
        st.markdown('<h2 style="font-size:28px;">Top 10 Highest-Paying Job Titles</h2>', unsafe_allow_html=True)
        average_salary_by_job = df.groupby("job_title")["salary_in_usd"].mean().sort_values(ascending=False)
        top_10_highest = average_salary_by_job.head(10)
        fig, ax = plt.subplots(figsize=(14, 8))
        sns.barplot(x=top_10_highest.values, y=top_10_highest.index, palette="Blues_r", ax=ax)
        add_data_labels(ax, orientation='h')  # Add data labels to the right
        ax.set_title("Top 10 Highest-Paying Job Titles", fontsize=18)
        ax.set_xlabel("Average Salary (USD)", fontsize=14)
        ax.set_ylabel("Job Titles", fontsize=14)
        ax.grid(axis='x', linestyle='--', alpha=0.7)
        st.pyplot(fig)

    elif chart_type == "Top 10 Lowest-Paying Job Titles":
        st.markdown('<h2 style="font-size:28px;">Top 10 Lowest-Paying Job Titles</h2>', unsafe_allow_html=True)
        average_salary_by_job = df.groupby("job_title")["salary_in_usd"].mean().sort_values(ascending=True)
        top_10_lowest = average_salary_by_job.head(10)
        fig, ax = plt.subplots(figsize=(14, 8))
        sns.barplot(x=top_10_lowest.values, y=top_10_lowest.index, palette="Reds_r", ax=ax)
        add_data_labels(ax, orientation='h')  # Add data labels to the right
        ax.set_title("Top 10 Lowest-Paying Job Titles", fontsize=18)
        ax.set_xlabel("Average Salary (USD)", fontsize=14)
        ax.set_ylabel("Job Titles", fontsize=14)
        ax.grid(axis='x', linestyle='--', alpha=0.7)
        st.pyplot(fig)

    elif chart_type == "Top 7 Highest-Paying Company Locations":
        st.markdown('<h2 style="font-size:28px;">Top 7 Highest-Paying Company Locations</h2>', unsafe_allow_html=True)
        average_salary_by_location = df.groupby("company_location")["salary_in_usd"].mean().sort_values(ascending=False)
        top_7_highest_location = average_salary_by_location.head(7)
        fig, ax = plt.subplots(figsize=(14, 8))
        sns.barplot(x=top_7_highest_location.values, y=top_7_highest_location.index, palette="Blues_r", ax=ax)
        add_data_labels(ax, orientation='h')  # Add data labels to the right
        ax.set_title("Top 7 Highest-Paying Company Locations", fontsize=18)
        ax.set_xlabel("Average Salary (USD)", fontsize=14)
        ax.set_ylabel("Company Locations", fontsize=14)
        ax.grid(axis="x", linestyle="--", alpha=0.5)
        st.pyplot(fig)

    elif chart_type == "Average Salary by Work Model":
        st.markdown('<h2 style="font-size:28px;">Average Salary by Work Model</h2>', unsafe_allow_html=True)
        average_salary_by_work_model = df.groupby("work_models")["salary_in_usd"].mean()
        fig, ax = plt.subplots(figsize=(14, 8))
        sns.barplot(x=average_salary_by_work_model.index, y=average_salary_by_work_model.values, palette="viridis", ax=ax)
        add_data_labels(ax, orientation='v')  # Add data labels on top
        ax.set_title("Average Salary by Work Model", fontsize=18)
        ax.set_xlabel("Work Model", fontsize=14)
        ax.set_ylabel("Average Salary (USD)", fontsize=14)
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        st.pyplot(fig)

    elif chart_type == "Average Salary by Employment Type":
        st.markdown('<h2 style="font-size:28px;">Average Salary by Employment Type</h2>', unsafe_allow_html=True)
        average_salary_by_employment_type = df.groupby("employment_type")["salary_in_usd"].mean()
        fig, ax = plt.subplots(figsize=(14, 8))
        sns.barplot(x=average_salary_by_employment_type.index, y=average_salary_by_employment_type.values, palette="coolwarm", ax=ax)
        add_data_labels(ax, orientation='v')  # Add data labels on top
        ax.set_title("Average Salary by Employment Type", fontsize=18)
        ax.set_xlabel("Employment Type", fontsize=14)
        ax.set_ylabel("Average Salary (USD)", fontsize=14)
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        st.pyplot(fig)

    elif chart_type == "Average Salary by Experience Level":
        st.markdown('<h2 style="font-size:28px;">Average Salary by Experience Level</h2>', unsafe_allow_html=True)
        average_salary_by_experience = df.groupby("experience_level")["salary_in_usd"].mean()
        fig, ax = plt.subplots(figsize=(14, 8))
        sns.barplot(x=average_salary_by_experience.index, y=average_salary_by_experience.values, palette="viridis", ax=ax)
        add_data_labels(ax, orientation='v')  # Add data labels on top
        ax.set_title("Average Salary by Experience Level", fontsize=18)
        ax.set_xlabel("Experience Level", fontsize=14)
        ax.set_ylabel("Average Salary (USD)", fontsize=14)
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        st.pyplot(fig)

else:
    st.markdown('<h3 style="font-size:24px;">Please upload a CSV file to get started.</h3>', unsafe_allow_html=True)

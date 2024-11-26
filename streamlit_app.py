import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to load the dataset
def load_data():
    uploaded_file = st.file_uploader("Upload your CSV data", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        return df
    else:
        st.warning("Please upload a CSV file to proceed.")
        return None

# Function to display conclusions
def display_conclusion(description):
    st.write("### Conclusion")
    st.info(description)

# Title and description
st.title("Data Science Job Role Salary Analysis")
st.write("""
    This app provides an analysis of data science job role salaries from 2020 to 2024, 
    including insights into job titles, experience levels, company locations, work models, 
    and more.
""")

# Sidebar for selecting different analysis options
st.sidebar.title("Select Analysis")
options = ["Average Salary Trend", "Top Paying Job Titles", "Salary by Experience", 
           "Highest Paying Locations", "Salary by Work Model", "Employment Type vs Salary",
           "Company Size and Salary", "Larger Companies vs Smaller Companies"]
selection = st.sidebar.selectbox("Choose the analysis you want to view:", options)

# Load data
df = load_data()

# If the data is loaded, proceed with the analysis
if df is not None:
    # Question 1: Average Salary Trend
    if selection == "Average Salary Trend":
        average_salary_per_year = df.groupby("work_year")["salary_in_usd"].mean()
        st.write("### Average Salary Trend (2020–2024)")
        st.line_chart(average_salary_per_year)
        conclusion = f"The average salary has {'increased' if average_salary_per_year.diff().mean() > 0 else 'decreased'} over the years, with a notable {'rise' if average_salary_per_year.diff().mean() > 0 else 'drop'} in recent years."
        display_conclusion(conclusion)

    # Question 2: Top Paying Job Titles
    elif selection == "Top Paying Job Titles":
        top_5_highest = df.groupby("job_title")["salary_in_usd"].mean().nlargest(5)
        top_5_lowest = df.groupby("job_title")["salary_in_usd"].mean().nsmallest(5)
        st.write("### Top 5 Highest-Paying Job Titles")
        st.bar_chart(top_5_highest)
        st.write("### Top 5 Lowest-Paying Job Titles")
        st.bar_chart(top_5_lowest)
        conclusion = (
            f"The top-paying job titles include {', '.join(top_5_highest.index)}, "
            f"while {', '.join(top_5_lowest.index)} are among the lowest-paying roles."
        )
        display_conclusion(conclusion)

    # Question 3: Salary by Experience Level
    elif selection == "Salary by Experience":
        average_salary_by_experience = df.groupby("experience_level")["salary_in_usd"].mean()
        st.write("### Average Salary by Experience Level")
        st.bar_chart(average_salary_by_experience)
        conclusion = (
            f"Salaries generally {'increase' if average_salary_by_experience.is_monotonic else 'vary'} with experience level, "
            f"with {average_salary_by_experience.idxmax()} roles offering the highest pay on average."
        )
        display_conclusion(conclusion)

    # Question 4: Highest Paying Locations
    elif selection == "Highest Paying Locations":
        top_5_locations = df.groupby("company_location")["salary_in_usd"].mean().nlargest(5)
        st.write("### Top 5 Highest Paying Locations")
        st.bar_chart(top_5_locations)
        conclusion = f"The highest-paying locations include {', '.join(top_5_locations.index)}."
        display_conclusion(conclusion)

    # Question 5: Salary by Work Model
    elif selection == "Salary by Work Model":
        average_salary_by_work_model = df.groupby("work_model")["salary_in_usd"].mean()
        st.write("### Average Salary by Work Model")
        st.bar_chart(average_salary_by_work_model)
        conclusion = (
            f"{average_salary_by_work_model.idxmax()} work models offer the highest average salaries, "
            f"while {average_salary_by_work_model.idxmin()} models have the lowest."
        )
        display_conclusion(conclusion)

    # Question 6: Employment Type vs Salary
    elif selection == "Employment Type vs Salary":
        average_salary_by_employment_type = df.groupby("employment_type")["salary_in_usd"].mean()
        st.write("### Average Salary by Employment Type")
        st.bar_chart(average_salary_by_employment_type)
        conclusion = (
            f"{average_salary_by_employment_type.idxmax()} employment types offer the highest pay, "
            f"indicating that employment type significantly impacts salary."
        )
        display_conclusion(conclusion)

    # Question 7: Company Size and Salary
    elif selection == "Company Size and Salary":
        average_salary_by_company_size_job = df.groupby(["company_size", "job_title"])["salary_in_usd"].mean().unstack()
        st.write("### Average Salary by Company Size and Job Title")
        st.dataframe(average_salary_by_company_size_job)
        conclusion = (
            f"Larger companies tend to pay {'more' if df.groupby('company_size')['salary_in_usd'].mean()['L'] > df.groupby('company_size')['salary_in_usd'].mean()['S'] else 'less'} than smaller ones."
        )
        display_conclusion(conclusion)

    # Question 8: Larger Companies vs Smaller Companies
    elif selection == "Larger Companies vs Smaller Companies":
        average_salary_by_company_size = df.groupby("company_size")["salary_in_usd"].mean()
        st.write("### Average Salary by Company Size")
        st.bar_chart(average_salary_by_company_size)
        conclusion = (
            f"On average, larger companies offer {'higher' if average_salary_by_company_size.idxmax() == 'L' else 'lower'} salaries "
            f"than smaller companies."
        )
        
        display_conclusion(conclusion)

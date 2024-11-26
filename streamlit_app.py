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

    # Question 2: Top Paying Job Titles
    elif selection == "Top Paying Job Titles":
        top_5_highest = df.groupby("job_title")["salary_in_usd"].mean().nlargest(5)
        top_5_lowest = df.groupby("job_title")["salary_in_usd"].mean().nsmallest(5)
        st.write("### Top 5 Highest-Paying Job Titles")
        st.bar_chart(top_5_highest)
        st.write("### Top 5 Lowest-Paying Job Titles")
        st.bar_chart(top_5_lowest)

    # Question 3: Salary by Experience Level
    elif selection == "Salary by Experience":
        average_salary_by_experience = df.groupby("experience_level")["salary_in_usd"].mean()
        st.write("### Average Salary by Experience Level")
        st.bar_chart(average_salary_by_experience)

    # Question 4: Highest Paying Locations
    elif selection == "Highest Paying Locations":
        top_5_locations = df.groupby("company_location")["salary_in_usd"].mean().nlargest(5)
        st.write("### Top 5 Highest Paying Locations")
        st.bar_chart(top_5_locations)

    # Question 5: Salary by Work Model
    elif selection == "Salary by Work Model":
        average_salary_by_work_model = df.groupby("work_models")["salary_in_usd"].mean()
        st.write("### Average Salary by Work Model")
        st.bar_chart(average_salary_by_work_model)

    # Question 6: Employment Type vs Salary
    elif selection == "Employment Type vs Salary":
        average_salary_by_employment_type = df.groupby("employment_type")["salary_in_usd"].mean()
        st.write("### Average Salary by Employment Type")
        st.bar_chart(average_salary_by_employment_type)

    # Question 7: Company Size and Salary
    elif selection == "Company Size and Salary":
        average_salary_by_company_size_job = df.groupby(["company_size", "job_title"])["salary_in_usd"].mean().unstack()
        st.write("### Average Salary by Company Size and Job Title")
        st.bar_chart(average_salary_by_company_size_job)

    # Question 8: Larger Companies vs Smaller Companies
    elif selection == "Larger Companies vs Smaller Companies":
        average_salary_by_company_size = df.groupby("company_size")["salary_in_usd"].mean()
        st.write("### Average Salary by Company Size")
        st.bar_chart(average_salary_by_company_size)
    

# Sample data (you can replace this with your actual dataset)
data = {'Category': ['A', 'B', 'C', 'D'],
        'Value': [25, 40, 55, 70]}
df = pd.DataFrame(data)

# Streamlit App Layout
st.title("Bar Chart with Data Labels")

# Plot the bar chart using Seaborn
st.subheader("Bar Chart with Labels on Top")
plt.figure(figsize=(8, 6))

# Create the bar plot
ax = sns.barplot(x='Category', y='Value', data=df)

# Add labels on top of the bars
for p in ax.patches:
    ax.annotate(f'{p.get_height()}',  # Text to display (the height of the bar)
                (p.get_x() + p.get_width() / 2, p.get_height()),  # Position (center of the bar)
                ha='center', va='center',  # Text alignment
                fontsize=10, color='black',  # Font size and color
                xytext=(0, 5),  # Offset text 5 units above the bar
                textcoords='offset points')

# Customize the plot
ax.set_title('Bar Chart with Labels on Top')
ax.set_xlabel('Categories')
ax.set_ylabel('Values')

# Display the plot in Streamlit
st.pyplot(plt)


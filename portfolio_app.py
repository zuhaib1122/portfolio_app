from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

import streamlit as  st
import pandas as pd
st.set_page_config(page_title = 'PORTFOLIO',page_icon= "🚀",  layout = 'wide', initial_sidebar_state = 'auto')
# sidebar for navigation and contact
with st.sidebar:
    st.title('Navigation')
    selection = st.radio('Goto', ['About me', 'Projects', 'Education', 'Contact'])
if selection == 'About me':
    col1, col2 = st.columns([1,3], gap='large')
    with col1:
        st.image('MY_PIC.jpeg', width=200)
    with col2:
        st.title('Hafiz Zuhaib Idrees')
        st.subheader('Mathematician & Python Developer | Specializing in Data Science, Streamlit Apps, & HVAC Solutions')
    st.header("About me")

    st.markdown(
    """
    ### **Welcome to my professional space**  
    I am a data scientist, Python developer, and mathematician based in Lahore, Pakistan, specializing in transforming raw, complex operational datasets into actionable insights. My work sits at the intersection of advanced mathematical logic, software engineering, and modern data analytics.
    My journey includes extensive experience in technical data processing, meticulous data entry, and structured analysis. Using Python libraries like Pandas, NumPy, and Scikit-learn, alongside SQL and Excel, I excel at cleaning messy, unstructured inputs, building analytical pipelines, and developing interactive web dashboards with Streamlit. While my foundational background includes hands-on exposure to industrial refrigeration systems and hardware prototyping—such as working with microcontrollers and temperature sensors—my primary expertise is dedicated to solving data-driven problems.
    I leverage my unique technical perspective to handle the complete data lifecycle: extracting messy records, performing rigorous exploratory data analysis, and designing clean, structured databases that empower informed decision-making.
    ### **The Power of Mathematics and Code**  
    I hold a Bachelor of Science in Mathematics from the Virtual University of Pakistan, which gave me the analytical foundation to dive deep into Data Science. I specialize in turning raw data into actionable insights using Python libraries (like Pandas, NumPy, and Scikit-learn) and managing databases using Google BigQuery. I love building interactive web applications and dashboards using Streamlit to make complex data accessible and intuitive. 

    ### **Mastering Mathematics and Writing Code Without Sight**  
    As a visually impaired developer and educator, my approach to technology is rooted in deep resilience and precision. Through online teaching and academic work, I routinely write complex mathematical equations and technical documents directly into Microsoft Word using screen readers like NVDA and JAWS. Navigating complex programming syntax, debugging Python scripts, and designing functional web apps entirely through auditory feedback requires immense focus. 

    ### **A Strategic Advantage for Forward-Thinking Businesses**  
    To business leaders and employers looking to strengthen their teams: true capability lives in the mind, logic, and determination of an individual, not in physical sight. Hiring professionals with disabilities is not just an act of inclusion—it is a smart business advantage. Navigating a world built for sighted individuals requires constant adaptation, creative problem-solving, and meticulous attention to detail. Those same traits make engineers and developers with disabilities exceptionally resilient, hyper-focused, and innovative problem-solvers. By opening doors to talent across all abilities, companies unlock fresh perspectives that drive better software, sharper analysis, and stronger business results.

    ### **What's Next?**  
    Whether I am preparing for competitive public service examinations, engineering a new refrigeration controller, or deploying an interactive web tool, my goal remains the same: to solve difficult problems and build systems that make a tangible, lasting difference.
    """
)
elif selection == 'Projects':
    st.header('My Projects')
    st.markdown('Explore a selection of industrial-grade web applications and data analytics tools designed to streamline business operations.')
    # pdf to excel conversion 
    with st.container(border=True):
            col1, col2 = st.columns([2, 3], gap="large")
            with col1:
                st.subheader("PDF to Excel Data Automation & Business Analytics")
                st.caption("Python | Pandas | Excel Automation | Pivot Tables & Visualization")
                st.write(
                    """An automated data engineering solution designed to extract, clean, and structure unstructured multi-page PDF documents into clean, analysis-ready tabular formats."""
                )
            with col2:
                with st.container(border=True):
                    st.info("### ***Key Insight:***")
                    st.info("Turns unformatted text records into structured data models, enabling quick calculations, top-performer identification, and visual business insights.")
                    with open("Nest Aero Sales Data for 2013 & 2014.pdf", "rb") as pdf_file:
                        st.download_button(
                        label="🔗 Click Here to Download & View Raw Pdf File",
                        data=pdf_file,
                        file_name="Nest Aero Sales Data for 2013 & 2014.pdf",
                        mime="application/pdf",
                        )

                        


                    with open("Nest_Aero_Sales_Extracted.xlsx", "rb") as file:
                        st.download_button(
                        label="🔗 Click Here to Download & View Clean File",
                        data=file,
                        file_name="Nest_Aero_Sales_Extracted.xlsx",
                        mime=(
                        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                        ),
                        )
    


        # Project: Pakistan Fuel Pricing & Crisis Analytics
    with st.container(border=True):
        col1, col2 = st.columns([2, 3], gap="large")
        with col1:
            st.subheader("Pakistan Fuel Pricing & Crisis Analytics (2020–2026)")
            st.caption("Python | Pandas | Streamlit | Matplotlib & Seaborn | Correlation Analysis")
            st.write(
                "An exploratory data analysis dashboard tracking fuel pricing dynamics, global Brent crude impact, "
                "and shifting tax ratios across the worldwide economic crisis era (2020–2026). This project analyzes "
                "how pandemic disruptions, global energy shocks, and local fiscal adjustments collided to reshape "
                "consumer fuel costs in Pakistan."
            )
        with col2:
            with st.container(border=True):
                st.info("### ***Key Insight:***")
                st.info("Unpacks multi-year volatility using dual-axis temporal charts and statistical correlation matrices.")
                st.markdown("### [🔗 Click Here to View](https://petrol-price-analysis-85op9jt3ujnbuaxlwjsbz7.streamlit.app)")

    #st.markdown("---")
# Retail analysis
    with st.container(border=True):
            col1, col2 = st.columns([2, 3], gap="large")
            with col1:
                st.subheader("Retail Analytics & Inventory Optimization ")
                st.caption("Python | Pandas | Streamlit | Plotly | CSV Data Processing")
                st.write(
                    """An interactive enterprise command center dashboard designed to track multi-location retail performance, regional revenue distribution, and dynamic inventory stock runways.
This project empowers business operators to monitor key metrics; including Total Revenue, Units Sold, and Stock Runway (Days Remaining); while offering a custom CSV upload feature that allows organizations to instantly plug in and analyze their own operational datasets."""
                )
            with col2:
                with st.container(border=True):
                    st.info("### **Key Insight:**")
                    st.info("Streamlines inventory forecasting by combining real-time metric calculations with dynamic, visual charts that highlight regional sales variations and low-stock thresholds.")
                    st.markdown("### [🔗 Click Here to View](https://9uzcygkro6tdcxpfrgzphp.streamlit.app/)")
    
            #st.markdown("---")
    # customer billing app
    with st.container(border=True):
            col1, col2 = st.columns([2, 3], gap="large")
            with col1:
                st.subheader("Customer Billing & Cloud Portal")
                st.caption("Python | Streamlit | Gspread | Google Sheets API | Cloud Secrets Management")
                st.write(
"""A modern, cloud-connected web application built to eliminate traditional paper-based record-keeping in commercial operations. This tool captures customer billing data securely from any location, instantly syncs entries to a cloud database, and automatically generates an on-screen receipt ready for immediate sharing via screenshot."""
                    )
                    
            with col2:
                with st.container(border=True):
                    st.info("### ***Key Insight:***")
                    st.info("Replaces manual ledger friction with automated cloud logging and instant receipt generation, eliminating paperwork errors.")
                    st.markdown("### [🔗 Click here to view live app](https://kjfihhcrfx4washxaspvky.streamlit.app/)")
                    st.markdown("### [🔗 Click here to inspect entries inside google sheete](https://docs.google.com/spreadsheets/d/1eosnb5f2t95W2HEnhrpVXT6UEi4MFxgRISZmNX1xq3Y/edit?gid=0#gid=0)")
                        
    
            #st.markdown("---")

            # Excel Sales Analysis 
    with st.container(border=True):
        col1, col2 = st.columns([2, 3], gap="large")
        with col1:
            st.subheader("Excel Business Intelligence & Multi-Sheet Pivot Reporting")
            st.caption("Advanced Excel | PivotTables | Conditional Formatting | Data Modeling")
            st.write(
                """An interactive analysis tool built across multiple structured worksheets, featuring dynamic PivotTables and custom conditional formatting to easily track sales performance, yearly trends, and customer patterns."""
            )
        with col2:
            with st.container(border=True):
                st.info("### ***Key Insight:***")
                st.info("Transforms raw transaction logs into executive-ready business insights using dynamic date grouping, interactive filters, and custom conditional formatting.")
                with open("sales_analysis.xlsx", "rb") as file:
                    st.download_button(
                    label="🔗 Click Here to Download & View File",
                    data=file,
                    file_name="sales_analysis.xlsx",
                    mime=(
                    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    ),
                    )
    #st.markdown("---")

    #Data cleaning
    with st.container(border=True):
            col1, col2 = st.columns([2, 3], gap="large")
            with col1:
                st.subheader("Hotel Booking Data Cleansing & Structured Pipeline")
                st.caption("Python | Pandas | Microsoft Excel | Data Transformation")
                st.write(
                    """An automated data-cleaning workflow designed to ingest, parse, and structure messy, multi-delimited records into clean tabular formats. This project addresses unformatted raw data entries containing mixed separators (~ and |) and inconsistent currency markers (₹, Rs, INR), transforming them into an analysis-ready dataset."""
                )
            with col2:
                with st.container(border=True):
                    st.info("### ***Key Insight:***")
                    st.info("Converts raw, unstructured booking logs into clean, standardized database-ready records, significantly reducing manual data-entry overhead and improving reporting accuracy.")
                    with open("Proj.xlsx", "rb") as file:
                        st.download_button(
                        label="🔗 Click Here to Download & View File",
                        data=file,
                        file_name="Proj.xlsx",
                        mime=(
                        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                        ),
                        )
            #st.markdown("---")

elif selection == 'Education':
    st.header('Educational Details')
# bachlors
    with st.container(border=True):
        st.subheader('Graduation')
        col1,col2 = st.columns([3,2], gap="large")
        with col1:
            st.markdown('### Bachelors of Science in Mathematics (BS-Math)')
            st.caption('Virtual University of Pakistan')
        with col2:
            with st.container(border=True):
                st.markdown(
    "Successfully completed a rigorous 4-year curriculum with comprehensive"
    " training in quantitative analysis.<br>Specialization: Mathematical logic,"
    " numerical methods, and data-driven problem-solving structures.",
    unsafe_allow_html=True,
)
                # diploma
    with st.container(border=True):
            st.subheader('DAE')
            col1,col2 = st.columns([3,2], gap="large")
            with col1:
                st.markdown('### Diploma of Associate Engineering in RAC Technology')
                st.caption('Govt college of technology railway road Lahore')
            with col2:
                with st.container(border=True):
                    st.markdown(
    "Completed a comprehensive 3-year technical diploma in Refrigeration and"
    " Air-Conditioning Technology.<br><b>Achievement:</b> Secured 3rd position"
    " across Punjab (Board of Technical Education) and received an award"
    " medal for academic excellence.",
    unsafe_allow_html=True,
)
# Intermediate
    with st.container(border=True):
        st.subheader('Intermediate')
        st.markdown('### FSc Pre-engineering')
        st.caption('Govt Islamia college railway road  Lahore')
    with st.container(border=True):
        st.subheader('Matriculation')    
        st.caption('Islah e Moashrah high school Lahore')
# additional certifications
    st.markdown(
    """
<div style="border: 1px solid rgba(250, 250, 250, 0.2); padding: 20px; border-radius: 10px; margin-bottom: 20px;">
    <h3>Certifications & Professional Development</h3>
    <h4>Kaggle Data Science & Machine Learning Certifications</h4>
    <p>Completed intensive hands-on micro-courses covering Python, Pandas, Machine Learning, and Data Visualization, strengthening practical data analytics capabilities.</p>
</div>
""",
    unsafe_allow_html=True,
)
elif selection == 'Contact':
    st.header('Contact Details')
    
st.markdown("## Get In Touch")
st.write(
    "Open to full-time roles, freelance projects, and collaborations in"
    " **Data Analysis, Machine Learning, and Industrial Automation Systems**."
)

col1, col2 = st.columns(2)

with col1:
  with st.container(border=True):
    st.subheader("Direct Contact Info")
    st.write("📍 **Location:** Lahore, Pakistan")
    st.write(
        "📧 **Email:**"
        " [zuhaib12325@gmail.com](mailto:zuhaib12325@gmail.com)"
    )
    st.write("📱 **Phone/WhatsApp:** Available upon request")
    st.write("[🔗 **Linkedin: ** ](https://www.linkedin.com/feed/)")

    with col2:
        with st.container(border=True):
            st.subheader("Send a Message")
            contact_name = st.text_input("Your Name")
            contact_email = st.text_input("Your Email")
            contact_message = st.text_area(
            "Type your query"
            )

        if st.button("Send Message"):
            if contact_name and contact_message:
                try:
                    sender_email = "zuhaib12325@gmail.com"
                    # Replace with your 16-character Google App Password
                    sender_password = "wpqb upyq qntr odtu"
                    receiver_email = "zuhaib12325@gmail.com"

                    msg = MIMEMultipart()
                    msg["From"] = sender_email
                    msg["To"] = receiver_email
                    msg["Subject"] = f"Portfolio Inquiry from {contact_name}"

                    body = (
                        f"You have a new message from your portfolio app:\n\n"
                        f"Name: {contact_name}\n"
                        f"Email: {contact_email}\n\n"
                        f"Message:\n{contact_message}"
                    )
                    msg.attach(MIMEText(body, "plain"))

                    server = smtplib.SMTP("smtp.gmail.com", 587)
                    server.starttls()
                    server.login(sender_email, sender_password)
                    server.sendmail(sender_email, receiver_email, msg.as_string())
                    server.quit()

                    st.success(
                        "Thank you! Your message has been sent directly to my email."
                    )

                except Exception as e:
                    st.error(
                        f"Failed to send message due to a technical error. Details: {e}"
                    )
            else:
                st.error("Please fill in your name and message before sending.")

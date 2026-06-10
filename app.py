import streamlit as st
import pandas as pd
import datetime
import altair as alt
# ==========================================
# 1. INITIALIZE DEMO DATA 
# ==========================================

# 1. STUDENTS TABLE
if "students" not in st.session_state:
    st.session_state.students = pd.DataFrame([
        {
            "Student_ID": 1001, "Student_Name": "Mel", "Student_Email": "mel@gmail.com",
            "Cohort": "3", "Skills": "Python, SQL, Tableau, ML", 
            "Interests": "Computer Vision", "Capstone_Status": "Matched"
        },
        {
            "Student_ID": 1002, "Student_Name": "Frank", "Student_Email": "frank@gmail.com",
            "Cohort": "4", "Skills": "Python, Computer Vision, ML", 
            "Interests": "Computer Vision", "Capstone_Status": "Unmatched"
        },
        {
            "Student_ID": 1003, "Student_Name": "Sam", "Student_Email": "sam@gmail.com",
            "Cohort": "4", "Skills": "Java, Python, Web development, Mobile App Dev", 
            "Interests": "App Dev", "Capstone_Status": "Unmatched"
        },
        {
            "Student_ID": 1004, "Student_Name": "Vic", "Student_Email": "vic@gmail.com",
            "Cohort": "4", "Skills": "Python, Robotics, Web development", 
            "Interests": "Sensor tech", "Capstone_Status": "Unmatched"
        }
    ])

# 2. MENTORS TABLE
if "mentors" not in st.session_state:
    st.session_state.mentors = pd.DataFrame([
        {
            "Mentor_ID": 5001, "Mentor_Name": "Robbie", 
            "Mentor_Email": "robbie@abc.com", "Company": "ABC Health Lab", 
            "Department_or_Role": "Principal Researcher"
        },
        {
            "Mentor_ID": 5002, "Mentor_Name": "Jack", 
            "Mentor_Email": "jack@abc.com", "Company": "ABC Enterprise", 
            "Department_or_Role": "Engineering Lead"
        },
        {
            "Mentor_ID": 5003, "Mentor_Name": "Jesse", 
            "Mentor_Email": "jesse@abc.com", "Company": "ABC Innovation Lab", 
            "Department_or_Role": "Director"
        },
    ])

# 3. PROJECTS TABLE
if "projects" not in st.session_state:
    st.session_state.projects = pd.DataFrame([
        {
            "Project_ID": 101, 
            "Mentor_ID": 5001,
            "Mentor_Name": "Robbie", 
            "Mentor_Email": "robbie@abc.com",
            "Company": "ABC Health Lab", 
            "Title": "ML classification of Chest X-Rays", 
            "Description": "Using ML to classify chest X-ray images",
            "Project_Type": "Listed", 
            "Required_Skills": "Python, ML", 
            "Location": "Hybrid",
            "Duration": "12 months",
            "Stipend": "$1000",
            "Available_Places": 2, 
            "Approval_Status": "Approved",
            "Open_Full_Status": "Open",
            "Admin_Comments": "NA"
        },
        {
            "Project_ID": 102, 
            "Mentor_ID": 5001,
            "Mentor_Name": "Robbie", 
            "Mentor_Email": "robbie@abc.com",
            "Company": "ABC Health Lab", 
            "Title": "X-ray to Text", 
            "Description": "Image parsing to translate x-ray images to text description",
            "Project_Type": "Listed", 
            "Required_Skills": "Python, ML", 
            "Location": "Hybrid",
            "Duration": "12 months",
            "Stipend": "$1000",
            "Available_Places": 1, 
            "Approval_Status": "Approved",
            "Open_Full_Status": "Open",
            "Admin_Comments": "NA"
        },
        {
            "Project_ID": 103,
            "Mentor_ID": 5002,
            "Mentor_Name": "Jack", 
            "Mentor_Email": "jack@abc.com",
            "Company": "ABC Enterprise", 
            "Title": "Mobile App for Food Waste Reduction", 
            "Description": "Building a cross-platform application",
            "Project_Type": "Listed", 
            "Required_Skills": "Web development, Mobile App Dev", 
            "Location": "Hybrid",
            "Duration": "12 months",
            "Stipend": "$800",
            "Available_Places": 2, 
            "Approval_Status": "Approved",
            "Open_Full_Status": "Open",
            "Admin_Comments": "NA"
        },
        {
            "Project_ID": 104, 
            "Mentor_ID": 5003,
            "Mentor_Name": "Jesse", 
            "Mentor_Email": "jesse@abc.com",
            "Company": "ABC Innovation Lab", 
            "Title": "Health tracker wearable", 
            "Description": "Creating a wearable device to track health metrics",
            "Project_Type": "Listed", 
            "Required_Skills": "Sensor tech, Embedded Systems", 
            "Location": "On-site",
            "Duration": "6 months",
            "Stipend": "$300",
            "Available_Places": 1, 
            "Approval_Status": "Approved",
            "Open_Full_Status": "Open",
            "Admin_Comments": "NA"
        },
    ])

# 4. APPLICATIONS TABLE
if "applications" not in st.session_state:
    st.session_state.applications = pd.DataFrame([
        {
            "Application_ID": 201, "Student_ID": 1004, "Project_ID": 101, 
            "Date_Applied": "2026-06-01", "Application_Status": "Unsuccessful", 
            "Mentor_Comments": "Lacks intermediate ML experience", 
            "Reason_Unsuccessful": "Lack of required skills", "Date_Updated": "2026-06-03"
        },
        {
            "Application_ID": 202, "Student_ID": 1004, "Project_ID": 102, 
            "Date_Applied": "2026-06-01", "Application_Status": "Unsuccessful", 
            "Mentor_Comments": "Lacks intermediate ML experience", 
            "Reason_Unsuccessful": "Lack of required skills", "Date_Updated": "2026-06-03"
        },
        {
            "Application_ID": 203, "Student_ID": 1001, "Project_ID": 101, 
            "Date_Applied": "2026-06-04", "Application_Status": "Successful", 
            "Mentor_Comments": "Ok", 
            "Reason_Unsuccessful": "NA", "Date_Updated": "2026-06-04"
        },
        {
            "Application_ID": 204, "Student_ID": 1002, "Project_ID": 102, 
            "Date_Applied": "2026-06-04", "Application_Status": "Submitted", 
            "Mentor_Comments": "NA", 
            "Reason_Unsuccessful": "NA", "Date_Updated": "2026-06-05"
        }    
    ])

# 5. PAIRINGS TABLE
if "final_pairings" not in st.session_state:
    st.session_state.final_pairings = pd.DataFrame([
        {       
            "Pairing_ID": 1,
            "Student_ID": 1001,
            "Mentor_ID": 5001,
            "Project_ID": 101,
            "Project_Type": "Listed",
            "Title": "ML classification of Chest X-Rays",
            "Start_Date": "2026-07-01",
            "Duration": "12 months",
            "Stipend": "$1000",
            "Approval_Status": "Approved",
        }
    ])

if "draft_letters" not in st.session_state:
    st.session_state.draft_letters = {}

# ==========================================
# 2. APP NAVIGATION & LAYOUT
# ==========================================
st.set_page_config(page_title="Capstone Matcher", layout="wide")
st.title("Capstone Project & Pairing Management System")

# Role Switcher in Sidebar
role = st.sidebar.radio("Switch User Role View:", ["Student View", "Mentor View", "Admin View"])

# ==========================================
# 3. STUDENT VIEW
# ==========================================
if role == "Student View":
    st.header("Student Portal")
    
    v_email = st.text_input("Enter your registered email address to access the portal:", value="vic@gmail.com")
    is_verified = False
    verified_student_id = None

    if v_email:
        df_s = pd.DataFrame(st.session_state.students)
        match_indices = df_s[df_s["Student_Email"].str.lower() == v_email.strip().lower()].index
        
        if not match_indices.empty:
            idx = match_indices[0]
            student_data = st.session_state.students.iloc[idx]
            is_verified = True # set flags to true
            verified_student_id = student_data['Student_ID']
            st.success(f"Verified: Welcome back, {student_data['Student_Name']}!")
            
            # Display Read-Only Profile Metadata in a grid
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Student ID", f"#{student_data['Student_ID']}")
            c2.metric("Cohort", student_data['Cohort'])
            c3.metric("Email Address", student_data['Student_Email'])
            
            # Dynamic color tag status metric logic
            status = student_data['Capstone_Status']
            c4.metric("Capstone Status", status)

            # Profile Information Editor Layout
            st.markdown("#### Update Your Core Credentials")
            with st.form(key="profile_editor_form"):
                new_skills = st.text_input("Technical Skills", value=student_data['Skills'])
                new_interests = st.text_input("Domain Interests", value=student_data['Interests'])
                
                save_profile = st.form_submit_button("Save Profile Changes")
                
                if save_profile:
                    # Update back into memory tracking state vectors
                    st.session_state.students.at[idx, "Skills"] = new_skills
                    st.session_state.students.at[idx, "Interests"] = new_interests
                    st.toast("⚡ Profile parameters updated inside database instance!")
                    st.rerun()
                    
        else:
            st.error("Profile not found. Please review or correct the text input.")
    st.markdown("---")

    # conditional tabs display
    if is_verified:
        tab1, tab2, tab3 = st.tabs(["Projects", "My Applications", "Submit Self-Sourced Project"])
        
        with tab1:
            st.subheader("Available Approved Projects")
            df_p = pd.DataFrame(st.session_state.projects)
            df_a = pd.DataFrame(st.session_state.applications)

            # Only display projects that are Approved and Open
            available_projects = df_p[(df_p["Approval_Status"] == "Approved") & (df_p["Open_Full_Status"] == "Open") & (df_p["Project_Type"] == "Listed")]
            if not available_projects.empty:
                for _, row in available_projects.iterrows():
                    with st.container():
                        st.markdown(f"#### {row['Title']}")
                        st.markdown(f"**Mentor:** {row['Mentor_Name']}, {row['Company']}. Contact: {row['Mentor_Email']}")
                        st.markdown(f"**Location:** {row['Location']} | **Duration:** {row['Duration']} | **Available Places:** {row['Available_Places']}")
                        st.write(row['Description'])
                        st.caption(f"**Required Skills:** {row['Required_Skills']}")
                        
                        with st.form(key=f"app_form_{row['Project_ID']}"):
                            submit_app = st.form_submit_button("Apply")
                            
                            if submit_app:
                                if not df_a.empty:
                                    is_duplicate = not df_a[(df_a["Student_ID"] == verified_student_id) & (df_a["Project_ID"] == row['Project_ID'])].empty
                                else:
                                    is_duplicate = False
                                    
                                if is_duplicate:
                                    st.warning("⚠️ You have already submitted an application for this specific project.")
                                else:
                                    new_app = {
                                        "Application_ID": int(len(st.session_state.applications) + 201),
                                        "Student_ID": int(verified_student_id),
                                        "Project_ID": int(row['Project_ID']),
                                        "Date_Applied": str(datetime.date.today()),
                                        "Application_Status": "Submitted",
                                        "Mentor_Comments": "NA",
                                        "Reason_Unsuccessful": "NA",
                                        "Date_Updated": str(datetime.date.today())
                                    }
                                    st.session_state.applications = pd.concat([st.session_state.applications, pd.DataFrame([new_app])], ignore_index=True)
                                    st.success(f"Application submitted successfully for '{row['Title']}'!")
                                    # st.rerun()
                        st.markdown("---")
            else:
                st.info("No open capstone projects are available right now.")

        with tab2:
            st.subheader("Track Your Applications")
            df_a = pd.DataFrame(st.session_state.applications)
            df_p = pd.DataFrame(st.session_state.projects)
            
            # Filter applications specifically for verified student
            my_apps = df_a[df_a["Student_ID"] == verified_student_id]
            
            if not my_apps.empty:
                # Merge to inherit project descriptions and titles
                my_apps_display = my_apps.merge(df_p, on="Project_ID", how="left")
                
                display_summary = my_apps_display[[
                    "Application_ID", "Title", "Date_Applied", 
                    "Application_Status", "Mentor_Comments", "Reason_Unsuccessful", "Date_Updated"
                ]].rename(columns={
                    "Title": "Project Title",
                    "Date_Applied": "Date Applied",
                    "Application_Status": "Status",
                    "Mentor_Comments": "Mentor Feedback",
                    "Reason_Unsuccessful": "Rejection Reason",
                    "Date_Updated": "Last Updated"
                })
                
                st.dataframe(display_summary, width='stretch', hide_index=True)
            else:
                st.info("You have not submitted any project applications yet.")


        with tab3:
            st.subheader("Submit a Self-Sourced Project")
            df_p = pd.DataFrame(st.session_state.projects)
            
            with st.form(key="student_self_sourced_form_v2"):
                s_title = st.text_input("Project Title")
                s_desc = st.text_area("Project Description")
                s_mentor = st.text_input("Proposed Industry Mentor Name")
                s_email = st.text_input("Proposed Industry Mentor Email")
                s_comp = st.text_input("Proposed Company / Organization")
                s_skills = st.text_input("Required Skills (comma-separated, e.g., Python, SQL)")
                s_loc = st.selectbox("Location Type", ["On-site", "Remote", "Hybrid"])
                s_dur = st.selectbox("Project Duration", ["3 Months", "6 Months", "12 Months"])
                s_stipend = st.selectbox("Stipend Offered", ["$0 (Unpaid)", "$300", "$500", "$800", "$1000+"])

                submit_self = st.form_submit_button("Submit for Review")
                
                if submit_self:
                    if s_title and s_desc and s_mentor and s_email:
                        is_duplicate_proposal = not df_p[
                            (df_p["Title"].str.lower() == s_title.strip().lower()) & 
                            (df_p["Mentor_ID"].isin(st.session_state.mentors[st.session_state.mentors["Mentor_Email"].str.lower() == s_email.strip().lower()]["Mentor_ID"]))
                        ].empty
                        
                        if is_duplicate_proposal:
                            st.warning("This project setup/title has already been cataloged by our system.")
                        else:
                            new_m_id = int(len(st.session_state.mentors) + 5001)
                            new_p_id = int(len(st.session_state.projects) + 101)
                            
                            new_mentor = {
                                "Mentor_ID": new_m_id, "Mentor_Name": s_mentor, "Mentor_Email": s_email,
                                "Company": s_comp, "Department_or_Role": "External Advisor"
                            }
                            
                            new_project = {
                                "Project_ID": new_p_id, "Title": s_title, "Mentor_ID": new_m_id, "Mentor_Name": s_mentor, 
                                "Mentor_Email": s_email, "Company": s_comp, "Description": s_desc, "Required_Skills": s_skills, 
                                "Location": s_loc, "Duration": s_dur, "Available_Places": 1, "Stipend": s_stipend, 
                                "Approval_Status": "Pending", "Open_Full_Status": "Open", "Project_Type": "Self-Sourced"
                            }
                            
                            new_app = {
                                "Application_ID": int(len(st.session_state.applications) + 201),
                                "Student_ID": int(verified_student_id),
                                "Project_ID": new_p_id,
                                "Date_Applied": str(datetime.date.today()),
                                "Application_Status": "Pending Self-Sourced",
                                "Mentor_Comments": "NA",
                                "Reason_Unsuccessful": "NA",
                                "Date_Updated": str(datetime.date.today())
                            }
                            
                            st.session_state.mentors = pd.concat([st.session_state.mentors, pd.DataFrame([new_mentor])], ignore_index=True)
                            st.session_state.projects = pd.concat([st.session_state.projects, pd.DataFrame([new_project])], ignore_index=True)
                            st.session_state.applications = pd.concat([st.session_state.applications, pd.DataFrame([new_app])], ignore_index=True)
                            
                            st.success("Custom proposal submitted")
                            # st.rerun()
                    else:
                        st.error("Please provide a title, description, and valid contact criteria for your mentor.")
# ==========================================
# 4. MENTOR VIEW
# ==========================================
elif role == "Mentor View":
    st.header("Mentor Portal")

    m_email = st.text_input("Enter your registered mentor email address to unlock your dashboard:", key="mentor_portal_email", value="robbie@abc.com")
    is_mentor_verified = False
    verified_mentor_id = None
    
    if m_email:
        df_m = pd.DataFrame(st.session_state.mentors)
        print("\ndf_m\n")
        print(df_m)
        match_mentors = df_m[df_m["Mentor_Email"].str.lower() == m_email.strip().lower()].index
        
        if not match_mentors.empty:
            m_idx = match_mentors[0]
            mentor_data = st.session_state.mentors.iloc[m_idx]
            
            # Set validation flags
            is_mentor_verified = True
            verified_mentor_id = mentor_data['Mentor_ID']
            
            st.success(f"Verified: Welcome back, {mentor_data['Mentor_Name']}!")
            
            # Display Core Entity Attributes
            m_col1, m_col2, m_col3 = st.columns(3)
            m_col1.metric("Mentor ID", f"#{mentor_data['Mentor_ID']}")
            m_col2.metric("Company", mentor_data['Company'])
            m_col3.metric("Role / Department", mentor_data['Department_or_Role'])
        else:
            st.error("Mentor profile identity match not found. Please verify your address.")

    st.markdown("---")

    # ==========================================
    # 2. CONDITIONAL MENTOR ACTION TABS
    # ==========================================
    if is_mentor_verified:
        m_tab1, m_tab2 = st.tabs(["Submit New Project", "Review Student Applications"])
        
        # -------------------------------------------------------------
        # TAB 1: SUBMIT NEW CAPSTONE PROJECT
        # -------------------------------------------------------------
        with m_tab1:
            st.write("### Offer a New Capstone Project")
            st.caption("Submit a standard project description to be added to the student marketplace upon admin vetting.")
            
            with st.form(key="mentor_project_submission_form"):
                m_title = st.text_input("Project Title")
                m_desc = st.text_area("Project Description")
                m_skills = st.text_input("Required Skills (comma-separated, e.g., Python, SQL)")
                m_loc = st.selectbox("Location Type", ["On-site", "Remote", "Hybrid"])
                m_dur = st.selectbox("Project Duration", ["3 Months", "6 Months", "12 Months"])
                m_stipend = st.selectbox("Stipend Offered", ["$0 (Unpaid)", "$300", "$500", "$800", "$1000+"])
                m_places = st.number_input("Available Places / Vacancies", min_value=1, max_value=5, value=1, step=1)
                
                submit_proj = st.form_submit_button("Submit Project to Admin for Review")
                
                if submit_proj:

                    if m_title and m_desc and m_skills:
                        new_p_id = int(len(st.session_state.projects) + 101)
                        
                        new_project_entry = {
                            "Project_ID": new_p_id,
                            "Mentor_ID": int(verified_mentor_id),
                            "Mentor_Name": mentor_data['Mentor_Name'], 
                            "Mentor_Email": m_email, 
                            "Company": mentor_data['Company'], 
                            "Title": m_title,
                            "Description": m_desc,
                            "Project_Type": "Listed",
                            "Required_Skills": m_skills,
                            "Location": m_loc,
                            "Duration": m_dur,
                            "Stipend": m_stipend,
                            "Available_Places": int(m_places),
                            "Approval_Status": "Pending",
                            "Open_Full_Status": "Open",
                        }

                        st.session_state.projects = pd.concat([st.session_state.projects, pd.DataFrame([new_project_entry])], ignore_index=True)
                        st.success(f"'{m_title}' submitted! Waiting for Admin vetting review.")
                        # st.rerun()
                    else:
                        st.error("Please provide a project title, descriptions, and required skills.")

            # -------------------------------------------------------------
            # TAB 2: REVIEW STUDENT APPLICATIONS
            # -------------------------------------------------------------
            with m_tab2:
                st.write("### All Student Applications")
                st.caption("Below is a master list of all students who have applied to your capstone projects.")
                
                df_p = pd.DataFrame(st.session_state.projects)
                df_a = pd.DataFrame(st.session_state.applications)
                df_s = pd.DataFrame(st.session_state.students)
                
                # 1. Isolate projects belonging solely to this specific verified mentor
                my_projects = df_p[df_p["Mentor_ID"] == verified_mentor_id]
                my_project_ids = my_projects["Project_ID"].tolist()
                
                # 2. Filter applications routed to those projects
                mentor_apps = df_a[df_a["Project_ID"].isin(my_project_ids)]
                
                if not mentor_apps.empty:
                    # Join datasets to pull human-readable names and statuses
                    m_review_df = mentor_apps.merge(df_p, on="Project_ID", how="left")
                    m_review_df = m_review_df.merge(df_s, on="Student_ID", how="left")
                    
                    # Format and rename columns to match the required directory view
                    directory_df = m_review_df[[
                        "Application_ID", "Title", "Student_Name", 
                        "Approval_Status", "Application_Status", "Date_Applied"
                    ]].rename(columns={
                        "Title": "Project Title",
                        "Student_Name": "Applicant Student",
                        "Approval_Status": "Project Admin Status",
                        "Application_Status": "Application Match Status",
                        "Date_Applied": "Date Applied"
                    })
                    
                    # Render the master table overview
                    st.dataframe(directory_df, use_container_width=True, hide_index=True)
                    
                    # 3. Action / Processing Section placed immediately below the grid
                    st.markdown("---")
                    st.write("#### Pending Student Applications")
                    
                    pending_reviews = m_review_df[m_review_df["Application_Status"] == "Submitted"]
                    
                    if not pending_reviews.empty:
                        # Build list of options for the selector dropdown
                        app_options = {
                            f"App #{row['Application_ID']} | {row['Student_Name']} — {row['Title']}": row['Application_ID'] 
                            for _, row in pending_reviews.iterrows()
                        }
                        
                        selected_app_label = st.selectbox("Select an application to evaluate:", list(app_options.keys()))
                        selected_app_id = app_options[selected_app_label]
                        
                        # Fetch details for the explicitly selected row
                        target_row = pending_reviews[pending_reviews["Application_ID"] == selected_app_id].iloc[0]
                        
                        # Render applicant info box
                        with st.container():
                            st.info(f"**Reviewing Details for {target_row['Student_Name']}**\n\n"
                                    f"**Interests:** {target_row['Interests']}\n\n"
                                    f"**Skills:** {target_row['Skills']}")
                            
                            st.write("### AI-Generated Candidate Fit Summary")
                            st.caption("Automated analysis comparing the applicant's profile text against your project requirements.")

                            # mock summary response
                            mock_summary = """
                            **Fit Analysis:**
                            The applicant demonstrates a strong academic background in data structures and Python programming, aligning well with your technical stack. 

                            **Key Alignment Markers:**
                            * **Student Statement:** Highly interested in automated pipeline architectures and machine learning model tracking.
                            * **Project Match:** Strong crossover with your project's focus on structured data parsing. The student's elective coursework in predictive modeling directly supports your milestone goals.
                            * **Recommendation:** **High Fit.** The student possesses the foundational coding skills required, though they may need initial mentorship regarding domain-specific corporate workflows.
                            """

                            if "ai_summary_generated" not in st.session_state:
                                st.session_state.ai_summary_generated = False

                            if st.button("✨ Run AI Profile Review", type="primary"):
                                st.session_state.ai_summary_generated = True

                            # Conditional rendering block to display the results
                            if st.session_state.ai_summary_generated:
                                st.markdown(mock_summary)
                            else:
                                st.warning("Generate an automated synthesis of this candidate's statements.")
                                
                        with st.form(key=f"mentor_table_eval_form_{selected_app_id}"):
                            m_action = st.radio("Review Decision", ["Approve & Match", "Decline Candidate"])
                            m_feedback = st.text_input("Mentor Comments / Feedback")
                            m_fail_reason = st.text_input("Reason Unsuccessful (If declining)", value="NA")
                            
                            if st.form_submit_button("Submit Evaluation"):

                                if m_action == "Approve & Match":
                                    st.session_state.applications.loc[st.session_state.applications["Application_ID"] == selected_app_id, "Application_Status"] = "Successful"
                                    target_student_id = int(target_row['Student_ID'])
                                    st.session_state.students.loc[
                                        st.session_state.students["Student_ID"].astype(int) == target_student_id, "Capstone_Status"
                                    ] = "Matched"

                                else:
                                    st.session_state.applications.loc[st.session_state.applications["Application_ID"] == selected_app_id, "Application_Status"] = "Unsuccessful"
                                    st.session_state.applications.loc[st.session_state.applications["Application_ID"] == selected_app_id, "Reason_Unsuccessful"] = m_fail_reason
                                
                                # Update comments and timestamp metadata parameters
                                st.session_state.applications.loc[st.session_state.applications["Application_ID"] == selected_app_id, "Mentor_Comments"] = m_feedback
                                st.session_state.applications.loc[st.session_state.applications["Application_ID"] == selected_app_id, "Date_Updated"] = str(datetime.date.today())
                                
                                st.success("Student evaluation submitted successfully!")
                                st.rerun()
                    else:
                        st.info("All incoming applications for your projects have been successfully reviewed and processed.")
                else:
                    st.info("No student applications have been received for your listed projects yet.")

            st.markdown("---")
            st.write("### Your Projects")
            st.caption("This table tracks projects you have proposed")

            # 1. Pull ALL projects for this mentor, removing the "Pending" status restriction
            my_all_projects = df_p[df_p["Mentor_ID"] == verified_mentor_id]

            if not my_all_projects.empty:
                # 2. Select display columns, making sure to include Approval_Status
                project_history_display = my_all_projects[[
                    "Project_ID", "Title", "Location", "Duration", "Approval_Status"
                ]].rename(columns={
                    "Project_ID": "Project ID",
                    "Title": "Project Title",
                    "Available_Places": "Vacancies",
                    "Approval_Status": "Admin Status"
                })
                
                # 3. Render the complete history tracking table
                st.dataframe(project_history_display, use_container_width=True, hide_index=True)
            else:
                st.info("You have not submitted any project proposals yet.")
    else:
        st.info("Please complete your mentor registration email authentication checks.")

# ==========================================
# 5. ADMIN VIEW & DASHBOARD
# ==========================================
else:
    st.header("Administrative Control & Metrics")
    
    df_p = pd.DataFrame(st.session_state.projects)
    df_a = pd.DataFrame(st.session_state.applications)
    
    # ------------------------------------------
    # DASHBOARD METRICS 
    # ------------------------------------------
    st.subheader("Live Analytics Dashboard")

    if df_p.empty:
        st.warning("No projects available right now.")

    else:
        col1, col2, col3, col4 = st.columns(4)

        total_approved = len(df_p[df_p["Approval_Status"] == "Approved"])
        total_apps = len(df_a)
        if df_a.empty:
            confirmed_pairings = 0
        else: confirmed_pairings = len(df_a[df_a["Application_Status"] == "Successful"])
    
        # Simple Unmatched Student logic (Total unique applicants minus successful ones)
        unique_students = df_a["Student_ID"].nunique() if not df_a.empty else 0
        successful_students = df_a[df_a["Application_Status"] == "Successful"]["Student_ID"].nunique() if not df_a.empty else 0
        unmatched_students = max(0, unique_students - successful_students)
        
        col1.metric("Approved Projects", total_approved)
        col2.metric("Total Applications", total_apps)
        col3.metric("Confirmed Pairings", confirmed_pairings)
        col4.metric("Unmatched Students", unmatched_students)
        
        # Graphs and alerts
        st.markdown("---")
        st.subheader("All Project Submissions")
        st.dataframe(
            df_p[["Project_ID", "Title", "Project_Type", "Mentor_Name", "Approval_Status"]],
            width='stretch'
        )

        st.subheader("Applications Per Listed Project")
        if not df_a.empty:
            app_counts = df_a.merge(df_p, on="Project_ID")
            app_counts = app_counts[app_counts["Project_Type"] == "Listed"].groupby("Title").size().reset_index(name="Count")            
            
            
            chart_height = max(150, len(app_counts) * 50)

            chart = (
                alt.Chart(app_counts)
                .mark_bar(size=25)  
                .encode(
                    x=alt.X("Count:Q", title="Number of Applications", axis=alt.Axis(format="d")),
                    y=alt.Y(
                        "Title:N", 
                        title=None,
                        sort="-x",
                        axis=alt.Axis(
                            labelLimit=300,   
                            labelFontSize=15, 
                            titleFontSize=14  
                        )
                    )
                )
                .properties(
                    height=chart_height
                )
            )

            st.altair_chart(chart, use_container_width=True)

        else:
            st.caption("No application data available yet.")

        st.markdown("---")
        st.subheader("Pairing Status Overview")

        col_left, col_right = st.columns(2)
        df_s = pd.DataFrame(st.session_state.students)
        df_m = pd.DataFrame(st.session_state.mentors)
        df_pairings = pd.DataFrame(st.session_state.final_pairings)

        print('pairings\n')
        print(df_pairings)

        
        with col_left:
            st.markdown("**Successful Matches**")
            
            if not df_pairings.empty:
                # Merge the pairings record with student and mentor names 
                matched_display = df_pairings.merge(df_s, on="Student_ID", how="left")
                matched_display = matched_display.merge(df_m, on="Mentor_ID", how="left")
                
                visible_columns = [
                    "Pairing_ID", 
                    "Student_ID", 
                    "Student_Name",
                    "Mentor_ID", 
                    "Mentor_Name", 
                    "Title", 
                    "Project_Type",
                ]
                
                # Format headers for screen readability 
                renamed_display = matched_display[visible_columns].rename(columns={
                    "Pairing_ID": "Pairing ID",
                    "Student_ID": "Student ID",
                    "Student_Name": "Student Name",
                    "Mentor_ID": "Mentor ID",
                    "Mentor_Name": "Mentor Name",
                    "Title": "Project Title",
                    "Project_Type": "Project Type",
                })
                
                st.dataframe(renamed_display, use_container_width=True, hide_index=True)
            else:
                st.info("No successful final pairings recorded in the database model yet.")

        with col_right:
            unmatched_records = []
            alert_triggered = False

            if not st.session_state.students.empty:
                df_s_lookup = pd.DataFrame(st.session_state.students)
                df_a_lookup = pd.DataFrame(st.session_state.applications) if not df_a.empty else pd.DataFrame()
                
                # 1. Map out rejection metrics if applications data exists
                if not df_a_lookup.empty:
                    fail_counts = df_a_lookup[df_a_lookup["Application_Status"] == "Unsuccessful"].groupby("Student_ID").size().to_dict()
                else:
                    fail_counts = {}

                # 2. Loop through all students to evaluate status and build the summary directory
                for _, s_row in df_s_lookup.iterrows():
                    stud_id = int(s_row['Student_ID'])
                    current_status = str(s_row['Capstone_Status']).strip()
                    
                    # Target anyone who is NOT matched
                    if current_status.lower() != "matched":
                        fails_count = fail_counts.get(stud_id, 0)
                        
                        # Store entry details for the table
                        unmatched_records.append({
                            "Student ID": stud_id,
                            "Student Name": s_row['Student_Name'],
                            "Cohort": s_row['Cohort'],
                            "Current Status": current_status,
                            "Total Rejections": fails_count
                        })
                        
                        # 3. Alert if they hit the critical threshold (fails >= 2)
                        if fails_count >= 2:
                            alert_triggered = True
                            st.error(
                                f"**Support Needed:** Student **{s_row['Student_Name']}** (#{stud_id}) "
                                f"has suffered {fails_count} rejections and is still **{current_status}**. "
                                f"Immediate intervention recommended."
                            )
                
                if not alert_triggered:
                    st.success("No critical student exceptions detected.")
                
                # 4. Render the Unmatched Table View
                st.write("### Unmatched Students")
                st.caption("All registered candidates who have not yet secured a finalized project allocation match.")
                
                if unmatched_records:
                    df_unmatched = pd.DataFrame(unmatched_records)
                    # Sort by rejections descending so students struggling the most surface to the top
                    df_unmatched = df_unmatched.sort_values(by="Total Rejections", ascending=False)
                    
                    st.dataframe(df_unmatched, use_container_width=True, hide_index=True)
                else:
                    st.info("Every student in the database has been successfully matched to a project.")
            else:
                st.info("No student records available to evaluate.")
                
        st.markdown("---")
        st.write("### Common Reasons for Unsuccessful Applications")

        # Mock data
        mock_rejection_reasons = pd.DataFrame([
            {"Stated Reason / Feedback Category": "Resubmit with more details (Scope unverified)", "Count": 3},
            {"Stated Reason / Feedback Category": "Project timeline does not meet capstone duration criteria", "Count": 2},
            {"Stated Reason / Feedback Category": "Missing explicit corporate mentor sign-off credentials", "Count": 1},
            {"Stated Reason / Feedback Category": "Technical scope too narrow", "Count": 1},
            {"Stated Reason / Feedback Category": "Duplicate project proposal submission detected", "Count": 1}
        ])

        st.dataframe(mock_rejection_reasons, use_container_width=True, hide_index=True)


        # ------------------------------------------
        # ADMIN WORKFLOW TABS
        # ------------------------------------------
        st.markdown("---")
        tab1, tab2 = st.tabs(["Project Approvals Pipeline", "Pairing Approvals & Letter Generation"])
        
        with tab1:
            st.subheader("Review Submitted Projects (Listed & Self-Sourced)")
            pending_projects = df_p[df_p["Approval_Status"] == "Pending"]
            
            if pending_projects.empty:
                st.info("No projects currently awaiting vetting.")
            else:
                st.dataframe(pending_projects[["Project_ID", "Title", "Mentor_Name", "Mentor_Email", "Project_Type", "Approval_Status"]])

                proj_to_vet = st.selectbox("Choose a Project ID to take action on:", pending_projects["Project_ID"].tolist())

                action = st.radio("Action:", ["Approve", "Reject"])

                rejection_reason = ""
                if action == "Reject":
                    rejection_reason = st.text_input("Enter Rejection Reason / Clarification notes:", value="Resubmit with more details")

                if st.button("Process Project"):
                    chosen_status = "Approved" if action == "Approve" else "Rejected"
                    
                    project_row = st.session_state.projects[st.session_state.projects["Project_ID"] == proj_to_vet]
                    
                    if not project_row.empty:
                        p_type = project_row.iloc[0].get("Project_Type", "Listed")
                        project_title = project_row.iloc[0].get("Title", "Untitled Project")
                        project_duration = project_row.iloc[0].get("Duration", "6 Months")
                        project_stipend = project_row.iloc[0].get("Stipend", "$0 (Unpaid)")
                        target_mentor_id = project_row.iloc[0].get("Mentor_ID")

                        # --- PATH 1: APPROVAL ---
                        if chosen_status == "Approved":
                            st.session_state.projects.loc[st.session_state.projects["Project_ID"] == proj_to_vet, "Approval_Status"] = "Approved"
                            
                            if p_type == "Self-Sourced":
                                matching_apps = st.session_state.applications[st.session_state.applications["Project_ID"] == proj_to_vet]
                                
                                if not matching_apps.empty:
                                    target_app_id = matching_apps.iloc[0]["Application_ID"]
                                    target_student_id = matching_apps.iloc[0]["Student_ID"]
                                    
                                    # Update status logs
                                    st.session_state.applications.loc[st.session_state.applications["Application_ID"] == target_app_id, "Application_Status"] = "Successful"
                                    st.session_state.students.loc[st.session_state.students["Student_ID"] == target_student_id, "Capstone_Status"] = "Matched"
                                    
                                    # Append transaction directly to the Final Pairings data model
                                    new_pairing_id = int(len(st.session_state.final_pairings) + 1)
                                    new_pairing_record = {
                                        "Pairing_ID": new_pairing_id,
                                        "Student_ID": int(target_student_id),
                                        "Mentor_ID": int(target_mentor_id),
                                        "Project_ID": int(proj_to_vet),
                                        "Project_Type": "Self-Sourced",
                                        "Title": str(project_title),
                                        "Start_Date": str(datetime.date.today()),
                                        "Duration": str(project_duration),
                                        "Stipend": project_stipend,
                                        "Approval_Status": "Approved",
                                    }
                                    st.session_state.final_pairings = pd.concat([st.session_state.final_pairings, pd.DataFrame([new_pairing_record])], ignore_index=True)
                                    st.toast("System matched the self-sourced records successfully!")

                        # --- PATH 2: REJECTION / CLARIFICATION ---
                        elif chosen_status == "Rejected":
                            st.session_state.projects.loc[st.session_state.projects["Project_ID"] == proj_to_vet, "Approval_Status"] = "Rejected"
                            
                            if "Admin_Comments" in st.session_state.projects.columns:
                                st.session_state.projects.loc[st.session_state.projects["Project_ID"] == proj_to_vet, "Admin_Comments"] = rejection_reason
                            
                            if p_type == "Self-Sourced":
                                matching_apps = st.session_state.applications[st.session_state.applications["Project_ID"] == proj_to_vet]
                                
                                if not matching_apps.empty:
                                    target_app_id = matching_apps.iloc[0]["Application_ID"]
                                    
                                    st.session_state.applications.loc[st.session_state.applications["Application_ID"] == target_app_id, "Application_Status"] = "Rejected"
                                    st.session_state.applications.loc[st.session_state.applications["Application_ID"] == target_app_id, "Reason_Unsuccessful"] = rejection_reason

                        st.success(f"Project #{proj_to_vet} processed as {chosen_status}!")
                        st.rerun()
        with tab2:
            st.subheader("Finalize Matches & Generate Draft Letters")
            
            if df_a.empty:
                st.info("No applications to review for pairing finalization.")
                st.stop()
            successful_apps = df_a[df_a["Application_Status"] == "Successful"]
            
            if successful_apps.empty:
                st.info("No pairings are currently marked 'Successful' by mentors awaiting admin finalization.")
            else:

                merged_final = successful_apps.merge(df_p, on="Project_ID", how="left").merge(df_s, on="Student_ID", how="left")
                st.dataframe(merged_final[["Application_ID", "Student_Name", "Title", "Company", "Mentor_Name"]])
                
                target_app = st.selectbox("Select Application ID to generate letter:", successful_apps["Application_ID"].tolist())
                
                if st.button("Run Rule-Check & Generate Confirmation Letter"):
                    row_info = merged_final[merged_final["Application_ID"] == target_app].iloc[0]
                    
                    if pd.isna(row_info['Mentor_Name']) or row_info['Mentor_Name'] == "":
                        st.error("Exception Detected: Missing Mentor Contact details. Automation aborted.")
                    else:
                        target_student_id = int(row_info["Student_ID"])
                        target_mentor_id = int(row_info["Mentor_ID"])
                        target_project_id = int(row_info["Project_ID"])
                        project_type = str(row_info.get("Project_Type", "Listed"))
                        project_duration = str(row_info.get("Duration", "6 Months"))
                        project_stipend = str(row_info.get("Stipend", "$0 (Unpaid)"))

                        df_pairings = st.session_state.final_pairings
                        is_already_paired = False
                        
                        if not df_pairings.empty:
                            is_already_paired = not df_pairings[
                                (df_pairings["Student_ID"] == target_student_id) & 
                                (df_pairings["Project_ID"] == target_project_id)
                            ].empty
                        
                        if not is_already_paired:
                            new_pairing_id = int(len(df_pairings) + 1)
                            new_pairing_record = {
                                "Pairing_ID": new_pairing_id,
                                "Student_ID": target_student_id,
                                "Mentor_ID": target_mentor_id,
                                "Project_ID": target_project_id,
                                "Project_Type": project_type,
                                "Title": str(row_info["Title"]),
                                "Start_Date": str(datetime.date.today()),
                                "Duration": project_duration,
                                "Stipend": project_stipend,
                                "Approval_Status": "Approved",
                            }
                            st.session_state.final_pairings = pd.concat([st.session_state.final_pairings, pd.DataFrame([new_pairing_record])], ignore_index=True)
                        else:
                            draft_letter = f"""
DEAR {row_info['Student_Name'].upper()},

We are pleased to inform you that your application for the Capstone Project 
"{row_info['Title']}" has been formally approved. 

You will be operating under the supervision of {row_info['Mentor_Name']} at {row_info['Company']}.
Please coordinate directly with your mentor at {row_info["Mentor_Email"]} regarding onboarding timelines.

Regards,
Capstone Administration Offices"""
                            st.session_state.draft_letters[target_app] = draft_letter
                            st.success("Draft Letter generated successfully!")
                
                if target_app in st.session_state.draft_letters:
                    st.text_area("Generated Draft (Ready to copy/send):", value=st.session_state.draft_letters[target_app], height=200)
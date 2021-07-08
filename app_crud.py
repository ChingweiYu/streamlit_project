import streamlit as st
import pandas as pd 
from db_fxns import * 
import streamlit.components.v1 as stc



# Data Viz Pkgs
import plotly.express as px 




def main():
    col1, col2 = st.beta_columns(2)
    col1.subheader('學生訊息管理系統')
    create_table()
    result = view_all_data()

    clean_df = pd.DataFrame(result,columns=["School_number_text","PersonName","Gender","Birth_date","College","Grades"])
    st.dataframe(clean_df)
    col2.subheader('新增或改動的資料')

    School_number_text = col2.text_input("School_number")
    PersonName = col2.text_input("Name")
    Gender = col2.text_input("Gender")
    Birth_date = col2.text_input("Birth_date")
    College = col2.text_input("College")
    Grades = col2.text_input("Grades")

    if col1.button("Add"):
        if (len(School_number_text)==0):
            pass
        else:
            add_data(School_number_text,PersonName,Gender,Birth_date,College,Grades)
            # st.success("Added")



    if col1.button("Update"):
        edit_task_data(School_number_text,PersonName,Gender,Birth_date,College,Grades)
		# st.success("Updated")


    if col1.button("Delete"):
        delete_data(School_number_text)
		# st.success("Deleted")

    # col1.button("Re-run")
    col1.button("Re-load")



if __name__ == '__main__':
	main()

# -*- coding: utf-8 -*-
"""Untitled11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hOmNM-CCXCDx5j2nlDGzkgWJrr262MfW
"""

!pip install streamlit

pip install easyocr

!pip install pyngrok

pip install streamlit-option-menu

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import streamlit as st
# from PIL import Image
# import pandas as pd
# import numpy as np
# import easyocr
# import re
# import os
# from streamlit_option_menu import option_menu
# from IPython.display import display
# import sqlite3
# 
# reader=easyocr.Reader(['en'])
# st.markdown("<h1 style='text-align: center; color: red;'>BizCardX: Extracting Business Card Data with OCR</h1>", unsafe_allow_html=True)
# 
# conn = sqlite3.connect('bizcard1db(2).db')
# cursor = conn.cursor()
# query="""Create table if not exists card_data(id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     company_name TEXT,
#                     card_holder TEXT,
#                     designation TEXT,
#                     mob_no varchar(20),
#                     email text,
#                     website text,
#                     area text,
#                     city text,
#                     state text,
#                     pincode varchar(10),
#                     image longblob)"""
# cursor.execute(query)
# selected = option_menu(None, ["Home","Upload & Extract","Modify"],default_index=0,
#                        orientation="horizontal")
# if selected=='Home':
#     st.write("Bizcard Extraction is a Python application built with Streamlit, EasyOCR, regex function, and MySQL database. It allows users to extract information from business cards and store it in a MySQL database for further analysis. The main purpose of Bizcard is to automate the process of extracting key details from business card images, such as the name, designation, company, contact information, and other relevant data. By leveraging the power of OCR (Optical Character Recognition) provided by EasyOCR, Bizcard is able to extract text from the images.")
# elif selected=='Upload & Extract':
#     st.write("Welcome")
# 
#     uploaded_card = st.file_uploader("Choose a file", type=["png", "jpg", "jpeg"])
# 
#     if uploaded_card is not None:
#         def save_card(uploaded_card):
#             uploaded_cards_dir = os.path.join(os.getcwd(), "uploaded_cards")
#             with open(os.path.join(uploaded_cards_dir, uploaded_card.name), "wb") as f:
#                 f.write(uploaded_card.getbuffer())
# 
# 
#         save_card(uploaded_card)
#         #view uploaded card
#         image_width=400
#         st.image(uploaded_card,width=image_width, caption="Uploaded Card Image")
#     if st.button(":blue[Extract card data & upload to DB]"):
#         def image_to_text(image_path):
#             img = Image.open(image_path)
#             img_np = np.array(img)
#             text = reader.readtext(img_np, detail=0, paragraph=False)
#             return text
# 
# 
#         def image_to_text2(image_path):
#             img = Image.open(image_path)
#             img_np = np.array(img)
#             text2 = reader.readtext(img_np, detail=0, paragraph=True)
#             return text2
#         data = image_to_text(uploaded_card)
#         data2 = image_to_text2(uploaded_card)
# 
#         def img_to_binary(uploaded_file):
#           if uploaded_file is not None:
#             # Read the contents of the uploaded file as bytes
#             file_contents = uploaded_file.read()
#             return file_contents
#           else:
#             return None
# 
#         extracted_data={'company_name':[],'card_holder':[],'designation':[],'mob_no':[],'email':[],'website':[],'area':[],'city':[],'state':[],'pincode':[],'image':img_to_binary(uploaded_card)}
#         def get_data(data,data2):
#           for index,i in enumerate(data):
#             #To get website
#             if i.lower()=='www' or i.lower()=='www ':
#               k=data.index(i)
#               extracted_data['website'].append(i+' '+data[k+1])
#             elif 'www' in i.lower() or 'www ' in i.lower() or 'www.' in i.lower() and '.com' in i:
#               extracted_data['website'].append(i)
# 
#             #To get email
#             if '@' in i:
#               extracted_data['email'].append(i)
# 
#             #To get cardholder name
#             if index==0:
#               extracted_data['card_holder'].append(i)
# 
#             #To get designation
#             if index==1:
#               extracted_data['designation'].append(i)
# 
#             #To get mobile no.
#             if '-' in i:
#               extracted_data['mob_no'].append(i)
#         #To get company name
#           for index,i in enumerate(data2):
#             if index==(len(data2)-1):
#               k=i
#               if '.com' not in k:
#                 extracted_data['company_name'].append(k)
#               else:
#                 u=len(data2)-2
#                 extracted_data['company_name'].append(data2[u])
#             #To get the area
#             if 'st' in i.lower():
#               match1=re.findall(r'\b\d+\s+\w+\s+st\b',i)
#               if match1:
#                 extracted_data['area'].append(*match1)
#               match2=re.findall(r'\b\d+\s+\w+\s+St\b',i)
#               if match2:
#                 extracted_data['area'].append(*match2)
#               match3=re.findall(r'\b\d+\s+\w+\s+St.\b',i)
#               if match3:
#                 extracted_data['area'].append(*match3)
# 
#             #To get pincode,state,city
#             if 'st' in i.lower():
#               m=i.split(',')
#               mstripped=[s.strip() for s in m]
#               pin=mstripped[-1].split(' ')[-1]
#               state=mstripped[-1].split(' ')[0]
#               city=mstripped[1]
#               extracted_data['pincode'].append(pin)
#               extracted_data['state'].append(state)
#               extracted_data['city'].append(city)
# 
#           return extracted_data['company_name'],extracted_data['card_holder'],extracted_data['designation'],extracted_data['mob_no'],extracted_data['email'],extracted_data['website'],extracted_data['area'],extracted_data['city'],extracted_data['state'],extracted_data['pincode']
#         get_data(data,data2)
#   #FUNCTION TO CREATE DATAFRAME
#         def create_df(data):
#           df = pd.DataFrame(data)
#           return df
#         data_df=create_df(extracted_data)
#         st.write(data_df)
#         data_df.to_sql('card_data', conn, index=False, if_exists='append')
#         conn.commit()
#         st.success("##Data Extracted !!& Uploaded to database successfully!")
# elif selected=='Modify':
#   cursor.execute("SELECT card_holder FROM card_data")
#   result = cursor.fetchall()
#   st.write(result)
#   business_cards = {}
#   for row in result:
#     business_cards[row[0]] = row[0]
#   options = ["None"] + list(business_cards.keys())
#   selected_card = st.selectbox("**Select a card**", options)
#   if selected_card == "None":
#     st.write("No card selected.")
#   else:
#     st.markdown("Edit the data below")
#     query="select company_name,card_holder,designation,mob_no,email,website,area,city,state,pincode from card_data WHERE card_holder=%s"
#     cursor.execute(query, (selected_card,))
# 
#     result = cursor.fetchone()
# 
#     # DISPLAYING ALL THE INFORMATIONS
#     company_name = st.text_input("Company_Name", result[0])
#     card_holder = st.text_input("Card_Holder", result[1])
#     designation = st.text_input("Designation", result[2])
#     mobile_number = st.text_input("Mobile_Number", result[3])
#     email = st.text_input("Email", result[4])
#     website = st.text_input("Website", result[5])
#     area = st.text_input("Area", result[6])
#     city = st.text_input("City", result[7])
#     state = st.text_input("State", result[8])
#     pin_code = st.text_input("Pin_Code", result[9])
# 
# 
#     if st.button(":blue[Commit changes to DB]"):
        # Update the information for the selected business card in the database
        cursor.execute("""UPDATE card_data SET company_name=?,card_holder=?,designation=?,mob_no=?,email=?,website=?,area=?,city=?,state=?,pincode=?
                        WHERE card_holder=?""", (company_name, card_holder, designation, mobile_number, email, website, area, city, state, pin_code,
        selected_card))
        conn.commit()
        st.success("Information updated in database successfully.")

        st.write("The updated data:")
        cursor.execute("""select company_name,card_holder,designation,mob_no,email,website,area,city,state,pincode from card_data where card_holder=?""",(card_holder,))
        result=pd.DataFrame(cursor.fetchall(),columns=['company_name','card_holder','designation','mob_no','email','website','area','city','state','pincode'])

        st.write(result)
  if select=='DELETE':
    cursor.execute("SELECT card_holder FROM card_data")
    result = cursor.fetchall()
    business_cards = {}
    for row in result:
      business_cards[row[0]] = row[0]
    options = ["None"] + list(business_cards.keys())
    selected_card = st.selectbox("**Select a card**", options)
    if selected_card == "None":
      st.write("No card selected.")
    else:
      st.write(f"### You have selected :green[**{selected_card}'s**] card to delete")
      st.write("#### Proceed to delete this card?")
      if st.button("Yes Delete Business Card"):
        cursor.execute(f"DELETE FROM card_data WHERE card_holder='{selected_card}'")
        conn.commit()
        st.success("Business card information deleted")
      elif st.button("Cancel"):
        st.write("Deletion cancelled")


#

!npm install localtunnel

!streamlit run /content/app.py &>/content/logs.txt & npx localtunnel --port 8501 & curl ipv4.icanhazip.com

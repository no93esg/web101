import streamlit as st
import datetime

# Title
st.title("Hello :yellow[Suthasinee!!]")
st.header("Let's Goooooooo")

# Initialize session state
if 'step' not in st.session_state:
    st.session_state['step'] = 0

# START Button
if st.session_state.step == 0:
    st.markdown("สวัสดีครับเบบี๋! เบ๊บมีคำถามพิเศษให้เล่น ลองตอบดูนะ 😊")
    if st.button("เริ่มกันเลย!!!"):
        st.session_state.step = 1   

# Q1
if st.session_state.step == 1 :
    today = datetime.date.today()
    #next_year = today.year + 1
    start_date = today
    end_date = today
    #jan_1 = datetime.date(next_year, 1, 1)
    #dec_31 = datetime.date(next_year, 12, 31)
    ans1 = st.date_input(
        "เลือกวันที่ไปเที่ยว",
        (start_date,end_date),
        format="DD.MM.YYYY" 
    )
    
    if st.button("ส่งคำตอบข้อ 1"):
        if str(ans1[0]) == "2026-06-12" and str(ans1[1]) == "2026-06-14" :
            st.write(f"วันที่ไปเที่ยวคือ {ans1[0]} ถึง {ans1[1]}")
            st.success("ถูกต้องจ้า! ไปกันต่อออออออออ 🤗")
            st.session_state.step = 2
        else :
            st.error("ผิดจ้าไอ้สัส")

# Q2
if st.session_state.step == 2 :
    ans2 = st.selectbox(
    "ไปเที่ยวที่ไหน ??",
    ("ญี่ปุ่น", "เกาหลี", "ภูทับเบิก"),
    index=None,
    placeholder="เลือกสถานที่....",
    )

    if st.button("ส่งคำตอบข้อ 2") :
        if ans2 == "ภูทับเบิก" :
            st.success("เก่งมากจ้า! ไปกันต่อออออออออ 🤗")
            st.session_state.step = 3
        else :
            st.error("ไม่มีตังจ้าาา")

# Q3
if st.session_state.step == 3 :

    check1 = st.checkbox("เพชร1")
    check2 = st.checkbox("เพชร2")
    check3 = st.checkbox("เพชร3")
    if check1 and check2 and check3 :
        st.success("เพชรเป็นคนหาที่พักและที่เที่ยววว เย้ๆ")
        st.session_state.step = 4

# Final
if st.session_state.step == 4 :
    if st.button("ไปเที่ยวกันนนนนน"):
        st.balloons()
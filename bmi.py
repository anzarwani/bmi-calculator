import streamlit as st

st.title("BMI Calculator")

st.subheader("WEIGHT")
weight = st.number_input("Enter Your Weight")
weight_unit = st.selectbox("Unit", ('kg', 'pound'))

st.subheader('HEIGHT')
height = st.number_input("Enter Your height")
height_unit = st.selectbox("Unit", ('feet', 'meter'))

if height_unit == 'feet':
    inch = st.number_input("Inches")

st.write(' ')

def bmi(weight, weight_unit, height, height_unit):
    if height_unit == 'feet':
        height = height * 12 + inch
        height = height/39.37
    if weight_unit == 'pound':
        weight = weight * 0.45359237
    bmi_value = weight/(height * height)
    st.metric("Your BMI Is : ", "{:.2f}".format(bmi_value))

    if bmi_value < 18.5:
        st.warning("BELOW NORMAL WEIGHT")

    elif bmi_value >= 18.5 and bmi_value < 25:
        st.success("NORMAL WEIGHT")
    elif bmi_value >= 25 and bmi_value < 30:
        st.warning("OVERWIEGHT")
    elif bmi_value >= 30 and bmi_value < 35:
        st.warning("OBESITY CLASS 1")
    elif bmi_value >= 35 and bmi_value < 40:
        st.warning("OBESITY CLASS 2")
    else:
        st.warning("OBESITY CLASS 3")

col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')
with col2:
    cal = st.button(label = "Calculate My BMI")
with col3:
    st.write(' ')
if cal:
    bmi(weight, weight_unit, height, height_unit)

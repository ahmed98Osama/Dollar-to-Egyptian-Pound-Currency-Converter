import streamlit as st
import requests
from bs4 import BeautifulSoup
import datetime

# st.set_page_config(page_keyboard_intercept=True)
st.set_page_config(
    page_title="Dollar to Pound", page_icon="🤑", initial_sidebar_state="collapsed"
)


def update_price(conversion_type, amount):
    # Get the page content
    page = requests.get("https://www.currency.me.uk/convert/usd/egp")
    html = BeautifulSoup(page.content, "html.parser")

    # Get the answer element from the page
    answer_element = html.select_one("input[id='answer']")
    answer_value = float(answer_element["value"])

    round_amount = "{:,}".format(round(amount, 2))

    # Convert the amount based on the conversion type
    if conversion_type == "(usd_to_egp ) United States Dollar to Egyptian Pound":
        converted_amount = amount * answer_value
        round_converted_amount = "{:,}".format(round(converted_amount, 2))

        round_answer_value = "{:,}".format(round(answer_value, 2))
        st.write(
            f"<span style='color: green'>{1.00} USD</span> is equal to <span style='color: orange'>{round_answer_value} EGP</span>",
            unsafe_allow_html=True,
        )
        st.write(
            f"<h2 style='color: green'>{round_amount} USD</h2> is equal to <h2 style='color: orange'>{round_converted_amount} EGP</h2>",
            unsafe_allow_html=True,
        )
    elif conversion_type == "(egp_to_usd) Egyptian Pound to United States Dollar":
        converted_amount = amount / answer_value
        round_converted_amount = "{:,}".format(round(converted_amount, 2))

        round_answer_value = "{:,}".format(round(1 / answer_value, 2))
        st.write(
            f"<span style='color: orange'>{1.00} EGP</span> is equal to <span style='color: green'>{round_answer_value} USD</span>",
            unsafe_allow_html=True,
        )
        st.write(
            f"<h2 style='color: orange'>{round_amount} EGP</h2> is equal to <h2 style='color: green'>{round_converted_amount} USD</h2>",
            unsafe_allow_html=True,
        )
    else:
        # Invalid conversion type
        st.write("Invalid conversion type")


# Write the header text
st.write(
    "<h1> <span style='color: green'> USD</span> to <span style='color:orange'>EGP</span> Currency Converter </h1>",
    unsafe_allow_html=True,
)

# Get the current date and time in Egypt
now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=2)))
day = now.strftime("%A")
st.write(
    f"<h5>Current Date and Time in Egypt (GMT+2): {day}, {now.strftime('%Y-%m-%d %H:%M:%S')}</h5>",
    unsafe_allow_html=True,
)


# Get the conversion type and amount from the user
conversion_type = st.selectbox(
    "Select the conversion type",
    [
        "(usd_to_egp ) United States Dollar to Egyptian Pound",
        "(egp_to_usd) Egyptian Pound to United States Dollar",
    ],
    key="conversion_type",
)
amount = st.number_input(
    "Enter the amount you want to convert", key="amount", step=0.1, min_value=0.0
)

# If the user clicks the convert button, show a spinner and convert the amount
if st.button("Convert"):
    with st.spinner("Converting..."):
        update_price(conversion_type, amount)

# Write the source information and credits
st.write(
    "<h6>This currency converter uses data from <a href='https://www.currency.me.uk/convert/usd/egp' target='_blank'>currency.me.uk</a>.</h6>",
    unsafe_allow_html=True,
)
st.write(
    "<h6>Created by  <a href='https://github.com/ahmed98Osama' style='color: skyblue' target='_blank'>Ahmed Osama</a>, inspierd by <a href='https://www.linkedin.com/in/abdelrahmanmagdy2011/' style='color: red' target='_blank'>Abdelrahman Magdy</a>,  and assisted by <span style='color: #1b8266'>ChatGPT</span>.</h6>",
    unsafe_allow_html=True,
)



show_more = False

if st.button(' بلاش تدوس '):
    show_more = True
    if st.button(' خليك فاكر اني قولتلك بلاش '):
    show_more2 = True
    
if show_more2:
    show_more = False 
    show_more2 = False
    st.write(
    "<h5> <span style='color: gold'> موقع ملهوش لزمة و ممكن تعملها من جوجل بس الفراغ يعمل اكتر من كدا </span>  </h5>",
    unsafe_allow_html=True,
)



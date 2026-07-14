import streamlit as st
import requests

# -------------------------
# Google Apps Script URL
# -------------------------
URL = "https://script.google.com/macros/s/AKfycbwr7bXY4Gep2hWkJg8cSuPXoLRC4Y_MOCNrJlvfvwbK__PM5A6SonnPbcuWZ2kIDfG5/exec"

# -------------------------
# Website Configuration
# -------------------------
st.set_page_config(
    page_title="Feedback Desk",
    page_icon="📢",
    layout="centered"
)

# -------------------------
# Background Image + Styling
# -------------------------
st.markdown("""
<style>
.stApp {
    background-image: url("https://plus.unsplash.com/premium_photo-1682309504951-43bae484e04d?q=80&w=1934&auto=format&fit=crop&ixlib=rb-4.1.0");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

.stTextInput, .stTextArea, .stSelectbox {
    background-color: rgba(255,255,255,0.9) !important;
    color: black !important;
    font-weight: bold;
    border-radius: 8px;
    padding: 10px;
}

div.stButton > button:first-child {
    background-color: white;
    color: #007bff;
    border: 2px solid #007bff;
    padding: 10px 0px;
    width: 100%;
    border-radius: 8px;
    font-size: 18px;
    font-weight: bold;
    cursor: pointer;
    transition: 0.3s;
}

div.stButton > button:first-child:hover {
    background-color: #007bff;
    color: white;
}

h1, p {
    color: black;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# Website Title
# -------------------------
st.title("📢 Feedback Desk")
st.write("Submit your feedback safely and easily")

# -------------------------
# Feedback Form
# -------------------------
name = st.text_input("Enter your Name")
email = st.text_input("Enter your Email")
category = st.selectbox(
    "Select Category",
    ["Hostel", "Academic", "Transport", "Cafeteria"]
)

year = ""
if category == "Academic":
    year = st.selectbox(
        "Select Your Year",
        ["1st Year", "2nd Year", "3rd Year", "4th Year"]
    )

feedback = st.text_area("Write your feedback here")

# -------------------------
# Submit Button
# -------------------------
if st.button("Submit Feedback"):

    if not name or not email or not feedback:
        st.warning("⚠ Please fill all the fields")

    else:

        data = {
            "name": name,
            "email": email,
            "category": category,
            "year": year,
            "feedback": feedback
        }

        try:
            response = requests.post(URL, json=data)
            st.write(response.status_code)
            st.write(response.text)

            if response.status_code == 200:

                msg = f"✅ Feedback for {category}"

                if category == "Academic":
                    msg += f" ({year})"

                msg += " submitted successfully!"

                st.success(msg)

            else:
                st.error("❌ Failed to save feedback.")

        except Exception as e:
            st.error(f"❌ Error: {e}")
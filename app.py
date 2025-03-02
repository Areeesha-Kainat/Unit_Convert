import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyAirGKFXwyaMurrXF1K8ZAFcUwoUN7LqyE")
model = genai.GenerativeModel('gemini-2.0-flash-exp')

# Page setup
st.set_page_config(page_title="Areesha's Multi-Tool App", page_icon="💬", layout="wide")
# st.title("Areesha's Multi-Tool App")  #ff0000  or #1f69c1
st.markdown("""
    <h1 style='color: #1f69c1; font-size: 48px;'>  
        Areesha's Multi-Tool App
    </h1>
""", unsafe_allow_html=True)


# Session State for navigation
if 'page' not in st.session_state:
    st.session_state.page = "Home Page"

# Back Button
if st.session_state.page != "Home Page":
    if st.button("⬅️ Back"):
        st.session_state.page = "Home Page"
        st.rerun()

# Navigation Logic
if st.session_state.page == "Home Page":
    st.subheader("Welcome! What would you like to do?")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Gemini AI Chatbot"):
            st.session_state.page = "Gemini AI Chatbot"
            st.rerun()
    with col2:
        if st.button("Unit Converter"):
            st.session_state.page = "Unit Converter"
            st.rerun()


    st.markdown("---")

    st.markdown("""
    ##  Welcome to Areesha's Multi-Tool 
    
     Hello, what would you like to do?  
     choose either **Chat with Gemini** or use the **Unit Converter**.

    ---

    ###  What does this app provide?

    Areesha's Multi-Tool App is designed to make your daily tasks easier by offering:
    
    - 💬 **Gemini AI Chatbot** – Have natural conversations with Google's Gemini AI.  
      Ask questions, seek help, brainstorm ideas, or get quick explanations on any topic.
    
    - 🔄 **Unit Converter** – Instantly convert values between different units.  
      Supports conversions for **Length**, **Weight**, and **Temperature** with accurate results.

    ---

    ###  How does it work?

    1. **Choose a Tool:**  
       Use the **sidebar** to select either "Gemini AI Chatbot" or "Unit Converter".
    
    2. **Interact:**  
       - If you pick **Gemini AI**, type your question and chat with AI.  
       - If you pick **Unit Converter**, enter a value and select units to convert.
    
    3. **Get Results Instantly:**  
       See the chatbot's smart replies or your conversion results directly on the page.

    ---

    ### Why use this app?

    - Simple and modern interface  
    - Fast and reliable responses  
    - Combines multiple helpful tools in one place  
    - Accessible anytime, anywhere  

    ---

    ### Bonus Tip:
    Try asking Gemini AI for **life hacks**, **study tips**, or **fun facts**. You might discover something amazing!


    """)
elif st.session_state.page == "Gemini AI Chatbot":
    st.header("💬 Chat with Gemini AI")

    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("You:", key="user_input")

    if st.button("Send"):
        if user_input:
            st.session_state.chat_history.append(("You", user_input))
            response = model.generate_content(user_input)
            bot_reply = response.text
            st.session_state.chat_history.append(("Gemini", bot_reply))

    for sender, message in st.session_state.chat_history:
        st.markdown(f"**{sender}:** {message}")

elif st.session_state.page == "Unit Converter":
    st.header(" Google-Like Unit Converter")

    conversion_types = {
        "Length": {"Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000, "Mile": 0.000621371, "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701},
        "Weight": {"Kilogram": 1, "Gram": 1000, "Milligram": 1_000_000, "Pound": 2.20462, "Ounce": 35.274},
        "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
    }

    category = st.selectbox("Choose a category:", list(conversion_types.keys()))
    value = st.number_input("Enter value:", min_value=0.0, format="%.2f")

    if category != "Temperature":
        from_unit = st.selectbox("From:", conversion_types[category].keys())
        to_unit = st.selectbox("To:", conversion_types[category].keys())
    else:
        from_unit = st.selectbox("From:", conversion_types["Temperature"])
        to_unit = st.selectbox("To:", conversion_types["Temperature"])

    def convert(value, from_unit, to_unit, category):
        if category == "Temperature":
            if from_unit == "Celsius" and to_unit == "Fahrenheit":
                return (value * 9/5) + 32
            elif from_unit == "Celsius" and to_unit == "Kelvin":
                return value + 273.15
            elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                return (value - 32) * 5/9
            elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
                return (value - 32) * 5/9 + 273.15
            elif from_unit == "Kelvin" and to_unit == "Celsius":
                return value - 273.15
            elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
                return (value - 273.15) * 9/5 + 32
            else:
                return value
        else:
            return value * (conversion_types[category][to_unit] / conversion_types[category][from_unit])

    if st.button("Convert 🔄"):
        if from_unit == to_unit:
            st.warning("Select different units to convert!")
        else:
            result = convert(value, from_unit, to_unit, category)
            st.success(f"✅ {value} {from_unit} = {result:.2f} {to_unit}")

# Footer
st.markdown("---")
st.write("Developed by Areesha Kainat")





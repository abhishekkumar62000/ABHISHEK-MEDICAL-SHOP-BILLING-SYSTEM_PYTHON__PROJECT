import streamlit as st # type: ignore
import pandas as pd # type: ignore

# Medicine menu dictionary
medicines_menu = {
    "Paracetamol": 15,
    "Ibuprofen 400mg": 20,
    "Aspirin": 25,
    "Amoxicillin 500mg": 40,
    "Azithromycin 250mg": 70,
    "Cefixime 200mg": 120,
    "Pantoprazole": 55,
    "Omeprazole 20mg": 40,
    "Ranitidine 150mg": 25,
    "Metformin 500mg": 35,
    "Glimepiride 1mg": 45,
    "Atorvastatin 10mg": 90,
    "Rosuvastatin": 110,
    "Telmisartan 40mg": 50,
    "Amlodipine 5mg": 30,
    "Losartan": 40,
    "Hydrochlorothiazide 25mg": 20,
    "Montelukast 10mg": 85,
    "Levocetirizine 5mg": 20,
    "Cetirizine 10mg": 25,
    "Fexofenadine 120mg": 90,
    "Dolo": 30,
    "Crocin Advance 500mg": 25,
    "Combiflam": 35,
    "Domperidone 10mg": 25,
    "Ondansetron 4mg": 50,
    "Dicyclomine 10mg": 30,
    "Meftal Spas": 50,
    "Digene Tablets": 30,
    "ORS Sachet": 20,
    "Electral Powder": 25,
    "Betadine Solution 100ml": 60,
    "Dettol Antiseptic 100ml": 70,
    "Burnol Cream 20g": 45,
    "Soframycin 10g": 35,
    "Calamine Lotion 100ml": 60,
    "Povidone-Iodine Ointment": 50,
    "Multivitamin Tablets": 150,
    "Vitamin C 500mg": 70,
    "Zincovit Tablets": 100,
    "Revital Capsules": 350,
    "B-Complex Tablets": 25,
    "Calcium Tablets": 80,
    "Ivermectin 12mg": 50,
    "Albendazole 400mg": 15,
    "Ciprofloxacin 500mg": 40,
    "Metronidazole 400mg": 35,
    "Clotrimazole Cream 15g": 45,
    "Ketoconazole Shampoo": 150,
}

# Medicine usage instructions
doctor_recommendations = {
    "Paracetamol": "Take 1 tablet after meals to reduce fever and mild pain,  Please follow your doctor's prescription.",
    "Ibuprofen 400mg": "Take 1 tablet after meals to relieve pain and inflammation, Please follow your doctor's prescription.",
    "Aspirin": "Take 1 tablet daily after meals to reduce the risk of blood clots, Please follow your doctor's prescription.",
    "Amoxicillin 500mg": "Take 1 capsule every 8 hours with water for bacterial infections, Please follow your doctor's prescription.",
    "Azithromycin 250mg": "Take 2 tablets on the first day, followed by 1 tablet daily for 4 days, Please follow your doctor's prescription.",
    "Cefixime 200mg": "Take 1 tablet every 12 hours for bacterial infections, Please follow your doctor's prescription.",
    "Pantoprazole": "Take 1 tablet 30 minutes before breakfast to reduce stomach acid, Please follow your doctor's prescription.",
    "Omeprazole 20mg": "Take 1 capsule before meals to manage acidity and heartburn, Please follow your doctor's prescription.",
    "Ranitidine 150mg": "Take 1 tablet after dinner to reduce stomach acid, Please follow your doctor's prescription.",
    "Metformin 500mg": "Take 1 tablet with meals to control blood sugar levels, Please follow your doctor's prescription.",
    "Glimepiride 1mg": "Take 1 tablet before breakfast to control blood sugar levels, Please follow your doctor's prescription.",
    "Atorvastatin 10mg": "Take 1 tablet at bedtime to lower cholesterol levels, Please follow your doctor's prescription.",
    "Rosuvastatin": "Take 1 tablet at bedtime to manage cholesterol levels, Please follow your doctor's prescription.",
    "Telmisartan 40mg": "Take 1 tablet daily to control high blood pressure, Please follow your doctor's prescription.",
    "Amlodipine 5mg": "Take 1 tablet in the morning to manage blood pressure, Please follow your doctor's prescription.",
    "Losartan": "Take 1 tablet daily to control high blood pressure, Please follow your doctor's prescription.",
    "Hydrochlorothiazide 25mg": "Take 1 tablet in the morning to manage water retention and blood pressure.",
    "Montelukast 10mg": "Take 1 tablet daily in the evening to manage allergies and asthma, Please follow your doctor's prescription.",
    "Levocetirizine 5mg": "Take 1 tablet at night to relieve allergy symptoms, Please follow your doctor's prescription.",
    "Cetirizine 10mg": "Take 1 tablet daily to relieve allergy symptoms, Please follow your doctor's prescription.",
    "Fexofenadine 120mg": "Take 1 tablet daily for allergy relief, Please follow your doctor's prescription.",
    "Dolo": "Take 1 tablet after meals for pain and fever relief, Please follow your doctor's prescription.",
    "Crocin Advance 500mg": "Take 1 tablet after meals to reduce fever and mild pain, Please follow your doctor's prescription.",
    "Combiflam": "Take 1 tablet after meals to relieve pain and inflammation, Please follow your doctor's prescription.",
    "Domperidone 10mg": "Take 1 tablet before meals to prevent nausea and vomiting, Please follow your doctor's prescription.",
    "Ondansetron 4mg": "Take 1 tablet before meals to manage nausea and vomiting, Please follow your doctor's prescription.",
    "Dicyclomine 10mg": "Take 1 tablet after meals to relieve abdominal cramps, Please follow your doctor's prescription.",
    "Meftal Spas": "Take 1 tablet after meals to relieve menstrual cramps, Please follow your doctor's prescription.",
    "Digene Tablets": "Chew 1 tablet after meals to relieve acidity and indigestion, Please follow your doctor's prescription.",
    "ORS Sachet": "Dissolve 1 sachet in 1 liter of water and drink to rehydrate, Please follow your doctor's prescription.",
    "Electral Powder": "Dissolve 1 sachet in water to restore electrolytes, Please follow your doctor's prescription.",
    "Betadine Solution 100ml": "Apply directly to wounds to prevent infection, Please follow your doctor's prescription.",
    "Dettol Antiseptic 100ml": "Dilute in water and use for cleaning wounds, Please follow your doctor's prescription.",
    "Burnol Cream 20g": "Apply directly to burns to soothe and prevent infection, Please follow your doctor's prescription.",
    "Soframycin 10g": "Apply a thin layer to infected skin areas, Please follow your doctor's prescription.",
    "Calamine Lotion 100ml": "Apply to skin to relieve itching and irritation, Please follow your doctor's prescription.",
    "Povidone-Iodine Ointment": "Apply directly to wounds to prevent infection, Please follow your doctor's prescription.",
    "Multivitamin Tablets": "Take 1 tablet daily after meals to boost immunity , Please follow your doctor's prescription.",
    "Vitamin C 500mg": "Take 1 tablet daily to boost immunity and skin health, Please follow your doctor's prescription.",
    "Zincovit Tablets": "Take 1 tablet daily after meals as a nutritional supplement, Please follow your doctor's prescription.",
    "Revital Capsules": "Take 1 capsule daily after meals to improve energy and vitality, Please follow your doctor's prescription.",
    "B-Complex Tablets": "Take 1 tablet daily after meals for overall health, Please follow your doctor's prescription.",
    "Calcium Tablets": "Take 1 tablet daily to maintain bone health, Please follow your doctor's prescription.",
    "Ivermectin 12mg": "Take 1 tablet as prescribed for parasitic infections, Please follow your doctor's prescription.",
    "Albendazole 400mg": "Take 1 tablet at bedtime to treat worm infections, Please follow your doctor's prescription.",
    "Ciprofloxacin 500mg": "Take 1 tablet every 12 hours for bacterial infections, Please follow your doctor's prescription.",
    "Metronidazole 400mg": "Take 1 tablet every 8 hours to treat infections, Please follow your doctor's prescription.",
    "Clotrimazole Cream 15g": "Apply to affected areas twice daily for fungal infections, Please follow your doctor's prescription.",
    "Ketoconazole Shampoo": "Use twice weekly to treat dandruff and fungal infections, Please follow your doctor's prescription.",
}


# Streamlit app
st.title("🧑‍⚕️😷Abhishek Medical+ Shop Billing System🏥🩺")
st.markdown("Welcome to **Abhishek Medical Shop**! Enjoy a 10% discount on total purchases over 1000 INR.")

# Multi-Language Support
from deep_translator import GoogleTranslator # type: ignore

# Language selection
language = st.sidebar.selectbox("Choose Language:", ["English", "Hindi"])

# Translate text
if language == "Hindi":
    translated_text = GoogleTranslator(source="auto", target="hi").translate("Welcome to Abhishek Medical Shop")
    st.title(translated_text)
else:
    st.title("Welcome to Abhishek Medical Shop")




# Light/Dark mode toggle
st.markdown("---")
st.sidebar.title("🎨 Theme Selector")

theme = st.sidebar.radio("Choose Theme:", ["Light", "Dark"])
if theme == "Dark":
    st.markdown(
        """
        <style>
        body { background-color: #1e1e1e; color: white; }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.sidebar.markdown("<style>div { color: white; }</style>", unsafe_allow_html=True)
else:
    st.markdown(
        """
        <style>
        body { background-color: white; color: black; }
        </style>
        """,
        unsafe_allow_html=True,
    )

import streamlit as st

# Add new medicine pic to sidebar
medicine_path = "image 4.jpg"  # Ensure this file is in the same directory as your script
try:
    st.sidebar.image(medicine_path)
except FileNotFoundError:
    st.sidebar.warning("image 4 file not found. Please check the file path.")

# Add another new medicine pic to sidebar
medicine_path = "image 1.jpg"  # Ensure this file is in the same directory as your script
try:
    st.sidebar.image(medicine_path)
except FileNotFoundError:
    st.sidebar.warning("image 1 file not found. Please check the file path.")

# Add developer title and pic to sidebar
st.sidebar.title("Developer: Abhishek Kumar")
developer_path = "my.jpg"  # Ensure this file is in the same directory as your script
try:
    st.sidebar.image(developer_path)
except FileNotFoundError:
    st.sidebar.warning("my.jpg file not found. Please check the file path.")



# Customer details
name = st.text_input("Enter your name:")
phone = st.text_input("Enter your phone number:")

if st.button("Add Details"):
    if name and phone:
        st.success(f"Thank you, {name}! Your details are saved.")
        st.markdown(
            """
            ### Welcome to Abhishek Medical+ Shop!
            1. We value your health and well-being.
            2. All medicines are certified and quality checked.
            3. We provide 24/7 customer support.
            4. Get free consultations for your prescriptions.
            5. Discounts available on bulk purchases.
            6. Thank you for choosing us as your trusted pharmacy.
            7. Enjoy a 10% discount on medicines above 1000 INR.
            """
        )
    else:
        st.error("Please enter both your name and phone number.")
        
# Personalized greeting based on user's name
if name:
    st.markdown(f"👋 Hello, **{name}**! Welcome to Abhishek Medical+ Shop! 😊")
    st.markdown("We are delighted to serve you. Please explore our services and products.")
    
# Prescription upload    
uploaded_file = st.file_uploader("Upload your prescription (PDF/Image):")
if uploaded_file:
    st.success("Prescription uploaded successfully!")
    # Optionally display the uploaded file or store it for further processing


# Create a DataFrame from the medicines_menu dictionary
menu_df = pd.DataFrame(list(medicines_menu.items()), columns=["Medicine", "Price (INR)"])


# Category filter for medicines
st.markdown("---")
st.subheader("🗂️ Filter by Category")

categories = {
    "Pain Relief": ["Paracetamol", "Ibuprofen 400mg", "Aspirin", "Dolo", "Crocin Advance 500mg"],
    "Antibiotics": ["Amoxicillin 500mg", "Azithromycin 250mg", "Cefixime 200mg"],
    "Vitamins & Supplements": ["Multivitamin Tablets", "Vitamin C 500mg", "Zincovit Tablets", "Revital Capsules"],
    "Antacids": ["Pantoprazole", "Omeprazole 20mg", "Ranitidine 150mg"],
}

selected_category = st.selectbox("Select a category:", options=list(categories.keys()))
if selected_category:
    st.write(f"Medicines under **{selected_category}**:")
    filtered_medicines = categories[selected_category]
    filtered_df = menu_df[menu_df["Medicine"].isin(filtered_medicines)]
    st.dataframe(filtered_df)




# Add a search bar to filter medicines
st.markdown("---")
st.subheader("🔍 Search Medicines")
search_term = st.text_input("Search for a medicine by name:")
if search_term:
    filtered_menu_df = menu_df[menu_df["Medicine"].str.contains(search_term, case=False, na=False)]
    st.dataframe(filtered_menu_df)
else:
    st.dataframe(menu_df)

# Medicine selection
selected_medicine = st.selectbox("Choose a medicine:", options=menu_df["Medicine"].tolist())
quantity = st.number_input("Enter quantity:", min_value=1, step=1, value=1)


# Cart dictionary
if "cart" not in st.session_state:
    st.session_state.cart = {}

# Add to cart
if st.button("Add to Cart"):
    if selected_medicine in st.session_state.cart:
        st.session_state.cart[selected_medicine] += quantity
    else:
        st.session_state.cart[selected_medicine] = quantity
    st.success(f"Added {quantity} x {selected_medicine} to cart.")
    
    # Calculate subtotal
    cart_items = [
        {"Medicine": med, "Quantity": qty, "Price (INR)": medicines_menu[med], "Total": qty * medicines_menu[med]}
        for med, qty in st.session_state.cart.items()
    ]
    subtotal = sum(item["Total"] for item in cart_items)
    



# Display cart
st.markdown("---")
st.subheader("Cart")
if st.session_state.cart:
    cart_items = [
        {"Medicine": med, "Quantity": qty, "Price (INR)": medicines_menu[med], "Total": qty * medicines_menu[med]}
        for med, qty in st.session_state.cart.items()
    ]
    cart_df = pd.DataFrame(cart_items)
    st.dataframe(cart_df)
    
    
    
    # Calculate subtotal
    subtotal = sum(item["Total"] for item in cart_items)
    
    # Discount progress bar
    st.markdown("---")
    st.subheader("📈 Discount Progress")

    if subtotal < 1000:
        st.progress(subtotal / 1000)
        st.info(f"💰 Spend {1000 - subtotal} INR more to unlock a 10% discount!")
    elif subtotal >= 1000:
        st.success("🎉 Congratulations! You've unlocked a 10% discount!")


    # Calculate totals
    subtotal = sum(item["Total"] for item in cart_items)
    discount = 0.1 * subtotal if subtotal >= 1000 else (0.05 * subtotal if subtotal >= 800 else 0)
    final_total = subtotal - discount

    st.markdown(f"**Subtotal:** {subtotal} INR")
    st.markdown(f"**Discount:** -{discount:.2f} INR")
    st.markdown(f"**Total Amount:** {final_total:.2f} INR")

    

# Loyalty point
if subtotal >= 500:
    loyalty_points = subtotal // 100  # 1 point per 100 INR spent
    st.info(f"🎁 You’ve earned {loyalty_points} loyalty points!")


    # Generate receipt
    if st.button("Generate Receipt"):
        st.markdown("---")
        st.subheader("Receipt")
        st.write(f"**Name:** {name}")
        st.write(f"**Phone Number:** {phone}")
        st.table(cart_df)
        st.write(f"**Subtotal:** {subtotal} INR")
        st.write(f"**Discount:** -{discount:.2f} INR")
        st.write(f"**Total Amount:** {final_total:.2f} INR")

        st.markdown("---")
        st.subheader("Medicine Instructions")
        for med, qty in st.session_state.cart.items():
            instructions = doctor_recommendations.get(med, "Please follow your doctor's prescription.")
            st.markdown(f"- **{med}**: {instructions}")
else:
    st.write("Your cart is empty. Add medicines to proceed.")
    
    
# Automatically Email/SMS billing
import smtplib

def send_email(to_email, subject, body):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("your_email", "your_password")
    message = f"Subject: {subject}\n\n{body}"
    server.sendmail("your_email", to_email, message)
    server.quit()
    st.success(f"Receipt sent to {to_email}")

if st.button("Send Receipt via Email"):
    if name and phone:
        receipt_details = f"Name: {name}\nPhone: {phone}\nTotal: {final_total} INR"
        send_email("customer_email@example.com", "Your Receipt from Abhishek Medical+ Shop", receipt_details)
        
        
# Online Payment Integration
import qrcode # type: ignore

if st.button("Generate Payment QR Code"):
    qr_data = f"Total Amount: {final_total} INR"
    qr_code = qrcode.make(qr_data)
    qr_code.save("payment_qr.png")
    st.image("payment_qr.png", caption="Scan to Pay")
    
    
# Analytics Dashboard
import matplotlib.pyplot as plt # type: ignore

# Sample sales data visualization
sales_data = {"Paracetamol": 50, "Ibuprofen 400mg": 30, "Amoxicillin 500mg": 20}
fig, ax = plt.subplots()
ax.bar(sales_data.keys(), sales_data.values())
st.pyplot(fig)


    
    
# Feedback form
st.markdown("---")
st.subheader("💬 Feedback Form")

feedback = st.text_area("We value your feedback! Please share your thoughts here:")
if st.button("Submit Feedback"):
    if feedback:
        st.success("Thank you for your feedback! 😊")
    else:
        st.error("Please enter your feedback before submitting.")


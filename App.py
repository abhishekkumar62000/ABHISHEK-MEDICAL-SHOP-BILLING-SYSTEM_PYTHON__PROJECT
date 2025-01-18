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

# Streamlit app
st.title("Abhishek Medical+ Shop Billing System")
st.markdown("Welcome to **Abhishek Medical Shop**! Enjoy a 10% discount on total purchases over 1000 INR.")

# Customer details
name = st.text_input("Enter your name:")
phone = st.text_input("Enter your phone number:")

st.markdown("---")
st.subheader("Select Medicines")

# Create a DataFrame for the menu
menu_df = pd.DataFrame(list(medicines_menu.items()), columns=["Medicine", "Price (INR)"])
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

    # Calculate totals
    subtotal = sum(item["Total"] for item in cart_items)
    discount = 0.1 * subtotal if subtotal >= 1000 else (0.05 * subtotal if subtotal >= 800 else 0)
    final_total = subtotal - discount

    st.markdown(f"**Subtotal:** {subtotal} INR")
    st.markdown(f"**Discount:** -{discount:.2f} INR")
    st.markdown(f"**Total Amount:** {final_total:.2f} INR")

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
else:
    st.write("Your cart is empty. Add medicines to proceed.")

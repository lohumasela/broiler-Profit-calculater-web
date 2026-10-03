import streamlit as st

st.set_page_config(page_title="Broiler Profit - Limpopo", page_icon="🐔")

st.title("Broiler Profit Calculator")
st.caption("Built for smallholder farmers in Limpopo - by Lohu")

col1, col2 = st.columns(2)
with col1:
    num_chicks = st.number_input("Number of chicks", 10, 10000, 100)
    chick_price = st.number_input("Price per chick (R)", 5.0, 50.0, 12.5)
    mortality = st.number_input("Expected deaths", 0, 100, 5)
with col2:
    feed_per_bird = st.number_input("Feed per bird (kg)", 1.0, 10.0, 4.5)
    feed_price = st.number_input("Feed price per kg (R)", 5.0, 30.0, 9.2)
    selling_price = st.number_input("Selling price per bird (R)", 30.0, 200.0, 75.0)

if st.button("Calculate Profit ", use_container_width=True):
    surviving = num_chicks - mortality
    total_chick_cost = num_chicks * chick_price
    total_feed_kg = surviving * feed_per_bird
    total_feed_cost = total_feed_kg * feed_price
    total_cost = total_chick_cost + total_feed_cost
    total_income = surviving * selling_price
    profit = total_income - total_cost
    
    st.divider()
    st.metric("Surviving birds", f"{surviving}")
    st.metric("Total Cost", f"R{total_cost:.2f}")
    st.metric("Total Income", f"R{total_income:.2f}")
    st.metric("PROFIT", f"R{profit:.2f}", f"R{profit/surviving:.2f} per bird")
    
    if profit > 0:
        st.success(f"Profit! Break-even is R{total_cost/surviving:.2f} per bird")
    else:
        st.error(" Loss - check feed price or selling price")

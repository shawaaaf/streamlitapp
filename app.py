import streamlit as st

st.set_page_config(page_title="E-Commerce Platform", page_icon="🛒", layout="wide")


# --- Neon Spade Background and Enhanced CSS ---
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #0f2027, #2c5364, #ff00cc, #333399);
        min-height: 100vh;
        overflow-x: hidden;
    }
    .neon-spade {
        position: fixed;
        top: 0; left: 0; width: 100vw; height: 100vh;
        z-index: -1;
        pointer-events: none;
        background: transparent;
    }
    .neon-spade svg {
        position: absolute;
        left: 50%; top: 50%;
        transform: translate(-50%, -50%) scale(2.5);
        filter: drop-shadow(0 0 40px #ff00cc) drop-shadow(0 0 80px #00ffe7) drop-shadow(0 0 120px #333399);
        opacity: 0.5;
        animation: neonPulse 3s infinite alternate;
    }
    @keyframes neonPulse {
        0% { filter: drop-shadow(0 0 40px #ff00cc) drop-shadow(0 0 80px #00ffe7) drop-shadow(0 0 120px #333399); }
        100% { filter: drop-shadow(0 0 80px #ff00cc) drop-shadow(0 0 160px #00ffe7) drop-shadow(0 0 240px #333399); }
    }
    .product-card {
        background: rgba(248,249,250,0.95);
        padding: 1rem;
        border-radius: 16px;
        margin: 0.5rem;
        box-shadow: 0 2px 16px #ff00cc44, 0 2px 8px #33339922;
        text-align: center;
        transition: transform 0.4s cubic-bezier(.68,-0.55,.27,1.55), box-shadow 0.4s;
        animation: fadeInUp 1.2s;
    }
    .product-card:hover {
        transform: scale(1.07) rotate(-2deg);
        box-shadow: 0 8px 32px #00ffe788, 0 8px 32px #ff00cc88;
        animation: neonGlow 0.8s;
    }
    @keyframes fadeInUp {
        0% { opacity: 0; transform: translateY(40px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    @keyframes neonGlow {
        0% { box-shadow: 0 2px 16px #ff00cc44, 0 2px 8px #33339922; }
        100% { box-shadow: 0 8px 32px #00ffe788, 0 8px 32px #ff00cc88; }
    }
    .cart-item {
        background: #ecf0f1;
        padding: 0.5rem;
        border-radius: 8px;
        margin-bottom: 0.5rem;
        animation: fadeInLeft 1s;
    }
    @keyframes fadeInLeft {
        0% { opacity: 0; transform: translateX(-30px); }
        100% { opacity: 1; transform: translateX(0); }
    }
    .checkout-success {
        color: #ff00cc;
        font-weight: bold;
        text-shadow: 0 0 8px #00ffe7, 0 0 16px #333399;
        animation: fadeIn 1.2s;
    }
    </style>
    <div class="neon-spade">
        <svg width="300" height="300" viewBox="0 0 100 100">
            <path d="M50 10 Q80 40 50 70 Q20 40 50 10 Z" fill="none" stroke="#ff00cc" stroke-width="4"/>
            <path d="M50 70 Q55 80 50 90 Q45 80 50 70 Z" fill="#00ffe7" stroke="#333399" stroke-width="2"/>
        </svg>
    </div>
""", unsafe_allow_html=True)

# --- Product Catalog with Component Images ---
products = [
    {
        "id": 1,
        "name": "Wireless Headphones",
        "price": 59.99,
        "image": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=400&q=80",
        "component": "Audio",
        "component_image": "https://cdn-icons-png.flaticon.com/512/727/727245.png"
    },
    {
        "id": 2,
        "name": "Smart Watch",
        "price": 129.99,
        "image": "https://images.unsplash.com/photo-1519125323398-675f0ddb6308?auto=format&fit=crop&w=400&q=80",
        "component": "Wearable",
        "component_image": "https://cdn-icons-png.flaticon.com/512/2921/2921826.png"
    },
    {
        "id": 3,
        "name": "Bluetooth Speaker",
        "price": 39.99,
        "image": "https://images.unsplash.com/photo-1465101046530-73398c7f28ca?auto=format&fit=crop&w=400&q=80",
        "component": "Speaker",
        "component_image": "https://cdn-icons-png.flaticon.com/512/1041/1041916.png"
    },
    {
        "id": 4,
        "name": "Fitness Tracker",
        "price": 49.99,
        "image": "https://images.unsplash.com/photo-1516574187841-cb9cc2ca948b?auto=format&fit=crop&w=400&q=80",
        "component": "Fitness",
        "component_image": "https://cdn-icons-png.flaticon.com/512/2965/2965278.png"
    },
    {
        "id": 5,
        "name": "Gaming Mouse",
        "price": 29.99,
        "image": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=400&q=80",
        "component": "Gaming",
        "component_image": "https://cdn-icons-png.flaticon.com/512/1055/1055687.png"
    },
]

st.title("🛒 Modern E-Commerce Platform")
st.markdown("Welcome! Browse our products and add them to your cart.")

# --- Cart State ---
if "cart" not in st.session_state:
    st.session_state.cart = {}

def add_to_cart(product_id):
    st.session_state.cart[product_id] = st.session_state.cart.get(product_id, 0) + 1

def remove_from_cart(product_id):
    if product_id in st.session_state.cart:
        st.session_state.cart[product_id] -= 1
        if st.session_state.cart[product_id] <= 0:
            del st.session_state.cart[product_id]

# --- Product Display ---
st.subheader("Products")
cols = st.columns(len(products))
for idx, product in enumerate(products):
    with cols[idx]:
        st.markdown(f"<div class='product-card'>", unsafe_allow_html=True)
        # Main product image with fade-in animation
        st.markdown(f"<img src='{product['image']}' width='150' style='border-radius:12px; box-shadow:0 0 16px #ff00cc88; animation: fadeInUp 1.2s;'>", unsafe_allow_html=True)
        st.write(f"**{product['name']}**")
        st.write(f"💲 {product['price']:.2f}")
        # Component image and label with neon border
        st.markdown(f"<div style='margin:8px 0;'><img src='{product['component_image']}' width='40' style='border:2px solid #00ffe7; border-radius:50%; box-shadow:0 0 8px #ff00cc; margin-right:8px; vertical-align:middle;'> <span style='color:#ff00cc; font-weight:bold; text-shadow:0 0 8px #00ffe7;'>{product['component']}</span></div>", unsafe_allow_html=True)
        # Add to Cart button with transition
        if st.button("Add to Cart", key=f"add_{product['id']}"):
            add_to_cart(product["id"])
        st.markdown("</div>", unsafe_allow_html=True)

# --- Cart Display ---
st.sidebar.header("🛒 Your Cart")
total = 0
for product_id, qty in list(st.session_state.cart.items()):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        st.sidebar.markdown(f"<div class='cart-item'>", unsafe_allow_html=True)
        st.sidebar.markdown(f"<img src='{product['component_image']}' width='28' style='border:2px solid #ff00cc; border-radius:50%; margin-right:8px; vertical-align:middle;'> <span style='color:#333399; font-weight:bold;'>{product['component']}</span>", unsafe_allow_html=True)
        st.sidebar.write(f"{product['name']} x {qty}")
        st.sidebar.write(f"Subtotal: ${product['price'] * qty:.2f}")
        if st.sidebar.button("Remove", key=f"remove_{product_id}"):
            remove_from_cart(product_id)
        st.sidebar.markdown("</div>", unsafe_allow_html=True)
        total += product['price'] * qty

if total > 0:
    st.sidebar.write(f"**Total: ${total:.2f}**")
    if st.sidebar.button("Checkout"):
        st.sidebar.markdown("<div class='checkout-success'>Thank you for your purchase! 🎉</div>", unsafe_allow_html=True)
        st.session_state.cart = {}
else:
    st.sidebar.info("Your cart is empty.")

# --- Footer ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #7f8c8d;'>© 2025 Modern E-Commerce Demo</p>", unsafe_allow_html=True)
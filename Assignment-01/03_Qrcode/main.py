import streamlit as st
import qrcode
from PIL import Image
import io

st.set_page_config(page_title="QR Code Generator", page_icon="🔲")

st.title("🔲 QR Code Generator")
st.write("Enter your data below to generate a QR code.")

# Input box
data = st.text_input("Enter the data for QR Code:", "Don't forget to subscribe")

if st.button("Generate QR Code"):
    # Generate QR Code
    qr = qrcode.make(data)
    
    # Show image in Streamlit
    buf = io.BytesIO()
    qr.save(buf, format='PNG')
    buf.seek(0)
    
    st.image(buf, caption="Generated QR Code", use_container_width=False)

    # Download button
    st.download_button(
        label="📥 Download QR Code",
        data=buf,
        file_name="myqrcode.png",
        mime="image/png"
    )

# 🔲 QR Code Generator - Python Project

This program allows users to **generate a QR Code** for any input text or URL.
- The user inputs any string (e.g., text, website URL).
- The program instantly creates a **QR code image** based on the input.
- Users can **download** the generated QR code.

---

## 🛠️ How It Works
1️⃣ The user types a message or URL in the input box.  
2️⃣ Clicks the **"Generate QR Code"** button.  
3️⃣ A QR code is generated and shown instantly.  
4️⃣ The user can download the QR Code as a **PNG file**.

---

## 🖥️ Code Implementation (Streamlit App)
```python
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
```

---

## 📌 Example Output
```
Enter the data for QR Code: https://www.example.com
[QR Code Image displayed]
📥 Download QR Code
```

---

## 🔗 Google Colab Notebook
[Open in Google Colab](https://colab.research.google.com/drive/1eblvgGS9bu8QUiBA85G6iwaVdgD3jKMU?usp=sharing)

---

✅ **Quick, Easy & Fun QR Code Generator!**

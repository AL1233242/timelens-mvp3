import streamlit as st
from PIL import Image
import openai
import os

# Set your OpenAI API key (use Streamlit Secrets in production)
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="TimeLens – AI for Watch Collectors", layout="centered")
st.title("🕒 TimeLens")
st.subheader("AI-Powered Watch Insights, in Seconds")

st.markdown("""
Upload a photo of your watch and let our AI analyze it for:
- Brand & model identification
- Price estimate
- Listing title & product description
- **Authenticity Confidence Score** 🛡️
""")

uploaded_file = st.file_uploader("📷 Upload a watch photo", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Watch", use_column_width=True)

    with st.spinner("Analyzing your watch with AI..."):
        base_prompt = (
            "You are an expert watch authenticator and reseller. Given the uploaded image, identify the watch brand, model, style, materials, and approximate market value."
            " Then, create a short eBay-style listing title, followed by a 2-sentence product description."
            " Finally, based on visual indicators like engravings, proportions, logo precision, and finishing details, give a 0–100% authenticity confidence score."
            " Mention any red flags or reasons for low confidence."
        )

        response = openai.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=[
                {"role": "system", "content": "You are a world-class watch expert and authenticator."},
                {"role": "user", "content": [
                    {"type": "text", "text": base_prompt},
                    {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64," + uploaded_file.getvalue().decode("latin1")}}
                ]},
            ],
            max_tokens=1000
        )

        output = response.choices[0].message.content
        st.markdown("---")
        st.markdown("### 📝 AI Analysis")
        st.markdown(output)

        st.markdown("---")
        st.markdown("#### ✅ Want to get early access to full features?")
        st.markdown("[Join the Waitlist](https://tally.so/r/nPZNjV)")

st.markdown("---")
st.caption("TimeLens – Built with 💡 + 🧠")

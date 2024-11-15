import streamlit as st
from openai import OpenAI
import base64

# Initialize the OpenAI client
client = OpenAI(
    base_url="https://inference-api.netmind.ai/inference-api/openai/v1",
    api_key="ee8102d182a8493eb0b9fc2c42735f61",  # Replace with your NetMind API key
)

model_name = "stabilityai/stable-diffusion-3.5-large"

def generate_image(prompt):
    """
    Generate an image from the given prompt using OpenAI client.
    """
    try:
        response = client.images.generate(
            model=model_name,
            prompt=prompt,
            response_format="b64_json"
        )
        return response.data[0].b64_json
    except Exception as e:
        st.error(f"Error generating image: {e}")
        return None


def save_image(base64_data):
    """
    Display the base64-encoded image in Streamlit.
    """
    try:
        image_data = base64.b64decode(base64_data)
        st.image(image_data, caption="Generated Image", use_column_width=True)
    except Exception as e:
        st.error(f"Error displaying image: {e}")


def main():
    """
    Main function to get input from the user and generate an image.
    """
    st.title("Image Generation with Stable Diffusion")
    
    # Create a text input field for the prompt
    prompt = st.text_input("Enter your image prompt", "A beautiful sunrise over a mountain range")
    
    if st.button("Generate Image"):
        if prompt:
            st.info("Generating image, please wait...")
            image_base64 = generate_image(prompt)
            
            if image_base64:
                save_image(image_base64)
                st.success("Image generation successful!")
            else:
                st.error("Failed to generate image.")
        else:
            st.warning("Prompt cannot be empty.")


if __name__ == "__main__":
    main()

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
        print(f"Error generating image: {e}")
        return None


def save_image(base64_data, filename="generated_image.png"):
    """
    Save the base64-encoded image to a file.
    """
    try:
        with open(filename, "wb") as f:
            f.write(base64.b64decode(base64_data))
        print(f"Image saved as {filename}")
    except Exception as e:
        print(f"Error saving image: {e}")


def main():
    """
    Main function to get input from the user and generate an image.
    """
    prompt = input("Enter your image prompt (e.g., A beautiful sunrise over a mountain range): ").strip()
    if not prompt:
        print("Prompt cannot be empty.")
        return

    print("Generating image, please wait...")
    image_base64 = generate_image(prompt)

    if image_base64:
        save_image(image_base64)
        print("Image generation successful!")
    else:
        print("Failed to generate image.")


if __name__ == "__main__":
    main()

import requests
from fastapi import FastAPI
app = FastAPI(title="File Text Extractor API", description="API to extract text from PDF, DOCX, and TXT files", version="0.1.0")
# url = "https://925d-2401-4900-1cd0-4432-a454-7c7d-744d-37d1.ngrok-free.app/api/generate"  # Updated URL with endpoint

# # Set up the headers, assuming JSON input and output
# headers = {
#     "Content-Type": "application/json",
#     "Authorization": "Bearer your_public_api_key_here"  # Replace with your actual public API key
# }

# # Define the payload, assuming 'gemma2' is the model you want to use
# payload = {
#     "model": "gemma2",  # Specify Gemma2 as the model
#     "prompt": "Hello, world!"  # Your input prompt here
# }

# # Send the POST request to the Ollama server
# response = requests.post(url, json=payload, headers=headers)

# # Check for a successful response
# if response.status_code == 200:
#     print(response.json())  # Print the generated response from the model
# else:
#     print(f"Request failed with status code {response.status_code}")
#     print(response.text)



response = requests.get("http://localhost:11434/api/v1/generate")
print(response.status_code)
print(response.text)

@app.get("/parse_resume2")
async def extract_text():
    response = requests.get("https://af5c-2401-4900-1cd0-4432-a454-7c7d-744d-37d1.ngrok-free.app/parse_resume")
    print(response.status_code)
    print(response.text)

from langchain_ollama import OllamaLLM
import json
import re

# Initialize the model
model = OllamaLLM(model="llama3")

def parseResumeViaLlm(text):
# Strict prompt to enforce JSON format
    prompt = f"""
    Extract all relevant details from the following resume in a structured format. 
    You must return a **valid JSON object only** with the following fields:
    - name
    - contact_information (phone, email)
    - work_experience (job title, company, responsibilities, dates)
    - total_experience
    - education (degrees, institutions, graduation dates)
    - skills
    - certifications_and_achievements
    - additional_details (e.g., languages, hobbies)

    Do not include any text, notes, or explanations outside the JSON object.
    Strictly return valid JSON only.

    Resume: {text}
    """

    # Invoke the model with the strict prompt
    result = model.invoke(input=prompt)
    try:
        # if json_match:
        clean_json = result  # Get the cleaned JSON content
        ttt = clean_json.split('```')[1]

        json_result = json.loads(ttt)  # Parse the cleaned JSON
        return  json.dumps(json_result, indent=4)

    except json.JSONDecodeError as e:
        print(e)
        return f"Error {e}"
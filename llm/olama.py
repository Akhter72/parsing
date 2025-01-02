from langchain_ollama import OllamaLLM
import json
import re

# Initialize the model
model = OllamaLLM(model="llama3")

def parseResumeViaLlm(text):
# Strict prompt to enforce JSON format
    prompt = f"""
    Extract all relevant details from the following resume in a strictted json format. ans skills should also show the related amount of experience in years
    Do not include any text, notes, or explanations in response.
    Strictly return valid JSON only.
    dont include any headings or descriptions in response.
    if Json data is not availabel, that time return empty String

    You must return a **valid JSON object only** with the following fields:
    - name
    - contact_information (phone, email)
    - work_experience (job title, company, responsibilities, dates)
    - total_experience
    - education (degrees, institutions, graduation dates)
    - skills (name, related_experience)
    - certifications_and_achievements
    - additional_details (e.g., languages, hobbies)

    

    Resume: {text}
    """

    # Invoke the model with the strict prompt
    result = model.invoke(input=prompt)
    try:
        # if json_match:
        # clean_json = result  # Get the cleaned JSON content
        # ttt = clean_json.split('```')[1]

        json_result = json.loads(result)   # Parse the cleaned JSON
        return json_result
        # return  json.dumps(json_result, indent=4)

    except json.JSONDecodeError as e:
        print(e)
        return {}
        # parseResumeViaLlm(text)


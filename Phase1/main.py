from schema import ProtocolExtraction  
from fastapi import FastAPI, Body,HTTPException
from google import genai
from pydantic import ValidationError
import json
app = FastAPI()


# Create Gemini client
client = genai.Client(api_key="AIzaSyD05a8QAN75IfsRGw4zUSMxRPqvPWreRdM")

# Deepgram client
# deepgram = Deepgram("YOUR_DEEPGRAM_API_KEY")


@app.post("/extract-criteria", response_model=ProtocolExtraction)
async def extract_criteria(request: ProtocolRequest):
 
    # Prompt for Gemini
    prompt = f"""
    Extract inclusion and exclusion criteria from following text.
    Output ONLY valid JSON. Do not include explanations, comments, or text outside JSON.
    Output should be in json format and strictly follow pydantic model.

    {EligibilityCriteria.schema_json(indent=2)}

    Text: {content}
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
           contents=[
                {"role": "system", "parts": ["You are a strict JSON extractor."]},
                {"role": "user", "parts": [prompt]}
            ]
        )

        
        raw_output = response.text.strip()

        # Step 1: Ensure JSON is valid
        try:
            parsed_json = json.loads(raw_output)
        except json.JSONDecodeError as je:
            raise HTTPException(status_code=400, detail=f"Invalid JSON from LLM: {je}")

        # Step 2: Validate against Pydantic
        try:
            criteria = ProtocolExtraction.parse_obj(parsed_json)
        except ValidationError as ve:
            raise HTTPException(status_code=400, detail=ve.errors())

        return criteria.dict()
    
    except Exception as e:
        # Return error details so you can debug
        return {"error": str(e)}


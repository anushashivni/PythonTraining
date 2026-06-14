except json.JSONDecodeError as je:
            raise HTTPException(status_code=400, detail=f"Invalid JSON from LLM: {je}")
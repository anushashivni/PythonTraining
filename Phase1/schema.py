from pydantic import BaseModel, Field
from typing import List, Optional

class Criterion(BaseModel):
    category: str = Field(..., description="E.g., Age, Diagnosis, Medication, Lab Result")
    operator: str = Field(..., description="E.g., >, <, =, includes, excludes")
    value: str = Field(..., description="The specific value or condition")
    original_text: str = Field(..., description="The exact quote from the source text for verification")

class ProtocolExtraction(BaseModel):
    inclusion_criteria: List[Criterion]
    exclusion_criteria: List[Criterion]
    summary: str
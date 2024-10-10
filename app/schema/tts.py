from pydantic import BaseModel, Field


class TextRequest(BaseModel):

    text: str = Field(
        ...,
        example="سلام دوستان",
        description="The text to synthesize into speech.",
    )

    voice: str = Field(
        "male",
        example="female",
        description="Voice option, either 'male' or 'female' (default is 'male').",
    )

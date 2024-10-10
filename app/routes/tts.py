import uuid

import torch
from fastapi import APIRouter, HTTPException

from app.schema.tts import TextRequest
from app.utils.synthesizer import get_synthesizer

router = APIRouter()


@router.get("/check_cuda/", summary="Check CUDA availability")
def check_cuda():
    return {"cuda_available": torch.cuda.is_available()}


@router.get("/cuda_devices/", summary="Count CUDA devices")
def count_cuda_devices():
    return {"cuda_devices": torch.cuda.device_count()}


@router.post("/synthesize/", summary="Convert text to speech")
async def synthesize_speech(request: TextRequest):
    """
    Convert text to speech based on the specified voice (male or female).
    """

    text = request.text
    voice = request.voice.lower()
    synthesizer = get_synthesizer(voice)

    if synthesizer is None:
        raise HTTPException(
            status_code=400,
            detail="Invalid voice option. Choose 'male' or 'female'.",
        )

    try:
        waves = synthesizer.tts(text)
        output_filename = f"./generated/{uuid.uuid4()}.wav"
        synthesizer.save_wav(waves, output_filename)
        return {"message": "Speech synthesized", "file": output_filename}

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred: {str(e)}",
        )

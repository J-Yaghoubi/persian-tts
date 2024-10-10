import torch
from TTS.utils.synthesizer import Synthesizer

from app.settings.config import (
    FEMALE_CONFIG_PATH,
    FEMALE_MODEL_PATH,
    MALE_CONFIG_PATH,
    MALE_MODEL_PATH,
)


def get_synthesizer(voice: str):
    """
    Return the appropriate synthesizer based on the voice (male/female).
    """

    cuda = torch.cuda.is_available()

    if voice == "male":
        return Synthesizer(
            tts_checkpoint=MALE_MODEL_PATH,
            tts_config_path=MALE_CONFIG_PATH,
            use_cuda=cuda,
        )

    elif voice == "female":
        return Synthesizer(
            tts_checkpoint=FEMALE_MODEL_PATH,
            tts_config_path=FEMALE_CONFIG_PATH,
            use_cuda=cuda,
        )

    return None

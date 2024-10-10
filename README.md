## Persian TTS (Text to Speech)

This **FastAPI** application provides a straightforward example of converting Persian text into a WAV audio file. The operation is performed using the **TTS package** and the **espeak-ng** engine.

Please note that additional work is needed to make this example production-ready.

</br>

## Preparation

Follow the steps below to install the required packages:

```bash
# create a virtual environment using supported python version for TTS
virtualenv -p python3.9.18 .venv

# activate the virtual environment
source .venv/bin/activate

# install the required packages
pip install fastapi uvicorn TTS

# install espeak-ng on your machine. This is ubuntu specific example
sudo apt-get -y install espeak-ng
```

</br>

Now download the models and put them in the `./static` directory with the following commands:

```bash
# male model
wget -O male.pth https://huggingface.co/Kamtera/persian-tts-male1-vits/resolve/main/checkpoint_88000.pth
wget -O male.json https://huggingface.co/Kamtera/persian-tts-male1-vits/resolve/main/config.json

# female model
wget -O female.pth https://huggingface.co/Kamtera/persian-tts-female-vits/resolve/main/best_model_30824.pth
wget -O female.json https://huggingface.co/Kamtera/persian-tts-female-vits/resolve/main/config.json
```

</br>

## Play With

Start the API by running the following command. Then open your browser and navigate to `http://127.0.0.1:8000/docs` to access the API documentation:

```bash
uvicorn app.main:app --reload
```

</br>

### References

---

- [TTS package](https://github.com/coqui-ai/TTS)
- [Trained Model](https://huggingface.co/spaces/Kamtera/Persian-tts-CoquiTTS)

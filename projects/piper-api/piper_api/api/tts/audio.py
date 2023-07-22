from functools import partial

from flask import Response, request
from flask_restful import Resource
from piper_api.piper import Piper
from piper_api.utils import (
    generate_audio,
    get_available_voices,
    get_voices_with_generated_id,
)


class VoicesResource(Resource):
    def get(self):
        """Endpoint retrieves a list of available voices for each language, with their respective voice types.
        ---
        tags:
            - TTS
        responses:
            200:
                description: A list of available voices for different languages
        """
        available_voices = get_available_voices()
        list_available_voices = [
            {"id": k, "voices": v} for k, v in available_voices.items()
        ]
        return list_available_voices, 200


class TTSResource(Resource):
    def get(self):
        """This endpoint synthesizes audio from the given text using the specified voice ID.
        ---
        tags:
            - TTS
        parameters:
            - name: text
              in: query
              required: true
              type: string
              description: The text to generate audio
            - name: voice_id
              in: query
              required: true
              type: string
              enum: ['pt_BR-faber-medium', 'pt_BR-edresson-low']
              description: The ID of the voice to generate audio
        responses:
            200:
                description: The generated audio file in WAV format
                content:
                    application/octet-stream:
                        schema:
                            type: string
                            format: binary
                            example: audio.wav
        """
        synthesis_text = request.args.get("text")
        voice_id = request.args.get("voice_id")
        available_voices = get_voices_with_generated_id()

        if not synthesis_text:
            return {"message": "The 'text' parameter is required."}, 400

        if not voice_id:
            return {"message": "The 'voice_id' parameter is required."}, 400

        if voice_id not in available_voices:
            return {"message": "The 'voice_id' is invalid."}, 400

        model = available_voices[voice_id]
        voice = Piper(
            model,
            config_path=f"{model}.json",
            use_cuda=False,
        )
        synthesize = partial(voice.synthesize)
        wav_bytes = synthesize(synthesis_text)
        return Response(generate_audio(wav_bytes), mimetype="audio/wav")

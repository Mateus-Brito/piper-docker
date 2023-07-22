from flask import Blueprint
from flask_restful import Api
from piper_api.api.tts.audio import TTSResource, VoicesResource

blueprint = Blueprint("v1", __name__, url_prefix="/api")
tts = Api(blueprint)


tts.add_resource(TTSResource, "/tts", endpoint="tts")
tts.add_resource(VoicesResource, "/tts/voices", endpoint="tts-voices")

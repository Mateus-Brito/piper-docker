import glob
import os
from pathlib import Path
from typing import Generator

from piper_api.settings import PIPER_VOICES_PATH


def find_files_with_extension(directory, extension):
    """
    Finds files with the given extension in the specified directory and its subdirectories.

    Args:
        directory (str): The base directory to search for files.
        extension (str): The file extension to filter the files.

    Returns:
        List[str]: A list of file paths that match the specified extension.
    """
    matched_files = []
    pattern = os.path.join(directory, f"**/*.{extension}")
    matched_files = glob.glob(pattern, recursive=True)
    return matched_files


def get_voices_paths():
    """
    Retrieves a list of paths to voice files in the 'pt' directory under PIPER_VOICES_PATH.

    Returns:
        List[str]: A list of file paths to the voice files with the 'onnx' extension.
    """
    root_voices_path = PIPER_VOICES_PATH + "/pt"
    voices_files = find_files_with_extension(root_voices_path, "onnx")
    return voices_files


def get_available_voices() -> dict:
    """
    Returns a dictionary of available voices.

    Returns:
        dict: A dictionary containing information about available voices.
    """
    available_voices = {}
    for voice_path in get_voices_paths():
        file_name = Path(voice_path).stem
        lang, voice_name, quality = file_name.split("-")
        if lang not in available_voices:
            available_voices[lang] = {}
        if voice_name not in available_voices[lang]:
            available_voices[lang][voice_name] = {"id": file_name, "quality": [quality]}
        else:
            available_voices[lang][voice_name]["quality"].append(quality)
    return available_voices


def get_voices_with_generated_id() -> dict:
    """
    Returns a dictionary of voices with their generated IDs.

    Returns:
        dict: A dictionary containing information about voices.
    """
    voices_dict = {}
    for voice_path in get_voices_paths():
        file_name = Path(voice_path).stem
        voices_dict[file_name] = voice_path
    return voices_dict


def generate_audio(wav_bytes: bytes) -> Generator[bytes, None, None]:
    """Generate audio data from WAV bytes.

    This function takes a byte array representing a WAV audio file and yields data in chunks of 1024 bytes.
    It allows processing audio data in a streaming fashion, which can be useful for large audio files.

    Args:
        wav_bytes (bytes): The input byte array containing the WAV audio data.

    Yields:
        bytes: A chunk of audio data, represented as a bytes object, with a maximum size of 1024 bytes.
    """
    chunk_size = 1024
    offset = 0
    while offset < len(wav_bytes):
        data = wav_bytes[offset : offset + chunk_size]
        offset += chunk_size
        yield data

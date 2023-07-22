# Piper-Docker: Text-to-Speech API using Flask and Swagger

![Piper-Docker Swagger](https://github.com/Mateus-Brito/piper-docker/assets/13570164/e08c0756-60dc-4dcf-afc0-3d8cfe94d0bc)

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)

## Introduction

Welcome to Piper-Docker, a powerful Text-to-Speech (TTS) API built with Flask and Swagger. This project aims to provide an easy-to-use API that leverages the [piper](https://github.com/rhasspy/piper) library, offering a variety of voice models from the [piper-voices](https://huggingface.co/rhasspy/piper-voices/) project to generate high-quality audio from text input.

## Installation

To get started with Piper-Docker, follow these steps:

1. Ensure you have Docker installed on your system.
2. Clone the Piper-Docker repository:
   ```bash
   git clone https://github.com/Mateus-Brito/piper-docker.git
   cd piper-docker
   ```
3. Install the project and its dependencies using `make`:
   ```bash
   make install
   ```
   This command will set up the required dependencies and create a Docker container with the application ready to run.

## Usage

Once you have installed Piper-Docker, it's time to run the application. To do this, simply execute the following command:

```bash
make start
```

This will start the Flask server and Swagger UI at http://localhost:5000/apidocs/, allowing you to interact with the API and generate audio from text using various voice models available in 'piper-voices'.

## API Endpoints

Piper-Docker exposes the following API endpoints:

- `GET /api/tts?text=&voice_id=`: Synthesizes audio from the given text using the specified voice ID.
- `GET /tts/voices`: Retrieves a list of available voices for each language, with their respective voice types.

---

> **Note**
> The MODEL_CARD file for each voice contains important licensing information. Piper is intended for text to speech research, and does not impose any additional restrictions on voice models. Some voices may have restrictive licenses,  however, so please review them carefully!

Happy text-to-speech synthesis! 🎤🔊
# scene-helper

A CLI agent that turns short scene descriptions into video clips.

It uses an LLM (OpenAI) to expand casual descriptions into detailed cinematic prompts, then sends them to [Runway ML](https://runwayml.com/) for video generation.

## Setup

1. **Install dependencies:**

   ```bash
   pip install -e .
   ```

2. **Configure API keys** — copy `.env.example` to `.env` and fill in your keys:

   ```bash
   cp .env.example .env
   ```

   You need:
   - `RUNWAYML_API_SECRET` — from [Runway API settings](https://app.runwayml.com/)
   - `OPENAI_API_KEY` — from [OpenAI](https://platform.openai.com/api-keys)

## Usage

```bash
# Basic — describe a scene and get a video
scene-helper "a cat sitting on a windowsill at sunset"

# Skip LLM expansion, use your prompt directly
scene-helper --no-expand "Slow dolly shot of a tabby cat on a windowsill, golden hour light streaming through glass, dust motes in the air"

# Customize model, ratio, and duration
scene-helper --model gen4.5 --ratio 1280:720 --duration 8 "a spaceship launching from a desert planet"
```

Output videos are saved to the `output/` directory.

## How it works

1. **Expand** — Your short description is sent to GPT-4o-mini, which expands it into a detailed visual prompt with camera angles, lighting, and style
2. **Generate** — The expanded prompt is sent to Runway ML's text-to-video API
3. **Download** — The finished video is downloaded and saved locally

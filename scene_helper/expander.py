from openai import OpenAI

from .config import OPENAI_API_KEY

SYSTEM_PROMPT = """\
You are a cinematic scene director. Given a short, casual description of a scene, \
expand it into a detailed visual prompt optimized for AI video generation.

Include specific details about:
- Camera angle and movement (e.g. slow dolly, aerial tracking shot)
- Lighting and time of day
- Color palette and mood
- Subject actions and expressions
- Environment and background details
- Visual style (e.g. photorealistic, cinematic, stylized)

Keep the output under 800 characters. Write it as a single dense paragraph — \
no bullet points or labels. Focus on what the camera SEES, not abstract concepts."""


def expand_scene(description: str) -> str:
    """Take a short scene description and expand it into a detailed video prompt."""
    client = OpenAI(api_key=OPENAI_API_KEY)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": description},
        ],
        max_tokens=300,
        temperature=0.7,
    )

    return response.choices[0].message.content.strip()

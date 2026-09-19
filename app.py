import os
from flask import Flask, render_template, request, jsonify
from google import genai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None

LEVEL_PROMPTS = {
    "five": "a curious 5-year-old. Use very short sentences, everyday comparisons "
            "(toys, animals, food, family), and zero jargon.",
    "teen": "a smart high schooler with no background in this topic. Use relatable "
            "analogies, plain language, and light structure. Avoid unexplained jargon.",
    "college": "a college student encountering this for the first time in their major. "
               "You can use some technical vocabulary, but define any term that isn't "
               "common knowledge.",
    "expert": "a professional who already works in an adjacent field. Be precise and "
              "technical, skip basic definitions, and focus on what's distinctive or "
              "non-obvious about this specific text.",
}

SYSTEM_PROMPT = (
    "You explain confusing text clearly, at the reading level the user asks for. "
    "Rules:\n"
    "1. Never say things like 'imagine you are five' or refer to the audience directly.\n"
    "2. Open with a one-sentence plain-language summary of what the text is really saying.\n"
    "3. Then explain the key ideas in short paragraphs or a tight bulleted list — "
    "whichever fits better.\n"
    "4. If there are technical terms essential to understanding, define them briefly, "
    "in the requested register.\n"
    "5. Do not pad with filler, disclaimers, or restate the question.\n"
    "6. Keep the whole answer under 220 words unless the source text is very long."
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/explain", methods=["POST"])
def explain():
    if client is None:
        return jsonify({
            "error": "No GEMINI_API_KEY found on the server. Add one to your .env file "
                     "(see .env.example) and restart the app."
        }), 500

    data = request.get_json(silent=True) or {}
    text = (data.get("text") or "").strip()
    level = data.get("level", "teen")

    if not text:
        return jsonify({"error": "Paste some text first."}), 400
    if len(text) > 6000:
        return jsonify({"error": "That's a lot of text — keep it under 6000 characters."}), 400
    if level not in LEVEL_PROMPTS:
        level = "teen"

    user_prompt = (
        f"Explain the following text for {LEVEL_PROMPTS[level]}\n\n"
        f"---\nTEXT TO EXPLAIN:\n{text}\n---"
    )

    try:
        interaction = client.interactions.create(
            model="gemini-3.6-flash",
            input=user_prompt,
            system_instruction=SYSTEM_PROMPT,
            generation_config={
                "max_output_tokens": 2000,
                "thinking_level": "minimal",
            },
        )
        explanation = getattr(interaction, "output_text", None)
        if not explanation and getattr(interaction, "outputs", None):
            explanation = interaction.outputs[-1].text
        explanation = (explanation or "").strip()
        if not explanation:
            return jsonify({"error": "The AI returned an empty response. Try again."}), 502
        return jsonify({"explanation": explanation})
    except Exception as exc:  # keep the demo resilient during judging
        return jsonify({"error": f"The AI request failed: {exc}"}), 502


if __name__ == "__main__":
    app.run(debug=True, port=5000)

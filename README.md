# Jarvis educational starter

A runnable Python example showing a small assistant with explicit intent routing and confirmation before a browser action. This is newly prepared educational code, separate from my ongoing Jarvis workflow using existing AI tools and connectors. It is not a release of my complete personal assistant.

## Run

Install Python 3.11 or later, then:

```sh
python jarvis.py
```

No API keys, accounts or extra packages are required. Try `help`, `time`, `open github documentation` and `quit`. Opening the fixed documentation URL requires typing `y`; other input cancels. Unknown commands are rejected.

## How to extend it

1. Capture a local wake word and short audio segment only after activation.
2. Convert that segment to text with a selected speech-to-text engine.
3. Pass recognised text to an explicit command router such as `respond`.
4. Use narrowly scoped action functions with confirmation where appropriate.
5. Speak the response using a text-to-speech engine, then return to idle.

Wake-word detection, microphone capture, speech recognition, spoken responses and calendar or email integrations are not implemented in this starter. Those require separate modules and configuration. Choose those components for your device before adding them.

Keep connector permissions limited. Review before sending messages or changing files. Never execute arbitrary recognised speech or model output as shell commands. Avoid retaining recordings and private briefings by default.

For optional cloud services, read credentials from server-side environment variables. Keep `.env` ignored and use only empty placeholders in `.env.example`. Never put secrets in browser code or variables prefixed `VITE_`. Do not commit logs containing account information.

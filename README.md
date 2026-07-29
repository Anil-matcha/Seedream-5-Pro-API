# Awesome AI Game Generation [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of tools, models, research, and resources for generating games with AI — from prompt-to-playable-game platforms to real-time neural world models.

AI game generation covers everything from LLM-assisted asset/code scaffolding to full **world models** that generate playable, interactive worlds frame-by-frame with no traditional game engine at all. This list tracks both ends of that spectrum.

## Contents

- [World Models & Research](#world-models--research)
- [Prompt-to-Game Platforms](#prompt-to-game-platforms)
- [AI Tools for Game Developers](#ai-tools-for-game-developers)
- [Game Engine AI Integrations](#game-engine-ai-integrations)
- [Papers](#papers)
- [Related Awesome Lists](#related-awesome-lists)
- [Contributing](#contributing)

## World Models & Research

Systems that generate an interactive, playable world in real time from actions/prompts, rather than assembling a traditional game engine.

- [Genie 3](https://en.wikipedia.org/wiki/Genie_(AI_model)) — Google DeepMind's real-time interactive world model; generates playable 3D worlds frame-by-frame from a prompt, trained on 30,000+ hours of gameplay.
- [GameNGen](https://anthemcreation.com/en/artificial-intelligence/gamengen-and-doom-ai-video-games-real-time-generation/) — Google research showing a diffusion model can run DOOM in real time as a neural game engine, with no explicit game logic.
- [Oasis](https://github.com/etched-ai/open-oasis) — Open-weights real-time generative Minecraft-like world model.
- [Matrix-Game](https://arxiv.org/abs/2506.18701) — Interactive world foundation model for controllable game world generation.
- [HunyuanWorld 1.0](https://github.com/Tencent-Hunyuan/HunyuanWorld-1.0) — Generates immersive, explorable, interactive 3D worlds from text or images.
- [Yan](https://arxiv.org/abs/2508.08601) — Tencent's foundational interactive video generation model for game-like worlds.

## Prompt-to-Game Platforms

Tools where you describe a game in natural language and get a playable result.

- [Rosebud AI](https://rosebud.ai/) — Prompt-to-game platform; generates playable 2D/3D games (Phaser-based) with an in-browser chat editor, exportable code, and free hosting.
- [Ludo.ai](https://ludo.ai/) — Ideation/research tool for game designers combining text/image generation with AI-powered market and trend search.

## AI Tools for Game Developers

AI-assisted tooling for asset generation, NPCs, and traditional game dev pipelines (not full-game generation).

- [Unity MCP Plugin](https://github.com/CoplayDev/unity-mcp) — Editor bridge letting Claude/Cursor/MCP-compatible AI control the Unity Editor.
- See [simoninithomas/awesome-ai-tools-for-game-dev](https://github.com/simoninithomas/awesome-ai-tools-for-game-dev) for a deep catalog of asset/texture/voice generation tools for traditional pipelines.

## Game Engine AI Integrations

- [Unity MCP](https://github.com/CoplayDev/unity-mcp) — MCP server exposing Unity Editor control to AI agents.
- Godot + AI agent workflows — emerging category; see GitHub topic [`ai-game-development`](https://github.com/topics/ai-game-development) for active projects.

## Papers

- Genie 3: A new frontier for world models — Google DeepMind (2025)
- [Generative AI in Game Development: A Qualitative Research Synthesis](https://arxiv.org/html/2509.11898v1) (2025)
- [From Masks to Worlds: A Hitchhiker's Guide to World Models](https://arxiv.org/pdf/2510.20668) (2025)
- [Simulating the Visual World with Artificial Intelligence: A Roadmap](https://arxiv.org/pdf/2511.08585) (2025)
- [Visual Generation in the New Era: An Evolution from Atomic Mapping to Agentic World Modeling](https://arxiv.org/pdf/2604.28185) (2026)
- Generative Games: Positioning, Progress and Prospects — [Preprints.org](https://www.preprints.org/manuscript/202412.1531) (2024)

## Related Awesome Lists

- [JingyeChen/awesome-game-generation](https://github.com/JingyeChen/awesome-game-generation) — research-focused list of game generation techniques.
- [lappemic/awesome-ai-built-games](https://github.com/lappemic/awesome-ai-built-games) — games built primarily by prompting LLMs.
- [simoninithomas/awesome-ai-tools-for-game-dev](https://github.com/simoninithomas/awesome-ai-tools-for-game-dev) — AI tools for traditional game dev pipelines.
- [datamllab/awesome-game-ai](https://github.com/datamllab/awesome-game-ai) — multi-agent reinforcement learning in games.

## Contributing

Contributions welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first. Make sure your addition is genuinely relevant to **AI-driven game generation** (not general game dev or general game AI — see the related lists above for those).

## License

[CC0](LICENSE) — public domain.

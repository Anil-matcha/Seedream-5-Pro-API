---
name: seedream-5-pro
description: Use the Seedream 5.5 API for image generation, editing, and layer decomposition, or generate and edit images with Seedream 5.0 Pro (by ByteDance).
version: 1.0.0
metadata:
  openclaw:
    requires:
      env:
        - MUAPI_API_KEY
      bins:
        - python3.11
    emoji: 🎨
    homepage: https://muapi.ai
    os: ["macos", "linux"]
---

# Seedream 5.5 API and Seedream 5.0 Pro API

This skill provides Seedream 5.5 image generation, multi-reference editing, and layer decomposition through MuAPI. Seedream 5.5 is a distinct model from Seedream 5.0 Pro; its endpoints use `resolution`, `output_format`, and `background` parameters. The 5.0 Pro commands below remain available for existing projects.

Seedream 5.0 Pro is ByteDance's flagship text-to-image model, delivering maximum-fidelity AI art with advanced visual reasoning and precise typography. This skill allows you to generate images from text and edit existing images using natural language commands.

## Prerequisites

- **MUAPI_API_KEY**: You must have an API key from [muapi.ai](https://muapi.ai). Set it as an environment variable.

## Usage Guide

### Seedream 5.5 API

Generate images with native transparent-background output:
```bash
python3.11 skills/seedream-5-pro/seedream_cli.py t2i-5-5 --prompt "A glass perfume bottle on a pale stone plinth" --resolution 2K --background transparent --wait
```

Edit one or more reference images (up to 10):
```bash
python3.11 skills/seedream-5-pro/seedream_cli.py edit-5-5 --images "https://example.com/product.png" --prompt "Remove the background and keep the product edges crisp" --background transparent --wait
```

Split a flat image into a base image and transparent layers:
```bash
python3.11 skills/seedream-5-pro/seedream_cli.py layers-5-5 --image_url "https://example.com/poster.png" --prompt "Separate the headline, photo, and border" --max_images 6 --wait
```

Layer decomposition is billed by the requested `max_images` slots, even if fewer layers are returned. Keep this value close to the number of outputs you need. The [Seedream 5.5 API guide](https://muapi.ai/seedream-5.5) has endpoint parameters and current pricing.

ByteDance's [Seedream 5.5 announcement](https://seed.bytedance.com/en/blog/more-realistic-images-more-stable-editing-across-100-rounds-introducing-seedream-5-5) describes native transparent assets, more realistic output, and more stable multi-turn editing. ByteDance says a Seedream 5.5 Pro version will follow; this skill's `*-5-5` commands call the current 5.5 endpoints, not a Pro endpoint.

You can use Seedream 5.0 Pro to create images in various aspect ratios (1:1, 16:9, 9:16, 4:3, 3:4) and resolutions (1K, 2K, 4K).

### Text-to-Image
Generate an image from a descriptive text prompt.
```bash
python3.11 skills/seedream-5-pro/seedream_cli.py t2i --prompt "A cinematic portrait of a cyberpunk samurai in a neon-lit Tokyo alley" --size 4K --wait
```

### Image Editing
Edit an existing image using natural language.
```bash
python3.11 skills/seedream-5-pro/seedream_cli.py edit --images "https://example.com/photo.jpg" --prompt "Change the background to a cyberpunk cityscape at night" --wait
```

### Base (non-Pro) & Legacy Versions
Generate with the base Seedream 5.0 model or earlier versions for version-pinned pipelines.
```bash
python3.11 skills/seedream-5-pro/seedream_cli.py t2i-v5 --prompt "A quick draft of a mountain landscape at dawn" --wait
python3.11 skills/seedream-5-pro/seedream_cli.py t2i-v4-5 --prompt "A surreal sci-fi cityscape floating above the clouds" --wait
python3.11 skills/seedream-5-pro/seedream_cli.py t2i-v4 --prompt "A fantasy castle on a floating island" --wait
python3.11 skills/seedream-5-pro/seedream_cli.py t2i-v3 --prompt "An anime-style portrait of a warrior princess" --wait
```

## Tips for Best Results

- **Be Descriptive**: Detailed prompts result in better image quality and more accurate scene construction.
- **Wait for Completion**: Use the `--wait` flag to receive the final image URL directly. Without it, you will receive a `request_id` which you can check later using the `status` command.
- **Aspect Ratios**: Use `1:1` for square, `16:9`/`9:16` for widescreen/vertical content.
- **Resolution**: Use `--size 4K` for maximum fidelity, `--size 1K` for fast drafts.
- **Reproducibility**: Pass `--seed` to get deterministic, repeatable generations.

## Commands Reference

| Command | Arguments | Description |
| :--- | :--- | :--- |
| `t2i` | `--prompt`, `--aspect_ratio`, `--size`, `--num_images`, `--seed`, `--wait` | Text to Image (Seedream 5.0 Pro) |
| `edit` | `--images`, `--prompt`, `--aspect_ratio`, `--size`, `--seed`, `--wait` | Image Editing (Seedream 5.0 Pro Edit) |
| `t2i-v5` | `--prompt`, `--aspect_ratio`, `--size`, `--num_images`, `--seed`, `--wait` | Text to Image (Seedream 5.0 base) |
| `edit-v5` | `--images`, `--prompt`, `--aspect_ratio`, `--size`, `--seed`, `--wait` | Image Editing (Seedream 5.0 base Edit) |
| `t2i-v4-5` | `--prompt`, `--aspect_ratio`, `--size`, `--num_images`, `--seed`, `--wait` | Text to Image (Seedream 4.5) |
| `edit-v4-5` | `--images`, `--prompt`, `--aspect_ratio`, `--size`, `--seed`, `--wait` | Image Editing (Seedream 4.5) |
| `t2i-v4` | `--prompt`, `--aspect_ratio`, `--size`, `--num_images`, `--seed`, `--wait` | Text to Image (Seedream v4) |
| `edit-v4` | `--images`, `--prompt`, `--aspect_ratio`, `--size`, `--seed`, `--wait` | Image Editing (Seedream v4) |
| `t2i-v3` | `--prompt`, `--aspect_ratio`, `--size`, `--num_images`, `--seed`, `--wait` | Text to Image (Seedream v3) |
| `status`| `--request_id` | Check Task Status |

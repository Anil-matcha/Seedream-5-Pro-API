import json
from mcp.server.fastmcp import FastMCP
from seedream_api import SeedreamAPI

# Initialize FastMCP server
mcp = FastMCP("Seedream 5.5 and 5.0 Pro API Server")

# Helper to get API client
def get_api():
    return SeedreamAPI()

@mcp.tool()
def text_to_image(prompt: str, aspect_ratio: str = "1:1", size: str = "2K", num_images: int = 1, seed: int = None) -> str:
    """
    Generate an image from a text prompt using Seedream 5.0 Pro.

    :param prompt: Descriptive text prompt.
    :param aspect_ratio: Image aspect ratio (e.g., '1:1', '16:9', '9:16', '4:3', '3:4').
    :param size: Output resolution — '1K', '2K', or '4K'.
    :param num_images: Number of images to generate (1-4).
    :param seed: Optional seed for reproducible generations.
    """
    api = get_api()
    result = api.text_to_image(prompt, aspect_ratio, size, num_images, seed)
    return json.dumps(result, indent=2)

@mcp.tool()
def edit_image(prompt: str, image_urls: list[str], aspect_ratio: str = "1:1", size: str = "2K", seed: int = None) -> str:
    """
    Edit an existing image using natural language with Seedream 5.0 Pro Edit.

    :param prompt: Instruction describing the desired edit.
    :param image_urls: List of source image URLs.
    :param aspect_ratio: Output aspect ratio.
    :param size: Output resolution — '1K', '2K', or '4K'.
    :param seed: Optional seed for reproducible generations.
    """
    api = get_api()
    result = api.edit_image(prompt, image_urls, aspect_ratio, size, seed)
    return json.dumps(result, indent=2)

@mcp.tool()
def seedream_55_text_to_image(prompt: str, aspect_ratio: str = "1:1", resolution: str = "1K", output_format: str = "png", background: str = "auto") -> str:
    """Generate an image with the Seedream 5.5 API through MuAPI.

    Use resolution 1K, 1.5K, or 2K. Set background to transparent for a PNG with alpha.
    """
    api = get_api()
    result = api.text_to_image_v5_5(prompt, aspect_ratio, resolution, output_format, background)
    return json.dumps(result, indent=2)

@mcp.tool()
def seedream_55_edit_image(prompt: str, images_list: list[str], aspect_ratio: str = None, resolution: str = "1K", output_format: str = "png", background: str = "auto") -> str:
    """Edit one to ten reference images with the Seedream 5.5 API."""
    api = get_api()
    result = api.edit_image_v5_5(prompt, images_list, aspect_ratio, resolution, output_format, background)
    return json.dumps(result, indent=2)

@mcp.tool()
def seedream_55_decompose_layers(image_url: str, prompt: str = None, resolution: str = "1K", max_images: int = 30, output_format: str = "png") -> str:
    """Split one image into a base image and transparent PNG layers.

    Billing follows max_images (2-100), the maximum requested output slots.
    """
    api = get_api()
    result = api.decompose_layers_v5_5(image_url, prompt, resolution, max_images, output_format)
    return json.dumps(result, indent=2)

@mcp.tool()
def text_to_image_v5(prompt: str, aspect_ratio: str = "1:1", size: str = "2K", num_images: int = 1, seed: int = None) -> str:
    """
    Generate an image from a text prompt using Seedream 5.0 (base, non-Pro).
    """
    api = get_api()
    result = api.text_to_image_v5(prompt, aspect_ratio, size, num_images, seed)
    return json.dumps(result, indent=2)

@mcp.tool()
def edit_image_v5(prompt: str, image_urls: list[str], aspect_ratio: str = "1:1", size: str = "2K", seed: int = None) -> str:
    """
    Edit an existing image using Seedream 5.0 Edit (base, non-Pro).
    """
    api = get_api()
    result = api.edit_image_v5(prompt, image_urls, aspect_ratio, size, seed)
    return json.dumps(result, indent=2)

@mcp.tool()
def text_to_image_v4_5(prompt: str, aspect_ratio: str = "1:1", size: str = "2K", num_images: int = 1, seed: int = None) -> str:
    """
    Generate an image from a text prompt using Seedream 4.5.
    """
    api = get_api()
    result = api.text_to_image_v4_5(prompt, aspect_ratio, size, num_images, seed)
    return json.dumps(result, indent=2)

@mcp.tool()
def edit_image_v4_5(prompt: str, image_urls: list[str], aspect_ratio: str = "1:1", size: str = "2K", seed: int = None) -> str:
    """
    Edit an existing image using Seedream 4.5 Edit.
    """
    api = get_api()
    result = api.edit_image_v4_5(prompt, image_urls, aspect_ratio, size, seed)
    return json.dumps(result, indent=2)

@mcp.tool()
def text_to_image_v4(prompt: str, aspect_ratio: str = "1:1", size: str = "2K", num_images: int = 1, seed: int = None) -> str:
    """
    Generate an image from a text prompt using Seedream v4.
    """
    api = get_api()
    result = api.text_to_image_v4(prompt, aspect_ratio, size, num_images, seed)
    return json.dumps(result, indent=2)

@mcp.tool()
def edit_image_v4(prompt: str, image_urls: list[str], aspect_ratio: str = "1:1", size: str = "2K", seed: int = None) -> str:
    """
    Edit an existing image using Seedream v4 Edit.
    """
    api = get_api()
    result = api.edit_image_v4(prompt, image_urls, aspect_ratio, size, seed)
    return json.dumps(result, indent=2)

@mcp.tool()
def text_to_image_v3(prompt: str, aspect_ratio: str = "1:1", size: str = "1K", num_images: int = 1, seed: int = None) -> str:
    """
    Generate an image from a text prompt using Seedream v3.
    """
    api = get_api()
    result = api.text_to_image_v3(prompt, aspect_ratio, size, num_images, seed)
    return json.dumps(result, indent=2)

@mcp.tool()
def upload_file(file_path: str) -> str:
    """
    Upload a local image file to MuAPI for use in generation/edit tasks.

    :param file_path: Local path to the file.
    """
    api = get_api()
    result = api.upload_file(file_path)
    return json.dumps(result, indent=2)

@mcp.tool()
def get_task_status(request_id: str) -> str:
    """
    Check the status and get results of a generation task.

    :param request_id: The ID returned from a generation tool call.
    """
    api = get_api()
    result = api.get_result(request_id)
    return json.dumps(result, indent=2)

if __name__ == "__main__":
    mcp.run()

from .image2text import Image2Text, LoadImage2TextModel, Image2TextWithTags
from .text2prompt import LoadText2PromptModel,Text2Prompt,Text2GPTPrompt
from .install import check_and_install, check_and_install_version


check_and_install_version("Pillow","10.1.0",import_name="PIL")

check_and_install_version("huggingface_hub","0.20.1")
# > 4.37.1 Qwen-1.5
check_and_install_version("transformers","4.37.1")
check_and_install_version("einops","0.7.0")
check_and_install("torchvision")
check_and_install_version("accelerate","0.25.0")
check_and_install_version("timm","0.9.12")
check_and_install_version("autoawq","0.2.3",import_name="awq")

## Qwen1_8 Prompt
check_and_install_version("tiktoken","0.6.0")
check_and_install_version("transformers_stream_generator", "0.0.4",import_name="transformers_stream_generator")

NODE_CLASS_MAPPINGS = {
    "Image2Text": Image2Text,
    "LoadImage2TextModel": LoadImage2TextModel,
    "Image2TextWithTags": Image2TextWithTags,
    "LoadText2PromptModel":LoadText2PromptModel,
    "Text2Prompt":Text2Prompt,
    "Text2GPTPrompt":Text2GPTPrompt

}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "Image2Text": "Image to Text",
    "LoadImage2TextModel": "Loader Image to Text Model",
    "Image2TextWithTags":"Image to Text with Tags",
    "LoadText2PromptModel":"Loader Text to Prompt Model",
    "Text2Prompt":"Text to Prompt",
    "Text2GPTPrompt":"Multi Text to GPTPrompt"
}

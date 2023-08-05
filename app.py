import os
os.system(f"git lfs install")
os.system(f"git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui /home/demo/source/stable-diffusion-webui")

os.chdir(f"/home/demo/source/stable-diffusion-webui")

os.system(f"sudo apt install python3.10 python3.10-distutils")
os.system(f"sudo apt-get install python3-pip")
os.system(f"pip3 install virtualenv ")
os.system(f"virtualenv venv ")
os.system(f"virtualenv -p /usr/bin/python3.10 venv")
os.system(f"source venv/bin/activate")

os.system(f"python3.10 -m venv venv")

# !./webui.sh




os.system(f"git clone https://huggingface.co/embed/negative /home/demo/source/stable-diffusion-webui/embeddings/negative")
os.system(f"git clone https://huggingface.co/embed/lora /home/demo/source/stable-diffusion-webui/models/Lora/positive")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/embed/upscale/resolve/main/4x-UltraSharp.pth -d /home/demo/source/stable-diffusion-webui/models/ESRGAN -o 4x-UltraSharp.pth")

os.system(f"git clone https://github.com/eskaviam/sd-webui-faceswaplab.git /home/demo/source/stable-diffusion-webui/extensions/sd-webui-faceswaplab")

os.system(f"wget https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth -O /home/demo/source/stable-diffusion-webui/extensions/sd-webui-segment-anything/models/sam/sam_vit_h_4b8939.pth")
os.system(f"git clone https://github.com/continue-revolution/sd-webui-segment-anything.git /home/demo/source/stable-diffusion-webui/extensions/sd-webui-segment-anything")
os.system(f"git clone https://github.com/vladmandic/sd-extension-system-info.git /home/demo/source/stable-diffusion-webui/extensions/sd-extension-system-info")

os.system(f"git clone https://github.com/AlUlkesh/stable-diffusion-webui-images-browser /home/demo/source/stable-diffusion-webui/extensions/stable-diffusion-webui-images-browser")

os.system(f"git clone https://github.com/camenduru/sd-civitai-browser /home/demo/source/stable-diffusion-webui/extensions/sd-civitai-browser")




os.system(f"git clone -b dev https://github.com/camenduru/sd-webui-aspect-ratio-helper /home/demo/source/stable-diffusion-webui/extensions/sd-webui-aspect-ratio-helper")

# os.system(f"sed -i -e 's/\"sd_model_checkpoint\"\,/\"sd_model_checkpoint\,sd_vae\,CLIP_stop_at_last_layers\"\,/g' /home/demo/source/stable-diffusion-webui/modules/shared.py")

# os.system(f"python3 launch.py --port 8266 --listen --cors-allow-origins=* --xformers --enable-insecure-extension-access --theme dark --gradio-queue --disable-safe-unpickle")
# os.system(f"curl -o /home/demo/source/stable-diffusion-webui/extensions/sd-webui-segment-anything/models/sam/sam_vit_h_4b8939.pth https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth")


import os

# Definir o local para armazenamento dos modelos e cache
os.environ["HF_HOME"] = "D:/Rafael/huggingface"
os.environ["HUGGINGFACE_HUB_CACHE"] = "D:/Rafael/huggingface/cache"

import torch
from diffusers import StableDiffusionPipeline

# Definir o cache do PyTorch
torch.hub.set_dir("D:/Rafael/huggingface/torch")

# Verificar se há uma GPU disponível
if torch.cuda.is_available():
    device = torch.device("cuda")
    print("✅ GPU disponível:", torch.cuda.get_device_name(0))
    dtype = torch.float16  # Melhor otimização para GPUs Nvidia
else:
    device = torch.device("cpu")
    print("⚠️ GPU não disponível, utilizando CPU.")
    dtype = torch.float32  # Mantém precisão adequada para CPU

# Carregar o pipeline do Stable Diffusion com otimização para GPU
pipeline = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4",
    torch_dtype=dtype  # Reduz o consumo de VRAM
)

# Mover o modelo para a GPU (se disponível)
pipeline.to(device)

# Solicitar o prompt ao usuário
prompt = input("Digite a descrição da imagem que deseja gerar: ")

# Gerar a imagem a partir do prompt
with torch.autocast(device.type) if torch.cuda.is_available() else torch.no_grad():
    imagem = pipeline(prompt).images[0]

# Salvar e exibir a imagem gerada
imagem.save("imagem_gerada.png")
imagem.show()

print("✅ Imagem gerada e salva como 'imagem_gerada.png'!")

import os

# Configurar diretórios para modelos e cache
os.environ["HF_HOME"] = "D:/Rafael/huggingface"
os.environ["HUGGINGFACE_HUB_CACHE"] = "D:/Rafael/huggingface/cache"



import torch

torch.hub.set_dir("D:/Rafael/huggingface/torch")

import threading
from flask import Flask, render_template, request, jsonify, send_from_directory
from diffusers import StableDiffusionPipeline




# Verificar se há uma GPU disponível
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
dtype = torch.float16 if torch.cuda.is_available() else torch.float32

# Carregar o modelo Stable Diffusion uma única vez
pipeline = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4",
    torch_dtype=dtype
)
pipeline.safety_checker = None
pipeline.to(device)

# Criar diretório para salvar imagens geradas
output_folder = "static/generated"
os.makedirs(output_folder, exist_ok=True)

# Criar aplicação Flask
app = Flask(__name__)

# Variável global para armazenar status
status = {"progress": "Aguardando prompt...", "image": None}

# Função para gerar a imagem em uma thread separada
def generate_image(prompt):
    global status

    status["progress"] = "🔄 Gerando imagem..."
    with torch.autocast(device.type) if torch.cuda.is_available() else torch.no_grad():
        image = pipeline(prompt).images[0]

    image_path = os.path.join(output_folder, "generated_image.png")
    image.save(image_path)
    status["progress"] = "✅ Imagem gerada com sucesso!"
    status["image"] = "generated_image.png"

# Rota principal para exibir a página
@app.route("/")
def index():
    return render_template("index.html")

# Rota para iniciar a geração da imagem
@app.route("/generate", methods=["POST"])
def generate():
    global status

    prompt = request.form["prompt"]
    if not prompt:
        return jsonify({"error": "Por favor, insira um prompt."})

    status["progress"] = "🚀 Iniciando geração..."
    status["image"] = None

    # Iniciar a geração em uma thread separada para não travar a página
    threading.Thread(target=generate_image, args=(prompt,)).start()

    return jsonify({"message": "Geração iniciada!"})

# Rota para obter o status da geração
@app.route("/status")
def get_status():
    return jsonify(status)

# Rota para servir a imagem gerada
@app.route("/static/generated/<filename>")
def serve_image(filename):
    return send_from_directory(output_folder, filename)

# Iniciar servidor Flask
if __name__ == "__main__":
    app.run(debug=True)

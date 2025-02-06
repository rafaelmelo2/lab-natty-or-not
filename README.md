# IA de Criação de Imagens

```
# Ia de criação de imagens

## 📒 Descrição
Este projeto é uma aplicação web desenvolvida em Python utilizando o framework Flask e o modelo de difusão estável (Stable Diffusion) para gerar imagens a partir de descrições textuais fornecidas pelo usuário. A aplicação permite que os usuários insiram um prompt textual, que é então processado para gerar uma imagem correspondente, exibindo o progresso da geração em tempo real.

## 🤖 Tecnologias Utilizadas
Python: Linguagem de programação principal utilizada no desenvolvimento da aplicação.
Flask: Framework web utilizado para criar a interface e gerenciar as rotas da aplicação.
Stable Diffusion: Modelo de inteligência artificial utilizado para a geração de imagens a partir de descrições textuais.
Torch (PyTorch): Biblioteca de aprendizado profundo utilizada para carregar e executar o modelo de difusão estável.
Threading: Utilizado para processar a geração de imagens em uma thread separada, permitindo a atualização em tempo real do status na interface web.

## 🧐 Processo de Criação
Configuração do Ambiente:
    Definimos variáveis de ambiente para especificar os diretórios onde os modelos e caches serão armazenados, garantindo uma organização adequada dos arquivos.
Configuramos o diretório para o cache do Torch, otimizando o armazenamento dos modelos.

Inicialização do Modelo:
    Verificamos a disponibilidade de uma GPU para acelerar o processamento. Caso disponível, o dispositivo é configurado para utilizar CUDA; caso contrário, o processamento é realizado na CPU.
Carregamos o modelo Stable Diffusion pré-treinado, ajustando o tipo de dados conforme o dispositivo disponível e desativando o verificador de segurança para simplificar o processo.

Configuração do Flask:
    Criamos uma aplicação Flask e definimos rotas para a página principal, geração de imagens, verificação de status e fornecimento das imagens geradas.
Implementamos uma variável global para armazenar o status da geração da imagem, permitindo a atualização em tempo real na interface do usuário.

Geração de Imagens:
    Desenvolvemos uma função que processa o prompt fornecido pelo usuário em uma thread separada, utilizando o modelo Stable Diffusion para gerar a imagem correspondente.
A imagem gerada é salva em um diretório específico e o status é atualizado para refletir o progresso e a conclusão da geração.

Interface do Usuário:
    Criamos templates HTML para a interface do usuário, permitindo a inserção do prompt e exibindo o status da geração da imagem.
Implementamos atualizações em tempo real do status utilizando requisições assíncronas, melhorando a experiência do usuário.

## 🚀 Resultados
A aplicação resultante permite que os usuários gerem imagens realistas a partir de descrições textuais de forma eficiente. A interface web é intuitiva, fornecendo feedback em tempo real sobre o progresso da geração da imagem e exibindo o resultado final diretamente na página. A utilização de processamento paralelo através de threads garante que a interface permaneça responsiva durante o processo de geração.

## 💭 Reflexão (Opcional)
Desenvolver esta aplicação destacou o potencial das IAs generativas na criação de conteúdo visual a partir de descrições textuais. Um dos desafios enfrentados foi garantir que as imagens geradas fossem coerentes com os prompts fornecidos, especialmente ao desativar o verificador de segurança do modelo. Isso ressalta a importância de implementar mecanismos adicionais para garantir a segurança e a adequação do conteúdo gerado em aplicações futuras.
```

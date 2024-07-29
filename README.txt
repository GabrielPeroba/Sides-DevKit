#SIDES: Sistema Inteligente de Detecc ̧  ̃ao de Eventos Sonoros

Este projeto realiza a detecção de sons em tempo real utilizando um modelo de SVM (Support Vector Machine) para classificar diferentes tipos de sons.

## Índice

- [Instalação](#instalação)
- [Uso](#uso)
- [Contribuição](#contribuição)
- [Contato](#contato)

## Instalação


### Pré-requisitos

- Python 3.6 ou superior


Certifique-se de ter as seguintes bibliotecas instaladas:

- numpy==1.21.0
- librosa==0.8.1
- scikit-learn==0.24.2
- pyaudio==0.2.11
- pandas==1.3.0
- matplotlib==3.4.2
- seaborn==0.11.1
- pillow==8.3.1
- scipy==1.7.0
- tkinter (incluído na distribuição padrão do Python)
- IPython==7.25.0

### Passo a passo

1. Clone o repositório:
    ```bash
    git clone https://github.com/usuario/nome-do-projeto.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd nome-do-projeto
    ```
3. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Windows: venv\Scripts\activate
    ```
4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

Instruções para utilizar o programa.

### Preparação dos dados

1. Coloque os arquivos de áudio (.wav) no diretório especificado no código (por exemplo, `C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\SED\\sons\\`).

### Execução

1. Execute o script principal:
    ```bash
    python main.py
    ```
2. O programa iniciará a detecção de som em tempo real. Pressione `Ctrl+C` para parar a execução.

## Estrutura do Código

- `extract_files_and_labels(directory)`: Extrai arquivos de áudio e seus respectivos rótulos.
- `extract_features(audio, sample_rate=44100, window_size=0.024, hop_size=0.01)`: Extrai características (MFCCs) dos áudios.
- `train_model(features, labels)`: Treina um modelo de SVM com os recursos extraídos.
- `real_time_sound_detection(model, label_encoder)`: Realiza a detecção de som em tempo real usando o modelo treinado.
- `show_alert(label)`: Exibe um alerta visual ao detectar certos sons.


## Contato

Gabriel S. Peroba - [gabriel.peroba@poli.ufrj.br]

import os
import numpy as np
import librosa
from sklearn import datasets
from sklearn.model_selection import train_test_split 
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
import pyaudio
import time
import collections
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from IPython import display
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
from sklearn.preprocessing import LabelEncoder
import scipy.signal



# Configuracao do Pyaudio
CHUNK_SIZE = 1024
FORMAT = pyaudio.paFloat32  
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 1000
DETECTION_INTERVAL = 2


# Cache para guardar features pre-computadas
feature_cache = {}

# 1. Extracao de classes
def extract_files_and_labels(directory):
    files = [f for f in os.listdir(directory) if f.endswith('.wav')]
    labels = [f.split('_')[0] for f in files]

    # Contar o número de amostras por classe
    label_counts = collections.Counter(labels)
    print("Number of instances per class: ", label_counts)

    return files, labels

# 2. Extracao de features
def extract_features(audio, sample_rate=44100, window_size=0.05, hop_size=0.01):
    if isinstance(audio, str):  # Caminho do arquivo
        audio, sample_rate = librosa.load(audio, sr=sample_rate, res_type='kaiser_fast', dtype=np.float32)  #Especificidades

    # Apply windowing function
    n_samples = len(audio)
    window = scipy.signal.windows.hamming(int(window_size * sample_rate), sym=False)
    hop_length = int(hop_size * sample_rate)
    audio = audio[:len(window) + hop_length * (len(audio) - len(window)) // hop_length]
    frames = librosa.util.frame(audio, frame_length=len(window), hop_length=hop_length)

    # Calculate MFCCs
    mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40, n_fft=len(window), hop_length=hop_length, window=window)
    mfccs_processed = np.mean(mfccs.T, axis=0)

    return mfccs_processed

# 3. Treinamento do Modelo
def train_model(features, labels):

    # Converter features para array numpy
    features = np.array(features)
    labels = np.array(labels)

    #Label encoder
    label_encoder = LabelEncoder()
    labels_encoded = label_encoder.fit_transform(labels)

    X_train, X_test, y_train, y_test = train_test_split(features, labels_encoded, test_size=0.2, random_state=42)

    print("Number of samples in training set:", X_train.shape[0])
    print("Number of samples in testing set:", X_test.shape[0])

    # Definir o nome das classes e numero de classes
    target_names = label_encoder.classes_
    n_class = len(target_names)

    # Contar ocorrencias
    train_class_counts = {target_names[i]: np.sum(y_train == i) for i in range(n_class)}
    test_class_counts = {target_names[i]: np.sum(y_test == i) for i in range(n_class)}

    print("\nTraining set class counts:")
    for class_name, count in train_class_counts.items():
        print(f"{class_name}: {count}")
    
    print("\nTesting set class counts:")
    for class_name, count in test_class_counts.items():
        print(f"{class_name}: {count}")

    svm_classifier = SVC(kernel='linear')
    svm_classifier.fit(X_train, y_train)
    y_pred = svm_classifier.predict(X_test)

    
    y_pred_labels = label_encoder.inverse_transform(y_pred)
    y_test_labels = label_encoder.inverse_transform(y_test)

    # Classification Report
    classification_report_dict = classification_report(y_test_labels, y_pred_labels, output_dict=True, zero_division=1)
    classification_report_df = pd.DataFrame(classification_report_dict).transpose()

    print("Classification Report:")
    print(classification_report_df)

    report1 = classification_report(y_test, y_pred, target_names=target_names, digits=4, output_dict=True)
    df = pd.DataFrame(report1).T
    df.rename(columns={'precision': 'Precisão', 'recall': 'Revocação', 'f1-score': 'F1-Score'}, inplace=True)
    df_metrics = df.iloc[:n_class, :n_class].drop(columns=['support'])  # Remover coluna Support

    colors = ['#8fdba3', '#ffb073', '#c6b1fc', '#88ebfc', '#ff5c5c']
    sns.set_theme(style='whitegrid', font_scale=1.35)
    ax = df_metrics.plot(kind='bar', color=colors[:n_class])

    ax.yaxis.set_major_locator(MultipleLocator(0.1))
    ax.yaxis.set_minor_locator(MultipleLocator(0.05))
    ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.01),
              ncol=3, fancybox=True, shadow=False, fontsize=40)
    ax.set(ylim=(0, 1.0))
    ax.tick_params(axis='x', labelsize=16, labelrotation=0)
    ax.tick_params(axis='y', labelsize=40)

    # Atualizar eixo x
    ax.set_xticklabels(target_names, fontsize=40)

    plt.show()


    return svm_classifier



def real_time_sound_detection(model, label_encoder):
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK_SIZE)

    try:
        while True:
            start_time = time.time()  # Record the start time of the 1-second interval
            audio_buffer = []

            while time.time() - start_time < DETECTION_INTERVAL:
                audio_data = np.frombuffer(stream.read(CHUNK_SIZE), dtype=np.float32)
                audio_buffer.extend(audio_data)

            audio_features = extract_features(np.array(audio_buffer), sample_rate=RATE)
            prediction = model.predict([audio_features])

            # Convert the predicted label back to the original class name
            predicted_label = label_encoder.inverse_transform(prediction)[0]
            print(f"Detected Sound: {predicted_label}")

            with open("compartilhado.txt", "w") as file:
                file.write(f"Som detectado: {predicted_label}")

            # Check for a specific label and trigger the alert
            if predicted_label == "alarme":
                with open("compartilhado2.txt", "w") as file:
                    file.write("1")
                #show_alert(prediction[0])

                with open("compartilhado3.txt", "w") as file:
                    file.write("sirene")

            elif predicted_label == "explosao":
                with open("compartilhado2.txt", "w") as file:
                    file.write("1")
                #show_alert(prediction[0])

                with open("compartilhado3.txt", "w") as file:
                    file.write("explosao")

            elif predicted_label == "tempestade":
                with open("compartilhado2.txt", "w") as file:
                    file.write("1")
                #show_alert(prediction[0])

                with open("compartilhado3.txt", "w") as file:
                    file.write("tempestade")

            else:
                with open("compartilhado2.txt", "w") as file:
                    file.write("0")

    except KeyboardInterrupt:
        pass

    # Close the microphone stream
    stream.stop_stream()
    stream.close()
    p.terminate()


def show_alert(label):
    # Crear mensagem pop-up
    alert_window = tk.Toplevel()
    alert_window.title("Alert")

    # Carregar e mostrar imagem
    image = Image.open("Diretorio de imagens + aviso.png")  # Provide the path to your image file
    photo = ImageTk.PhotoImage(image)

    label_image = tk.Label(alert_window, image=photo)
    label_image.image = photo
    label_image.pack()

    # Mostrar mensaem de alarme
    label_message = tk.Label(alert_window, text="Alarm")
    label_message.pack()

    # Fechar janela de aviso
    close_button = tk.Button(alert_window, text="Close", command=alert_window.destroy)
    close_button.pack()

    alert_window.mainloop()


# Funcao para fechar janela de aviso
def close_alert():
    global alert_window
    if alert_window is not None:
        alert_window.destroy()
        alert_window = None

  
# 5. Funcao main
def main():
    directory = 'Diretorio de sons'
    files, labels = extract_files_and_labels(directory)
    features = [extract_features(os.path.join(directory, f)) for f in files]
    model = train_model(features, labels)
    label_encoder = LabelEncoder()
    label_encoder.fit(labels)
    print("Real-time sound detection started. Press Ctrl+C to exit.")
    real_time_sound_detection(model, label_encoder)

if __name__ == "__main__":
    main()

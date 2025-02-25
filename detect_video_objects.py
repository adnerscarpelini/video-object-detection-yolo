import cv2
import numpy as np
from ultralytics import YOLO

# Configurações
exibir_video = True  # True para mostrar o vídeo com detecções, False para apenas processar
exibir_apenas_pessoas = False  # True para detectar só pessoas, False para incluir carros

# Carregar modelo YOLO pré-treinado
model = YOLO("yolov8n.pt")

# Caminho do vídeo (use r"" para evitar problemas com barras invertidas)
video_path = r"C:\......"

# Abrir o vídeo
cap = cv2.VideoCapture(video_path)

# Obter FPS para converter frames em tempo
fps = cap.get(cv2.CAP_PROP_FPS)
frame_count = 0
horarios_detectados = set()  # Usamos um set para evitar salvar o mesmo segundo várias vezes

# Obter as dimensões do vídeo
ret, frame = cap.read()
if not ret:
    print("Erro ao ler o vídeo!")
    cap.release()
    exit()

frame_height, frame_width = frame.shape[:2]

# Processar o vídeo
cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Voltar para o primeiro frame
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # Sai do loop quando o vídeo termina

    frame_count += 1
    segundos = frame_count / fps  # Converte frame para segundos

    # Detectar objetos no frame
    results = model(frame)

    # Se não houver detecções, ignora o log de objetos não encontrados
    if not results:
        continue

    # Verificar se há alguma pessoa ou carro detectado
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])  # Classe do objeto detectado
            class_name = model.names[class_id]  # Nome da classe detectada

            # Filtrar se for apenas pessoas ou incluir carros
            if exibir_apenas_pessoas and class_id != 0:  
                continue  # Se ativado, ignora tudo que não for pessoa

            horarios_detectados.add(round(segundos))  # Armazena tempo em segundos inteiros
            print(f"{class_name} detectado em {segundos:.2f} segundos")

            # Se exibição estiver ativada, desenha a caixa no frame
            if exibir_video:
                x1, y1, x2, y2 = map(int, box.xyxy[0])  # Coordenadas da caixa
                cor = (0, 255, 0) if class_id == 0 else (255, 0, 0)  # Verde para pessoa, azul para carro
                cv2.rectangle(frame, (x1, y1), (x2, y2), cor, 2)
                cv2.putText(frame, class_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, cor, 2)

    # Exibir vídeo se ativado
    if exibir_video:
        cv2.imshow("Detecção de Objetos", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Pressione 'q' para sair
            break

cap.release()
cv2.destroyAllWindows()

# Salvar horários detectados em um arquivo
with open("horarios_detectados.txt", "w") as f:
    for t in sorted(horarios_detectados):
        f.write(f"{t} segundos\n")

print("✅ Análise concluída! Horários salvos em 'horarios_detectados.txt'.")

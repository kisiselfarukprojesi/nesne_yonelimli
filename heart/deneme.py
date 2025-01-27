import cv2
import numpy as np
import matplotlib.pyplot as plt
import csv

def process_video(video_path, mm_per_pixel, output_video_path, output_csv_path):
    cap = cv2.VideoCapture(video_path)

    # Video özelliklerini al ve çıktı videosu için ayar yap
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    out = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

    # CSV dosyasını yazmak için ayar yap
    with open(output_csv_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Frame", "Width (mm)", "Height (mm)"])  # Başlık satırı

        frame_count = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame_count += 1

            # Gri tonlamaya çevir ve kontrastı artır
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            enhanced_frame = cv2.equalizeHist(gray_frame)

            # Otsu ile eşikleme
            otsu_thresh_value, otsu_thresh_img = cv2.threshold(
                enhanced_frame, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
            )

            # Canny kenar tespiti
            threshold1 = otsu_thresh_value * 0.5  # Alt eşik değeri
            threshold2 = otsu_thresh_value       # Üst eşik değeri
            edges = cv2.Canny(enhanced_frame, threshold1, threshold2)

            # Kontur (kenar) bulma
            contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # En büyük konturu seç (kalp kapağı olduğunu varsayalım)
            if contours:
                largest_contour = max(contours, key=cv2.contourArea)
                
                # Konturun sınırlarını bul
                x, y, w, h = cv2.boundingRect(largest_contour)
                valve_width = w * mm_per_pixel  # Genişlik (mm)
                valve_height = h * mm_per_pixel  # Uzunluk (mm)

                # Sonuçları videoya yaz
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, f"Width: {valve_width:.2f} mm", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.putText(frame, f"Height: {valve_height:.2f} mm", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                # CSV dosyasına yaz
                writer.writerow([frame_count, valve_width, valve_height])

            # Çıktı videosuna yaz
            out.write(frame)

        print(f"İşleme tamamlandı. Video {output_video_path} ve veriler {output_csv_path} dosyasına kaydedildi.")

    cap.release()
    out.release()

# Video yolu ve pikselden mm'ye dönüşüm oranı
video_path = "/workspaces/nesne_yonelimli/heart/4_5800996453060974223.mp4"
output_video_path = "/workspaces/nesne_yonelimli/heart/output_video.mp4"
output_csv_path = "/workspaces/nesne_yonelimli/heart/output_data.csv"
mm_per_pixel = 0.1  # Pikselin mm'ye dönüşüm oranı

process_video(video_path, mm_per_pixel, output_video_path, output_csv_path)

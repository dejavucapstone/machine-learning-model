from PIL import Image
import os

# Path ke folder gambar
folder_path = r"C:\Users\arkaa\Downloads\kettlebells 2\kettlebells 2"
output_size = (640, 640)

# Loop untuk semua file dalam folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # Memeriksa apakah file adalah gambar
    if os.path.isfile(file_path) and filename.lower().endswith(('png', 'jpeg', 'jpg')):
        with Image.open(file_path) as img:
            # Konversi ke JPG jika bukan JPG
            if img.format != 'JPEG':
                img = img.convert('RGB')  # Mengonversi ke RGB untuk menyimpan sebagai JPG
                new_filename = os.path.splitext(filename)[0] + ".jpg"
                new_file_path = os.path.join(folder_path, new_filename)
                img = img.resize(output_size)
                img.save(new_file_path, 'JPEG')
                print(f"{filename} dikonversi dan diubah ukurannya menjadi {new_filename}")
            else:
                # Jika sudah JPG, hanya mengubah ukuran
                img = img.resize(output_size)
                img.save(file_path)
                print(f"{filename} diubah ukurannya")

print("Proses selesai.")

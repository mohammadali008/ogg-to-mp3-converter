import os
import subprocess

# Set your folder path here
source_folder = r"..."  # 🔁 replace with your actual folder path
output_folder = os.path.join(source_folder, "converted_mp3")
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(source_folder):
    if filename.lower().endswith(".ogg"):
        input_path = os.path.join(source_folder, filename)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".mp3")

        print(f"Converting {filename} → {os.path.basename(output_path)}...")
        subprocess.run([
            "ffmpeg",
            "-i", input_path,
            "-q:a", "0",  # High quality audio
            output_path
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print("✅ Done! All OGG files converted to MP3.")

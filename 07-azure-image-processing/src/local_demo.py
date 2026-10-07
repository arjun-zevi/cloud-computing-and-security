"""Runs the SAME threading + Pillow logic on a local folder (no Azure account needed).
Use it to test the logic before running app.py against Azure."""
import os
import threading

from PIL import Image

IN, OUT = "sample_images", "processed_images"
lock = threading.Lock()
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

# create 4 sample images if the folder is empty
if not os.listdir(IN):
    for i, colour in enumerate(["red", "green", "blue", "orange"], start=1):
        Image.new("RGB", (800, 600), colour).save(os.path.join(IN, f"image{i}.jpg"))


def process_image(name):
    img = Image.open(os.path.join(IN, name)).convert("RGB").resize((200, 200))
    img.save(os.path.join(OUT, "processed_" + name), format="JPEG")
    with lock:
        print(f"[{threading.current_thread().name}] processed {name} -> processed_{name}")


threads = [threading.Thread(target=process_image, args=(n,), name=f"Thread-{i}")
           for i, n in enumerate(sorted(os.listdir(IN)), start=1)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print("All images processed successfully")

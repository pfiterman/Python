
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox

from PIL import Image


def convert_png_to_webp():
    root.withdraw()

    input_path = filedialog.askopenfilename(
        parent=root,
        title="Select transparent PNG",
        filetypes=[
            ("PNG images", "*.png"),
            ("All files", "*.*")
        ]
    )

    if not input_path:
        return

    try:
        with Image.open(input_path) as image:
            image.load()
            image = image.convert("RGBA")

            original_name = Path(input_path).stem
            suggested_name = f"{original_name}.webp"

            output_path = filedialog.asksaveasfilename(
                parent=root,
                title="Save WebP image",
                initialfile=suggested_name,
                defaultextension=".webp",
                filetypes=[("WebP images", "*.webp")]
            )

            if not output_path:
                return

            output_path = str(Path(output_path).with_suffix(".webp"))

            image.save(
                output_path,
                format="WEBP",
                quality=90,
                method=6
            )

        messagebox.showinfo(
            "Success",
            f"WebP image saved successfully:\n\n{output_path}",
            parent=root
        )

    except Exception as error:
        messagebox.showerror(
            "Conversion error",
            f"Could not convert image:\n\n{error}",
            parent=root
        )


root = tk.Tk()
root.withdraw()

convert_png_to_webp()

root.destroy()

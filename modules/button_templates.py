import json
from pathlib import Path
import customtkinter as ctk

class ButtonTemplate:
    FORMATS = {}
    SIZES = {}
    PRESETS = {}

    @classmethod
    def load_from_json(cls, filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            raise RuntimeError(f"Erro ao carregar template JSON: {e}")

        cls.FORMATS = data.get("FORMATS", {})
        cls.PRESETS = data.get("PRESETS", {})

        def make_font_lambda(size, weight):
            return lambda: ctk.CTkFont(size=size, weight=weight)

        sizes = data.get("SIZES", {})
        for key, val in sizes.items():
            font_data = val.get("font", {})
            size = font_data.get("size", 14)
            weight = font_data.get("weight", "normal")
            val["font"] = make_font_lambda(size, weight)
            val.setdefault("text_color", ["white", "white"])
            val.setdefault("text_color_disabled", ["#A9A9A9", "#5A5A5A"])

        cls.SIZES = sizes

# Carregue automaticamente quando importar
config_path = Path(__file__).parent / "../themes/default.json"
ButtonTemplate.load_from_json(config_path)

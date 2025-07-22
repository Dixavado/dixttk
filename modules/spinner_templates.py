# spinner_templates.py
import json
from pathlib import Path

class SpinnerTemplate:
    SPINNERS = {}

    @classmethod
    def load_from_json(cls, filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                cls.SPINNERS = json.load(f)
        except Exception as e:
            raise RuntimeError(f"Erro ao carregar spinner JSON: {e}")

    @classmethod
    def get(cls, name, fallback=None):
        return cls.SPINNERS.get(name, fallback or ["|", "/", "-", "\\"])


# Carrega automaticamente ao importar
default_path = Path(__file__).parent / "../themes/spinner.json"
SpinnerTemplate.load_from_json(default_path)

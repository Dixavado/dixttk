import customtkinter as ctk
from .modules.button_templates import ButtonTemplate
from .modules.tooltip import Tooltip
from .modules.spinner_templates import SpinnerTemplate
import tkinter as tk
from typing import Optional, Callable, Dict, Any, List


class Spinner(ctk.CTkFrame):
    DEFAULT_SYMBOLS: List[str] = ["|", "/", "-", "\\"]
    DEFAULT_SPEED: int = 100
    DEFAULT_FG_COLOR: str = "#FFFFFF"
    
    def __init__(
        self,
        master: tk.Widget,
        size: int = 20,
        speed: Optional[int] = None,
        symbols: Optional[List[str]] = None,
        fg_color: Optional[str] = None,
        bg_color: Optional[str] = None,
        **kwargs
    ):
        super().__init__(master, width=size, height=size, **kwargs)

        self.speed = speed or self.DEFAULT_SPEED
        self.symbols = symbols or self.DEFAULT_SYMBOLS
        self._index = 0
        self._running = False
        self._after_id: Optional[str] = None

        font_size = max(8, size - 4)
        label_bg = bg_color or master.cget("bg")
        label_fg = fg_color or self.DEFAULT_FG_COLOR

        self.label = ctk.CTkLabel(
            self,
            text=self.symbols[0],
            font=ctk.CTkFont(size=font_size, weight="bold"),
            text_color=label_fg,
            fg_color=label_bg
        )
        self.label.pack(expand=True, fill="both")

    def start(self) -> None:
        if self._running:
            return
        self._running = True
        self._animate()

    def stop(self) -> None:
        if not self._running:
            return
        self._running = False
        if self._after_id is not None:
            self.after_cancel(self._after_id)
            self._after_id = None

    def is_running(self) -> bool:
        return self._running

    def _animate(self) -> None:
        if not self._running:
            return
        self.label.configure(text=self.symbols[self._index])
        self._index = (self._index + 1) % len(self.symbols)
        self._after_id = self.after(self.speed, self._animate)


class CustomButton(ctk.CTkButton):
    DEFAULT_TEXT_COLOR = ("white", "white")
    DEFAULT_TEXT_COLOR_DISABLED = ("#A9A9A9", "#5A5A5A")
    DEFAULT_CURSOR = "hand2"

    def __init__(
        self,
        master: tk.Widget,
        tooltip: Optional[str] = None,
        show_spinner: bool = False,
        spinner_name: str = "classic",
        **kwargs
    ):
        kwargs.setdefault("text_color", self.DEFAULT_TEXT_COLOR)
        kwargs.setdefault("text_color_disabled", self.DEFAULT_TEXT_COLOR_DISABLED)
        kwargs.setdefault("state", "normal")
        kwargs.setdefault("cursor", self.DEFAULT_CURSOR)

        super().__init__(master, **kwargs)

        self._spinner_symbols = SpinnerTemplate.get(spinner_name) or SpinnerTemplate.get("classic")
        self._spinner: Optional[Spinner] = None
        self._spinner_visible: bool = False

        if show_spinner:
            self._create_spinner()

        self._tooltip = Tooltip(self, tooltip) if tooltip else None
        self.bind("<Destroy>", self._on_destroy)

    def _create_spinner(self) -> None:
        if self._spinner is None:
            # Corrigindo cor de fundo: tenta pegar fg_color do botão, senão usa preto
            bg_color = self.cget("fg_color") or "#000000"
            self._spinner = Spinner(self, size=32, symbols=self._spinner_symbols, bg_color=bg_color)
            self._spinner.place(relx=1.0, rely=0.5, anchor="e", x=-8)
            self._spinner.start()
            self._spinner_visible = True

    def show_spinner(self) -> None:
        if not self._spinner_visible:
            self._create_spinner()

    def hide_spinner(self) -> None:
        if self._spinner and self._spinner_visible:
            self._spinner.stop()
            self._spinner.place_forget()
            self._spinner_visible = False

    def toggle_spinner(self) -> None:
        if self._spinner_visible:
            self.hide_spinner()
        else:
            self.show_spinner()

    def _on_destroy(self, event: tk.Event) -> None:
        if self._spinner:
            self._spinner.stop()


class ButtonFactory:
    def create(
        self,
        master: tk.Widget,
        text: str = "",
        command: Optional[Callable] = None,
        shape: str = "rounded",
        size: str = "default",
        preset: Optional[str] = None,
        custom_size: Optional[Dict[str, Any]] = None,
        image: Optional[tk.PhotoImage] = None,
        show_text_with_image: bool = True,
        image_side: str = "left",
        tooltip: Optional[str] = None,
        show_spinner: bool = False,
        spinner_name: str = "classic",
        text_color: Optional[Any] = None,
        text_color_disabled: Optional[Any] = None,
        fg_color: Optional[Any] = None,
        hover_color: Optional[Any] = None,
        border_color: Optional[Any] = None,
        border_width: Optional[int] = None,
    ) -> CustomButton:
        config: Dict[str, Any] = {}

        self._apply_size(size, config)
        self._apply_shape(shape, config)

        if preset:
            self._apply_preset(preset, config)

        self._apply_colors(
            config,
            text_color=text_color,
            text_color_disabled=text_color_disabled,
            fg_color=fg_color,
            hover_color=hover_color,
            border_color=border_color,
            border_width=border_width,
        )

        if custom_size:
            self._apply_custom_size(custom_size, config)

        self._apply_font(config)

        self._adjust_for_shape(shape, config)

        self._apply_text_and_image(config, text, image, show_text_with_image, image_side)

        return CustomButton(
            master,
            command=command,
            tooltip=tooltip,
            show_spinner=show_spinner,
            spinner_name=spinner_name,
            **config
        )

    def _apply_size(self, size: str, config: Dict[str, Any]) -> None:
        size_tpl = ButtonTemplate.SIZES.get(size, {})
        config.update(size_tpl)

    def _apply_shape(self, shape: str, config: Dict[str, Any]) -> None:
        format_tpl = ButtonTemplate.FORMATS.get(shape, {})
        config.update(format_tpl)

    def _apply_preset(self, preset: str, config: Dict[str, Any]) -> None:
        preset_tpl = ButtonTemplate.PRESETS.get(preset, {})
        config.update(preset_tpl)

    def _apply_colors(
        self,
        config: Dict[str, Any],
        *,
        text_color: Optional[Any],
        text_color_disabled: Optional[Any],
        fg_color: Optional[Any],
        hover_color: Optional[Any],
        border_color: Optional[Any],
        border_width: Optional[int]
    ) -> None:
        color_params = {
            "text_color": text_color,
            "text_color_disabled": text_color_disabled,
            "fg_color": fg_color,
            "hover_color": hover_color,
            "border_color": border_color,
            "border_width": border_width,
        }
        for key, val in color_params.items():
            if val is not None:
                config[key] = val

    def _apply_custom_size(self, custom_size: Dict[str, Any], config: Dict[str, Any]) -> None:
        for key in ["width", "height", "font"]:
            if key in custom_size:
                config[key] = custom_size[key]

    def _apply_font(self, config: Dict[str, Any]) -> None:
        font = config.get("font")
        if callable(font):
            config["font"] = font()

    def _adjust_for_shape(self, shape: str, config: Dict[str, Any]) -> None:
        if shape == "circle":
            altura = config.get("height", 6)
            config["corner_radius"] = altura // 2

    def _apply_text_and_image(
        self,
        config: Dict[str, Any],
        text: str,
        image: Optional[tk.PhotoImage],
        show_text_with_image: bool,
        image_side: str
    ) -> None:
        if image:
            config["image"] = image
            config["compound"] = image_side
            config["text"] = text if show_text_with_image else ""
        else:
            config["text"] = text

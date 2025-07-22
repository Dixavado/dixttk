
# Dix Custom Theme - CustomTkinter Theme Factory

Este módulo fornece uma fábrica de  personaliçoes de Themas para `customtkinter`.
Por hora, lida com botões customizados com suporte a tooltips, spinner animado e diversas opções de estilo.

---

## Conteúdo

- `Tooltip`: Classe para exibir uma tooltip simples ao passar o mouse sobre um widget.
- `Spinner`: Animação de texto simples que pode ser usada para indicar carregamento.
- `CustomButton`: Botão customizado que pode mostrar tooltip e spinner.
- `ButtonFactory`: Fábrica para criar botões configurados a partir de templates predefinidos.

---

## Requisitos

- Python 3.7+
- [customtkinter](https://github.com/TomSchimansky/CustomTkinter)
- Pillow (para manipulação de imagens, caso use ícones)

---

## Uso

### Importação

```python
import customtkinter as ctk
from dixttk import ButtonFactory
```

### Criando um botão customizado

```python
factory = ButtonFactory()

btn = factory.create(
    master=frame,
    text="Clique Aqui",
    shape="rounded",       # Formatos: 'rounded', 'default', 'squared', 'circle'
    size="default",        # Tamanhos: 'small', 'default', 'big'
    tooltip="Este é um botão!",
    show_spinner=True      # Mostra o spinner animado no botão
)
btn.pack(padx=10, pady=10)
```

### Parâmetros do método `create`

| Parâmetro           | Tipo      | Descrição                                                                                     |
|---------------------|-----------|-----------------------------------------------------------------------------------------------|
| `master`            | widget    | Widget pai onde o botão será inserido                                                         |
| `text`              | str       | Texto do botão                                                                                |
| `command`           | callable  | Função chamada ao clicar no botão                                                             |
| `shape`             | str       | Formato do botão (ex: `'rounded'`, `'default'`, `'squared'`, `'circle'`)                       |
| `size`              | str       | Tamanho do botão (`'small'`, `'default'`, `'big'`)                                            |
| `preset`            | str       | Template de estilo predefinido (opcional, depende do seu `ButtonTemplate`)                     |
| `custom_size`        | dict      | Customização manual do tamanho/font (ex: `{"width": 100, "height": 30, "font": ctk.CTkFont()}`) |
| `image`             | ctk.CTkImage | Ícone/imagem do botão (opcional)                                                            |
| `show_text_with_image` | bool    | Mostra texto junto com o ícone                                                                |
| `image_side`        | str       | Posição do ícone (`'left'`, `'right'`, `'top'`, `'bottom'`)                                   |
| `tooltip`           | str       | Texto da tooltip que aparece ao passar o mouse                                                |
| `show_spinner`      | bool      | Mostra o spinner animado no botão                                                            |
| `text_color`        | tuple     | Cor do texto (ex: `("white", "white")`)                                                      |
| `text_color_disabled` | tuple   | Cor do texto quando desabilitado                                                             |
| `fg_color`          | str       | Cor de fundo do botão                                                                         |
| `hover_color`       | str       | Cor do botão ao passar o mouse                                                                |
| `border_color`      | str       | Cor da borda                                                                                  |
| `border_width`      | int       | Largura da borda                                                                             |

---

## Classes detalhadas

### Tooltip

Exibe um tooltip flutuante simples para widgets `tkinter` ou `customtkinter`.

- Delay configurável (padrão 500ms).
- Posicionamento automático ao lado do cursor.

### Spinner

Widget que exibe um símbolo animado para indicar processamento ou carregamento.

- Ícones usados: ⏳, ⌛, ⏰
- Velocidade de animação configurável.

### CustomButton

Extensão de `ctk.CTkButton` com:

- Tooltip integrado
- Spinner integrado (opcional)
- Estilização via `ButtonFactory`

### ButtonFactory

Fábrica que cria instâncias de `CustomButton` aplicando templates de tamanho, formato e presets (definidos em `ButtonTemplate`).

---

## Exemplos rápidos

```python
factory = ButtonFactory()

# Botão padrão arredondado com tooltip
btn1 = factory.create(frame, text="Salvar", shape="rounded", tooltip="Clique para salvar")
btn1.pack()

# Botão circular só com ícone e spinner
icon = ctk.CTkImage(...)  # sua imagem aqui
btn2 = factory.create(frame, image=icon, shape="circle", show_text_with_image=False, show_spinner=True)
btn2.pack()
```

---

## Nota

- `ButtonTemplate` deve estar implementado no seu projeto para fornecer as configurações de tamanhos, formatos e presets.
- Customize os templates para alterar estilos padrão.

---

## Licença

MIT License

---

## Autor

Diixavado

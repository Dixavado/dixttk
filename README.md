
# Dix Custom Theme - CustomTkinter Theme Factory


# CustomTkinter Button & Spinner Components

Este projeto oferece componentes personalizados baseados em [customtkinter](https://github.com/TomSchimansky/CustomTkinter), facilitando a criação de botões com estilos avançados, tooltips, spinners animados e configuração via templates JSON.

---

## Sumário

- [Funcionalidades](#funcionalidades)  
- [Instalação](#instalação)  
- [Componentes Principais](#componentes-principais)  
- [Exemplos de Uso](#exemplos-de-uso)  
- [Configuração e Personalização](#configuração-e-personalização)  
- [Estrutura dos Arquivos](#estrutura-dos-arquivos)  
- [Licença](#licença)  

---

## Funcionalidades

- **Spinner animado**: Símbolos giratórios configuráveis para indicar processos em andamento.  
- **Botão customizado**: Botões com suporte a tooltips, spinners integrados, imagens e texto, cores customizáveis e presets de estilo.  
- **Fábrica de botões**: Criação fácil e padronizada de botões via `ButtonFactory`, com presets e ajustes dinâmicos.  
- **Templates JSON**: Configurações externas para estilos de botões e spinners, facilitando manutenção e temas.  
- **Tooltip simples**: Mostra dicas informativas ao passar o mouse sobre componentes.  

---

## Instalação

1. Instale o **customtkinter** (caso ainda não tenha):
    ```bash
    pip install customtkinter
    ```

2. Certifique-se que seu ambiente tem suporte a tkinter (geralmente já vem com Python).

3. Coloque o projeto na sua estrutura ou importe os módulos conforme necessário.

---

## Componentes Principais

### Spinner

Classe `Spinner(ctk.CTkFrame)` que exibe um símbolo animado (ex: `|`, `/`, `-`, `\`) de forma cíclica para indicar carregamento.

**Parâmetros principais:**

- `size`: tamanho do spinner (pixels)
- `speed`: velocidade da animação (ms entre frames)
- `symbols`: lista de símbolos para animação
- `fg_color`, `bg_color`: cores do texto e fundo

**Exemplo:**

```python
spinner = Spinner(master, size=30, speed=80)
spinner.pack()
spinner.start()
```

---

### CustomButton

Estende o `CTkButton` para incluir:

- Spinner embutido ativável
- Tooltip configurável
- Controle de estados e estilos customizados

**Parâmetros adicionais:**

- `tooltip`: texto do tooltip (opcional)
- `show_spinner`: exibir spinner na criação (bool)
- `spinner_name`: nome do template de spinner para usar

**Exemplo:**

```python
btn = CustomButton(
    master,
    text="Processar",
    tooltip="Clique para iniciar o processamento",
    show_spinner=True,
    spinner_name="dots"
)
btn.pack()
```

---

### ButtonFactory

Fábrica que cria botões usando presets, formatos, tamanhos e cores configurados.

**Método principal:**

```python
btn = ButtonFactory().create(
    master,
    text="Enviar",
    command=my_command,
    shape="rounded",
    size="large",
    preset="primary",
    tooltip="Enviar dados",
    show_spinner=False
)
```

Parâmetros adicionais permitem passar imagens, cores customizadas, largura, altura, bordas etc.

---

## Exemplos Detalhados

### Exemplo 1 — Botão simples com tooltip

```python
import customtkinter as ctk

root = ctk.CTk()
button = CustomButton(root, text="Salvar", tooltip="Salva as alterações")
button.pack(padx=20, pady=20)
root.mainloop()
```

---

### Exemplo 2 — Botão com spinner dinâmico

```python
def on_click():
    btn.show_spinner()
    # Simula tarefa
    root.after(3000, btn.hide_spinner)

root = ctk.CTk()
btn = CustomButton(root, text="Carregar", show_spinner=False, tooltip="Clique para carregar")
btn.configure(command=on_click)
btn.pack(padx=20, pady=20)
root.mainloop()
```

---

### Exemplo 3 — Botão circular e grande com preset

```python
factory = ButtonFactory()
btn = factory.create(
    root,
    text="OK",
    shape="circle",
    size="large",
    preset="primary",
    show_spinner=True
)
btn.pack(padx=20, pady=20)
```

---

## Configuração e Personalização

### Templates JSON

- **default.json** (botões) define formatos, tamanhos e presets:

```json
{
  "FORMATS": {
    "rounded": { "corner_radius": 12 },
    "circle": { "corner_radius": 20 }
  },
  "SIZES": {
    "default": { "width": 100, "height": 40, "font": {"size": 14, "weight": "bold"} },
    "large": { "width": 140, "height": 50, "font": {"size": 18, "weight": "bold"} }
  },
  "PRESETS": {
    "primary": {
      "fg_color": "#1E90FF",
      "hover_color": "#1C86EE",
      "text_color": ["white", "white"]
    }
  }
}
```

- **spinner.json** define os símbolos para spinners, por exemplo:

```json
{
  "classic": ["|", "/", "-", "\"],
  "dots": [".  ", ".. ", "...", " ..", "  .", "   "]
}
```

---

### Alterando estilos

Você pode alterar cores, tamanhos e formatos em seus arquivos JSON para ajustar o visual de todos os botões/spinners instantaneamente.


---

## Contribuição

Sinta-se livre para abrir issues ou pull requests para melhorias, novos presets ou correções.

---

## Licença

Este projeto está licenciado sob a MIT License.

---

## Autor

Diixavado

from tkinter import ttk

def configure_material_style_for_btn() -> str:
    """
    仿 Material 风格的按钮
    :return: Material.TButton
    """
    style = ttk.Style()
    style.theme_use("clam")  # 允许修改背景色
    style.configure("Material.TButton",
                    foreground="white",
                    background="#2196F3",  # Material Blue 500
                    borderwidth=0,
                    focuscolor="none",
                    padding=(10, 5))
    style.map("Material.TButton",
              background=[("active", "#1976D2")])  # hover 时颜色加深
    return "Material.TButton"

def configure_fluent__style_for_btn() -> str:
    """
    仿 Fluent风格的按钮
    :return: Fluent.TButton
    """
    style = ttk.Style()
    style.theme_use("clam")  # 允许修改背景色

    # 定义 Fluent 按钮样式
    style.configure("Fluent.TButton",
                    font=("Segoe UI", 11),
                    foreground="#FFFFFF",
                    background="#0078D4",  # Fluent 蓝色
                    borderwidth=0,
                    focuscolor="none",
                    padding=(5, 5),
                    relief="flat")
    style.map("Fluent.TButton",
              background=[
                  ("active", "#106EBE"),
              ],
              foreground=[("active", "#FFFFFF")])
    return "Fluent.TButton"
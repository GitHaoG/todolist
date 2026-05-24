import ui

class ToDoApp:
    def __init__(self):
        pass

    def use_tk_window(self):
        pass

    def use_qt_window(self):
        pass

def main() -> None:
    # ui.MaterialStyles.configure_material_style_for_btn()
    root_window = ui.Tk_MainWindow()
    root_window.mainloop()
    pass

if __name__ == "__main__":
    main()
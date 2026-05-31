from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QApplication
from PySide6.QtCore import Qt

class Qt_MainWindow(QWidget):
    SNAP_THRESHOLD = 30  # 吸附触发距离（像素）

    def __init__(self,
                 parent=None,
                 enable_snap=True):
        super().__init__(parent)

        self.setWindowTitle("ToDoList")
        self.setMinimumSize(300, 600)
        self.resize(300, 600)

        self._enable_snap = enable_snap
        self._is_snapping = False

        self._place_right_center()

        # 拿到焦点后 下面这个窗体可以变大一些，就不要手动可以调了
        return

    def _place_right_center(self):
        """将窗口放置在屏幕右侧、垂直居中"""
        screen = QApplication.primaryScreen()
        screen_rect = screen.availableGeometry()
        x = screen_rect.width() - self.width()
        y = (screen_rect.height() - self.height()) // 2
        self.move(x, y)

    def moveEvent(self, event):
        if self._enable_snap and not self._is_snapping:
            self._snap_to_edges()
        super().moveEvent(event)

    def _snap_to_edges(self):
        screen = QApplication.primaryScreen().availableGeometry()
        current_pos = self.pos()
        new_x = current_pos.x()
        new_y = current_pos.y()

        # 左边缘吸附
        if current_pos.x() < self.SNAP_THRESHOLD:
            new_x = 0
            new_y = (screen.height() - self.height()) // 2
        # 右边缘吸附（elif 保证不会同时触发）
        elif (screen.width() - current_pos.x() - self.width()) < self.SNAP_THRESHOLD:
            new_x = screen.width() - self.width()
            new_y = (screen.height() - self.height()) // 2

        if new_x != current_pos.x() or new_y != current_pos.y():
            self._is_snapping = True
            self.move(new_x, new_y)
            self._is_snapping = False

import sys
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QVBoxLayout, QLabel, QApplication, \
    QPushButton, QMainWindow, QMessageBox, QComboBox, QTabWidget


class EditTarea1(QMainWindow):
    def __init__(self):
        super(EditTarea1, self).__init__()

        self.setWindowTitle("ELIMINAR TAREAS")
        self.setWindowIcon(QtGui.QIcon("imagenes/icono1.png"))

        self.ancho = 600
        self.alto = 500
        self.resize(self.ancho, self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.set_background_image("imagenes/fnd2e.png")

        self.letra1 = QtGui.QFont()
        self.letra1.setFamily("Andale mono")
        self.letra1.setPointSize(10)

        self.letra2 = QtGui.QFont()
        self.letra2.setFamily("Andale mono")
        self.letra2.setPointSize(12)

        self.tab_widget = QTabWidget(self)
        self.tab_widget.setGeometry(20, 20, self.ancho - 40, self.alto - 40)

        # Crear pestañas para cada tipo de tarea
        self.crear_tab_tarea("Chef", "chef")
        self.crear_tab_tarea("Jardinero", "jardinero")
        self.crear_tab_tarea("Enfermero", "enfermero")

    def crear_tab_tarea(self, nombre_tab, tipo_tarea):
        tab = QWidget()

        letra_tab = QtGui.QFont()
        letra_tab.setFamily("Arial")
        letra_tab.setPointSize(12)

        tab_layout = QVBoxLayout()

        login = QLabel(tab)
        login.setText(f"Seleccionar Tarea ({nombre_tab}):")
        login.setFont(letra_tab)
        login.setStyleSheet("background-color: #White; color: #0000FF; padding: 10px;")
        login.setFixedWidth(300)
        tab_layout.addWidget(login)

        # Lista desplegable para seleccionar la tarea
        tareasCombo = QComboBox(tab)
        tareasCombo.setFixedWidth(300)
        tab_layout.addWidget(tareasCombo)

        # Botón para eliminar la tarea seleccionada
        eliminarTareaBtn = QPushButton(tab)
        eliminarTareaBtn.setText(f"Eliminar Tarea ({nombre_tab})")
        eliminarTareaBtn.setFixedWidth(300)
        eliminarTareaBtn.setStyleSheet("background-color: #50D4FA; color: #000000  ; padding: 10px;")
        eliminarTareaBtn.clicked.connect(lambda: self.eliminar_tarea(tipo_tarea, tareasCombo))
        tab_layout.addWidget(eliminarTareaBtn)

        tab.setLayout(tab_layout)
        self.tab_widget.addTab(tab, nombre_tab)

        # Llenar la lista desplegable con las tareas existentes
        self.llenar_lista_tareas(tipo_tarea, tareasCombo)

    def llenar_lista_tareas(self, tipo_tarea, combo_box):
        # Lógica para leer las tareas desde el archivo y agregarlas a la lista desplegable
        nombre_archivo = f"{tipo_tarea}_tareas.txt"
        with open(nombre_archivo, "r") as file:
            for linea in file:
                tarea_info = linea.strip()  # Asumiendo que cada línea representa una tarea con un identificador único
                combo_box.addItem(tarea_info)

    def eliminar_tarea(self, tipo_tarea, combo_box):
        tarea_seleccionada = combo_box.currentText()

        # Obtiene el identificador único de la tarea seleccionada
        tarea_id, _ = tarea_seleccionada.split(": ", 1)

        # Implementa aquí la lógica para eliminar la tarea seleccionada del archivo correspondiente
        nombre_archivo = f"{tipo_tarea}_tareas.txt"
        try:
            with open(nombre_archivo, "r") as file:
                lineas = file.readlines()
            with open(nombre_archivo, "w") as file:
                for linea in lineas:
                    if tarea_id not in linea.split(":")[0].strip():
                        file.write(linea)
            QMessageBox.information(self, "Éxito", f"Tarea '{tarea_seleccionada}' eliminada con éxito.")
            combo_box.clear()
            self.llenar_lista_tareas(tipo_tarea, combo_box)  # Actualiza la lista después de la eliminación
        except Exception as e:
            print(f"Error al eliminar la tarea: {str(e)}")
            QMessageBox.warning(self, "Error", f"Error al eliminar la tarea: {str(e)}")

    def set_background_image(self, image_path):
        background_image = QPixmap(image_path).scaled(self.ancho, self.alto)
        background_label = QLabel(self)
        background_label.setPixmap(background_image)
        background_label.setGeometry(0, 0, self.ancho, self.alto)
        background_label.lower()


if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)

    ventana_eliminar_tarea = EditTarea1()
    ventana_eliminar_tarea.show()

    sys.exit(aplicacion.exec_())

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QTextEdit, QMessageBox, QListWidget, QComboBox

class ReportarTarea(QMainWindow):
    def __init__(self):
        super(ReportarTarea, self).__init__()

        self.setWindowTitle("Reportar Tarea")
        self.setWindowIcon(QtGui.QIcon("imagenes/icono1.png"))
        self.ancho = 800
        self.alto = 600
        self.resize(self.ancho, self.alto)

        pantalla = self.frameGeometry()
        centro = QApplication.desktop().screenGeometry().center()
        pantalla.moveCenter(centro)
        self.move(pantalla.topLeft())

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)
        self.set_background_image("imagenes/fnd2e.png")

        fuente = QFont()
        fuente.setFamily("Arial")
        fuente.setPointSize(18)

        fuente2 = QFont()
        fuente2.setFamily("Arial")
        fuente2.setPointSize(10)

        letrero1 = QLabel(self)
        letrero1.setText("Reportar Tarea")
        letrero1.setFont(fuente)
        letrero1.setStyleSheet("color: #09B4AC; padding: 30px;")
        letrero1.setFixedWidth(300)
        letrero1.move(300, 40)

        self.workerTypeComboBox = QComboBox(self)
        self.workerTypeComboBox.addItems(["Chef", "Jardinero", "Enfermero"])
        self.workerTypeComboBox.setGeometry(100, 70, 150, 30)
        self.workerTypeComboBox.currentIndexChanged.connect(self.update_task_list)

        self.reporteTarea = QTextEdit(self)
        self.reporteTarea.setPlaceholderText("Escribe aquí tu reporte de la tarea...")
        self.reporteTarea.setGeometry(300, 100, 300, 300)

        self.enviarReporte = QPushButton(self)
        self.enviarReporte.setText("Enviar Reporte")
        self.enviarReporte.setFixedWidth(200)
        self.enviarReporte.setFixedHeight(40)
        self.enviarReporte.setFont(fuente2)
        self.enviarReporte.setStyleSheet("background-color: #50D4FA; color: #000000  ; padding: 30px;")
        self.enviarReporte.move(325, 450)
        self.enviarReporte.clicked.connect(self.enviar_reporte)

        self.volverMenu = QPushButton(self)
        self.volverMenu.setText("Volver al Menú")
        self.volverMenu.setFixedWidth(200)
        self.volverMenu.setFixedHeight(40)
        self.volverMenu.setFont(fuente2)
        self.volverMenu.setStyleSheet("background-color: #50D4FA; color: #000000  ; padding: 30px;")
        self.volverMenu.move(325, 521)
        self.volverMenu.clicked.connect(self.cerrar_ventana)

        self.chef_tasks = self.load_tasks_from_file("chef_tareas.txt")
        self.jardinero_tasks = self.load_tasks_from_file("jardinero_tareas.txt")
        self.enfermero_tasks = self.load_tasks_from_file("enfermero_tareas.txt")

        self.task_list_widget = QListWidget(self)
        self.update_task_list()
        self.task_list_widget.setGeometry(100, 100, 200, 300)

    def load_tasks_from_file(self, filename):
        tasks = []
        try:
            with open(filename, 'r') as file:
                tasks = file.readlines()
            tasks = [task.strip() for task in tasks]
        except FileNotFoundError:
            pass
        return tasks

    def update_task_list(self):
        self.task_list_widget.clear()
        selected_worker_type = self.workerTypeComboBox.currentText()

        if selected_worker_type == "Chef":
            self.task_list_widget.addItems(self.chef_tasks)
        elif selected_worker_type == "Jardinero":
            self.task_list_widget.addItems(self.jardinero_tasks)
        elif selected_worker_type == "Enfermero":
            self.task_list_widget.addItems(self.enfermero_tasks)

    def enviar_reporte(self):
        selected_worker_type = self.workerTypeComboBox.currentText()
        selected_task = self.task_list_widget.currentItem().text()
        reporte = self.reporteTarea.toPlainText()

        if reporte:
            numero_reportes = self.obtener_numero_reportes()
            report_content = f"Reporte{numero_reportes + 1} - Tarea: {selected_task}\nReporte: {reporte}\n"

            with open("reportes_tareas.txt", 'a') as report_file:
                report_file.write(report_content + "\n\n")

            QMessageBox.information(self, "Reporte Enviado", "El reporte se ha enviado con éxito.")
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Por favor, escribe un reporte antes de enviarlo.")

    def obtener_numero_reportes(self):
        try:
            with open("reportes_tareas.txt", 'r') as reportes_file:
                reportes = reportes_file.readlines()
            return len(reportes) // 3
        except FileNotFoundError:
            return 0

    def cerrar_ventana(self):
        self.close()

    def set_background_image(self, image_path):
        background_image = QPixmap(image_path).scaled(self.ancho, self.alto)
        background_label = QLabel(self)
        background_label.setPixmap(background_image)
        background_label.setGeometry(0, 0, self.ancho, self.alto)
        background_label.lower()

if __name__ == '__main__':
    aplicacion1 = QApplication(sys.argv)
    v1 = ReportarTarea()
    v1.show()
    sys.exit(aplicacion1.exec_())

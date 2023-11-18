import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import (
    QWidget,
    QDesktopWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QApplication,
    QPushButton,
    QMainWindow,
    QMessageBox,
    QComboBox,
)

class addtarea11(QMainWindow):
    def __init__(self):
        super(addtarea11, self).__init__()

        self.setWindowTitle("Agregar Tarea")

        # Estableciendo las propiedades de ancho y alto
        self.ancho = 500
        self.alto = 500

        # Establecer el tamaño de la ventana:
        self.resize(self.ancho, self.alto)

        # Estas líneas hacen que la ventana se vea en el centro:
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # Para que la ventana no se pueda cambiar de tamaño
        # Se fija el ancho y el alto
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # Llamamos al método para establecer la imagen de fondo
        self.set_background_image("imagenes/fnd2e.png")

        # Hacemos el tipo de letra
        self.letra1 = QFont()
        self.letra1.setFamily("Arial")
        self.letra1.setPointSize(12)

        # Hacemos el tipo de letra
        self.letra2 = QFont()
        self.letra2.setFamily("Arial")
        self.letra2.setPointSize(12)

        # Hacemos el letrero
        self.letrero1 = QLabel(self)
        self.letrero1.setText("Titulo De la Tarea:")
        self.letrero1.setFont(self.letra1)
        self.letrero1.setStyleSheet("color: black; padding: 30px;")
        self.letrero1.setFixedWidth(250)
        self.letrero1.move(0, 20)

        # Hacemos el campo para ingresar el título de la tarea
        self.titleTask = QLineEdit(self)
        self.titleTask.setFixedWidth(400)
        self.titleTask.setStyleSheet("background-color: White")
        self.titleTask.setMaxLength(100)
        self.titleTask.move(30, 45)

        # Hacemos el letrero
        self.Qlabel1 = QLabel(self)
        self.Qlabel1.setText("Especificaciones:")
        self.Qlabel1.setFont(self.letra2)
        self.Qlabel1.setStyleSheet("background-color: #White; color: #FFFFFF; padding: 40px;")
        self.Qlabel1.setFixedWidth(200)
        self.Qlabel1.move(30, 80)

        # Hacemos el campo para ingresar las especificaciones de la tarea
        self.Qline1 = QLineEdit(self)
        self.Qline1.setFixedWidth(400)
        self.Qline1.setStyleSheet("background-color: White")
        self.Qline1.setMaxLength(300)
        self.Qline1.setFixedHeight(200)
        self.Qline1.move(30, 110)
        self.Qline1.setAlignment(Qt.AlignTop)

        # Hacemos un botón para agregar la tarea
        self.botonTarea = QPushButton(self)
        self.botonTarea.setText("Agregar Tarea")
        self.botonTarea.setFixedWidth(400)
        self.botonTarea.setStyleSheet("background-color: #50D4FA; color: #000000  ; padding: 30px;")
        self.botonTarea.move(30, 380)
        self.botonTarea.clicked.connect(self.guardar_tarea)

        # Hacemos el letrero
        self.Qlabel2 = QLabel(self)
        self.Qlabel2.setText("Agregar ID:")
        self.Qlabel2.setFont(self.letra1)
        self.Qlabel2.setStyleSheet("background-color: #White; color: #FFFFFF; padding: 40px;")
        self.Qlabel2.setFixedWidth(200)
        self.Qlabel2.move(30, 310)

        # Hacemos el campo para ingresar el ID de la tarea
        self.idTarea = QLineEdit(self)
        self.idTarea.setFixedWidth(400)
        self.idTarea.setStyleSheet("background-color: White")
        self.idTarea.setMaxLength(100)
        self.idTarea.move(30, 340)

        # Agregamos una lista desplegable para seleccionar un empleado
        self.listaEmpleados = QComboBox(self)
        self.listaEmpleados.setFixedWidth(400)
        self.listaEmpleados.setStyleSheet("background-color: White")
        self.listaEmpleados.move(30, 240)
        self.cargar_empleados()
        self.listaEmpleados.setCurrentIndex(-1)

        # Hacemos un botón para volver al menú
        self.volverMenu = QPushButton(self)
        self.volverMenu.setText("Volver Menu")
        self.volverMenu.setFixedWidth(400)
        self.volverMenu.setStyleSheet("background-color: #50D4FA; color: #000000  ; padding: 30px;")
        self.volverMenu.move(30, 420)
        self.volverMenu.clicked.connect(self.cerrar_ventana)

    def cargar_empleados(self):
        try:
            # Cargar los empleados desde el archivo "empleados.txt" en la lista desplegable
            with open("empleados.txt", "r") as file:
                for line in file:
                    # Verificar que haya al menos dos elementos después de aplicar split()
                    empleado_info = line.strip().split()
                    if len(empleado_info) >= 2:
                        empleado_id, empleado_nombre = empleado_info
                        self.listaEmpleados.addItem(f"{empleado_nombre} (ID: {empleado_id})")
                    else:
                        print(f"Formato incorrecto en línea: {line}")
        except Exception as e:
            print(f"Error al cargar empleados: {e}")

    def cerrar_ventana(self):
        self.close()

    def set_background_image(self, image_path):
        background_image = QPixmap(image_path).scaled(self.ancho, self.alto)

        background_label = QLabel(self)
        background_label.setPixmap(background_image)
        background_label.setGeometry(0, 0, self.ancho, self.alto)

        background_label.lower()

    def guardar_tarea(self):
        # Obtener los datos de la tarea
        titulo_tarea = self.titleTask.text()
        especificaciones_tarea = self.Qline1.text()
        id_tarea = self.idTarea.text()

        # Obtener el empleado seleccionado de la lista desplegable
        empleado_seleccionado = self.listaEmpleados.currentText()

        # Parsear el ID del empleado desde la cadena (por ejemplo, "Nombre (ID: 123)")
        id_empleado = empleado_seleccionado.split("(ID: ")[1].rstrip(")")

        # Crear una cadena con la información de la tarea y el empleado asignado
        tarea_info = f"Título: {titulo_tarea}\nEspecificaciones: {especificaciones_tarea}\nID: {id_tarea}\nEmpleado asignado (ID): {id_empleado}\n"

        # Escribir la información de la tarea en un archivo de texto
        with open("tareas.txt", "a") as file:
            file.write(tarea_info + "\n")

        QMessageBox.information(self, "Éxito", "Tarea agregada con éxito.")
        self.titleTask.clear()
        self.Qline1.clear()
        self.idTarea.clear()

if __name__ == '__main__':
    aplicacion1 = QApplication(sys.argv)
    v1 = addtarea11()
    v1.show()
    sys.exit(aplicacion1.exec_())

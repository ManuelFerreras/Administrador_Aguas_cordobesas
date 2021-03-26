''' IMPORTS '''
import sys
import threading
import datetime
import tkinter
import os
from time import sleep
import pyautogui
import json
import os
import pyodbc
from openpyxl import load_workbook
from tkinter import filedialog

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PySide2.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PySide2.QtCore import Slot

from clientes import Ui_Dialog
from seleccionar_access import Ui_MainWindow
 

''' DECLARACIÓN DE VARIABLES GLOBALES '''
index_seleccionado = 0   # Sirve para saber qué cliente estamos viendo actualmente.

clientes = []   # Sirve para almacenar los clientes cargados de la base de datos.
url = []   # Sirve para almacenar la url de aguas cordobesas de un cliente.

PATH_DATABASE = None   # Ubicación de la base de datos.
DRIVER_NAME = "Microsoft Access Driver (*.mdb)"   # Driver utilizado para leer la base de datos.


''' PROGRAMA '''

class Dialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__()
        self.ui = Ui_Dialog()
        self.setupUi(self)
        # Hago que no se le pueda modificar el tamaño a la ventana.
        self.setFixedSize(self.size())

        self.btn_exit.clicked.connect(self.salir)
        self.cb_seleccionar_cliente.currentIndexChanged.connect(self.cambiar_seleccion)
        self.btn_actualizar_aguas_cordobesas.clicked.connect(self.activar_extraer_un_info)
        self.btn_actualizar_agua_todos.clicked.connect(self.activar_extraer_info)

        # Deshabilito la opción "Sin Selección" del comboBox
        self.cb_seleccionar_cliente.model().item(0).setEnabled(False)

        # Deshabilito el botón para buscar el valor de Aguas Cordobesas por default
        # para que no se pueda buscar el valor de "Sin Selección".
        self.btn_actualizar_aguas_cordobesas.setEnabled(False)

        # Traigo la información de la base de datos.
        #    self.conectar_access()       

    def actualizar_nombres_clientes(self, index_temp):
        global index_seleccionado

        print("El index seleccionado es: ", index_temp)

        
        self.cb_seleccionar_cliente.clear()
        self.cb_seleccionar_cliente.addItem("Sin Seleccion")
        self.cb_seleccionar_cliente.model().item(0).setEnabled(False)

        for i in range(len(clientes)):
            self.cb_seleccionar_cliente.addItem(clientes[i][1])

        self.cb_seleccionar_cliente.setCurrentIndex(index_temp + 1)
        index_seleccionado = index_temp

    def actualizar_data(self):
        if clientes[index_seleccionado][11] != None and clientes[index_seleccionado][32] != None:
            self.btn_actualizar_aguas_cordobesas.setEnabled(True)
        else:
            self.btn_actualizar_aguas_cordobesas.setEnabled(False)


    @Slot()
    def cambiar_seleccion(self):
        # Modifica la información mostrada según el cliente seleccionado.
        self.btn_actualizar_aguas_cordobesas.setEnabled(True)
        self.le_periodo_a_buscar.setEnabled(True)
        global index_seleccionado
        index_seleccionado = self.cb_seleccionar_cliente.currentIndex() - 1
        print(index_seleccionado)
        self.actualizar_data()

    @Slot()
    def activar_extraer_un_info(self):
        # Comienzo la búsqueda de información de eaguas cordobesas en otro hilo.
        thread = threading.Thread(target = self.extraer_info_un_cliente, daemon=True)
        thread.start()

    @Slot()
    def activar_extraer_info(self):
        # Comienzo la búsqueda de información de eaguas cordobesas en otro hilo.
        thread = threading.Thread(target = self.actualizar_aguas_de_todos, daemon=True)
        thread.start()

    @Slot()
    def conectar_access(self):
        # Creo una conexión a la base de datos. 
        global conn
        conn = pyodbc.connect("Driver={%s};DBQ=%s;" % (DRIVER_NAME, PATH_DATABASE))

        # Selecciono de dónde extraer la información.
        global cursor
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Inquilinos")

        # Extraigo la información y la almaceno en el vector de clientes.
        for row in cursor.fetchall():
            clientes.append(row)

        # Cargo las opciones del comboBox por primera vez y printeo la información en pantalla.
        for i in range(len(clientes)):
            self.cb_seleccionar_cliente.addItem(clientes[i][1])
            print(f"{i+1} Clientes cargados.")
            print("\n")

        self.label_cantidad_clientes.setText(str(len(clientes)))
        

    def extraer_info_un_cliente(self):
        # Me fijo que el usuario haya aclarado qué periodo buscar.
        if self.le_periodo_a_buscar.text() != "":
            # Deshabilito los botones de actualizar Aguas Cordobesas.
            self.btn_actualizar_aguas_cordobesas.setEnabled(False)
            self.btn_actualizar_agua_todos.setEnabled(False)
            self.le_periodo_a_buscar.setEnabled(False)
             
            # Consigo el periodo deseado para buscar.
            periodo_deseado = int(self.le_periodo_a_buscar.text())

            # Abro un navegador en el url del cliente seleccionado.
            global index_seleccionado
            url = clientes[index_seleccionado][32]
            driver = webdriver.Chrome()
            print(url)
            driver.get(url)

            # Espero a que cargue la página.
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="sUf"]')))
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tbl-detalleDeuda"]/tbody[2]')))

            # Consigo el texto de la boleta.
            text = driver.find_element_by_xpath('//*[@id="tbl-detalleDeuda"]/tbody[2]').text
            codigo = driver.find_element_by_xpath('//*[@id="sUf"]').text
            
            # Extraigo la información relevante de la boleta.
            text = text.split()
            while len(text) > 10:
                comprobacion = text[1].split('/')
                if int(comprobacion[0]) == periodo_deseado:
                    break
                del text[0:10]
            text[8] = text[8].replace(",", ".")

            print(text)

            # Actualizo el vector de clientes con la información extraida.
            periodo = text[1].split('/')
            clientes[index_seleccionado][12] = text[8]
            clientes[index_seleccionado][11] = periodo[0]

            # Actualizo la base de datos con la información extraida y aplico cambios.
            cursor.execute("UPDATE [Inquilinos] SET [Aguas_Importe] = ?, [Aguas_cuota] = ? WHERE [URL_Aguas_Cbesas] = ?", text[8], periodo[0], url)
            conn.commit()
            print("Modificado")
            
            # Actualizo la información mostrada en la ventana.
            self.actualizar_data()

            # Cierro el navegador.
            driver.close()

            # Vuelvo a habilitar los botones para buscar Aguas Cordobesas.
            self.btn_actualizar_aguas_cordobesas.setEnabled(True)
            self.le_periodo_a_buscar.setEnabled(True)
            self.btn_actualizar_agua_todos.setEnabled(True)

    def actualizar_aguas_de_todos(self): # Este método es igual al otro pero lo hace con todos los clientes que posean cuenta de Aguas Cordobesas.
        if self.le_periodo_a_buscar.text() != "":
            self.btn_actualizar_aguas_cordobesas.setEnabled(False)
            self.btn_actualizar_agua_todos.setEnabled(False)
            self.le_periodo_a_buscar.setEnabled(False)

            periodo_deseado = int(self.le_periodo_a_buscar.text())
            driver = webdriver.Chrome()
            i = -1
            for row in clientes:
                i = i + 1
                if row[11] != None and row[32] != None:
                    url = row[32]

                    try:
                        driver.get(url)

                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="sUf"]')))
                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tbl-detalleDeuda"]/tbody[2]')))
                        text = driver.find_element_by_xpath('//*[@id="tbl-detalleDeuda"]/tbody[2]').text
                        codigo = driver.find_element_by_xpath('//*[@id="sUf"]').text
                        
                        text = text.split()

                        while len(text) > 10:
                            comprobacion = text[1].split('/')
                            if int(comprobacion[0]) == periodo_deseado:
                                break
                            del text[0:10]
                        
                            
                        text[8] = text[8].replace(",", ".")

                        print(text)

                        periodo = text[1].split('/')

                        clientes[i][12] = text[8]
                        clientes[i][11] = periodo[0]
                        cursor.execute("UPDATE [Inquilinos] SET [Aguas_Importe] = ?, [Aguas_cuota] = ? WHERE [URL_Aguas_Cbesas] = ?", text[8], periodo[0], url)
                        self.actualizar_data()
                        conn.commit()

                    except:
                        print('Error con el cliente')
                        cursor.execute("UPDATE [Inquilinos] SET [Aguas_Importe] = ?, [Aguas_cuota] = ? WHERE [URL_Aguas_Cbesas] = ?", "0", periodo_deseado, url)

            driver.close()
            print("Se ha completado la actualizacion")

            self.btn_actualizar_aguas_cordobesas.setEnabled(True)
            self.le_periodo_a_buscar.setEnabled(True)
            self.btn_actualizar_agua_todos.setEnabled(True)

        else:
            print('No ha especificado un periodo a buscar.')

    @Slot()
    def salir(self):
        # Sale del programa.
        sys.exit(app.exec_())



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_exit.clicked.connect(self.salir)
        self.ui.btn_elegir_archivo_access.clicked.connect(self.elegir_access)
        self.ui.pushButton.clicked.connect(self.abrir_ventana_clientes)


    @Slot()
    def salir(self):
        # Sale del programa.
        sys.exit(app.exec_())

    @Slot()
    def elegir_access(self):
        root = tkinter.Tk()
        root.withdraw() #use to hide tkinter window

        global PATH_DATABASE
        PATH_DATABASE = self.search_for_file_path(root)
        
        if PATH_DATABASE != None:
            self.ui.pushButton.setEnabled(True)

    @Slot()
    def abrir_ventana_clientes(self):
        main_window.hide()
        window.show()
        
        window.conectar_access()

    def search_for_file_path(self, root):
        currdir = os.getcwd()
        tempdir = filedialog.askopenfilename(parent=root, initialdir=currdir, title='Porfavor, eliga el archivo access', filetypes = [("Access Database File", "*.mdb")])

        return tempdir 

        
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Dialog()
    main_window = MainWindow()

    main_window.show()

    sys.exit(app.exec_())

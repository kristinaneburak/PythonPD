import sys
import os
import random
import csv
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox

class DatasetAnnotationApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()        
        self.prevclassName = "123"

    def initUI(self):
        self.setWindowTitle("Dataset Annotation App")

        self.folderpath = None
        self.class_label = None
        self.current_instance = None

        # Widgets
        self.select_folder_button = QtWidgets.QPushButton("Выбрать папку с датасетом", self)
        self.create_annotation_button = QtWidgets.QPushButton("Создать файл аннотации", self)
        self.next_goodclass_button = QtWidgets.QPushButton("Следующий отзыв", self)
        self.next_goodclass_button.setEnabled(False)
        self.class_image_label = QtWidgets.QLabel(self)

        button_style = """
            QPushButton {
                background-color: #d1a3bb;
                border: none;
                color: rose;
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                font-size: 32px;
                margin: 4px 2px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #FFC0CB;
            }
        """
        self.select_folder_button.setStyleSheet(button_style)
        self.create_annotation_button.setStyleSheet(button_style)
        self.next_goodclass_button.setStyleSheet(button_style)

        # Layout
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.select_folder_button)
        vbox.addWidget(self.create_annotation_button)
        vbox.addWidget(self.next_goodclass_button)
        vbox.addWidget(self.class_image_label)

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        # Signals
        self.select_folder_button.clicked.connect(self.select_folder)
        self.create_annotation_button.clicked.connect(self.create_annotation)
        self.next_goodclass_button.clicked.connect(self.show_good_reviews)
        

    def select_folder(self):
        self.folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Выберите папку с датасетом')
        if self.folderpath:
            self.next_goodclass_button.setEnabled(True)
    

    def create_annotation(self):
        if self.folderpath:
            annotation_file, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Создать файл аннотации', '', 'CSV Files (*.csv)')
            if annotation_file:
                dataset_path = self.folderpath
                output_csv = annotation_file

                with open(output_csv, 'w', newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerow(['Absolute path', 'Relative path', 'Class label'])

                    for root, dirs, files in os.walk(dataset_path):
                        for filename in files:
                            abs_path = os.path.join(root, filename)
                            rel_path = os.path.relpath(abs_path, start=dataset_path)
                            class_label = os.path.basename(root)
                            csv_writer.writerow([abs_path, rel_path, class_label])

    def show_good_reviews(self):
        if self.folderpath:
            self.current_instance = self.get_next_instance("", self.folderpath + '/')
            self.show_instance()

    

    def show_instance(self):
        if self.current_instance:
            with open(self.current_instance, 'r', encoding='utf-8') as file:
                file_text = file.read()

            message_box = QMessageBox(self)
            message_box.setWindowTitle(f"Следующий экземпляр класса {self.class_label}")
            message_box.setText(f"Путь к файлу: {self.current_instance}")
            message_box.setDetailedText(file_text)
            message_box.exec_()
        else:
            QtWidgets.QMessageBox.information(self, 'Конец датасета', f'Все экземпляры класса {self.class_label} закончились.')
            self.current_instance = None
    
    instances = []
    def get_next_instance(self, class_label, dataset_path):
        if self.prevclassName != class_label:
            self.instances = []
            self.prevclassName = class_label

        for root, dirs, files in os.walk(dataset_path):
            if os.path.basename(root) == class_label:
                self.instances.extend([os.path.join(root, filename) for filename in files])

        random.shuffle(self.instances)
        if self.instances:
            return self.instances.pop()
        else:
            return None
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = DatasetAnnotationApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

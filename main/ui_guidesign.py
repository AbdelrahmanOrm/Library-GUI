from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from main import library_instance


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(840, 690)
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setGeometry(QRect(210, 0, 431, 101))
        font1 = QFont()
        font1.setFamily(u"Georgia")
        font1.setPointSize(22)
        font1.setBold(False)
        font1.setWeight(50)
        self.label.setFont(font1)
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setFrameShadow(QFrame.Plain)
        self.label.setLineWidth(1)
        self.label.setMidLineWidth(0)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 150, 131, 31))
        font2 = QFont()
        font2.setFamily(u"Calibri")
        font2.setPointSize(17)
        self.label_2.setFont(font2)
        self.Book_button = QRadioButton(self.centralwidget)
        self.Book_button.setObjectName(u"Book_button")
        self.Book_button.setGeometry(QRect(210, 160, 131, 21))
        font3 = QFont()
        font3.setPointSize(12)
        self.Book_button.setFont(font3)
        self.author_button = QRadioButton(self.centralwidget)
        self.author_button.setObjectName(u"author_button")
        self.author_button.setGeometry(QRect(370, 160, 131, 21))
        self.author_button.setFont(font3)
        self.Searchbar = QTextEdit(self.centralwidget)
        self.Searchbar.setObjectName(u"Searchbar")
        self.Searchbar.setGeometry(QRect(30, 200, 421, 41))
        self.Searchbar.setFont(font)
        self.Searchbar.setAutoFillBackground(False)
        self.Searchbar.setStyleSheet(u"")
        self.Searchbar.setFrameShape(QFrame.NoFrame)
        self.Searchbar.setFrameShadow(QFrame.Plain)
        self.Searchbar.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.Searchbar.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.Searchbar.setOverwriteMode(False)

        # Adjusting Search button
        self.SearchButton = QPushButton(self.centralwidget)
        self.SearchButton.setObjectName(u"SearchButton")
        self.SearchButton.setGeometry(QRect(490, 200, 71, 41))
        font4 = QFont()
        font4.setFamily(u"Calibri")
        font4.setPointSize(10)
        self.SearchButton.setFont(font4)

        # Adjusting Clear button
        self.ClearButton = QPushButton(self.centralwidget)
        self.ClearButton.setObjectName(u"ClearButton")
        self.ClearButton.setGeometry(QRect(720, 560, 91, 41))
        font5 = QFont()
        font5.setFamily(u"Calibri")
        font5.setPointSize(12)
        self.ClearButton.setFont(font5)

        # Adjusting Buy button
        self.BuyButton = QPushButton(self.centralwidget)
        self.BuyButton.setObjectName(u"BuyButton")
        self.BuyButton.setGeometry(QRect(350, 490, 131, 41))
        font6 = QFont()
        font6.setFamily(u"Calibri Light")
        font6.setPointSize(12)
        self.BuyButton.setFont(font6)

        # Adjusting Results text-box
        self.Resultdetails = QTextBrowser(self.centralwidget)
        self.Resultdetails.setObjectName(u"Resultdetails")
        self.Resultdetails.setGeometry(QRect(30, 270, 781, 201))
        self.Resultdetails.setFrameShape(QFrame.Panel)
        self.Resultdetails.setFrameShadow(QFrame.Plain)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 843, 29))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        # Connect the Search button to the search function
        self.SearchButton.clicked.connect(self.search_button_clicked)
        QMetaObject.connectSlotsByName(MainWindow)

        # Connect the Clear button to the clear function
        self.ClearButton.clicked.connect(self.Clear)    # To clear all texts in textboxes

        # Connect the Buy button to the buy function
        self.BuyButton.clicked.connect(self.Buy)


    def search_button_clicked(self):                    # Search function
        # Get the selected search type (Book title or Author) from the radio button
        if self.Book_button.isChecked():
            search_type = "book_title"
        elif self.author_button.isChecked():
            search_type = "author"
        else:
            return  # No search type selected, do nothing

        # Get the user's input from the Searchbar (GUI)
        user_input = self.Searchbar.toPlainText().strip()  # To get the text from the Text-box

        # Perform the search based on the selected search type Radio button
        if search_type == "book_title":
            result = library_instance.searchBookByTitle(user_input)  # Call your search function for book titles
            print(result)
        elif search_type == "author":
            result = library_instance. searchBookByAuthor(user_input)  # Call your search function for authors
        else:
            result = {}  # Handle other cases

        # Display the result in the Resultdetails Text-Browser
        self.Resultdetails.clear()  # Clear the previous result
        if result:
            # Display the result in the Text-Browser
            for key, value in result.items():
                # Check if value is a dictionary before accessing its keys
                if isinstance(value, dict):
                    print(f"Title: {key}, Author: {value['author']}, Cost: {value['cost']}, Section: {value['section']}")
                    self.Resultdetails.append(f"Title: {key}")
                    self.Resultdetails.append(f"Author: {value['author']}")
                    self.Resultdetails.append(f"Cost: {value['cost']}")
                    self.Resultdetails.append(f"Section: {value['section']}")
                else:
                    if key == 'author':
                        self.Resultdetails.append(f"Author: {value}")
                    if key == 'cost':
                        self.Resultdetails.append(f"Cost: {value}")
                    if key == 'section':
                        self.Resultdetails.append(f"Section: {value}")

                self.Resultdetails.append("\n")
        else:
            self.Resultdetails.append("No result found")

    def Clear(self):                # Clear button function
        self.Resultdetails.clear()
        self.Searchbar.clear()

    def Buy(self):                  # Buy button function
        self.Resultdetails.clear()
        self.Resultdetails.append("Purchase done successfully")

    # setupUi
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Welcome to E book-store", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Search by ", None))
        # if QT_CONFIG(accessibility)
        self.Book_button.setAccessibleName(QCoreApplication.translate("MainWindow", u"Book_button", None))
        # endif // QT_CONFIG(accessibility)
        self.Book_button.setText(QCoreApplication.translate("MainWindow", u"Book title", None))
        # if QT_CONFIG(accessibility)
        self.author_button.setAccessibleName(QCoreApplication.translate("MainWindow", u"author_button", None))
        # endif // QT_CONFIG(accessibility)
        self.author_button.setText(QCoreApplication.translate("MainWindow", u"Author", None))
        # if QT_CONFIG(accessibility)
        self.Searchbar.setAccessibleName(QCoreApplication.translate("MainWindow", u"searchbar", None))
        # endif // QT_CONFIG(accessibility)
        # if QT_CONFIG(accessibility)
        self.Searchbar.setAccessibleDescription("")
        # endif // QT_CONFIG(accessibility)
        self.Searchbar.setDocumentTitle("")
        self.Searchbar.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Search Book-title or Author name", None))
        self.SearchButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.ClearButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.BuyButton.setText(QCoreApplication.translate("MainWindow", u"Buy", None))
        self.Resultdetails.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Result Details", None))

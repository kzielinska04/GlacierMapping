import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QFrame, QComboBox,
    QDateEdit, QMessageBox, QCalendarWidget
)
from PySide6.QtCore import (Qt, QDate, QLocale)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Zielinska_Lodowce_Inzynierka")
        self.resize(1000, 700)
        self.setStyleSheet("""
            QMainWindow{
                background-color: #F2F7F7;
            }
        """)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QHBoxLayout(central_widget)
        
        sidebar = QFrame()
        sidebar.setFixedWidth(290)
        sidebar.setStyleSheet("background-color: white; border-radius: 10px;")
        
        sidebar_layout = QVBoxLayout(sidebar)
        title = QLabel("Analiza powierzchni lodowca")
        title.setStyleSheet("""
            font.size: 24 px;
            font-weight: bold;
            color: #0B3D4A;
            padding: 15px
                            """)
        sidebar_layout.addWidget(title)
        
        glacier_label = QLabel("Wybierz lodowiec")
        sidebar_layout.addWidget(glacier_label)
        
        self.glacier_selector = QComboBox()
        self.glacier_selector.addItems([
            "Wszystkie lodowce Svalbardu",
            "A",
            "B",
            "C"
        ])
        
        sidebar_layout.addWidget(self.glacier_selector)
        
        date1_label = QLabel("Data początkowa")
        sidebar_layout.addWidget(date1_label)
        
        self.date1_selector = QDateEdit()
        self.date1_selector.setCalendarPopup(True)
        self.date1_selector.setDisplayFormat("dd.MM.yyyy")
        self.date1_selector.setDate(QDate(2025, 7, 25))
        self.date1_selector.setMinimumDate(QDate(2017, 1, 1))
        
        calendar1 = self.date1_selector.calendarWidget()
        calendar1.setLocale(QLocale("pl_PL"))
        calendar1.setNavigationBarVisible(True)
        calendar1.setGridVisible(True)
        calendar1.setFirstDayOfWeek(Qt.DayOfWeek.Monday)
        
        calendar1.setStyleSheet("""
            QCalendarWidget QToolButton {
                color: #0B3D4A;
                background-color: #F2F7F7;
                font-size: 14px;
                font-weight: bold;
                min-width: 35px;
                min-height: 28px;
            }

            QCalendarWidget QSpinBox {
                color: #0B3D4A;
                background-color: white;
                font-size: 14px;
            }
        """)
        
        
        
        
        sidebar_layout.addWidget(self.date1_selector)
        
        date2_label = QLabel("Data końcowa")
        sidebar_layout.addWidget(date2_label)
        
        self.date2_selector = QDateEdit()
        self.date2_selector.setCalendarPopup(True)
        self.date2_selector.setDisplayFormat("dd.MM.yyyy")
        self.date2_selector.setDate(QDate(2025, 9, 10))
        self.date2_selector.setMinimumDate(QDate(2017,1,1))
        
        calendar2 = self.date2_selector.calendarWidget()
        calendar2.setLocale(QLocale("pl_PL"))
        calendar2.setNavigationBarVisible(True)
        calendar2.setGridVisible(True)
        calendar2.setFirstDayOfWeek(Qt.DayOfWeek.Monday)
                
        calendar2.setStyleSheet("""
            QCalendarWidget QToolButton {
                color: #0B3D4A;
                background-color: #F2F7F7;
                font-size: 14px;
                font-weight: bold;
                min-width: 35px;
                min-height: 28px;
            }

            QCalendarWidget QSpinBox {
                color: #0B3D4A;
                background-color: white;
                font-size: 14px;
            }
        """)
        
                
                
                
                
                
                
        sidebar_layout.addWidget(self.date2_selector)
        
        analyze_button = QPushButton("Analizuj")
        analyze_button.setStyleSheet("""
        QPushButton {
            background-color: #81D8D0;
            color: #0B3D4A;
            font-size: 15px;
            font-weight: bold;
            padding: 12px;
            border-radius: 8px;
        }

        QPushButton:hover {
            background-color: #5FC4BA;
        }
    """)
        sidebar_layout.addWidget(analyze_button)
        
        analyze_button.clicked.connect(self.start_analysis)
        
        
        
        map_area = QFrame()
        map_area.setStyleSheet("background-color: white; border-radius: 10px")
    
        # Układ obszaru mapy
        map_layout = QVBoxLayout(map_area)

        # Nagłówek obszaru mapy
        map_title = QLabel("Podgląd mapy Svalbardu")
        map_title.setStyleSheet("""
            font-size: 22px;
            font-weight: bold;
            color: #0B3D4A;
            padding: 15px;
        """)
        
        
        map_placeholder = QLabel(
            "Tutaj zostanie wyświetlona mapa Svalbardu"
        )

        map_placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)

        map_placeholder.setStyleSheet("""
            color: #78909C;
            font-size: 16px;
            background-color: #F2F7F7;
            border-radius: 10px;
        """)

        map_layout.addWidget(map_title)
        map_layout.addWidget(map_placeholder)

        

        main_layout.addWidget(sidebar, 0)
        main_layout.addWidget(map_area, 1)
        
        
        
    def start_analysis(self):
        glacier = self.glacier_selector.currentText()

        date1 = self.date1_selector.date()
        date2 = self.date2_selector.date()

        if not self.is_valid_date(date1):
            QMessageBox.warning(
                self,
                "Nieprawidłowa data",
                "Data początkowa powinna mieścić się w przedziale 25.07-10.09"
            )
            return

        if not self.is_valid_date(date2):
            QMessageBox.warning(
                self,
                "Nieprawidłowa data",
                "Data końcowa powinna mieścić się w przedziale 25.07-10.09"
            )
            return
        
        if date2 <= date1:
            QMessageBox.warning(
                self,
                "Nieprawidłowa data",
                "Data końcowa musi być późniejsza, niż data początkowa"
            )


        QMessageBox.information(
            self,
            "Analiza",
            f"Lodowiec: {glacier}\n"
            f"Data początkowa: {date1}\n"
            f"Data końcowa: {date2}"
        )
        
        
        
    def is_valid_date(self, date):
        month = date.month()
        day = date.day()
        
        if date.year() <2017:
            return False
        
        if month == 7 and day >=25:
            return True
        if month == 8:
            return True
        
        if month == 9 and day <=10:
            return True
        
        return False

from howdoi import howdoi
from PySide2.QtWidgets import QApplication, QScrollArea, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QFontComboBox, QPushButton, QWidget, QTextEdit, QDial
from PySide2.QtGui import QFont
from PySide2.QtCore import Qt, QMargins
import sys


class GUIWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Fonts
        self.fontForte = QFont('Forte', 10)
        self.fontBox = QFontComboBox()
        self.fontBox.currentFontChanged.connect(self.onFontChange)
        
        # Title and window options
        self.setWindowTitle("HowDoI GUI")
        self.setMinimumSize(800, 600)
       
        # Buttons 
        self.button = QPushButton("Ask")
        self.button.resize(10,10)
        self.button.setFont(self.fontForte)
        self.button.clicked.connect(self.onAskEvent)
        
        # Dial
        self.dialLabel = QLabel()
        self.dialLabel.setText("Font size")
        self.dial = QDial()
        self.dial.setMaximumSize(100,100)
        self.dial.setNotchesVisible(True)
        self.dial.setMaximum(20)
        self.dial.setMinimum(5)
        self.dial.valueChanged.connect(self.onDialValueChangingZoom)
        
        # HowDoI answer label & scroll Area
        self.answerLabel = QLabel()
        self.answerLabel.setText("Waiting for your question...")
        self.answerLabel.setAlignment(Qt.AlignLeft)
        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.answerLabel)
        self.labelFont = self.answerLabel.font()
        
                
        # Input
        self.input = QLineEdit()
        self.input.setFont(self.fontForte)
        self.input.setPlaceholderText("Ask me anything")
        
        # Vertical Layout
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.button)
        layout.addWidget(self.fontBox)
        layout.addWidget(self.dialLabel)
        layout.addWidget(self.dial)
        layout.addWidget(self.scrollArea)
        container = QWidget()
        container.setLayout(layout)
        container.setContentsMargins(QMargins(5,5,5,5))
        self.setCentralWidget(container)
        
        
        
    def onDialValueChangingZoom(self):
        self.labelFont.setPointSize(self.dial.value())
        self.answerLabel.setFont(self.labelFont)
    
    def onAskEvent(self):
        self.answerLabel.setText(howdoi.howdoi(self.input.text() + " -a"))
        
    def onFontChange(self):
        self.labelFont = self.fontBox.currentFont()
        self.answerLabel.setFont(self.labelFont)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = GUIWindow()
    window.show()
    
    app.exec_()


'''
    This was the final work we worked on which used the concepts of classes and objects, 
    and the use of the PYQT library to create and build desktop applications with visuals, buttons and 
    other widgets that can be used to interact with the user. 

    In this application we calculate the health status of a person using the Rufier test which
      is a set of physical exercises designed to assess your cardiac performance during physical exertion.
'''


# connecting the app to PYQT
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit
from PyQt5.QtGui import QFont

# create the application
app = QApplication([])

# screen classes
class FirstScreen(QWidget):

    # constructor function
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    
    # setting the view of the screen
    def set_appear(self):
        self.setWindowTitle("Health App")
        self.resize(500, 500)
    
    # setting the components that are going to be on the screen
    def initUI(self):
        self.box_layout = QVBoxLayout()

        # objects
        self.welcome = QLabel("Welcome to the Health status detection program!")
        self.instructions = QLabel("This application allows you to use the Rufier test to make an intial diagnosis of your health. \nThe Rufier test is a set of physical exercises designed to assess your cardiac performance during physical exertion. \nThe subject lies in the supine position for 5 minutes and has their pulse rate measured for 15 seconds; \nthen, within 45 seconds, the subject performs 30 squats. \nWhen the exercise ends, the subject lies down and their pulse is measured again for 15 seconds \nand then for the last 15 seconds of the first minute of the recovery period. \nImportant!If you feel unwell during the test(dizziness, \ntinnnitus, shortness of breath, etc.), stop the test and consult a physician.")
        self.StartButton = QPushButton("Start")

        # adding the components to the layout of the screen
        self.box_layout.addWidget(self.welcome, alignment=Qt.AlignLeft)
        self.box_layout.addWidget(self.instructions, alignment=Qt.AlignLeft)
        self.box_layout.addWidget(self.StartButton, alignment=Qt.AlignCenter)

        # adding the layout to the screen
        self.setLayout(self.box_layout)
    
    def display_next_screen(self):
        self.hide()
        self.secondScreen = SecondScreen()
        self.secondScreen.show()

    # connectin the functions with the buttons or widgets in the form
    def connects(self):
        self.StartButton.clicked.connect(self.display_next_screen)
    
   

class SecondScreen(QWidget):

    #constructor
    def __init__(self):
        super().__init__()
        self.finalTestStarted = False
        self.set_appear()
        self.initUI()
        self.connects()
        self.hide()

    # timer functions
    def decrease_time(self):

        self.lbl_time.setText(self.time.toString("hh:mm:ss"))
        self.lbl_time.setFont(QFont("Times", 36, QFont.Bold))
        self.lbl_time.setStyleSheet("color: rgb(0, 0, 0)")
        self.time = self.time.addSecs(-1)
        seconds = int(self.time.toString("hh:mm:ss")[6:])
        if((seconds > 45 or seconds < 15) and self.finalTestStarted == True ):
            self.lbl_time.setStyleSheet("color: rgb(0,255,0)")
        if self.time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()



    def start_timer_15(self):
        self.time = QTime(0,0,15)
        self.timer.start(1000)

    def start_timer_45(self):
        self.time = QTime(0,0,45)
        self.timer.start(1000)
    
    def start_timer_60(self):
        self.finalTestStarted = True
        self.time = QTime(0,1,0)
        self.timer.start(1000)
    
    # defining the screen
    def set_appear(self):
        self.setWindowTitle("Tracking health issues")
        self.resize(500,500)
    
    # set the components
    def initUI(self):

        #creating a time object
        self.time = QTime(0,0,15)
        self.timer = QTimer()

        # timer label
        self.lbl_time = QLabel(self.time.toString("hh:mm:ss"))

        # layout
        self.box_layout = QVBoxLayout()

        #objects2
        self.instruction1 = QLabel("Hello, get ready to do some exercises !!")
        self.name = QLabel("Enter your full name:")
        self.full_name = QLineEdit("Full Name")
        self.lbl_years = QLabel("Full years:")
        self.year_input = QLineEdit("0")

        self.first_pulse_instructions = QLabel("Lie on your back and take your pulse for 15 seconds. Click the 'Start first test' button to start the timer. \nWrite down the result in the appropriate field.")

        self.first_pulse_button = QPushButton("Start the first test")
        self.first_test_input = QLineEdit("0")

        self.squats_instructions = QLabel("Perform 30 squats in 45 seconds. To do this, click the 'Start doing squats' button \nto  start the squat counter.")
        self.squats_button = QPushButton("Start doing squats")
        
        self.last_pulse_instructions = QLabel("Lie on your back and take your pulse for the fisrt 15 seconds of the minute, then for the last 15 seconds of the minute. \nPress the 'Start final test' button to start the timer. \nThe seconds that should be measuredare indicated in green and the minutes that should be measured are indicated in black. Write down the appropriate fields.")

        self.last_pulse_button = QPushButton("Start the final test")
        
        # show results button
        self.show_results_button = QPushButton("Show Results")

        self.final_test_input1 = QLineEdit("0")
        self.final_test_input2 = QLineEdit("0")

        # adding components to the layout of screen2
        self.box_layout.addWidget(self.name, alignment=Qt.AlignLeft)
        self.box_layout.addWidget(self.full_name, alignment=Qt.AlignLeft )
        self.box_layout.addWidget(self.lbl_years, alignment=Qt.AlignLeft)
        self.box_layout.addWidget(self.year_input, alignment=Qt.AlignLeft)
        self.box_layout.addWidget(self.first_pulse_instructions, alignment=Qt.AlignLeft)
        self.box_layout.addWidget(self.first_pulse_button, alignment=Qt.AlignLeft)
        self.box_layout.addWidget(self.first_test_input, alignment=Qt.AlignLeft)
        self.box_layout.addWidget(self.squats_instructions, alignment=Qt.AlignLeft)
        self.box_layout.addWidget(self.squats_button, alignment=Qt.AlignLeft)
        self.box_layout.addWidget(self.last_pulse_instructions, alignment=Qt.AlignLeft)
        self.box_layout.addWidget(self.last_pulse_button, alignment=Qt.AlignLeft)
        self.box_layout.addWidget(self.final_test_input1, alignment=Qt.AlignLeft)
        self.box_layout.addWidget(self.final_test_input2, alignment=Qt.AlignLeft)
        self.box_layout.addWidget(self.show_results_button, alignment=Qt.AlignCenter)

        self.box_layout.addWidget(self.lbl_time, alignment=Qt.AlignCenter)
    
        # adding the layout to screen
        self.setLayout(self.box_layout)
    
    # connects function
    def connects(self):
        self.timer.timeout.connect(self.decrease_time)
        self.first_pulse_button.clicked.connect(self.start_timer_15)
        self.squats_button.clicked.connect(self.start_timer_45)
        self.last_pulse_button.clicked.connect(self.start_timer_60)
        self.show_results_button.clicked.connect(self.showNextScreen)

    def onHide(self):
        self.hide()

    def showNextScreen(self):
        self.onHide()
        self.finalScreen = FinalScreen(self.full_name.text(),self.year_input.text(),self.first_test_input.text(),self.final_test_input1.text(), self.final_test_input2.text() )
        self.finalScreen.show()

# Final Screen
class FinalScreen(QWidget):

    # constructor
    def __init__(self, name, year,first_test, final1, final2):
        super().__init__()
        self.year = int(year)
        self.first_test = first_test
        self.final1 = final1
        self.final2 = final2
        self.user = name
        self.setAppear()
        self.initUI()
        self.hide()

    def setAppear(self):
        self.setWindowTitle("Results!")
        self.resize(500,500)
    
    def initUI(self):
        self.ruff =  (4*(int(self.first_test) + int(self.final1) + int(self.final2)) - 200) /10
        self.lbl_ruff = QLabel("Ruffier Index: "+str(self.ruff))
        Cardiac_perf = ""
        if self.year >= 15:
            if self.ruff >= 15:
                Cardiac_perf = "Low"
        elif self.ruff >= 11 and self.ruff <= 14.9:
            Cardiac_perf = "Satisfactory"
        elif self.ruff >= 6 and self.ruff <= 10.9:
            Cardiac_perf = "Average"
        elif self.ruff >= 0.5 and self.ruff <= 5.9:
            self.ruff = "Above average"
        elif self.year <= 0.4:
            Cardiac_perf = "High"
        elif self.year >= 13 and self.year < 14:
            if self.ruff >= 16.5:
                Cardiac_perf = "Low"
        elif self.ruff >= 12.5 and self.ruff <= 16.4:
            Cardiac_perf = "Satisfactory"
        elif self.ruff >= 7.5 and self.ruff <= 12.4:
            Cardiac_perf = "Average"
        elif self.ruff >= 2 and self.ruff <= 7.4:
            self.ruff = "Above average"
        elif self.year <= 01.9:
            Cardiac_perf = "High"
        elif self.year >= 11 and self.year< 12:
            if self.ruff >= 18:
                Cardiac_perf = "Low"
        elif self.ruff >= 14 and self.ruff <= 17.9:
            Cardiac_perf = "Satisfactory"
        elif self.ruff >= 9 and self.ruff <= 13.9:
            Cardiac_perf = "Average"
        elif self.ruff >= 3.5 and self.ruff <= 8.9:
            self.ruff = "Above average"
        elif self.year <= 3.4:
            Cardiac_perf = "High"
        elif self.year >= 9 and self.year< 10:
            if self.ruff >= 19.5:
                Cardiac_perf = "Low"
        elif self.ruff >= 15.5 and self.ruff <= 19.4:
            Cardiac_perf = "Satisfactory"
        elif self.ruff >= 10.5 and self.ruff <= 15.4:
            Cardiac_perf = "Average"
        elif self.ruff >= 5 and self.ruff <= 10.4:
            self.ruff = "Above average"
        elif self.year <= 4.9:
            Cardiac_perf = "High"
        elif self.year >= 7 and self.year< 8:
            if self.ruff >= 21:
                Cardiac_perf = "Low"
        elif self.ruff >= 17 and self.ruff <= 20.9:
            Cardiac_perf = "Satisfactory"
        elif self.ruff >= 12 and self.ruff <= 16.9:
            Cardiac_perf = "Average"
        elif self.ruff >= 6.5 and self.ruff <= 11.9:
            Cardiac_perf = "Above average"
        elif self.year <= 6.4:
            Cardiac_perf = "High"
        else:
            Cardiac_perf = "Your're too young to even have a phone :["
        

        self.cardiacResults = QLabel(str(self.user)+"'s Cardiac results: "+Cardiac_perf)

        # making the layout
        self.box_layout = QVBoxLayout()

        # add the labels to the layout
        self.box_layout.addWidget(self.lbl_ruff, alignment=Qt.AlignCenter )
        self.box_layout.addWidget(self.cardiacResults, alignment=Qt.AlignCenter )

        # set the layout
        self.setLayout(self.box_layout)



firstScreen = FirstScreen()

#running application
app.exec()
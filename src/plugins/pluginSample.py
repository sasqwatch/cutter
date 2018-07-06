import cutter
from cutter_plugin import CutterPlugin
from PySide2 import QtCore, QtWidgets
import shiboken2

class CutterSamplePlugin(CutterPlugin):
    def setupPlugin(self):
        self.name = 'SamplePlugin'
        self.description = 'A sample plugin written in python.'
        self.version = '1.0'
        self.author = 'xarkes'
        self.app = QtCore.QCoreApplication.instance()

    def setupInterface(self):
        print('Creating the dock widget...')
        main_window = None
        for widget in QtWidgets.QApplication.topLevelWidgets():
            if widget.objectName() == "MainWindow":
                main_window = widget
        dock_widget = QtWidgets.QDockWidget(main_window)
        dock_widget.setObjectName("FancyDockWidgetFromCoolPlugin")
        dock_widget.setWindowTitle('Test Widget')
        print(main_window, dock_widget)
        ptr = shiboken2.getCppPointer(dock_widget)[0]
        print(ptr)
        return ptr


# Instantiate our plugin
plugin = CutterSamplePlugin()


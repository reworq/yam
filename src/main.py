import os
import sys

from pathlib import Path

from PySide6.QtCore import Qt, QUrl
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWebEngineQuick import QtWebEngineQuick
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    exit_code = 0  # exit with OK code by default

    try:
        current_dir = Path(__file__).resolve().parent

        QApplication.setApplicationDisplayName("YAM")
        QApplication.setApplicationName("yam")
        QApplication.setApplicationVersion("0.0.1")
        QApplication.setOrganizationDomain("reworq.org")
        QApplication.setOrganizationName("reworq")

        # enable automatic scaling based on the pixel density of the monitor
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
        QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

        QtWebEngineQuick.initialize()

        app = QApplication(sys.argv)

        engine = QQmlApplicationEngine()
        engine.load(QUrl.fromLocalFile(str(current_dir / "main.qml")))

        exit_code = QApplication.exec() if engine.rootObjects() else 1

        del engine
        del app

        sys.stdout.flush()
        sys.stderr.flush()
    except BrokenPipeError:
        exit_code = 2

        # Python flushes standard streams on exit; redirect remaining output
        # to devnull to avoid another BrokenPipeError at shutdown.
        devnull = os.open(os.devnull, os.O_WRONLY)
        os.dup2(devnull, sys.stdout.fileno())

    sys.exit(exit_code)
else:
    print("ERROR: This file is not intended for importing!")
    sys.exit(1)

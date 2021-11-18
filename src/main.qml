import QtQuick
import QtQuick.Controls.Material
import QtWebEngine

ApplicationWindow {
    id: root

    readonly property real preferredWidth: 580
    readonly property real preferredHeight: 710

    function startApplication(args) {
        console.log(args)
        page.init()
        root.show()
    }

    function stopApplication() {
        page.del()
        root.hide()
    }

    minimumWidth: 520
    minimumHeight: 520
    width: root.preferredWidth
    height: root.preferredHeight
    title: Qt.application.displayName
    color: Material.background
    visible: false

    Material.theme: Material.System
    Material.accent: Material.color(Material.Yellow, Material.Shade500)

    menuBar: null

    header: null

    Item {
        anchors.fill: parent

        Label {
            anchors.centerIn: parent
            font {
                bold: true
                pixelSize: 32
            }
            text: qsTr("Yandex.Music is loading...")
            opacity: 0.5
            visible: page.loading
        }

        WebEngineView {
            id: page

            function init() {
                page.url = "https://music.yandex.com"
            }

            function del() {
                page.url = ""
            }

            anchors.fill: parent
            activeFocusOnPress: true
            backgroundColor: root.color
            profile: WebEngineProfile {
                offTheRecord: true
            }
            url: ""
            visible: !this.loading
        }

        ProgressBar {
            anchors {
                top: parent.top
                right: parent.right
                left: parent.left
            }
            from: 0
            to: 100
            value: page.loadProgress
            visible: page.loading
        }
    }

    footer: null

    Component.onCompleted: root.startApplication(Qt.application.arguments)

    Component.onDestruction: root.stopApplication()
}

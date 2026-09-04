from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class JherCPChecker(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=20, spacing=15)

        title = Label(
            text="JHER CP CHECKER",
            font_size="28sp"
        )

        scan = Button(
            text="START STORAGE SCAN",
            font_size="20sp"
        )

        result = Label(
            text="Ready",
            font_size="16sp"
        )

        def do_scan(instance):
            try:
                import os
                count = len(os.listdir("/sdcard"))
                result.text = f"Accessible storage items: {count}"
            except Exception:
                result.text = "Storage access unavailable"

        scan.bind(on_press=do_scan)

        layout.add_widget(title)
        layout.add_widget(scan)
        layout.add_widget(result)

        return layout

JherCPChecker().run()

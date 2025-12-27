from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from datetime import datetime


class TimeTrackerLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", spacing=10, padding=10, **kwargs)

        self.start_time = None
        self.stop_time = None

        self.ticket_id = TextInput(hint_text="Ticket ID", multiline=False)
        self.description = TextInput(hint_text="Description", multiline=True)
        self.time_spent = TextInput(
            hint_text="Time spent (minutes)",
            multiline=False,
            readonly=True
        )

        self.start_label = Label(text="Start time: -")
        self.stop_label = Label(text="Stop time: -")

        start_btn = Button(text="Start time")
        stop_btn = Button(text="Stop time")

        start_btn.bind(on_press=self.start_timer)
        stop_btn.bind(on_press=self.stop_timer)

        self.add_widget(self.ticket_id)
        self.add_widget(self.description)
        self.add_widget(self.time_spent)
        self.add_widget(start_btn)
        self.add_widget(stop_btn)
        self.add_widget(self.start_label)
        self.add_widget(self.stop_label)

    def start_timer(self, _):
        self.start_time = datetime.now()
        self.start_label.text = f"Start time: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}"
        self.stop_label.text = "Stop time: -"
        self.time_spent.text = ""

    def stop_timer(self, _):
        if not self.start_time:
            self.stop_label.text = "Stop time: Start time not set"
            return

        self.stop_time = datetime.now()
        self.stop_label.text = f"Stop time: {self.stop_time.strftime('%Y-%m-%d %H:%M:%S')}"

        delta = self.stop_time - self.start_time
        minutes = int(delta.total_seconds() // 60)
        self.time_spent.text = str(minutes)


class TimeTrackerApp(App):
    def build(self):
        return TimeTrackerLayout()


TimeTrackerApp().run()
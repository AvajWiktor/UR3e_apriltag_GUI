
class MainController:
    def __init__(self, main_model):
        self.main_model = main_model

    def detect_tag(self, tag_id):
        return self.main_model.detect_tag(tag_id)

    def connect_to_robot(self):
        self.main_model.connect_to_robot()

    def move_to_tag(self):
        self.main_model.move_to_tag()

    def move_to_target(self):
        self.main_model.move_to_target()

    def go_home(self):
        self.main_model.go_home()
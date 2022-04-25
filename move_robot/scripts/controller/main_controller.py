
class MainController:
    def __init__(self, robot_model, main_model):
        self.robot_model = robot_model
        self.main_model = main_model

    def detect_tag(self, tag_id):
        return self.main_model.detect_tag(tag_id)

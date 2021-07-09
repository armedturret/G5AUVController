class AUVController(object):
    def __init__(self, auv_state):
        self.__auv_state = auv_state
        self.__desired_heading = 0.0

    def get_desired_heading(self):
        return self.__desired_heading

    def decide(self, auv_state, gnext, rnext):
        self.__auv_state = auv_state
        return None 
class AUVController(object):
    def __init__(self, auv_state):
        self.__auv_state = auv_state
        self.__desired_heading = 0.0
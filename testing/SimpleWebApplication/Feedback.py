# Feedback class
class Feedback:
    count_id = 0

    # initializer method
    def __init__(self, first_name, last_name, gender, membership, remarks, email):
        Feedback.count_id += 1
        self.__feedback_id = Feedback.count_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__membership = membership
        self.__remarks = remarks
        self.__email = email


    # accessor methods
    def get_feedback_id(self):
        return self.__feedback_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_email(self):
        return self.__email

    def get_gender(self):
        return self.__gender

    def get_membership(self):
        return self.__membership

    def get_remarks(self):
        return self.__remarks



    # mutator methods
    def set_feedback_id(self, feedback_id):
        self.__feedback_id = feedback_id

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_email(self, email):
        self.__email = email

    def set_gender(self, gender):
        self.__gender = gender

    def set_membership(self, membership):
        self.__membership = membership

    def set_remarks(self, remarks):
        self.__remarks = remarks



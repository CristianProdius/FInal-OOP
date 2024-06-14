from enum import Enum

class StudyField(Enum):
    MECHANICAL_ENGINEERING = "MECHANICAL_ENGINEERING"
    SOFTWARE_ENGINEERING = "SOFTWARE_ENGINEERING"
    FOOD_TECHNOLOGY = "FOOD_TECHNOLOGY"
    URBANISM_ARCHITECTURE = "URBANISM_ARCHITECTURE"
    VETERINARY_MEDICINE = "VETERINARY_MEDICINE"

    @staticmethod
    def validation(field):
        return field in StudyField.__members__
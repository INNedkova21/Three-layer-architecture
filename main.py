from presentation_layer.presentation import PresentationLayer
from business_logic_layer.business_logic import BusinessLogicLayer
from data_access_layer.data_access import DataAccessLayer

if __name__ == "__main__":
    data_access = DataAccessLayer()
    business_logic = BusinessLogicLayer(data_access)
    presentation = PresentationLayer(business_logic)

    presentation.run()
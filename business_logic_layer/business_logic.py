class BusinessLogicLayer:
    def __init__(self, data_access):
        self.data_access = data_access

    def process_data(self, data):
        print("Business Logic Layer")
        processed_data = data.upper()
        return self.data_access.save_data(processed_data)
class PresentationLayer:
    def __init__(self, business_logic):
        self.business_logic = business_logic

    def run(self):
        print("Presentation Layer")
        data = input("Enter data: ")
        processed_data = self.business_logic.process_data(data)
        print(f"Processed data: {processed_data}")
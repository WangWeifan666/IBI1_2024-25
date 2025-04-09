class Patient:
    def __init__(self, patient_name, age, date_of_latest_admission, medical_history):
        """
        Initialize a patient object
    
        """
        self.patient_name = patient_name
        self.age = age
        self.date_of_latest_admission = date_of_latest_admission
        self.medical_history = medical_history

    def print_patient_details(self):
        """
        Print the details of the patient.

        """
        print(f"Patient Name: {self.patient_name}, Age: {self.age}, "
              f"Date of Latest Admission: {self.date_of_latest_admission}, "
              f"Medical History: {self.medical_history}")


# Example
patient1 = Patient("Jame", 30, "2025-04-07", "History of mild cold")
patient1.print_patient_details()    
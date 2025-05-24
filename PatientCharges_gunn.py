print("Patient Charges Program")
print("------------")
print()

class Patient:
    def __init__(self, firstname, middlename, lastname, address, city, state, zip1, phone, emerg_name, emerg_num):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.address = address
        self.city = city
        self.state = state
        self.zip1 = zip1
        self.phone = phone
        self.emerg_name = emerg_name
        self.emerg_num = emerg_num

    def __str__(self):
        return f"Name: {self.firstname} {self.middlename} {self.lastname}  \nAddress: {self.address}, {self.city}, {self.state}, {self.zip1} \nPhone: {self.phone} \nEmergency Contact: {self.emerg_name} \nEmergency Number: {self.emerg_num}"



class Procedure: 
        def __init__(self,proc_name, date, doc,  charges):
            self.proc_name = proc_name
            self.date = date
            self.doc = doc
            self.charges = charges

       
        def __str__(self): 
         return f"Procedure name: {self.proc_name} \nDate: {self.date} \nPractitioner: {self.doc} \nCharges: ${self.charges}"




def main():
    patient = Patient("Marvin", "Harvin", "Phillips", "34786 Apple Pie", "Honda", "IL", "60706", "123-555-5637", "James Bo", "123-555-4332")
    proc_1 = Procedure("Physical Exam", "04-19-25", "Dr. Irvine", "250.00")
    proc_2 = Procedure("X-ray", "04-19-25", "Dr. Jamison", "500.00")
    proc_3 = Procedure("Blood test", "04-19-25", "Dr. Smith", "200.00")






    print("Patient Info:")
    print(patient)
    print()
    print()
    print("Procedure Info")
    print("---------------")
    print()
    print(proc_1)
    print()
    print(proc_2)
    print()
    print(proc_3)





if __name__ =="__main__":
 main()
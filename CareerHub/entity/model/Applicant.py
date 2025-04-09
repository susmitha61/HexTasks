import pyodbc

class Applicant:
    def __init__(self, applicant_id=None, first_name=None, last_name=None, email=None, phone=None, resume=None):
        self.__applicant_id = applicant_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone = phone
        self.__resume = resume  # New attribute for Resume

    # Getters
    @property
    def applicant_id(self): return self.__applicant_id
    @property
    def first_name(self): return self.__first_name
    @property
    def last_name(self): return self.__last_name
    @property
    def email(self): return self.__email
    @property
    def phone(self): return self.__phone
    @property
    def resume(self): return self.__resume  # Getter for resume

    # Setters
    @applicant_id.setter
    def applicant_id(self, value): self.__applicant_id = value
    @first_name.setter
    def first_name(self, value): self.__first_name = value
    @last_name.setter
    def last_name(self, value): self.__last_name = value
    @email.setter
    def email(self, value): self.__email = value
    @phone.setter
    def phone(self, value): self.__phone = value
    @resume.setter
    def resume(self, value): self.__resume = value  # Setter for resume

    def __str__(self):
        return f"Applicant(applicant_id={self.applicant_id}, name='{self.first_name} {self.last_name}')"

    # Database connection (Assuming DBPropertyUtil for connection)
    @staticmethod
    def get_connection():
        connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=YOUR_SERVER;DATABASE=YOUR_DATABASE;Trusted_Connection=yes'
        return pyodbc.connect(connection_string)

    # CRUD Operations with SQL Queries

    @staticmethod
    def create_applicant(connection, first_name, last_name, email, phone, resume):
        query = """INSERT INTO Applicants (FirstName, LastName, Email, Phone, Resume)
                   VALUES (?, ?, ?, ?, ?)"""
        cursor = connection.cursor()
        cursor.execute(query, (first_name, last_name, email, phone, resume))
        connection.commit()
        print(f"Applicant '{first_name} {last_name}' added successfully!")

    @staticmethod
    def read_all_applicants(connection):
        query = "SELECT * FROM Applicants"
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

        applicants = []
        for row in result:
            applicant = Applicant(applicant_id=row[0], first_name=row[1], last_name=row[2], email=row[3], phone=row[4], resume=row[5])
            applicants.append(applicant)
        return applicants

    @staticmethod
    def read_applicant_by_id(connection, applicant_id):
        query = "SELECT * FROM Applicants WHERE ApplicantID = ?"
        cursor = connection.cursor()
        cursor.execute(query, (applicant_id,))
        result = cursor.fetchone()

        if result:
            return Applicant(applicant_id=result[0], first_name=result[1], last_name=result[2], email=result[3], phone=result[4], resume=result[5])
        return None

    @staticmethod
    def update_applicant(connection, applicant_id, first_name=None, last_name=None, email=None, phone=None, resume=None):
        applicant = Applicant.read_applicant_by_id(connection, applicant_id)
        if applicant:
            query = """UPDATE Applicants 
                       SET FirstName = ?, LastName = ?, Email = ?, Phone = ?, Resume = ?
                       WHERE ApplicantID = ?"""
            cursor = connection.cursor()
            cursor.execute(query, (first_name or applicant.first_name,
                                   last_name or applicant.last_name,
                                   email or applicant.email,
                                   phone or applicant.phone,
                                   resume or applicant.resume,
                                   applicant_id))
            connection.commit()
            print(f"Applicant with ID {applicant_id} updated successfully!")
        else:
            print(f"Applicant with ID {applicant_id} not found.")

    @staticmethod
    def delete_applicant(connection, applicant_id):
        query = "DELETE FROM Applicants WHERE ApplicantID = ?"
        cursor = connection.cursor()
        cursor.execute(query, (applicant_id,))
        connection.commit()
        print(f"Applicant with ID {applicant_id} deleted successfully!")

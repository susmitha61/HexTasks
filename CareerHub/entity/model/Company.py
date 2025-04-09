import pyodbc

class Company:
    def __init__(self, company_id=None, company_name=None,  location=None):
        self.__company_id = company_id
        self.__company_name = company_name
        self.__location = location

    # Getters
    @property
    def company_id(self): return self.__company_id
    @property
    def company_name(self): return self.__company_name
    @property
    def location(self): return self.__location

    # Setters
    @company_id.setter
    def company_id(self, value): self.__company_id = value
    @company_name.setter
    def company_name(self, value): self.__company_name = value

    @location.setter
    def location(self, value): self.__location = value

    def __str__(self):
        return f"Company(company_id={self.company_id}, name='{self.company_name}')"

    @staticmethod
    def create_company(connection, company_name, location):
        """
        Creates a new company in the Companies table.
        """
        query = """INSERT INTO Companies (CompanyName, Location)
                          VALUES (?, ?)"""
        params = (company_name, location)

        # Using cursor to execute the query
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()  # Commit the transaction
        print(f"Company '{company_name}' added successfully!")

    @staticmethod
    def read_all_companies(connection):
        """
        Fetches all companies from the Companies table.
        """
        query = "SELECT * FROM Companies"

        # Using cursor to execute the query
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

        companies = [Company(company_id=row[0], company_name=row[1], location=row[2]) for row in result]
        return companies

    @staticmethod
    def read_company_by_id(connection, company_id):
        """
        Fetches a company by its ID from the Companies table.
        """
        query = "SELECT * FROM Companies WHERE CompanyID = ?"
        params = (company_id,)

        # Using cursor to execute the query
        cursor = connection.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()

        if result:
            row = result[0]
            return Company(company_id=row[0], company_name=row[1], location=row[2])
        return None

    @staticmethod
    def update_company(connection, company_id, company_name=None, location=None):
        """
        Updates a company in the Companies table based on the company_id.
        """
        query = """UPDATE Companies 
                          SET CompanyName = ?, Location = ?
                          WHERE CompanyID = ?"""
        params = (company_name, location, company_id)

        # Using cursor to execute the query
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()  # Commit the transaction
        print(f"Company with ID {company_id} updated successfully!")

    @staticmethod
    def delete_company(connection, company_id):
        """
        Deletes a company from the Companies table by its ID.
        """
        query = "DELETE FROM Companies WHERE CompanyID = ?"
        params = (company_id,)

        # Using cursor to execute the query
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()  # Commit the transaction
        print(f"Company with ID {company_id} deleted successfully!")



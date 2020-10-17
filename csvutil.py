import csv

class CSV_Util():

    # login_data is a list of dictionaries taken from the csv file
    login_data = []

    def __init__(self):
        f = open("login_data.csv")
        csv_data = csv.DictReader(f)
        print(csv_data)
        for row in csv_data:
            self.login_data.append(row)
        f.close()

    def add_new_user(self, website, username, password):
        self.login_data[username] = password

    def update_csv(self):
        with open('LoginData.csv', 'w', newline='') as csvfile:
            fieldnames = ['name', 'password']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for key in self.login_data:
                writer.writerow({'name': key, 'password': self.login_data[key]})
        csvfile.close()

import csv

class CSV_Util():

    # login_data is a list of dictionaries taken from the csv file
    login_data = []

    def __init__(self):
        f = open("login_data.csv")
        csv_data = csv.DictReader(f)
        for row in csv_data:
            self.login_data.append(row)
        f.close()

    def add_new_password(self, website, username, password):
        new_password = {'website': website, 'username': username, 'password': password}
        self.login_data.append(new_password)

    def update_csv(self):
        with open('login_data.csv', 'w', newline='') as csvfile:
            fieldnames = ['website', 'username', 'password']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for row in self.login_data:
                writer.writerow({'website': row['website'], 'username': row['username'], 'password': row['password']})
        csvfile.close()

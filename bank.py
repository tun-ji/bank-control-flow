class Bank:
    clients = []

    # This function adds instantiated users to the client list
    def updater(self, client):
        self.clients.append(client)

    # This function iterates through the list of clients and checks to make sure the name and pin are correct
    def login(self, name, pin):
        for i in range(len(self.clients)):
            if name in self.clients[i].account.values() and pin in self.clients[i].account.values():
                print("Successfully logged in!")
                return self.clients[i]


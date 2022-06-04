from ApiService import ApiServiceInterface
import abc
"https://realpython.com/python-interface/"
class ApiServiceImplementation(ApiServiceInterface) :

    def __init__(self, host):
        self.host = host

    def load_data(self):
        return "Hello"

    def send_data(self, body: dict[str, str]):
        return body

if __name__ == "__main__":
    apiServiceImplementation = ApiServiceImplementation("0.0.0.0")
    print(apiServiceImplementation.load_data())
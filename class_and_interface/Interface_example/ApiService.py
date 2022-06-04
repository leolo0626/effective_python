import abc
class ApiServiceInterface(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def load_data(self):
        raise NotImplementedError("Load data must be implemented")

    @abc.abstractmethod
    def send_data(self, body: dict[str, str]):
        raise NotImplementedError("Send data must be implemented")

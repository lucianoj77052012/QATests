from abc import ABC, abstractmethod

class AbstractFrontend(ABC):

    @abstractmethod
    def navigate_to_url(self, url):
        pass
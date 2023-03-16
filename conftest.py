import pytest

class User:
    def __init__(self, age) -> None:
        self.age = age
    
    def RemoveAge(self) -> None:
        self.age = None

@pytest.fixture(scope="session")
def user():
    #pre-condition
    print("\nUser is created.")
    user = User(5)

    #test scenario
    yield user

    # post-condition
    print("\nUser's age is deleted.")
    user.RemoveAge
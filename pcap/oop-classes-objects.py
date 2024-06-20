class User:
    def __init__(self, user_nickname: str, user_city: str) -> None:
        """
        Creates user object
        :type user_nickname: str
        :type user_city: str
        """
        self.nickname = user_nickname
        self.city = user_city

    def introduce(self) -> None:
        """
        Introduce user
        :rtype: None
        """
        print("Hello, I am", self.nickname, "and I live in", self.city)


sample_user = User("Henia", "Berlin")
sample_user.introduce()

class Profile:
    username: str
    followers: list[str]
    following: list[str]
     
     def __init__(self, handle: str):
        self.username = handle
        self.followers = []
        self.following = []
    
    # Method definitions
    def follow(self, username: str) -> None:
        self.following.append(username)

     def following_count(self) -> int:
        return len(self.following)

my_prof: Profile = Profile("comp110fan") # Calls __init__()

my_prof.follow("hack110_unc")
print(my_prof.following_count())
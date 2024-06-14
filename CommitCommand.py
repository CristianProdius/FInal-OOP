from Commit import Commit

class CommitCommand:
    @staticmethod
    def invoke():
        Commit.make_commit()
        print("Commit performed!")
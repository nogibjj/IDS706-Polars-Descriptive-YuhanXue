from main import *


def test():
    data = pl.read_csv("diabetes.csv")
    assert data["Age"].mean() == get_mean(data, "Age")


if __name__ == "__main__":
    test()
    print("CICD Passed.")

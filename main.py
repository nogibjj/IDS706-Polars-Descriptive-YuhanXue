import polars as pl
import matplotlib.pyplot as plt


def get_mean(df: pl.DataFrame, col: str):
    return df[col].mean()


def get_median(df: pl.DataFrame, col: str):
    return df[col].median()


def get_stddev(df: pl.DataFrame, col: str):
    return df[col].std()


def get_scatter_plot(
    df: pl.DataFrame, xcol: str, ycol: str, title: str, xlabel: str, ylabel: str
):
    plt.scatter(df[xcol], df[ycol])
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.savefig(xlabel + "_vs_" + ylabel + ".png", dpi=300)
    plt.show()


if __name__ == "__main__":
    data = pl.read_csv("diabetes.csv")
    print(data.describe())
    print("=====================================")
    print("Data Report")
    for c in data.columns:
        print("============ " + c + " ============")
        print("Mean:", get_mean(data, c))
        print("Median:", get_median(data, c))
        print("Std Dev:", get_stddev(data, c))
    print("=====================================")
    get_scatter_plot(data, "Age", "BMI", "Age vs. BMI", "Age", "BMI")

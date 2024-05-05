import pandas as pd
import matplotlib.pyplot as plt
def tutorial():
    series = pd.Series(data=["UK", "France", "Italy"], index=["a", "b", "c"], name="country")
    
    

    series = pd.Series(data={"a": "UK", "b": "France", "c": "Italy"}, index=["b", "c", "d", "a"])
    print(series)

    print(series["a"])

    print(series[["c", "b"]])

def opgave2():
    df = pd.read_csv(r"Pandas\recipeData.csv", encoding='ISO-8859-1')
    før = len(df)
    df.dropna(inplace=True)  
    efter = før - len(df)
    print(f"Fjernet:{efter} rækker")
    fig = plt.figure("PrimaryTemp")
    axis = df["PrimaryTemp"].plot.hist()
    plt.show()
    fig = plt.figure("BoilGravity")
    axis = df["BoilGravity"].plot.hist()
    plt.show()
    return df

def main():
    df = opgave2()
    tutorial()
main()

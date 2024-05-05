import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.datasets import load_iris

def opgave1(dataset):
    sns.scatterplot(data=dataset, x="sepal_length", y="sepal_width", hue="species")
    plt.xlabel("Sepal Length")
    plt.ylabel("Sepal Width")
    plt.title("Sepal Length vs Sepal Width")
    plt.legend(title='Species')
    plt.show()

def opgave2(dataset):
    fig = px.scatter(dataset, x="sepal_length", y="sepal_width", color="species",
                    title="Sepal Length vs Sepal Width",
                    labels={"sepal_length": "Sepal Length (cm)", "sepal_width": "Sepal Width (cm)"},
                    hover_data={"species": True})
    fig.show()

# Example usage
iris = load_iris()
random_dataset = sns.load_dataset("iris")

opgave1(random_dataset)
opgave2(random_dataset)

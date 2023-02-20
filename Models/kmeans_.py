from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
import seaborn as sns
import matplotlib.pyplot as plt

def kmeans(df,cluster_numbers):
    kmeans = KMeans(n_clusters=cluster_numbers,random_state=1)
    kmeans.fit(df)

    cluster_labels = kmeans.labels_
    df_new = df.assign(Cluster = cluster_labels)

    model = TSNE()
    transformed = model.fit_transform(df)

    plt.title(f"Graph of {cluster_numbers} clusters.")
    sns.scatterplot(x=transformed[:,0],y = transformed[:,1],hue=cluster_labels,style=cluster_labels,palette="Set1")

    return df_new, cluster_labels
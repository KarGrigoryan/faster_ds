from sklearn import preprocessing  # to normalise existing X
from sklearn import cluster




class ClusterInterface:
        @staticmethod
        def method1(self, path: str, file_name: str) -> str:
            """method description"""
            pass

        @staticmethod
        def method2(self, full_file_name: str) -> dict:
            """method description"""
            pass






class cluster_model:
        @staticmethod
        def data_normalization(X):
            """
            X_norm ---> dataframe
            """
            X_Norm = preprocessing.normalize(X)
            return X_Norm

        
        @staticmethod
        def km_labels(X_norm, n_clusters=5):
            """
            X_norm---> normed dataframe
            """
            km2 = cluster.KMeans(n_clusters=n_clusters,init='random').fit(X_Norm)
            labels = km2.labels_
            labels = np.unique(labels)
            return labels
        
        
        @staticmethod
        def km_centers(X_norm, n_clusters=5):
            """
            X_norm---> normed dataframe
            """
            km2 = cluster.KMeans(n_clusters=n_clusters,init='random').fit(X_Norm)
            return km2.cluster_centers_
        
        
        @staticmethod
        def plot_km(X_norm, labels):
            #labels=km2.labels_
            plt.scatter(X_Norm[:,0],X_Norm[:,2], c=labels, cmap='rainbow')
            plt.show()

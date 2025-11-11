import pandas

class dump_data():

    def pull_data(self, file_name, topic, ourlier = False):
        pull_d = []
        df = pandas.read_csv(file_name)
        # pull_d = df[topic]
        # print(df[topic].quantile(0.25), df[topic].quantile(0.75), sep="\t")

        for i in df[topic]:
            pull_d.append(i)
    
        if ourlier:
            outliner = self.find_outliers_IQR(df[topic])
            # print(outliner)

        return pull_d
    
    def pull_allTocip(self, file_name, ourlier=True):
        pullAll_d = []
        tocip = []
        df = pandas.read_csv(file_name)
        for i in df:
            # print(df[i])
            tocip.append(i)
            pullAll_d.append(df[i])

        return tocip, pullAll_d
        

    def find_outliers_IQR(self,df):

        q1=df.quantile(0.25)

        q3=df.quantile(0.75)

        IQR=q3-q1

        outliers = df[((df<(q1-1.5*IQR)) | (df>(q3+1.5*IQR)))]

        return outliers
            

if __name__ == "__main__":
    d_data = dump_data()

    data = d_data.pull_allTocip("TESTlab/csvTest/tocips_file_20241003_033340.csv", ourlier=True)
    print(data)
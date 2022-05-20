
class CombineDataAndMetData:

    def __init__(self,input_data=None,meta_data=None):
        self.operation='Combine metadata with data'
        self.data=input_data
        self.meta_data=meta_data

    def create_metadata_column(self):
        self.data['Metadata_Condition']=''

    def add_condition_to_data(self):
        for x in range(0,self.data['Metadata_Well'].__len__()):
            condition=self.meta_data.loc[self.data['Metadata_Well'][x]==self.meta_data['Metadata_Well'],'Compound']
            print(condition)
            self.data[x,'Metadata_Condition']=condition[0]



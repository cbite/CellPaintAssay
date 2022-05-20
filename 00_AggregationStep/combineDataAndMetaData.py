import pandas as pd

class CombineDataAndMetData:

    def __init__(self,input_data=None,meta_data=None):
        self.operation='Combine metadata with data'
        self.data=input_data
        self.meta_data=meta_data
        self.compound_array=None

    def add_condition_to_data(self):
        compound_array=[]
        for x in range(0,self.data['Metadata_Well'].__len__()):
            well_input_data=self.data['Metadata_Well'][x]
            compound_in_well=self.meta_data.loc[self.meta_data['Metadata_Well']==well_input_data,'Compound'].values[0]
            compound_array.append(compound_in_well)
        df_compound_array=pd.DataFrame({'Metadata_Condition':compound_array})
        self.data_with_meta_data=pd.concat([self.data,df_compound_array],axis=1)

    def write_combined_data_output(self):
        self.data_with_meta_data.to_csv('Data_with_metadata.csv',sep=',',index=False)
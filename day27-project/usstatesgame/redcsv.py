'''
reading states csv file and arranging the coordinates

'''
import pandas
class Readcsv:
    def __init__(self):
        self.filename ="50_states.csv"
        self.data = pandas.read_csv("50_states.csv")
        #self.data_dict = data.to_dict()
        self.states= self.data["state"].to_list()
        self.x =self.data["x"].to_list()
        self.y=self.data["y"].to_list()

    def check_state(self,state):
        state =state.title()
        count =0
        for i in self.states:
            if(state ==i):
                self.state_nmae =state
                x_value = self.x[count]
                y_value =self.y[count]
                return (x_value,y_value)
            count+=1






    def get_name(self):
        return self.state_nmae
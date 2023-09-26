import csv

class System:
    def __init__(self):
        self.sensors_list = list()
        self.sensor_mapping_list = list()
        self.master_node_list = list()
        
    def config_system(self, file):
        data_file = open(file, 'r')
        reader = csv.DictReader(data_file)
        for row in reader:
            node_id = row['Node ID']
            type = row['Type']
            master_node_id = row['Master Node ID']
            
            if type == 'Master':
                self.master_node_list.append(int(master_node_id))
            elif type == "Sensor":
                self.sensors_list.append(int(node_id))
                self.sensor_mapping_list.append(int(master_node_id))
                
        
    def SensorAssignedCount(self, mapping_list, l, r, OverloadSensor):
        count = 0
        for i in range(l, r+1):
            if (mapping_list[i] == OverloadSensor): 
                count +=  1
        return count
    
    def OverloadNodeHelper(self,l, r):#O(nlogn)==> 2T(n/2) + n
        



       if r > l:
            mid = l + (r - l - 1) // 2   #divide
            self.OverloadNodeHelper(l, mid)  #conquer
            self.OverloadNodeHelper(mid + 1, r)  #conquer
            first_half = mid - 1 +1
            second_half = r - mid
            L = [0] * first_half
            R = [0] * second_half              
            overload_limit = len(self.sensors_list)//2
            ret_val = -1
            for node in self.master_node_list:
                if node in self.sensor_mapping_list:
                    count = self.SensorAssignedCount(self.sensor_mapping_list, 0, len(self.sensor_mapping_list)-1, node)
                    if count>=overload_limit:
                            ret_val = node
            return ret_val
            
                
        #pass
        
    def getOverloadedNode(self):
        return self.OverloadNodeHelper(0, len(self.sensor_mapping_list)-1)
    
    def getPotentialOverloadNode(self):
        first_half=len(self.sensor_mapping_list)//3
        second_half= len(self.sensor_mapping_list)//2
        return_value=-1
        for i in self.master_node_list:
            if i in self.sensor_mapping_list:
                count = self.SensorAssignedCount(self.sensor_mapping_list,0,len(self.sensor_mapping_list)-1,i)
                if first_half <= count < second_half:
                    return_value = i

                    
        return return_value
#        pass
    
if __name__ == "__main__":
    test_system1 = System()
    
    test_system1.config_system('app_data1.csv')
    
    print("Overloded Master Node : ", test_system1.getOverloadedNode())
    
    print("Partially Overloaded Master Node : ", test_system1.getPotentialOverloadNode())

    test_system2 = System()
    
    test_system2.config_system('app_data2.csv')
    
    print("Overloded Master Node : ", test_system2.getOverloadedNode())
    
    print("Partially Overloaded Master Node : ", test_system2.getPotentialOverloadNode())

    test_system3 = System()

    test_system3.config_system('app_data3.csv')
    
    print("Overloded Master Node : ", test_system3.getOverloadedNode())
    
    print("Partially Overloaded Master Node : ", test_system3.getPotentialOverloadNode())

    test_system4 = System()

    test_system4.config_system('app_data4.csv')
    
    print("Overloded Master Node : ", test_system4.getOverloadedNode())
    
    print("Partially Overloaded Master Node : ", test_system4.getPotentialOverloadNode())

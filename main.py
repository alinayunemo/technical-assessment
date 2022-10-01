
import json


data=open("data.json")

data=json.load(data)


# check if "Name" is existing or not
if data.get("Name")==None:
    print("no key = Name in your data")   
else:
   print("Name = "+data["Name"]  )    

# check if "CanRelist" is existing or not
if data.get("CanRelist")==None:
    print("no key = CanRelist in your data")   
else:
   print("CanRelist = "+str(data["CanRelist"] ) )   
   
# check if "Promotions" is existing or not
if data.get("Promotions"):
    Promotions=data["Promotions"]
    for dict_list in Promotions:
                # find the Feacture in Promotions dict list  
                if ("Feature" in dict_list.values()): 
                    print("Name ="+dict_list["Name"])
                    print("Description ="+dict_list["Description"])
else:
    print("no key = Promotions in your data!")  
    
                       
       
    
    
                    
            
                  
                  
    
    



import pickle
path = "./models/"

def writeModel(model, filename, extrapath=""): 
    pickle.dump(model, open(path+extrapath+filename, 'wb'))





def readModel(filename, extrapath=""):
    loaded_model = pickle.load(open(path+extrapath+filename, 'rb'))
    return loaded_model
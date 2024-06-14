import numpy as np

def calculate(list):
    #Calculations is a dictionary to save the results 
    calculations = {}
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
    
    else:
        a = np.reshape(list, (3, 3))

        # format 'calculation': [(on columns), (on rows), (on the flattened list)]
        calculations.update({'mean': [np.mean(a, axis=0).tolist(), np.mean(a, axis=1).tolist(), np.mean(a).tolist()]})
        calculations.update({'variance': [np.var(a, axis=0).tolist(), np.var(a, axis=1).tolist(), np.var(a).tolist()]})
        calculations.update({'standard deviation': [np.std(a, axis=0).tolist(), np.std(a, axis=1).tolist(), np.std(a).tolist()]})
        calculations.update({'max': [np.max(a, axis=0).tolist(), np.max(a, axis=1).tolist(), np.max(a).tolist()]})
        calculations.update({'min': [np.min(a, axis=0).tolist(), np.min(a, axis=1).tolist(), np.min(a).tolist()]})
        calculations.update({'sum': [np.sum(a, axis=0).tolist(), np.sum(a, axis=1).tolist(), np.sum(a).tolist()]})
    
        return calculations

import pandas as pd
import numpy as np
from . models import Bankdata


def bank_update(data):
    bank = pd.read_csv(data) # Read data from csv files
    n_bank = np.array(bank.values) #Converted datasets in csv as array objects
    for k in n_bank.tolist():
        # Get dataset values into database
        db  =  Bankdata(IFSC=str(k[0]),Bank_id=str(k[1]),Branch=k[2],Address=k[3],City=k[4],District=k[5],State=k[6],BankName=k[7])
        db.save()


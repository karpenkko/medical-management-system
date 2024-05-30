import pandas as pd
import os

FILE_PATH = "students.csv"

def studentData():
    if not os.path.exists(FILE_PATH):
        df = pd.DataFrame(columns=["StdID", "Firstname", "Surname", "DoB", "Age", "Gender", "Address", "Mobile"])
        df.to_csv(FILE_PATH, index=False)

def addStdRec(StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile):
    df = pd.read_csv(FILE_PATH)
    StdID = int(StdID)
    Age = int(Age)
    new_record = {"StdID": StdID, "Firstname": Firstname, "Surname": Surname, "DoB": DoB, "Age": Age, "Gender": Gender, "Address": Address, "Mobile": Mobile}
    df = df._append(new_record, ignore_index=True)
    df.to_csv(FILE_PATH, index=False)

def viewData():
    df = pd.read_csv(FILE_PATH)
    return df.values.tolist()

def deleteRec(id):
    df = pd.read_csv(FILE_PATH)
    df = df[df["StdID"] != id]
    df.to_csv(FILE_PATH, index=False)

def searchData(StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile):
    df = pd.read_csv(FILE_PATH)
    mask = (
        (df["StdID"] == StdID) |
        (df["Firstname"] == Firstname) |
        (df["Surname"] == Surname) |
        (df["DoB"] == DoB) |
        (df["Age"] == Age) |
        (df["Gender"] == Gender) |
        (df["Address"] == Address) |
        (df["Mobile"] == Mobile)
    )
    return df[mask].values.tolist()

def dataUpdate(StdID, new_StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile):
    df = pd.read_csv(FILE_PATH)
    new_StdID = int(new_StdID)
    Age = int(Age)
    print(StdID)
    df.loc[df["StdID"] == StdID, ["StdID", "Firstname", "Surname", "DoB", "Age", "Gender", "Address", "Mobile"]] = [new_StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile]
    df.to_csv(FILE_PATH, index=False)

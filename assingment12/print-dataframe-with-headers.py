import pandas as pd
class DFPlus(pd.DataFrame):
    @property
    def _constructor(self):
        return DFPlus
    
    @classmethod
    def from_csv(cls, filepath, **kwargs):
        df = pd.read_csv(filepath, **kwargs)
        return cls(df)
    
    def print_with_headers(self):
        x = len(self)
        pos = 0
        while pos < x:
            print(super().iloc[pos:pos+10])
            pos += 10
            if pos < x:
                input("\nPress Enter to continue: \n")

dfp = DFPlus.from_csv("../csv/products.csv")
dfp.print_with_headers
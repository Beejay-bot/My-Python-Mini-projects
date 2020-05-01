class Table:


    def __init__(self, filename):

        self.filename  = filename

        col_data = self.get_col_names()
        row_data = self.get_num_rows()
        # maxiumum_no = self.get_maxiumum_no
        # column_chooser = self.get_column

        self.col_names = col_data[1]
        self.col_count = col_data[0]
        self.row_count = row_data
        self.get_maxiumum_no = max 
        # self.get_column = column_chooser
    
    def get_col_names(self):

        col_row = open(self.filename, "r").readlines()[0]
        col_names = col_row.split(",")

        print("COLUMNS IN FILE : ")
        for name in (col_names):
            print(f"\t{name}")

        num_of_cols = len(col_names)
        
        return num_of_cols, col_names

    def get_num_rows(self):

        num_rows = len(open(self.filename, "r").readlines())-1

        return num_rows

    def get_numeric_cols(self):

        lines = open(self.filename, "r").readlines()
        lines.pop(0)

        list_of_tuples = map(lambda string: string.split(","), lines)

        unzipped_data = zip(*list_of_tuples)

        text_col = []
        num_col = []
        count = 0

        for line in unzipped_data:
            
            if not any(map(lambda x: x.replace(".", "").isnumeric(), line)):
                num_col.append(self.col_names[count])
            else:
                text_col.append(self.col_names[count])


            count += 1

        print(text_col)
        print(num_col)
            
    def _gt_(self,other):
        max_no = len(open(self.filename, "r").readlines())
        print("NUMBERS IN FILE : ")
        for no in (max_no):
            print(f"\t{no}")

        return max_no

    def get_column(self):
        column_chooser = (open(self.filename, "r").readlines())
        user_choice =  input("ENTER THE NAME OF THE COLUMN YOU WILL LIKE TO GET:")
        print(user_choice)
        for user_choice in column_chooser:
            return column_chooser

getting_the_column = (Table) 
Table.get_column(getting_the_column)

new_data = Table("DNMM_CDD_18C.csv")
print(new_data.filename)
new_data.col_names
print(new_data.row_count)
new_data.get_numeric_cols()

# file = open("DNMM_CDD_18C.csv", "r")
# print(len(file.readlines())-1)
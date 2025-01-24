import sys
import pandas as pd

def find_large_values(file_path1, threshold1, file_path2, threshold2):
    # Read the Excel file into a DataFrame
    df1 = pd.read_excel(file_path1, sheet_name="Percentages")
    df2 = pd.read_excel(file_path2, sheet_name="Counts")
    
    # Convert the DataFrame to a matrix (2D list)
    matrix = df1.values.tolist()
    matrix2 = df2.values.tolist()

    headers = df1.columns.tolist()
    
    # Find the row and column indices where values are larger than the threshold
    large_values_indices = []

    num_rows, num_columns = df1.shape


    for row_index in range(num_rows):
        for col_index in range(num_columns):
            
          
            if col_index <= 2:
                continue  

            value1 = matrix[row_index][col_index]  
            value2 = matrix2[row_index][col_index]
        

            if (value1 >= threshold1) and (value2 >= threshold2):
                large_values_indices.append(( headers[col_index], matrix[row_index][1], value2, value1))
    
    return large_values_indices

# Example usage

if len(sys.argv) != 5: 

    print("Usage: python percentage_count.py percentage_file percentage_threshold count_file count_threshold") 

    sys.exit(1) 


file_path1 = sys.argv[1]

file_path2 = sys.argv[3]

threshold1 = float(sys.argv[2])

threshold2 = int(sys.argv[4])

if threshold1 < 0 or threshold1 > 1: 

    print("Error: percentage threshold is not in range [0,1]") 
    exit(1)

data = find_large_values(file_path1, threshold1, file_path2, threshold2)

print("Percentage file:", file_path1) 
print("Percentage threshold:", threshold1) 
print("Count file:", file_path2) 
print("Count threshold:", threshold2) 

print("Output:")

for element in data: 

    print (element)


df = pd.DataFrame(data, columns=['Sample', 'Part2', "Count", "Percentage"])

# Write the DataFrame to an Excel file
df.to_excel('output.xlsx', index=False)

print("The result is written to output.xlsx.")


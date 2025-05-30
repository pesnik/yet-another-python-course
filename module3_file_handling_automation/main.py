def main():
    f = open('Microwave Link Report_05-19-2025_05-47-44.csv')
    
    lines = f.readlines()
    
    # Get total column count
    header_row = lines[0]
    columns = header_row.split(',')
    # print(len(columns))

    
    # print(columns[19])
 
    # for index in range(len(columns)):
    #     print(index, " no. columnt ti holo: ", columns[index])

    # 1 no column er naam holo 'x'
    # 2 no column er naam holo 'x'

    
    # Get the column ID for Source PLA Type
    i = 0
    limit = 107 # len(columns)

    while i < limit:
        # print(f"{i} no column ti holo: {columns[i]}")
        
        column_name = columns[i]
        if column_name == '"Source PLA Type"':
            print("Aho Vatija Aho!!!", i)
        
        i = i + 1
    
    # Which lines contains Source PLA Type as EPLA (Find First Occurence only)
    
    value_rows = lines[0:2]
    for line in value_rows:
        print(len(line.split(',')))
        columns = line.split(',')
        if columns[101] == 'EPLA':
            print("Eureka!!", columns[101])
            break
    
    
    
    
    f.close()


if __name__ == "__main__":
    main()

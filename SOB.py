import csv

with open('mempool.csv',"r") as data:
    everyrow = csv.reader(data, delimiter =',')   #Open the CSV file and read it

    for row in everyrow:
        for cell in row:
            output_val = row[0]
            # output_val_2 = row[1]
            # output_val_3 = row[2]
            # output_val_4 = row[4]

        print("The <txid>: ", output_val)         #Prints each txnids in new line
        # print("<Fee>: ", output_val_2)
        # print("<Weight>: ", output_val_3)
        # print("<Parents>: ", output_val_4)

    #
    # print("---------------------------------------------------------------------------------")
    #
    # to check for the existence of parent txnids if at all they exists in the printed output

    # if 'c357ca9bfc5d9690e11e135ca61383209a43f4ac7899c0815d08d06a21a67e28' in output_val:
    #     print("\nParent txids exist")
    # else:
    #     print("\nTried checking for parent_txids in the output, but no match found for parent_txnids !!")
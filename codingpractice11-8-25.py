try:
    sum = 0
    numFile = open('practicetext11-8-25.txt', 'r')
    # open the numbers.txt file
    #complete the for loop to continue reading so long as the file has more values
    for n in numFile:
        #complete the num statement below to store the next int in the file into num
        #remember by default the number will come from the file as a string and need to be converted to an int
        num = num.append(int(n))
        #this line prints out the num to make sure it is working
        print(num)
        #this line of code sums up all the numbers
        sum += num

    #displays the sum of the numbers
    print(sum)

    #close the file
    numFile.close()


except Exception as err:
    print(err)

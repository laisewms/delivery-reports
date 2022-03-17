#define a function to make it easier to change the files

def reports_generater(day,file):

    """This is a function that will generate the reports for the melon deliveries"""

#it will print the actual day
    print("Day ", day)

#it will open the files that will be passed as an argument
    the_file = open(file)

#iterate over each line in the file object
    for line in the_file:

        #it will remove the white spaces between the words
        line = line.rstrip()
    
        #creates a list of strings
        words = line.split('|')
 
        #assigning variables to each item in the list 
        melon = words[0]
        count = words[1]
        amount = words[2]

        print(f"Delivered {count} {melon}s for total of ${amount}")
        

    the_file.close()


reports_generater(1,'um-deliveries-day-1.txt')
reports_generater(2,'um-deliveries-day-2.txt')
reports_generater(3,'um-deliveries-day-3.txt')


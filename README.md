# python-challenge

Module_3_Challenge

PyBank

I added the os and csv modules. As I was writing the code I was setting my variables/counters but ended up having to place them all together at the top to keep things neat. I setup a path to retrieve the csv file and I ended up finding out that you can't run the code if any variables are outside of the "with" statement where I opened my csv file. So hence the reason I kept it all together. I defined my rows and columns to retrieve my total months and my net total. I then calculated the the changes for the entire period. I created an if statement so each month would be compared with the previous month and give the difference/change between the two. I made another if statement to keep record of the greatest increase and the greatest decrease. And finally I calculated the average of the profit/losses over the entire period with the exception of the first month since I didnt have any data before it to compare to. I then setup my print statements and my text file output.

PyPoll

I added the os and csv modules. I set my counters for the total amount of votes and the candidate votes. I set up the csv path to retrieve the csv file. I created a for loop that iterates through each row in the csv and counts the total number of votes. It also counts up the votes that each candidate receives and updates the empty dictionary, "candidate votes". I then calculated the percentage of votes by going through the candidate votes dictionary and calculating votes divided by total_votes and then multiply by 100. I then got the winner by using the max function to find the candidate with the highest number of votes. The keys parameter is used to find the the candidate name with the highest number of votes. I then setup my print statements and my text file output.

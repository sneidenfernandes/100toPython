Matka Simulation

Description of the Game

Welcome to the Matka Simulation Project! This simulation brings to life the exciting world of the Kalyan version of the popular Indian betting game called Matka. In this game, participants engage in random bets on a combination of numbers to cash.  This basic simulation outputs results presenting data on wins, losses, win rate, and return per unit amount bet.

Algorithm of the Game

Drawing Numbers (Patti): A set of three numbers is drawn from a list of cards. The specific cards used in this version of Matka are to be provided. This set of three numbers is known as the "patti." The patti is drawn twice a day, once in the morning and once in the evening.

Generating Open and Close Numbers: From each set of three numbers drawn, the digits are added together to create an open number and a close number. These numbers correspond to the morning and evening sessions of the draw, respectively. For example, if the patti drawn in the morning session is 5, 8, and 3, the open number would be 5+8+3 = 16 and the close number would be the last digit of the sum, i.e., 6.

Creating Jodi: The open and close digits are combined to form a "jodi," which is a two-digit number. For instance, if the open number is 16 and the close number is 6, the jodi would be 16-6.

Placing Bets on Jodi: In this simulation, the focus is on betting on the jodi. Participants can place bets on different jodi combinations. The odds of betting on a jodi are 90:1, meaning if you win, you'll receive 90 times your bet amount. Please note that there are multiple bets available in the full Matka game, but our simulation concentrates on the jodi bets.

File Structure

This project consists of two main files:

matka.py: This file contains the core logic and functions for simulating the Matka game, drawing numbers, generating open and close numbers and creating the jodi

simulation.py: In this file, the Matka simulation is run using the functions defined in matka.py. One can run n number of simulations by changing the input of the the 'kalyan.simulate(n)' method.

Libraries and Technologies Used

The Matka Simulation  is built using Python 3 and leverages the following libraries:

tqdm: This library provides a fast, extensible progress bar for loops and other iterable processes. It enhances the user experience by showing the progress of the simulation.

random: The random library is used to generate random numbers, essential for creating open and close numbers, and simulating the betting outcomes.


Disclaimer: Educational Purposes Only

This Matka Simulation Project is designed and developed solely for educational and learning purposes. The project's intent is to demonstrate the mechanics of the Matka game through a virtual simulation, offering insights into its rules and betting concepts. It is not intended for any form of gambling or real-world betting.


Feel free to explore the code in matka.py and simulation.py to understand the inner workings of the simulation and how the Matka game is brought to life in a virtual environment. Cheers!

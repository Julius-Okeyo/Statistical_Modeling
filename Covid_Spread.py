'''
KEY
P_I - Probability that a person picked at random is infected
      with covid-19.
      Equals the total number of infected people divided by
      the total population.
P_SS - Probability that a person picked at random is a superspreader.
P_SI - Probability that a superspreader interacts with another person.
P_NI - Probability that a non_superspreader interacts
        with another person.
P_N - Probability that a person contacts covid-19 from interacting
      with an infected person.

All measures are assumed to correspond to one day.
'''

global Total_Population
global Initial_Number_of_Infections
global P_I
global P_SS
global P_SI
global P_NI
global P_N
global Number_of_New_Infection

Number_of_New_Infections = 0
Total_Population = int(input('Total population: '))
Initial_Number_of_Infections = int(input('Initial number of infected persons: '))
P_I =  Initial_Number_of_Infections / Total_Population
P_SS = float(input('Probability of a randomly selected person being a superspreader: '))
P_SI = float(input('Average number of people a superspreader interacts with per day: ')) / Total_Population
P_NI = float(input('Average number of people a non-superspreader interacts with per day: ')) / Total_Population
P_N = float(input('Probability of a new infection resulting from an interaction: '))

def Probability_of_New_Infection(P_I,P_SS,P_SI,P_NI,P_N):
    global Number_of_New_Infections
    #Probability that a person is a superspreader and is infected with COVID-19.
    P_SS_I = P_SS * P_I
    #Probability that a superspreader interacts with a uninfected person.
    P_SI_I_n = P_SI * (1 - P_I)
    #Probability a new infection results from the interaction
    P1 = P_SS_I * P_SI_I_n * P_N
     #Probability that a person is a non-superspreader and is infected with COVID-19.
    P_NS_I = (1 - P_SS) * P_I
    #Probability that a non-superspreader interacts with a uninfected person.
    P_NI_I = P_NI * (1 - P_I)
    #Probability a new infection results from the interaction
    P2 = P_NS_I * P_NI_I * P_N

    Probability_of_New_Infection = P1 + P2
    Number_of_New_Infections = round(Probability_of_New_Infection * Total_Population)

def Time_Series_Projection(Number_of_Days):
    global P_I
    Total_Infection = Initial_Number_of_Infections
    for days in range (1,Number_of_Days+1):
        print(P_I)
        Probability_of_New_Infection(P_I,P_SS,P_SI,P_NI,P_N)
        Total_Infection += Number_of_New_Infections
        P_I = Total_Infection / Total_Population
    print('Total number of infected people: ',Total_Infection)
    return Total_Infection

Time_Series_Projection(30)
''' During the covid-19 pandemic one of the most crtical
aspects of the war was accurately predicting the number
of new infections over a given period of time. This code
may be used to predict the number of new infections likely
during a specific period given the following parameters.

KEY
P_I - Probability that a person picked at random is infected
      with covid-19 (Rate of infection).
      Equals the total number of infected people divided by
      the total population or total confirmed cases divided
      by the total tests conducted.
P_SS - Probability that a person picked at random is a superspreader.
Average number of people a superspreader interacts with daily.
Average number of people a non_superspreader interacts with daily.
P_N - Probability that a person contacts covid-19 from interacting
      with an infected person.

'''

global Total_Population
global Initial_Number_of_Infections
global P_I
global P_SS
global P_N
global Number_of_New_Infection
global Superspreader_Interactions
global Non_Superspreader_Interactions

Number_of_New_Infections = 0
Total_Population = int(input('Total population: '))
P_I =  float(input('Infection rate: '))
Initial_Number_of_Infections = P_I * Total_Population
P_SS = float(input('Probability of a randomly selected person being a superspreader: '))
Superspreader_Interactions = int(input('Average number of people a superspreader interacts with per day: '))
Non_Superspreader_Interactions = int(input('Average number of people a non-superspreader interacts with per day: '))
P_N = float(input('Probability of a new infection resulting from an interaction: '))

def Probability_of_New_Infection(P_I,P_SS,P_N):
    global Number_of_New_Infections
    #Probability that a person is a superspreader and is infected with COVID-19.
    P_SS_I = P_SS * P_I
    #Probability that a superspreader interacts with a uninfected person.
    P_SI_I_n = (1 - P_I)
    #Probability a new infection results from the interaction
    P1 = P_SS_I * P_SI_I_n * P_N
     #Probability that a person is a non-superspreader and is infected with COVID-19.
    P_NS_I = (1 - P_SS) * P_I
    #Probability that a non-superspreader interacts with a uninfected person.
    P_NI_I = (1 - P_I)
    #Probability a new infection results from the interaction
    P2 = P_NS_I * P_NI_I * P_N
    Number_of_New_Infections = round((P1 * Superspreader_Interactions) + (P2 * Non_Superspreader_Interactions))

def Time_Series_Projection(Number_of_Days):
    global P_I
    Total_Infection = Initial_Number_of_Infections
    for days in range (1,Number_of_Days+1):
        Probability_of_New_Infection(P_I,P_SS,P_N)
        Total_Infection += Number_of_New_Infections
        P_I = Total_Infection / Total_Population
    print('Total number of infected people: ',Total_Infection)
    return Total_Infection

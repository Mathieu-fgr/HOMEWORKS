#Part 1:Function that calculate the number of months needful to secure the down-payment
total_cost = int(input("What's the price of your dream house ?"))
annual_salary = int(input("What's your annual salary ?"))
def partie_3(portion_saved):
    mois = 0
    current_saving = 0
    monthly_salary = annual_salary/12
    while total_cost/4>= current_saving:
        mois += 1 
        current_saving+= monthly_salary*portion_saved
        interest = current_saving*0.07/12
        current_saving += interest
        #Part 3: if months are 6,12,18 etc... Each 6 months --> salary increase 
        if mois%6 == 0:
            monthly_salary*= 1.07
    return mois
#Part 4 : Recursive Function that verify if the down-payment can be reach
# If yes, this function return the needful portion to secure the down-payment in 36 months
def test(portion_saved):
    intervalle = [0,1] 
    compteur = 0
    valeur = 0
    if partie_3(1) > 36: 
        print("Impossible")
        
    else:
        while abs(intervalle[0] - intervalle[1]) > 1e-4: 
            mois = partie_3(portion_saved)
            if mois > 36:
                compteur += 1
                intervalle[0] = portion_saved
                portion_saved = (intervalle[0] + intervalle[1])/2
                valeur = portion_saved

            if mois < 36:
                compteur += 1
                intervalle[1] = portion_saved
                portion_saved = (intervalle[0] + intervalle[1])/2
                valeur = portion_saved

            if mois == 36:
                break
        print(f"There was {compteur} bissections")
        print(f"{valeur} for 36 months")
test(0.5)
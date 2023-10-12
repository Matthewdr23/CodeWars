# https://www.codewars.com/kata/5b7ea71db90cc0f17c000a5a/train/python



def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp) :
    m1_division = given_mass1 / molar_mass1
    m2_division = given_mass2 / molar_mass2
    m1_m2_addition = m1_division + m2_division
    T = temp + 273.15
    R = 0.082
    
    
    return (m1_m2_addition*(R*T))/volume 
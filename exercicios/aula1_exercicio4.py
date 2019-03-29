import math
cateto_oposto = 0.5
cateto_adjacente = 5
tangente_theta = cateto_oposto/cateto_adjacente
theta = math.atan(tangente_theta)

print('A sombra de um poste de 5 m de altura tem 50 cm de comprimento no chão')
print('O ângulo zenital do Sol é:')
print(theta, 'em radianos') 

theta_grau = (180*theta)/math.pi

print(theta_grau, 'em graus') 

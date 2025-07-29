/*--**Calcular gorjeta**
>>O programa deve receber um valor total da conta
>>O programa recebe a procentagem de gorjeta desejada
>>Exibir o valor final que o cliente pagará.
**Entrada**
Digite o valor da conta: 120.00  
Digite a porcentagem de gorjeta: 10  
**Saída**
Valor da gorjeta: R$ 12.00  
Total a pagar: R$ 132.00 */

valor_conta = float(input("Digite o valor da conta: ")) 
porc_gorjeta = float(input("Digite a porcentagem de gorjeta: ")) 
gorjeta = (porcentagem_gorjeta / 100) * valor_conta 
total_a_pagar = valor_conta + gorjeta 
print(f"Valor da gorjeta: R$ {gorjeta:.2f}") 
print(f"Total a pagar: R$ {total_a_pagar:.2f}")
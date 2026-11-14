import requests
headers ={
'Content-Type':'application/x-www-form-urlencoded',
'Accept':'application/json'
}
data = {
     'client':'AQUI_SU_CLIENT',
     'key':'AQUI_SU_KEY',
     'phone':'AQUI_EL_NUMERO_DE_CELULAR',#PARA ENVIAR MULTIPLES TELEFONOS TENDRAN QUE SER SEPARADOS POR COMAS ","
     'sms':'AQUI_EL_SMS_A_ENVIAR',
     'groups':"AQUI_ID_GRUPOS",#PARA ENVIAR MULTIPLES GRUPOS TENDRAN QUE SER SEPARADOS POR COMAS ","
     # Opcional. 1 (por defecto): mensaje transaccional. 0: mensaje comercial (publicidad, promociones);
     # los numeros inscritos en el Registro de Numeros Excluidos (RNE) que no aceptan SMS se rechazan con el error 1010.
     'is-transactional':'1',
     }

r = requests.post('https://www.onurix.com/api/v1/sms/send', headers = headers, data = data)

print(r.json())
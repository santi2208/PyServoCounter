# PyServoCounter
## Correr programa principal:  
cd RaspiService/  
python Main.py  
  
Parámetros      
'--all', '0: Un servo a la vez || 1: Todos los servos al mismo tiempo - Default: 1'   
'--num', 'Numero Fijo - Default: 0 - 9'   
'--time', 'Sleep Time: Intervalo de espera entre numero y numero - Default: 0.8'    
'--web', 'URL servidor al que reportar estado - Default: None'    
'--useWeb', 'Reporta estado a un servidor - Default: False'   

## Correr Servidor node.js  
cd WebDisplay/server    
node main.js    

### Acceder a Servidor node.js  
http://localhost:8012 


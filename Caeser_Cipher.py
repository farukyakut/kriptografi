##Bu uygulamada Cesar şifreleme algoritması ile cümleler şifrelenmektedir.

alfabe ="ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"

string_input = input("Şifrelenecek metni giriniz")
key_input = int(input("Anahtar uzunluğunu giriniz"))

length_input = len(string_input)
string_output=""

for i in range(length_input):
    print(i)
    character = string_input[i]
    print(character)
    if(alfabe.__contains__(character)):
        location_of_character = alfabe.find(character)
        print(location_of_character)
        new_location_character = location_of_character+key_input % 29
        
        string_output += alfabe[new_location_character]
    
    else:
        character = " "
        
        
          
print("Şifrelenmiş Metin = ", string_output) 
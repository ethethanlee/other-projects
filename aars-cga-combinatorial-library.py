from pathlib import Path
# import csv
import itertools

def mutate(positions, input, list_letters): #need to also include original in permutation

    # export file
    f = open('cartesian_product_aars.txt', 'w')

    numeric_pos = []
    list_letters.append(0) #0 means keep original
    # permutations = list(itertools.permutations(list_letters)) # all the permutations of our list of letters including the original
    for item in positions:
        numeric_pos.append(int(item[1:])) #make a list of the positions withou the letters in it
    pos_and_change = {}

    #create dictionary of {number:list_letters}
    for num in numeric_pos:
        pos_and_change[num] = list_letters

    #create list of dictionaries with what we want a change to look like, eg [{268: 'R', 279: 'R', 229: 'R', 230: 'R'}, {268: 'R', 279: 'R', 229: 'R', 230: 'K'},...]
    commands = [dict(zip(pos_and_change, v)) for v in itertools.product(*pos_and_change.values())] 
    print(commands)
    count = 1
    for dict_command in commands:
        output = ''
        for key in dict_command:
            # print(key-1)
            if dict_command[key] != 0:
                output = input[:key-1] + dict_command[key] + input[key:] #fixed indexing issues
                print(output[265:269])
        print(output[265:269])
        f.write(output+'\n')
    f.close()



list_letters = ['R', 'K'] #different letters we want to edit/try out

#positions in format of array Letter+number
positions = ['S268', 'S279', 'D229', 'L230']
# positions = ['D229', 'S268', 'S270']

# input sequence
input = 'MLKIFNTLTRQKEEFKPIHAGEVGMYVCGITVYDLCHIGHGRTFVAFDVVARYLRFLGYKLKYVRNITDIDDKIIKRANENGESFVAMVDRMIAEMHKDFDALNILRPDMEPRATHHIAEIIELTEQLIAKGHAYVADNGDVMFDVPTDPTYGVLSRQDLDQLQAGARVDVVDDKRNPMDFVLWKMSKEGEPSWPSPWGAGRPGWHIECSAMNCKQLGNHFDIHGGGSDLMFPHHENEIAQSTCAHDGQYVNYWMHSGMVMVDREKMSKSLGNFFTVRDVLKYYDAETVRYFLMSGHYRSQLNYSEENLKQARAALERLYTALRGTDKTVAPAGGEAFEARFIEAMDDDFNTPEAYSVLFDMAREVNRLKAEDMAAANAMASHLRKLSAVLGLLEQEPEAFLQSGAQADDSEVAEIEALIQQRLDARKAKDWAAADAARDRLNEMGIVLEDGPQGTTWRRK'
print(input[265:269])


mutate(positions,input,list_letters)

# set what you want positions and list_letters to be!


path = Path('aars-cga-input.txt')
# check if aars-cga-input.txt exists, and if so go thru each line and perform mutate func
if path.is_file():
    input_txt = open('aars-cga-input.txt', 'r')
    for sequence in input_txt:
        mutate(positions,sequence,list_letters)

#!/usr/bin/env python
# coding: utf-8

# #Q1 - Write a function using only list filter lambda that can tell whether a number is a Fibonacci number or not. You can use a pre-calculated list/dict to store fab numbers till 10000 

# In[209]:


def fibonacci(x:int):
    
    '''Function takes in positive integer value
    #fibonacci - creates a list of fibonacci numbers
    #check - To see if the number is fibonacci or not
    fibo_check - Will use filter function and give the output as list'''
    
    fibonacci = lambda number: number if number <= 1 else fibonacci(number - 1) + fibonacci(number - 2)
    listOfFibonacciNumbers = list(map(fibonacci, range(0, 30, 1)))
    print(listOfFibonacciNumbers) #list of Fibonacci numbers till 10000
    
    check = lambda a: (print(f'Its a Fibonacci Number:{a}')) if a in listOfFibonacciNumbers else print(f'Its Not a Fibonacci Number: {a}')
    
    fibo_check = list(filter(check,range(0,x)))
    
    return fibo_check


# In[221]:


fibonacci(10)


# Using reduce function - add only even numbers in a list

# In[134]:


from functools import reduce
list111=[1,2,3,4,5,6,7,8,9,10]

def sum_even(a:int, b:int):
    '''Function will take two positive integer positional arguements a,b
    And return the sum of the even values(a,b) between the range
    We later use this function to pass it through "reduce" function to get our output'''
    
    return sum(range(a + a%2, b+1, 2))

add_even = reduce(sum_even, list111)
'''The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.
This function is defined in “functools” module'''

print(add_even)


# In[223]:


sum_even(10,20)


# find the biggest character in a string (printable ASCII characters)

# In[224]:


from functools import reduce


# In[225]:


def big_charac(string='abcd') ->'str':
    
    '''Function will take any length string character as input
    The string is passed through a reduce function which will iterate through each character and get the,
    largest ASCII character value'''
    
    max_value = lambda a, b: a if a > b else b #Using lambda we get the largest between two values
    maximum = reduce(max_value, string)
    return(f'The Biggest Character in the string is: {maximum}')


# In[226]:


big_charac()


# 
# #Add Every 3rd Number in the List

# In[227]:


def add_third(x=20):
    '''Function will take a range a positive integers.
    using lambda sum of every third element in the above range is added.
    The same is passed through reduce functionto get a aggregated value'''
    
    l1=list(range(x)) #range of positive integers
    add_three= lambda a,b: sum(range(a,b,3)) #sum every third element in the list
    three = reduce(add_three,l1) #iterate the add_three function through the above range and aggregate the value
    return(f'The sum of every third element in the list: {three}')


# In[228]:


add_third()


# A list comprehension expression that takes a ~200-word paragraph, 
# and checks whether it has any of the swear words mentioned in the list.

# In[229]:


paragraph='''Swearing and taboo terms are utilised in the everyday communication and language of Australian people. In different social groups, profanities deviate from their standard functions to consolidate membership between the group’s participants. Swear words which are specifically chosen to support their function has the ability to attract attention, controversy and a response to an advertisement or commercial from the targeted audience. Moreover, swearing has a function in the expression of emotions, both positive and negative, to intensify, vent or reveal the feelings of its users.
Swearing reinforces in-group solidarity and rapport between social groups in Australia. Teenagers often employ lexemes which are regarded as profane and offensive in nature as a means of differentiating themselves from older generations. Terms which usually function as ones of offense or abuse are typically utilised with the non-standard personal pronoun ‘ya’, as in ‘ya sick c*nt’ and ‘ya dickhead’ as terms of endearment or even compliments between group members. Similarly, lexemes regarded by the wider community as politically incorrect or racist, such as ‘nigger’ can used within groups with different denotations and connotations to their original meaning. ‘Nigger’ can be used to describe a person, not necessarily of African descent, in a positive, friendly light, such as in the highly elliptic internet meme ‘He white, but he still my nigger’. The semantic change the lexeme has undergone is similar to the shift a word like ‘bugger’ – from a highly insulting or hurtful term, designed to offend, to one which can also be utilised as a friendly term of address. Australian tradesman or ‘tradies’ exemplify another group whose in-group language possesses an ‘excessive’ amount of swearing. However, the swear words, far from being abusive or rude, are “a tool used for building and maintaining positive affiliations between members of this unique culture.[1]” The use of profanities, specifically ‘f*ck’ and ‘c*nt’, amongst the tradesmen, as well as other ‘blue-collar’ workers is commonly associated with in-group membership. The swear words used by older tradesmen will in turn influence the language of the newly employed, who adjust and accommodate their language appropriately to suit the social context. In order to minimise the social distance between interlocutors and adhere to the ‘Communication Accommodation Theory’, swear or taboo terms will be employed by the members of various social groups.
The utilisation of profanities in Australia’s advertising industry provides a controversial, yet memorable impression on their audience and future buyers. The recent billboard campaign of the underwear manufacturer ‘Bonds’ revealed the single word ‘BOOBS’ to promote their new bra range. This Australian vernacular for a woman’s breasts is still a sensitive topic for most, resulting in a ‘shock-factor’ and memorability for potential buyers driving past. This word association is comparable to the English clothing brand FCUK, an initialism standing for French Connection United Kingdom with similarities with the lexeme ‘f*ck’. These campaigns are intended to be provocative, with the man behind the controversial ‘Don’t be a Dickhead’ road safety advertisements saying that he is “pleased with the uproar created by the controversial campaign.[2]” Commercials and advertisements also have a communicative purpose. Swear words, due to their controversial nature, attract the attention of viewers, fulfilling the functions of the text. TAC’s ‘bloody idiot’ campaigns feature slogans such as ‘If you drink and drive, you’re a bloody idiot’ and ‘Just a little bit over? You bloody idiot’. Although the adjective ‘bloody’ and the noun ‘idiot’ are no longer considered to be a profanity, its usage and designed effect is still the same as a more taboo intensifier or insult. The stupidity of drink-driving and speeding are conveyed to drivers by the blunt dysphemisms, pun on the word ‘bloody’ and the attention-seeking use of ‘bloody idiot’ in the government’s attempt to discourage inconsiderate driving. TAC’s use of the modifier ‘bloody’ contrasts in purpose and effect to the Tourism Australia’s 2007 advertisement ‘So where the bloody hell are you?’ The popular Australian colloquialism, rather than being of shock value, encapsulates the informality and friendliness of Australians. The intensifier ‘the bloody hell’ reveals a lack of conservatism in the Australian language and is combined with the structural ambiguity of the catch-phrase to promote tourism. Profanities are implemented by the commercial industry in various ways, depending on nature and purpose, to attract the attention of readers and to communicate a wide range of information to them.
Swearing also has the purpose of expressing the emotional state of its speaker. Expressions of frustration, stress or aggression are commonly associated with intensifying and emphasising negative emotions. Offensive name-calling is a form of emotive abusive language. Politically incorrect epithets such as ‘b*tch’, ‘c**ksucker’, ‘f*ggot’ and ‘f*ckhead’ are all heavily gender, race or sexually associative words, chosen to verbally maim the listener or topic during arguments. Online, abbreviations such as ‘WTF’ (what the f*ck), ‘FFS’ (for f*cks sake) and ‘GTFO’ (get the f*ck out) have been formed for internet users in chat forums, comment sections or posts to vent with profane exclamations of annoyance whilst being euphemistic and without having to explicitly type out the swear word. On the contrary, swearing is also used to emphasise positive feelings of surprise, joy or love. The lexeme ‘f*ck’ possesses extremely negative connotations. However, it can also modify a positive adjective to intensify the feeling, for example in the declaratives ‘That was f*cking awesome!’ or ‘I f*cking love it!’ This enthusiasm and passion for something is also shown through the recent prominence of online social network sites’ titled ‘F*ck Yeah [something]’, for example ‘F*ck Yeah Ryan Gosling’ or ‘F*ck Yeah 1920s!’The usage of the swear word highlights the extreme dedication, interest and enthusiasm, altering the original connotations of the lexeme. In these ways, swear words function as a means to communicate and reveal both positive and negative emotions between participants.
The use of profanities are growing becoming prominent in contemporary Australian society due to the variety of roles they play in communication. Swear words are able to establish solidarity between social groups and provide an effective means of advertising and expression of emotions. These profane terms, though are not an essential part of language, truly defines modern society, its people and its culture.'''

a='''4r5e
5h1t
5hit
a55
anal
anus
ar5e
arrse
arse
ass
ass-fucker
asses
assfucker
assfukka
asshole
assholes
asswhole
a_s_s
b!tch
b00bs
b17ch
b1tch
ballbag
balls
ballsack
bastard
beastial
beastiality
bellend
bestial
bestiality
bi+ch
biatch
bitch
bitcher
bitchers
bitches
bitchin
bitching
bloody
blow job
blowjob
blowjobs
boiolas
bollock
bollok
boner
boob
boobs
booobs
boooobs
booooobs
booooooobs
breasts
buceta
bugger
bum
bunny fucker
butt
butthole
buttmunch
buttplug
c0ck
c0cksucker
carpet muncher
cawk
chink
cipa
cl1t
clit
clitoris
clits
cnut
cock
cock-sucker
cockface
cockhead
cockmunch
cockmuncher
cocks
cocksuck 
cocksucked 
cocksucker
cocksucking
cocksucks 
cocksuka
cocksukka
cok
cokmuncher
coksucka
coon
cox
crap
cum
cummer
cumming
cums
cumshot
cunilingus
cunillingus
cunnilingus
cunt
cuntlick 
cuntlicker 
cuntlicking 
cunts
cyalis
cyberfuc
cyberfuck 
cyberfucked 
cyberfucker
cyberfuckers
cyberfucking 
d1ck
damn
dick
dickhead
dildo
dildos
dink
dinks
dirsa
dlck
dog-fucker
doggin
dogging
donkeyribber
doosh
duche
dyke
ejaculate
ejaculated
ejaculates 
ejaculating 
ejaculatings
ejaculation
ejakulate
f u c k
f u c k e r
f4nny
fag
fagging
faggitt
faggot
faggs
fagot
fagots
fags
fanny
fannyflaps
fannyfucker
fanyy
fatass
fcuk
fcuker
fcuking
feck
fecker
felching
fellate
fellatio
fingerfuck 
fingerfucked 
fingerfucker 
fingerfuckers
fingerfucking 
fingerfucks 
fistfuck
fistfucked 
fistfucker 
fistfuckers 
fistfucking 
fistfuckings 
fistfucks 
flange
fook
fooker
fuck
fucka
fucked
fucker
fuckers
fuckhead
fuckheads
fuckin
fucking
fuckings
fuckingshitmotherfucker
fuckme 
fucks
fuckwhit
fuckwit
fudge packer
fudgepacker
fuk
fuker
fukker
fukkin
fuks
fukwhit
fukwit
fux
fux0r
f_u_c_k
gangbang
gangbanged 
gangbangs 
gaylord
gaysex
goatse
God
god-dam
god-damned
goddamn
goddamned
hardcoresex 
hell
heshe
hoar
hoare
hoer
homo
hore
horniest
horny
hotsex
jack-off 
jackoff
jap
jerk-off 
jism
jiz 
jizm 
jizz
kawk
knob
knobead
knobed
knobend
knobhead
knobjocky
knobjokey
kock
kondum
kondums
kum
kummer
kumming
kums
kunilingus
l3i+ch
l3itch
labia
lmfao
lust
lusting
m0f0
m0fo
m45terbate
ma5terb8
ma5terbate
masochist
master-bate
masterb8
masterbat*
masterbat3
masterbate
masterbation
masterbations
masturbate
mo-fo
mof0
mofo
mothafuck
mothafucka
mothafuckas
mothafuckaz
mothafucked 
mothafucker
mothafuckers
mothafuckin
mothafucking 
mothafuckings
mothafucks
mother fucker
motherfuck
motherfucked
motherfucker
motherfuckers
motherfuckin
motherfucking
motherfuckings
motherfuckka
motherfucks
muff
mutha
muthafecker
muthafuckker
muther
mutherfucker
n1gga
n1gger
nazi
nigg3r
nigg4h
nigga
niggah
niggas
niggaz
nigger
niggers 
nob
nob jokey
nobhead
nobjocky
nobjokey
numbnuts
nutsack
orgasim 
orgasims 
orgasm
orgasms 
p0rn
pawn
pecker
penis
penisfucker
phonesex
phuck
phuk
phuked
phuking
phukked
phukking
phuks
phuq
pigfucker
pimpis
piss
pissed
pisser
pissers
pisses 
pissflaps
pissin 
pissing
pissoff 
poop
porn
porno
pornography
pornos
prick
pricks 
pron
pube
pusse
pussi
pussies
pussy
pussys 
rectum
retard
rimjaw
rimming
s hit
s.o.b.
sadist
schlong
screwing
scroat
scrote
scrotum
semen
sex
sh!+
sh!t
sh1t
shag
shagger
shaggin
shagging
shemale
shi+
shit
shitdick
shite
shited
shitey
shitfuck
shitfull
shithead
shiting
shitings
shits
shitted
shitter
shitters 
shitting
shittings
shitty 
skank
slut
sluts
smegma
smut
snatch
son-of-a-bitch
spac
spunk
s_h_i_t
t1tt1e5
t1tties
teets
teez
testical
testicle
tit
titfuck
tits
titt
tittie5
tittiefucker
titties
tittyfuck
tittywank
titwank
tosser
turd
tw4t
twat
twathead
twatty
twunt
twunter
v14gra
v1gra
vagina
viagra
vulva
w00se
wang
wank
wanker
wanky
whoar
whore
willies
willy
xrated
xxx
'''
#List comprehension to identify the swear words in the paragraph.
print([i for i in paragraph.split() for j in a.split() if i == j])


# Using list comprehension (and zip/lambda/etc if required) write expressions that
# 1.strips every vowel from a string provided

# In[230]:


def strip_vowel(string= 'tsai') -> str:
    '''Input a string character, the function will identify vowles and strip them.
    '''
    vowels=['a','e','i','o','u'] #predefined vowels in the list
    output = [i for i in string if i.lower() not in vowels] #using list comprehension to ge the job done
    return(f"The string without vowles is: {''.join(output)}")


# In[231]:


strip_vowel()


# Using list comprehension (and zip/lambda/etc if required) write expressions that:add 2 iterables a and b such that a is even and b is odd

# In[232]:


def add_iterables(x:int,y:int):
    
    '''Function takes an input of two lists of same ranges
    #step 1 - creates a even_list with all the even numbers
    #step 2 - creates a odd_list with all odd numbers
    #output - using list comprehension it sums the two lists'''
    
    l1 = range(0, x)
    l2 = range(0, y)
    
    even_list=[]
    [even_list.append(i) for i in l1 if i % 2 == 0]
    #print(even_list)
    odd_list = []
    [odd_list.append(i) for i in l2 if i %2 !=0]
    #print(odd_list)
    
    return (f'The sum of even and odd are: {[x + y for x, y in zip(even_list, odd_list)]}')


# In[233]:


add_iterables(15,15)


# Takes a small character string and shifts all characters by 5 

# In[234]:


shift = lambda inString, inOffset: "".join([chr(ord(x) + inOffset) for x in inString])

#Ord converts a string into ASCII character number
#chr converts the ASCII character value back to string
shift('tsai',5)


# Using randint, random.choice and list comprehensions, write an expression that generates 15 random KADDAADDDD number plates, where KA is fixed, D stands for a digit, and A stands for Capital alphabets. 10<<DD<<99 & 1000<<DDDD<<9999

# In[235]:


import random

def generate_num_plate(a,b) -> 'Input two positive integers':
    
    '''Input two positive integers a, b which defines the range of the values
    #Preefined letters list from A to Z
    #Using List Comprehension, generate random KA number plates based on the ranges given'''
    
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ['KA'+ '-' + str(x) + '-' + (random.choice(letters) + random.choice(letters)) + '-' +str(y) for x in range(0,a) for y in range(1000,b)]


# In[236]:


generate_num_plate(5,1005)


# In[ ]:





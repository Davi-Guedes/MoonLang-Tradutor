import os

try:
    import winsound
except ImportError:
    winsound = None


def tocar_heehee():
    arquivo = "heehee.wav"

    if winsound is not None and os.path.exists(arquivo):
        winsound.PlaySound(arquivo, winsound.SND_FILENAME)

# Desafio 2 - Verificador de musicas do Michael Jackson
# Se for musica do MJ: toca um HEEHEE
# Se nao for: toca dois HEEHEE
# Em vez de armazenar letras completas, o programa usa uma base de reconhecimento com títulos e trechos curtos famosos. Isso reduz o tamanho do código, evita dependência de internet e mantém a proposta simples dentro da MoonLang.
print("========================================")
print("   VERIFICADOR DE MUSICAS DO MJ")
print("========================================")
print("Digite o titulo da musica ou um pequeno trecho:")
entrada = input("> ").strip().lower().replace("'", "").replace("’", "").replace(",", "").replace(".", "").replace("?", "").replace("!", "").replace("(", "").replace(")", "").replace("-", " ").replace(":", "").replace(";", "")
titulos_mj = ["2 bad", "2000 watts", "2300 jackson street", "a brand new day", "a place with no name", "abc", "aint no sunshine", "al capone", "all in your name", "all the things you are", "another part of me", "baby be mine", "bad", "be a lion", "beat it", "beautiful girl", "behind the mask", "ben", "best of joy", "billie jean", "black or white", "blame it on the boogie", "blood on the dance floor", "blue gangsta", "break of dawn", "breaking news", "burn this disco out", "butterflies", "call on me", "can you feel it", "cant get outta the rain", "cant let her get away", "carousel", "centipede", "cheater", "chicago", "childhood", "cinderella stay awhile", "come together", "cry", "d s", "dangerous", "dapper dan", "dear michael", "dirty diana", "do you know where your children are", "doggin around", "dont be messin round", "dont let it get you down", "dont matter to me", "dont stop til you get enough", "dont walk away", "dream away", "earth song", "ease on down the road", "eaten alive", "enjoy yourself", "euphoria", "everybodys somebodys fool", "fall again", "farewell my summer love", "fly away", "for all time", "free", "get it", "get on the floor", "ghosts", "girl dont take your love from me", "girl youre so together", "girlfriend", "give in to me", "gone too soon", "got the hots", "got to be there", "greatest show on earth", "happy", "heal the world", "heartbreaker", "heaven can wait", "here i am come and take me", "history", "hold my hand", "hollywood tonight", "human nature", "i cant help it", "i cant make it another day", "i just cant stop loving you", "i like the way you love me", "i want you back", "i wanna be where you are", "ill be there", "ill come home to you", "im so blue", "in our small way", "in the back", "in the closet", "invincible", "is it scary", "its the falling in love", "jam", "johnny raven", "just a little bit of you", "just good friends", "keep the faith", "keep your head up", "lady in my life", "leave me alone", "liberian girl", "little susie", "love is here and now youre gone", "love never felt so good", "loving you", "man in the mirror", "maria you were the only one", "melodie", "money", "monkey business", "monster", "morning glow", "morphine", "much too soon", "music and me", "my girl", "off the wall", "on the line", "one day in your life", "people make the world go round", "price of fame", "privacy", "pyt", "pyt pretty young thing", "remember the time", "rock with you", "rockin robin", "say say say", "scared of the moon", "scream", "shake your body down to the ground", "she drives me wild", "she was loving me", "shes out of my life", "shes trouble", "shoo be doo be doo da day", "shout", "slave to the rhythm", "smile", "smooth criminal", "someone in the dark", "someone put your hand out", "speechless", "speed demon", "starlight", "state of shock", "stranger in moscow", "streetwalker", "sunset driver", "superfly sister", "tabloid junkie", "take me back", "the girl is mine", "the lady in my life", "the lost children", "the love you save", "the man", "the toy", "the way you make me feel", "there must be more to life than this", "they dont care about us", "this is it", "this place hotel", "this time around", "threatened", "thriller", "too young", "touch the one you love", "unbreakable", "up again", "we are here to change the world", "we are the world", "weve got a good thing going", "weve got forever", "weve had enough", "were almost there", "what a lovely way to go", "what goes around comes around", "whatever happens", "who do you know", "who is it", "why you wanna trip on me", "will you be there", "wings of my love", "with a childs heart", "workin day and night", "xscape", "you are my life", "you are not alone", "you are there", "you can cry on my shoulder", "you cant win", "you rock my world", "youve got a friend", "youve really got a hold on me"]
trechos_mj = ["annie are you ok", "youve been hit by", "a smooth criminal", "hee hee", "shamone", "aoow", "the kid is not my son", "cause this is thriller", "beat it just beat it", "im bad im bad", "whos bad", "black or white", "they dont really care about us", "heal the world", "make it a better place", "man in the mirror", "starting with the man", "remember the time", "do you remember", "you are not alone", "i am here with you", "dont stop til you get enough", "rock with you", "the way you make me feel", "you knock me off of my feet", "dirty diana", "jam", "dangerous", "in the closet", "scream", "earth song", "what about sunrise", "stranger in moscow", "blood on the dance floor", "you rock my world", "love never felt so good", "hold my hand", "behind the mask", "slave to the rhythm", "wanna be startin somethin", "mama se mama sa", "human nature", "why why", "liberian girl", "speed demon", "leave me alone", "smooth criminal", "billie jean", "thriller night", "beat it", "bad bad really really bad", "pyt", "pretty young thing", "abc easy as", "i want you back", "ill be there", "can you feel it", "blame it on the boogie", "shake your body", "say say say", "the girl is mine", "we are the world"]
musicas_mj = titulos_mj + trechos_mj
achou = False
total = len(musicas_mj) - 1
for i in range(0, total + 1):
    if musicas_mj[i] in entrada or entrada in musicas_mj[i]:
        achou = True
        break
if achou == True:
    print("Resultado: essa musica parece ser do Michael Jackson.")
    print("Sinal sonoro: 1 vez.")
    tocar_heehee()
else:
    print("Resultado: essa musica nao foi identificada como sendo do Michael Jackson.")
    print("Sinal sonoro: 2 vezes.")
    tocar_heehee()
    tocar_heehee()
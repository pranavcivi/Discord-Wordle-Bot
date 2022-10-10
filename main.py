import discord
import wordle

client = discord.Client()

secretWord = wordle.get_secret_word()

guessCount = 0

start_command = "start"

guess_command = "-"

game_started = False



#@client.event 
#async def on_ready():

@client.event
async def on_message(message):
  global guessCount
  global secretWord
  global game_started


  if message.channel.id == '''channel id''':
    channel = client.get_channel('''channel''')

    if message.content == start_command:
      game_started = True
      guessCount = 0
      secretWord = wordle.get_secret_word()
      print(secretWord)
      await channel.send('Hey! :wave:, guess a word idiot.')
    
    elif message.content.startswith(guess_command):
      if not game_started:
        await channel.send("Start the game first idiot")
        return
      userWord = message.content[len(guess_command):].strip()
      if secretWord != userWord:
        if not wordle.check_valid(userWord):
          await channel.send("Enter a valid word dummy")
          userWord = message.content
          return
        guessCount += 1
        await channel.send(wordle.checkPos(userWord, secretWord))

        userWord = message.content
      elif (userWord == secretWord) and (guessCount == 0):
        await channel.send(wordle.checkPos(userWord, secretWord))
        await channel.send("Congrats! You guessed it in 1 guess!")
        game_started = False
      elif (userWord == secretWord):
        await channel.send(wordle.checkPos(userWord, secretWord))
        await channel.send("Congrats! You guessed it in " + str(guessCount + 1) + " guesses!")
        game_started = False

client.run('''client code''')

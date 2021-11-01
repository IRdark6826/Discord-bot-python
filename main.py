import discord
from discord import Embed
from discord import channel
from discord.ext import commands
import random
from discord.ext.commands.converter import TextChannelConverter, VoiceChannelConverter
from discord.message import convert_emoji_reaction
import asyncio
import time
import datetime
from os import name
from discord_slash import ButtonStyle, SlashCommand
from discord_slash.utils.manage_components import *



intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix = "YOUR PREFIX", description = "NAME", intents = intents)
bot.remove_command('help')



@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=f" {len(bot.guilds)} serveurs | z.help"))
    print("Ready !")


async def ch_pr():
    await bot.wait_until_ready()
    statuses = ["Visual studio", f" {len(bot.guilds)} serveurs | z.help", "discord.py"]
    
    while not bot.is_closed():

        status = random.choice(statuses)

        await bot.change_presence(activity=discord.Game(name=status))

        await asyncio.sleep(5)
bot.loop.create_task(ch_pr())




@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, id=int("875823361039663205"))
    await member.add_roles(role)
    try:
        ctx = bot.get_channel(872905731152691280)
        try:
            embed = discord.Embed(colour=discord.Colour.red())
            embed.set_author(name=member.name, icon_url="https://cdn.discordapp.com/attachments/871755181359005746/872923135282937886/zeldris.gif")
            embed.add_field(name="Welcome" ,value=f"Hey,{member.mention}! Bienvenue dans le serveur **{member.guild.name}** j'espère que tu t'amusera bien !", inline=False)
            embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/871755181359005746/872923135282937886/zeldris.gif")
            embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/871755181359005746/872923135282937886/zeldris.gif")
            embed.set_image(url="https://cdn.discordapp.com/attachments/871755181359005746/872923135282937886/zeldris.gif")
            await ctx.send(embed = embed)
        except Exception as e:
            raise e
    except Exception as e:
        raise e


@bot.event
async def on_member_remove(member):
    try:
        channel = bot.get_channel(872905731152691280)
        try:
            embed = discord.Embed(colour=discord.Colour.red())
            embed.set_author(name=member.name, icon_url="https://cdn.discordapp.com/attachments/871755181359005746/872923135282937886/zeldris.gif")
            embed.add_field(name="Au revoir", value=f"{member.mention} a quitté le serveur **{member.guild.name}** .", inline=False)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/871755181359005746/872923135282937886/zeldris.gif")
            embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/871755181359005746/872923135282937886/zeldris.gif")
            embed.set_image(url="https://cdn.discordapp.com/attachments/871755181359005746/872923135282937886/zeldris.gif")
            await channel.send(embed=embed)
        except Exception as e:
            raise e
    except Exception as e:
        raise e



@bot.command()
async def help(ctx, argument=None):
    if argument is None:
        embed = discord.Embed(title="**Page d'aide général:**", description="📓 Mon préfix et ``z.``", color=0x0404B4)
        embed.add_field(name="**__Commande__**", 
        value="`z.help2 <commande>`")
        embed.add_field(name="**__AIDE__:**", 
        value="`z.help1`")
        embed.set_thumbnail(url = "https://media.discordapp.net/attachments/871755181359005746/872923135282937886/zeldris.gif")
        await ctx.send(embed = embed)


@bot.command()
async def zza(ctx):
    embed = discord.Embed(
        title = 'Help',
        description = 'Commande aide',
        color = 0x0404B4
    )
    embed.set_footer(text=f"Commande executée par: {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.add_field(name='General',value='`ping`, `invite`, `say`, `ping`')
    embed.add_field(name='Information',value='`userinfo`, `serverinfo`, `getinfo`')
    embed.add_field(name='Modération',value='`ban`, `unban`, `kick`, `clear`, `dm`, `newrole`, `rename`, `mute`, `unmute`')
    embed.add_field(name= 'Concours',value= '`giveaway`,`reroll`')
    await ctx.send(embed = embed)



@bot.command()
async def help2(ctx, commandSent=None):
    if commandSent != None:

        for command in bot.commands:
            if commandSent.lower() == command.name.lower():

                paramString = ""

                for param in command.clean_params:
                    paramString += param + ", "

                paramString = paramString[:-2]

                if len(command.clean_params) == 0:
                    paramString = "None"
                    
                embed=discord.Embed(title=f"HELP - {command.name}", description=command.description)
                embed.add_field(name="paramètres", value=paramString)
                await ctx.message.delete()
                await ctx.author.send(embed=embed)
        
    else:
        embed=discord.Embed(title="HELP", color = 0x0404B4)
        embed.add_field(name="**__Autre - Commande__**", value='\u200b', inline=False)
        embed.add_field(name="newrole", 
        value="> Crée un rôle", inline=False)
        embed.add_field(name="rename", 
        value="Rename un membre", inline=False)
        embed.add_field(name="dm", 
        value="> Permet d'envoyé un message", inline=False)
        embed.add_field(name="giveaway", 
        value="> Permet de lancé un concours", inline=False)
        embed.add_field(name="reroll", 
        value="> Relancé le giveaway", inline=False)
        embed.add_field(name="__ping__", 
        value="> Latence du bot", inline=False)
        embed.add_field(name="say", 
        value="> Faire parlé le bot.", inline=False)
        embed.add_field(name="invite", 
        value="> Invitation du bot et autre.", inline=False)
        embed.add_field(name="**__Informations - Commande d'informations__**", value='\u200b', inline=False)
        embed.add_field(name="getinfo", 
        value="> Info du serveur", inline=False)
        embed.add_field(name="userinfo", 
        value="> Info d'un membre", inline=False)
        embed.add_field(name="serverinfo", 
        value="> Info du serveur", inline=False)
        embed.add_field(name="**__Modération - Commande de modération__**", value='\u200b', inline=False)
        embed.add_field(name="ban", 
        value="> Bannir un membre du serveur", inline=False)
        embed.add_field(name="unban", 
        value="> Permet de débannir un membre", inline=False)
        embed.add_field(name="kick", 
        value="> Viré un membre du serveur", inline=False)
        embed.add_field(name="clear", 
        value="> Effacé des messages", inline=False)
        embed.add_field(name="mute", 
        value="> Permet de mute un membre", inline=False)
        embed.add_field(name="unmute", 
        value="> Permet de unmute un membre", inline=False)
        embed.add_field(name="warn", 
        value="> Permet d'avertir un membre", inline=False)
        await ctx.send(embed = embed)

@bot.command()
async def invite(ctx):
    embed=discord.Embed(title="__Links__")
    embed.add_field(name='**__Invitation Zeldris__**', value='[cliquez ici](https://discord.com/api/oauth2/authorize?client_id=872859708560658452&permissions=8&scope=bot)', inline=False)
    embed.add_field(name='**__Serveur Zeldris Support__**', value='[cliqué ici](https://discord.gg/NjrJewyhYE)', inline=False)
    embed.set_thumbnail(url ="https://cdn.discordapp.com/attachments/871755181359005746/872923135282937886/zeldris.gif")
    embed.set_footer(text=f"Commande executée par: {ctx.author}", icon_url="https://cdn.discordapp.com/attachments/871755181359005746/872923135282937886/zeldris.gif")
    await ctx.send(embed= embed)

@bot.command()
async def say(ctx, *texte):
    ctx.message.delete()
    await ctx.send(" ".join(texte))



@bot.command()
async def getinfo(ctx, info):
    server = ctx.guild
    if info == "membercount":
        await ctx.send(server.member_count)
        print("membercount")
    elif info == "numberofchannel":
        await ctx.send(len(server.text_channels) + len(server.voice_channels)) 
    elif info == "name":
        await ctx.send(server.name)
    else:
        await ctx.send("Mmmmmh....ceci n'est pas dans ma base de donnée.")



@bot.command()
@commands.has_permissions(administrator=True)
async def dm(ctx, user_id=None, *, args=None):
    if user_id != None and args != None:
        try:
            target = await bot.fetch_user(user_id)
            await target.send(args)

            await ctx.channel.send("'" + args + "' à été envoyé à: " + target.name)

        except:
            await ctx.channel.send("Mmmmh... Je ne peux pas envoyer le message... Verifiez que l'utilisateur à bien ses dm ouverts. Ou si l'ID de la personnes est bon.")

    else:
        await ctx.channel.send("Un id d'utilisateur ou/et des arguments sont absents.")




@bot.command(aliases=['make_role'])
@commands.has_permissions(manage_roles=True) # Check if the user executing the command can manage roles
async def newrole(ctx, *, name):
	guild = ctx.guild
	await guild.create_role(name=name)
	await ctx.send(f'Role `{name}` a bien était crée')



@bot.command(pass_context=True)
async def ping(ctx):
    """ Pong! """
    before = time.monotonic()
    message = await ctx.send("Pong!")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"Pong!  `{int(ping)}ms`")
    print(f'Ping {int(ping)}ms')

@bot.command()
async def serverinfo(ctx):
  name = str(ctx.guild.name)
  id = str(ctx.guild.id)
  owner = str(ctx.guild.owner)
  region = str(ctx.guild.region)
  memberCount = str(ctx.guild.member_count)

  embed = discord.Embed(Title = "**__Informations__**")
  embed.add_field(name ="**Nom du serveur**", value = name, inline = True)
  embed.add_field(name ="**Propriétaire du serveur**", value = owner, inline = True)
  embed.add_field(name ="**ID du serveur**", value = id, inline = True)
  embed.add_field(name ="**Nombre de membres**", value = memberCount, inline = True)
  embed.add_field(name ="**Région du serveur**", value = region, inline = True)
  await ctx.send(embed = embed)


@bot.command()
async def regle(ctx):
    embed = discord.Embed(title = "REGLE", color = 0x0404B4)
    embed.add_field(name="» __Il est interdit d’insulter ou de menacer__", value="`L'utilisation de insultes et de mots grossiers doit être réduite au minimum.`", inline=False)
    embed.add_field(name=" ━━━━━━━━━━━━━━━━━━━━━", value="\u200b", inline=False)
    embed.add_field(name="» __Pas de matériel pornographique / adulte / autre NSFW__", value="`Il s'agit d'un serveur communautaire et non destiné à partager ce type de matériel.`", inline=False)
    embed.add_field(name=" ━━━━━━━━━━━━━━━━━━━━━", value="\u200b", inline=False)
    embed.add_field(name="» __Publicité interdit__", value="`tout type de publicité est strictement interdit sauf dans les salons respectives.`", inline=False)
    embed.add_field(name=" ━━━━━━━━━━━━━━━━━━━━━", value="\u200b", inline=False)
    embed.add_field(name="» __Merci de respecter les haut-gradées.__", value="`Interdiction de rabaisser les fondateurs, administrateurs et modérateurs.`", inline=False)
    embed.add_field(name=" ━━━━━━━━━━━━━━━━━━━━━", value="\u200b", inline=False)
    embed.add_field(name="» __Pas de noms offensants ni de photos de profil__", value="`Il vous sera demandé de changer votre nom ou votre photo si cela est inappropriés`", inline=False)
    embed.add_field(name="» ━━━━━━━━━━━━━━━━━━━━━", value="\u200b", inline=False)
    embed.add_field(name="» __Voici les sanctions si vous ne respectez pas les règles :__", value="\u200b", inline=False)
    embed.add_field(name="\u200b", value="> Plus de 3 règles non respectées = sanction", inline=False)
    embed.add_field(name="» ━━━━━━━━━━━━━━━━━━━━━", value="\u200b", inline=False)
    embed.add_field(name="» __Raid / Spam / Flooding est interdit__", value="\u200b", inline=False)
    embed.add_field(name="» ━━━━━━━━━━━━━━━━━━━━━", value="\u200b", inline=False)
    embed.add_field(name="Merci de votre compréhension et passez un bon moment sur notre serveur support !", value="\u200b", inline=False)
    embed.set_image(url = "https://cdn.discordapp.com/attachments/849674752195821601/882235833258766436/luffy_12345.gif")
    await ctx.send(embed = embed)


@bot.command()
async def gstart(ctx, mins : int, *, prize: str):
    try:
        embed = discord.Embed(title = "Giveaway", description=f"{prize}", color = ctx.author.color)

        end = datetime.datetime.utcnow() + datetime.timedelta(seconds = mins)

        embed.add_field(name="Fin dans", value=f"{end} UTC")
        embed.set_footer(text=f"Fin dans {mins} minutes")

        my_msg = await ctx.send(embed = embed)

        await my_msg.add_reaction("🎉")

        await asyncio.sleep(mins)

        new_msg = await ctx.channel.fetch_message(my_msg.id)

        users = await new_msg.reactions[0].users().flatten()
        users.pop(users.index(bot.user))

        winner = random.choice(users)

        await ctx.send(f"Bravo! {winner.mention} à gagné {prize}!")

    except Exception as e:
        print(e)

def convert(time):
    pos = ["s","m","h","d"]

    time_dict = {"s" : 1, "m" : 60, "h" : 3600 , "d" : 3600*24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2


    return val * time_dict[unit]



@bot.command()
@commands.has_permissions(administrator=True)
async def giveaway(ctx):
    try:
        await ctx.send("Commençons ce giveaway! Entre chaque question, vous sera donner 15 secondes pour répondre.")

        questions = ["Dans quel salon voulez vous que le giveaway commence", 
                    "Combien de temps? (s|m|h|d)",
                    "Quel est le prix ?"]

        answers = []

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel 

        for i in questions:
            await ctx.send(i)

            try:
                msg = await bot.wait_for('message', timeout=15.0, check=check)
            except asyncio.TimeoutError:
                await ctx.send('Vous avez pris trop de temps à répondre! Veuillez réitérer la commande! ')
                return
            else:
                answers.append(msg.content)

        try:
            c_id = int(answers[0][2:-1])
        except:
            await ctx.send(f"Merci de bien vouloir mentionner un salon correctement!")
            return

        channel = bot.get_channel(c_id)

        time = convert(answers[1])
        if time == -1:
            await ctx.send(f"Vous n'avez pas répondu à la question avec les bonnes unités pour le temps! Utilisez: `(s|m|h|d)` la prochaine fois!")
            return
        elif time == -2:
            await ctx.send(f"L'heure doit être un nombre entier. Veuillez saisir un entier la prochaine fois")
            return            

        prize = answers[2]

        await ctx.send(f"Le giveaway à été lancé dans le salon: {channel.mention} et durera {answers[1]}!")


        embed = discord.Embed(title = "Giveaway!", description = f"{prize}", color = ctx.author.color)

        embed.add_field(name = "Lancé par:", value = ctx.author.mention)

        embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/871755181359005746/872923135282937886/zeldris.gif")

        embed.set_footer(text = f"Temps: {answers[1]}")

        my_msg = await channel.send(embed = embed)


        await my_msg.add_reaction("🎉")


        await asyncio.sleep(time)


        new_msg = await channel.fetch_message(my_msg.id)


        users = await new_msg.reactions[0].users().flatten()
        users.pop(users.index(bot.user))

        winner = random.choice(users)

        await channel.send(f"Félicitations! {winner.mention} à gagné: {prize}!")
    except Exception as e:
        print(e)



@bot.command()
@commands.has_permissions(administrator=True)
async def reroll(ctx, channel : discord.TextChannel, id_ : int):
    try:
        try:
            new_msg = await channel.fetch_message(id_)
        except:
            await ctx.send("Merci de bien vouloir entrer un ID correct!")
            return
        
        users = await new_msg.reactions[0].users().flatten()
        users.pop(users.index(bot.user))

        winner = random.choice(users)

        await channel.send(f"Félicitations! Le nouveau gagnant est: {winner.mention}!")
    except Exception as e:
        print(e)



@bot.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit = amount + 1)
    emb = discord.Embed (title = 'total {} message suprimé !'.format(amount), color = 0x0404B4)
    sendemb = await ctx.send(embed = emb)
    await asyncio.sleep(3)
    await sendemb.delete()



@bot.command()
@commands.has_permissions(ban_members=True)
async def kick(ctx, user : discord.User, *, reason = "Aucune raison n'a été donné"):
	await ctx.guild.kick(user, reason = reason)
	embed = discord.Embed(title = "**__Kick__**", description = "Un modérateur a kick !", url = "https://discord.gg/NjrJewyhYE", color=0x0404B4)
	embed.set_author(name = ctx.author.name, icon_url = "https://cdn.discordapp.com/attachments/871755181359005746/872923135282937886/zeldris.gif", url = "https://media.discordapp.net/attachments/871755181359005746/872923135282937886/zeldris.gif")
	embed.set_thumbnail(url = "https://media.discordapp.net/attachments/871755181359005746/872923135282937886/zeldris.gif")
	embed.add_field(name = "Membre kick", value = user.name, inline = True)
	embed.add_field(name = "Raison", value = reason, inline = True)
	embed.add_field(name = "Modérateur", value = ctx.author.name, inline = True)
	embed.set_footer(text='Zeldris')
	await ctx.send(embed = embed)



@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user : discord.User, *, reason = "Aucune raison n'a été donné"):
	await ctx.guild.ban(user, reason = reason)
	embed = discord.Embed(title = "**__Ban__**", description = "Un modérateur a ban !", url = "https://discord.gg/NjrJewyhYE", color=0x0404B4)
	embed.set_author(name = ctx.author.name, icon_url = "https://cdn.discordapp.com/attachments/871755181359005746/872923135282937886/zeldris.gif", url = "https://media.discordapp.net/attachments/871755181359005746/872923135282937886/zeldris.gif")
	embed.set_thumbnail(url = "https://media.discordapp.net/attachments/871755181359005746/872923135282937886/zeldris.gif")
	embed.add_field(name = "Membre banni", value = user.name, inline = True)
	embed.add_field(name = "Raison", value = reason, inline = True)
	embed.add_field(name = "Modérateur", value = ctx.author.name, inline = True)
	embed.set_footer(text='Zeldris')
	await ctx.send(embed = embed)


@bot.command()
async def unban(ctx, user, *reason):
    reason = " ".join(reason)
    UserName, userTag =  user.split("#")
    bannedUsers = await ctx.guild.bans()
    for i in bannedUsers:
        if i.user.name == UserName and i.user.discriminator == userTag:
            await ctx.guild.unban(i.user, reason = reason)
            await ctx.send(f"Le bannissement de {user} à été révoqué.")
            return
    await ctx.send(f"L'utilisateur {user} n'a pas été trouvé dans la liste des membres bannis") 



async def createMutedRole(ctx):
    mutedRole = await ctx.guild.create_role(name = "Muted", 
                                            permissions = discord.Permissions(
                                                send_messages = False,
                                                speak = False),
                                            reason = "Création du role Muted.")
    for channel in ctx.guild.channels:
        await channel.set_permissions(mutedRole, send_messages = False, speak = False)
    return mutedRole
    
async def getMutedRole(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "Muted":
            return role
    
    return await createMutedRole(ctx)



@bot.command(description="Mutes le joueur choisi.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    embed = discord.Embed(title="muted", description=f"{member.mention} est mute ", colour=discord.Colour.light_gray())
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f" Tu a était mute de: {guild.name} pour la raison: {reason}")



@bot.command(description="Unmutes un joueur choisi.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

   await member.remove_roles(mutedRole)
   await member.send(f" Tu a était unmute du serveur: - {ctx.guild.name}")
   embed = discord.Embed(title="unmute", description=f" unmute-{member.mention}",colour=discord.Colour.light_gray())
   await ctx.send(embed = embed)



@bot.command(name='warn',pass_context=True)
@commands.has_permissions(administrator=True)
async def warn(ctx,  user: discord.Member, args=None):
    if  user != None  and args != None: 
            embed = discord.Embed(title="**WARN!**", description="Mauvais comportement dans le serveur.", color=0x0404B4)
            embed.add_field(name="**Raison Du Warn**", 
            value= args)
            embed.add_field(name="Name", value=user.name)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/871755181359005746/872923135282937886/zeldris.gif")
            await ctx.send(embed = embed)
            await ctx.message.delete()


@bot.command()
async def help1(ctx):
    select = create_select(
        options=[
            create_select_option("Info", value="1", emoji="📰"),
            create_select_option("Modération", value="2", emoji="🔨"),
            create_select_option("Musique", value="3", emoji="🎼"),
            create_select_option("Haut gradées", value="4", emoji="👑"),
            create_select_option("Giveaway", value="5", emoji="🎊"),
            create_select_option("Fun", value="6", emoji="📊")
        ],
        placeholder="Choisis une catégorie.",
        min_values=1,
        max_values=1
    )
    fait_choix = await ctx.send("**__AIDE__**", components=[create_actionrow(select)])

    def check(m):
        return m.author_id == ctx.author.id and m.origin_message.id == fait_choix.id

    choice_ctx = await wait_for_component(bot, components=select, check=check)

    if choice_ctx.values[0] == "4":
        await choice_ctx.send("En dev...")
    else:
        await choice_ctx.send("En cours de dev...")





bot.run("YOUR TOKEN OF THE BOT")




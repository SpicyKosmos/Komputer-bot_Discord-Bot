import random
import subprocess
import sys
import discord
from discord.ext import tasks, commands
import os
import requests




TOKEN= #Your Discord Token
sunucu_id = #Your Server ID
channel1 = "bot-test"


intents=discord.Intents.default()
intents.message_content=True
intents.members = True
intents.guilds = True
intents.reactions = True
intents.presences =True
client = discord.Client(intents=intents)

bot= commands.Bot(command_prefix="!", intents=intents)

@bot.event #Bot çalışmaya başladığında
async def on_ready():
    print("Sunucu bağlantısı başarılı")
    server = bot.get_guild(263045299755417630)  # sunucunun ID'sini buraya yazın
    channel = discord.utils.get(server.text_channels, name="kompüter-bot")  # kanal adını buraya yazın
    message = f"```Yörünge stabil, navigasyon sistemleri çalışıyor ve batarya seviyeleri normal {bot.user.name} başlatılıyor.```"  # gönderilecek mesajı buraya yazın
    await channel.send(message)
    print("Ateşleme başlatıldı. Sistem hazır...")


@bot.command(name="yardım") #komut menüsü
async def test_metin(ctx):
    bosluk=" "
    await ctx.send(f"```\nYardım modülü devrede! Ne yapacağını bilmiyorsan aşağıdaki komutları dene;\n\n\n"
                   "🖥️sistem komutları:\n\n"
                   f"\t!off{bosluk:<19}# {bot.user.name}'ı kapatır.\n\n"
                   f"\t!reset{bosluk:<17}# {bot.user.name}'ı yeniden başlatır.\n\n"
                   f"💡Genel komutlar:\n\n"
                   f"\t!say <mesajınız>{bosluk:<7}# mesajınızı {bot.user.name} tarafından yazdırır.\n\n"
                   f"\t!rmember{bosluk:<15}# sunucudaki üyeler arasından rastgele birini seçer.\n\n"
                   f"\t!flipco{bosluk:<16}# Yazı-Tura oyunu.\n\n"
                   f"\t!remoji{bosluk:<16}# random bir emoji çağır.\n\n"
                   f"🎱Pokemon Catch komutları:\n\n"
                   f"\t!pokedex <name or id>{bosluk:<2}# Bir pokemon adı ya da id (1'den 1281'e kadar) ile o pokemonun bilgilerini gösterir.\n\n"
                   f"\t!pokecinfo{bosluk:<13}# pokec oyunu ile ilgili bilgiler\n\n"
                   f"\t!pokec{bosluk:<17}# pokec oyununu başlatıp bir poketopu atar ve bir pokemon yakalarsınız\n\n"
                   "🎲Zar komutları:\n\n"
                   f"\t!zar6{bosluk:<18}# 6'lık zar.\n\n"
                   f"\t!2zar6{bosluk:<17}# 2 tane 6'lık zar.\n\n"
                   f"\t!zar20{bosluk:<17}# 20'lik zar.\n\n"
                   f"\t!2zar20{bosluk:<16}# 2 tane 20'lik zar.\n\n"
                   f"\t!zar100{bosluk:<16}# 100lük zar.```")



@bot.event #kanala biri katıldığında ona bir text kanalından alttaki mesajı gönderir.
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name=channel1)
    guild = client.get_guild(sunucu_id)
    server_name = guild.name
    if channel:
        await channel.send(f"```Hoşgeldin {member.mention},{server_name} üyeleri seni selamlıyor. "
                          f"Ben {bot.user.name}, bu topluluk için Kosmos tarafından özel olarak hazırlandım. yardımcı olmamı istediğin bir şey varsa '!yardım' "
                          f"komutuyla neler yapabildiğime bakabilirsin```")


@bot.command(name="say") #bota bir mesaj yazdırır
async def say(ctx,*,message):
    await ctx.message.delete()
    await ctx.send(f"```{message}```")



@bot.command(name="rmember") #random bir üye seçer
async def random_member(ctx):
     guild = ctx.guild
     uye_isim = guild.members
     random_uye = random.choice(uye_isim)
     await ctx.send(random_uye.mention)



@bot.command(name="flipco") #yazı tura oyunu
async def flipcoin(ctx):
    coin_face = ["Yazı","Tura"]
    fcoin= random.choice(coin_face)
    await ctx.send(f"```{fcoin}```")



@bot.command(name="zar6") #6lık zar atar
async def zar6(ctx):
    zar6 = [*range(7)]
    sonuc = random.choice(zar6)
    await ctx.send(f"```Kader senin için şu zarı seçti:\t'{sonuc}'```")



@bot.command(name="2zar6") #2x6 zar atar
async def zar6x2(ctx):
    zar6 = [*range(7)]
    sonuc = random.choice(zar6)
    sonuc1= random.choice(zar6)
    toplam=sonuc+sonuc1
    await ctx.send(f"```1. zar:\t'{sonuc}'\n2. zar:\t'{sonuc1}'\nToplam:'{toplam}'```")



@bot.command(name="zar20") #20lık zar atar
async def zar20(ctx):
    zar20 = [*range(21)]
    sonuc = random.choice(zar20)
    await ctx.send(f"```Kader senin için şu zarı seçti:\t'{sonuc}'```")



@bot.command(name="2zar20") #2x20 zar atar
async def zar20x2(ctx):
    zar20 = [*range(21)]
    sonuc = random.choice(zar20)
    sonuc1= random.choice(zar20)
    toplam=sonuc+sonuc1
    await ctx.send(f"```1. zar:\t'{sonuc}'\n2. zar:\t'{sonuc1}'\nToplam:'{toplam}'```")



@bot.command(name="zar100") #100lık zar atar
async def zar100(ctx):
    zar100 = [*range(101)]
    sonuc = random.choice(zar100)
    await ctx.send(f"```Kader senin için şu zarı seçti:\t'{sonuc}'```")



@bot.command(name="remoji") #random emoji seçip yazdırır
async def remoji(ctx):
    emoji_list = ["😂", "😭", "❤️", "👀", "🔥", "😍", "🙏", "💯", "💕", "🤔", "👏", "😊", "👌", "😩", "😘", "😅", "😁", "🎉", "😳", "🤣", "💔", "🙄", "😴", "😒", "💀", "🤷", "😢", "👍", "😔", "😎", "😉", "🤤", "🥺", "👉", "😋", "🤗", "😌", "🙂", "👇", "😕", "🤦", "😜", "😑", "🤢", "😪", "😷", "🥴", "😞", "😤", "👊", "😡", "👑", "😠", "🌟", "😝", "🤯", "😬", "😭😭", "🎶", "🤑", "🤭", "😹", "😖", "😨", "😰", "🤫", "🤡", "🙌", "😮", "🤝", "😀", "🙈", "🤠", "😫", "💖", "👈", "😛", "🤪", "😵", "🔫", "🤘", "😚", "😓", "💫", "🧡", "😬😬", "🤞", "😇", "🌹", "🤐", "💩", "😶", "😐", "👻", "😰😰", "😙", "👑👑", "🙃", "😛😛", "🤢🤢", "🥰", "😆", "💃", "🤳", "😥", "😩😩", "🤔🤔", "😯", "🎂", "😇😇", "😫😫", "🍑", "🔪", "🎈", "😮😮", "😨😨", "😓😓", "🤯🤯", "🙏🏻", "😲", "😋😋", "💰", "🦋", "💀💀", "😖😖", "🍆", "🤡🤡", "😆😆", "😹😹", "🥵", "🌈", "🤥", "🚀", "🤧", "🤔🤔🤔", "🙊", "🙉", "🙊🙉", "🌸", "😔😔", "😟", "🎁", "💛", "😮😮😮", "🍺", "👁️👄👁️", "🤮", "🤯🤯🤯", "🤷‍♀️", "🤷‍♂️", "🤦‍♀️", "🤦‍♂️", "🥱", "😷😷", "🙏🏽", "💪", "🌊", "🌞", "🌝", "🌚", "🌎", "🌍", "🌏", "🍕", "🍔", "🍟", "🍩", "🍪", "🍫", "🍬", "🍭", "🍦", "🍺🍺", "🍻", "🍷", "🍸", "🍹", "🍾", "🍿", "🍽️", "🎥", "🎬", "🎧", "🎤", "🎵", "🎶", "🎼", "🎹", "🎸", "🎻", "🥁", "🎮", "🕹️", "🎲", "🃏", "🀄", "🎴", "👀👀", "👁️", "👁️‍🗨️", "👅", "👄", "👶", "👦", "👧", "🧒", "👩", "👨", "👵", "👴", "👥", "👤", "👥‍👥", "👩‍❤️‍👨", "👨‍❤️‍👨", "👩‍❤️‍👩", "💍", "💎", "🏆", "🎖️", "🥇", "🥈", "🥉", "🎓", "👔", "👕", "👖", "🧣", "🧤", "🧥", "🧦", "👗", "👘", "👙", "👚", "👛", "👜", "👝", "🎒", "👞", "👟", "👠", "👡", "👢", "👑👑👑", "👒", "🎩", "🎓", "💼", "👜", "👓", "🕶️", "💄", "💋", "🔥🔥🔥", "❄️", "🌬️", "🌪️", "🌫️", "🌬️", "☀️", "🌤️", "⛅", "🌥️", "🌦️", "🌧️", "⛈️", "🌩️", "🌨️", "❤️‍🩹", "💔💔💔", "💉", "🩸", "💊", "🧪", "🧬", "💡", "🔦", "💸", "💰💰", "💳", "💴", "💵", ]
    emoji_sec = random.choice(emoji_list)
    await ctx.send(f"```{emoji_sec}```")



@bot.command(name="pokedex")
async def pokedex(ctx,*,message):

    try:
        pokemon_url = "https://pokeapi.co/api/v2/pokemon/"
        pokemon_response = requests.get(pokemon_url)

        status_code= pokemon_response.status_code

        max_id_count="#1281"
        bosluk = " "

        girdi = message
        id_or_name = girdi.lower()
        payload = f"{id_or_name}/"
        pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{payload}"
        pokemon_response = requests.get(pokemon_url)
        data = pokemon_response.json()



        if status_code == 200:
            pokemon_id = data["id"]
            pokemon_name = data["name"]
            pokemon_type1 = data["types"][0]["type"]["name"]
            pokemon_height=data["height"]/10
            pokemon_weight=data["weight"]/10
            if len(data["types"]) == 1:

                await ctx.send(f"```id:{bosluk:<8}#{pokemon_id:}\n"
                      f"isim:{bosluk:<6}{pokemon_name}\n"
                      f"tür:{bosluk:<7}{pokemon_type1}\n"
                      f"uzunluk:{bosluk:<3}{pokemon_height} metre\n"
                      f"ağırlık:{bosluk:<3}{pokemon_weight} kilo```")

            elif len(data["types"]) > 1:
                pokemon_type2 = data["types"][1]["type"]["name"]

                await ctx.send(f"```id:{bosluk:<8}#{pokemon_id}\n"
                      f"isim:{bosluk:<6}{pokemon_name}\n"
                      f"tür:{bosluk:<7}{pokemon_type1}/{pokemon_type2}\n"
                      f"uzunluk:{bosluk:<3}{pokemon_height}\n"
                      f"ağırlık:{bosluk:<3}{pokemon_weight}```")
        else:
            await ctx.send("server'a bağlanılamıyor...")
    except:
        await ctx.send(f"```Hatalı bir index numarası ya da pokemon ismi girdiniz. Tekrar deneyin (max pokemon index:\t{max_id_count})```")



@bot.command(name="pokecinfo") #pokec oyunu ile ilgili info verir
async def pokec_info(ctx):
    await ctx.send("```Kurallar Basit eğer bir Pikachu, Charmender, Bulbasaur ya da Squirtle yakalarsan oyunu kazanırsın```")



@bot.command(name="pokec") #kullanıcı 151 pokemon arasından pikachu,Charmander,Squirtle ya da Bulbasaur yakalamaya çalışır.
async def pokeball(ctx):
    await ctx.send("```Poke topu atılıyor...```")
    pokemon_names = ['bulbasaur', 'ivysaur', 'venusaur', 'charmander', 'charmeleon', 'charizard', 'squirtle', 'wartortle', 'blastoise', 'caterpie', 'metapod', 'butterfree', 'weedle', 'kakuna', 'beedrill', 'pidgey', 'pidgeotto', 'pidgeot', 'rattata', 'raticate', 'spearow', 'fearow', 'ekans', 'arbok', 'pikachu', 'raichu', 'sandshrew', 'sandslash', 'nidoran-f', 'nidorina', 'nidoqueen', 'nidoran-m', 'nidorino', 'nidoking', 'clefairy', 'clefable', 'vulpix', 'ninetales', 'jigglypuff', 'wigglytuff', 'zubat', 'golbat', 'oddish', 'gloom', 'vileplume', 'paras', 'parasect', 'venonat', 'venomoth', 'diglett', 'dugtrio', 'meowth', 'persian', 'psyduck', 'golduck', 'mankey', 'primeape', 'growlithe', 'arcanine', 'poliwag', 'poliwhirl', 'poliwrath', 'abra', 'kadabra', 'alakazam', 'machop', 'machoke', 'machamp', 'bellsprout', 'weepinbell', 'victreebel', 'tentacool', 'tentacruel', 'geodude', 'graveler', 'golem', 'ponyta', 'rapidash', 'slowpoke', 'slowbro', 'magnemite', 'magneton', 'farfetchd', 'doduo', 'dodrio', 'seel', 'dewgong', 'grimer', 'muk', 'shellder', 'cloyster', 'gastly', 'haunter', 'gengar', 'onix', 'drowzee', 'hypno', 'krabby', 'kingler', 'voltorb', 'electrode', 'exeggcute', 'exeggutor', 'cubone', 'marowak', 'hitmonlee', 'hitmonchan', 'lickitung', 'koffing', 'weezing', 'rhyhorn', 'rhydon', 'chansey', 'tangela', 'kangaskhan', 'horsea', 'seadra', 'goldeen', 'seaking', 'staryu', 'starmie', 'mr-mime', 'scyther', 'jynx', 'electabuzz', 'magmar', 'pinsir', 'tauros', 'magikarp', 'gyarados', 'lapras', 'ditto', 'eevee', 'vaporeon', 'jolteon', 'flareon', 'porygon', 'omanyte', 'omastar', 'kabuto', 'kabutops', 'aerodactyl', 'snorlax', 'articuno', 'zapdos', 'moltres', 'dratini', 'dragonair', 'dragonite', 'mewtwo']
    pokemon_catch= random.choice(pokemon_names)
    if pokemon_catch == "pikachu":
        pokemon = pokemon_catch.upper()
        await ctx.send(f"```Tebrikler! Bir  ⚡️{pokemon}⚡️  yakaladın!```")
    elif pokemon_catch == "charmander":
        pokemon = pokemon_catch.upper()
        await ctx.send(f"```Tebrikler! Bir  🔥{pokemon}🔥  yakaladın!```")
    elif pokemon_catch == "squirtle":
        pokemon = pokemon_catch.upper()
        await ctx.send(f"```Tebrikler! Bir  💦{pokemon}💦  yakaladın!```")
    elif pokemon_catch == "bulbasaur":
        pokemon = pokemon_catch.upper()
        await ctx.send(f"```Tebrikler! Bir  🍃{pokemon}🍃  yakaladın!```")
    else:
        pokemon = pokemon_catch.upper()
        await ctx.send(f"```Yakaladığın Pokemon:  '{pokemon}'```")


@bot.command(name="off") #botu kapatır.
async def off(ctx):
    await ctx.send(f"```{bot.user.name} Kaçar!```")
    await bot.close()



@bot.command(name="reset") #botu yeniden başlatır.
async def restart(ctx):
    await ctx.send("```yüzüme biraz VD-40 çarpıp geliyorum.```")
    os.execv(sys.executable, ["Komputer.py"] + sys.argv)
    await ctx.send("```Tamam geldim, çalışmaya devam edebilirim.```")




bot.run(TOKEN)
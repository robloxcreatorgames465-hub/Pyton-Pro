import discord, random, os, requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

memes = ["mem1", "mem2", "mem3"]
consejos = ["Prefiere envases retornables ♻", 
            "Prefiere Bombillas LED 💡", 
            "Ahorra Agua 💧", 
            "Usa Electrodomesticos Eficientes 📱", 
            "El Vinagre Y Bicarbonato son buenos desengrasantes naturales 🥃🧂", 
            "No Botes Basura En La Calle 🗑", 
            "Evita Usar Aerosol (Dañan La Capa de Ozono)"]
img_name = random.choice(memes)

contenedores = {
    "plastico": "🟡 **Amarillo** (envases plásticos, botellas, tapas, etc.)",
    "vidrio": "🟢 **Verde** (botellas y frascos de vidrio limpios)",
    "papel": "🔵 **Azul** (papel, cartón y revistas)",
    "carton": "🔵 **Azul** (cartón y papeles)",
    "organico": "🟤 **Marrón** (restos de comida, cáscaras, hojas)",
    "pilas": "⚫ **Punto limpio o centro autorizado** (NO al contenedor)",
    "electronico": "⚫ **Punto limpio o reciclaje electrónico**",
}

riesgos = {
    "plastico": "🧴 El **plástico** tarda cientos de años en degradarse. Libera microplásticos que contaminan el agua y dañan la fauna marina.",
    "vidrio": "🍾 El **vidrio** no se degrada naturalmente. Si se rompe, puede causar heridas o incendios por efecto lupa.",
    "papel": "📄 El **papel** contamina si se mezcla con residuos orgánicos o aceites. Además, su producción excesiva contribuye a la deforestación.",
    "carton": "📦 El **cartón** mojado o sucio no se puede reciclar, y ocupa mucho espacio en vertederos.",
    "metal": "🥫 El **metal** tarda décadas en degradarse. La extracción minera para producirlo genera contaminación y daños ecológicos.",
    "tetrapak": "🥛 El **tetrapak** combina plástico, aluminio y cartón, lo que lo hace difícil de reciclar sin plantas especializadas.",
    "organico": "🍌 Los **residuos orgánicos** generan metano (gas de efecto invernadero) si se descomponen sin oxígeno en vertederos.",
    "pilas": "🔋 Las **pilas** contienen metales pesados (como mercurio y plomo) altamente tóxicos para el suelo y el agua.",
    "electronico": "💻 Los **residuos electrónicos** liberan sustancias peligrosas (plomo, cadmio, mercurio) si no se tratan correctamente.",
    "ropa": "👕 La **ropa sintética** libera microfibras plásticas al lavarse y tarda siglos en degradarse."}

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def minus(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left - right)

@bot.command()  
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    # Joined at can be None in very bizarre cases so just handle that as well
    if member.joined_at is None:
        await ctx.send(f'{member} has no join date.')
    else:
        await ctx.send(f'{member} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def mem(ctx):
    imagenes = os.listdir('imagenes')
    with open(f'imagenes/{random.choice(imagenes)}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def consejo(ctx):
    embed = discord.Embed(title="💡 Consejo ecológico", description=random.choice(consejos), color=0x00FF7F)
    await ctx.send(embed=embed)


@bot.command()
async def riesgo(ctx, material: str):
    material = material.lower()
    if material in riesgos:
        descripcion = riesgos[material]
        embed = discord.Embed(
            title=f"⚠️ Riesgos del {material.capitalize()}",
            description=descripcion,
            color=0xFF4444
        )
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"❓ No tengo información sobre los riesgos del material **{material}**. ¡Prueba con otro!")

@bot.command()
async def reciclar(ctx, material: str):
    material = material.lower()
    if material in contenedores:
        respuesta = contenedores[material]
        embed = discord.Embed(
            title=f"♻️ Reciclaje de {material.capitalize()}",
            description=f"{respuesta}",
            color=0x00AAFF
        )
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"🤔 No sé dónde va el material **{material}**. ¡Intenta con otro o escríbelo sin tildes!")


def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_dog_image_url():
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('dog')
async def dog(ctx):
    image_url = get_dog_image_url()
    embed = discord.Embed(title="🐶 ¡Un perrito para ti!")
    embed.set_image(url=image_url)
    await ctx.send(embed=embed)

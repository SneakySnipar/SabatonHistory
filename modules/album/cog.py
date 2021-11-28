from nextcord.ext import commands
import asyncio


class Album(commands.Cog, name="Albums"):
    """Receives album commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def albums(self, ctx):
        """Lists all the music"""
        import nextcord
        e1 = nextcord.Embed(
            title='Sabaton Albums',
            color=0x242bff,
            description='''
            1. Primo Victoria (2005)\n2. Attero Dominatus (2006)\n3. Metalizer (2007)\n4. The Art of War (2008)\n\
            5. Coat of Arms (2010)\n6. Carolus Rex (2012)\n7. Heroes (2014)\n8. The Last Stand (2016)\n\
            9. The Great War (2019)\n10. The War to End All Wars (2022)'''
        )
        e1.add_field(
            name='Navigation:',
            value='''To see another album, use the dropdown menu below\nTo learn about any\
             of these songs, type //learn (songname)\n\nPrev: none\nNext: Primo Victoria (2005)''',
            inline=False
        )

        e2 = nextcord.Embed(
            title='Primo Victoria (2005)',
            color=0x242bff,
            description='''Latin for, *Foremost Victory*, this is the debut studio album by Sabaton.\n\n**Song list:**\
            \n1. Primo Victoria\n2. Reign of Terror\n3. Panzer Battalion\n4. Wolfpack\n5. Counterstrike\n6. Stalingrad\
            \n7. Into the Fire\n 8. Purple Heart\n9. Metal Machine'''
        )
        e2.add_field(
            name='Navigation:',
            value='''To see another album, use the dropdown menu below\nTo learn about any of these songs,\
             type //learn (songname)\n\nPrev: All Albums\nNext: Attero Dominatus (2006)''',
            inline=False
        )
        e3 = nextcord.Embed(
            title='Attero Dominatus (2006)',
            color=0x242bff,
            description='''Sabaton's second studio album and the first to feature the signature camouflage gear and\
             Joakim's vest.\n\n**Song list:**\n1. Attero Dominatus\n2. Nuclear Attack\n3. Rise of Evil\n\
             4. In the Name of God\n5. We Burn\n6. Angel's Calling\n7. Back in Control\n 8. Light in the Black\n\
             9. Metal Crüe'''
        )
        e3.add_field(
            name='Navigation:',
            value='''To see another album, use the dropdown menu below\nTo learn about any of these songs, type //learn\
             (songname)\n\nPrev: Primo Victoria (2005)\nNext: Metalizer (2007)''',
            inline=False
        )
        e4 = nextcord.Embed(
            title='Metalizer (2007)',
            color=0x242bff,
            description='''Sabaton's third released studio album but it was recorded as their professional debut\
             album and released later due to conflicts with the band's first label.\n\n**Song list:**\n1. Hellrider\n\
             2. Thundergods\n 3. Metalizer\n4. Shadows\n5. Burn Your Crosses\n6. 7734\n7. Endless Nights\n8. Hail to\
              the King\n9. Thunderstorm\n10. Speeder\n11. Master of the World\n12. Jawbreaker'''
        )
        e4.add_field(
            name='Navigation:',
            value='''To see another album, use the dropdown menu below\nTo learn about any of these songs, type\
             //learn (songname)\n\nPrev: Attero Dominatus (2006)\nNext: The Art of War (2008)''',
            inline=False
        )
        e5 = nextcord.Embed(
            title='The Art of War (2008)',
            color=0x242bff,
            description='''Sabaton's fourth released studio album which is based on the ancient military treatise\
             by Sun Tzu, *The Art of War*. Each track corresponds to a chapter of the treatise and the songs are based\
              on battles where Sun Tzu's tactics applied.\n\n**Song list**\n1. Sun Tzu Says\n2. Ghost Division\n3.\
               The Art of War\n4. 40:1\n5. Unbreakable\n6. The Nature of Warfare\n7. Cliffs of Gallipoli\n8. Talvisota\
               \n9. Panzerkampf\n10. Union (Slopes of St. Benedict)\n11. The Price of a Mile\n12. Firestorm\n\
               13. A Secret'''
        )
        e5.add_field(
            name='Navigation:',
            value='''To see another album, use the dropdown menu below\nTo learn about any of these songs,\
             type //learn (songname)\n\nPrev: Metalizer (2007)\nNext: Coat of Arms (2010)''',
            inline=False
        )
        e6 = nextcord.Embed(
            title='Coat of Arms (2010)',
            color=0x242bff,
            description='''Sabaton's fifth released studio album\n\n**Song list:**\n1. Coat of Arms\n2. Midway\n\
            3. Uprising\n4. Screaming Eagles\n5. The Final Solution\n6. Aces in Exile\n7. Saboteurs\n8. Wehrmacht\n\
            9. White Death\n10. Metal Ripper'''
        )
        e6.add_field(
            name='Navigation:',
            value='''To see another album, use the dropdown menu below\nTo learn about any of these songs, type\
             //learn (songname)\n\nPrev: The Art of War(2008)\nNext: Carolus Rex (2012)''',
            inline=False
        )
        e7 = nextcord.Embed(
            title='Carolus Rex (2012)(EN/SV)',
            color=0x242bff,
            description='''Sabaton's sixth released studio album. A concept album based on the rise and fall of the\
             Swedish Empire, released with both an English *and* a Swedish version.\n\n**Song list:**\n1.\
              Dominium maris Baltici\n2. The Lion from the North/Lejonet från Norden\n3. Gott mit uns (EN/SV)\n\
              4. A Lifetime of War/En Livstid i krig\n5. 1648 (EN/SV)\n 6. The Carolean's Prayer/Karolinens bön\n\
              7. Carolus Rex (EN/SV)\n8. Killing Ground/Ett slag färgat rött\n9.Poltava (EN/SV)\n10. Long Live the\
               King/Konungens likfärd\n11. Ruina Imperii (SV)'''
        )
        e7.add_field(
            name='Navigation:',
            value='''To see another album, use the dropdown menu below\nTo learn about any of these songs, type\
             //learn (songname)\n\nPrev: Coat of Arms (2010)\nNext: Heroes (2014)''',
            inline=False
        )
        e8 = nextcord.Embed(
            title='Heroes (2014)',
            color=0x242bff,
            description='''Sabaton's seventh released studio album. The album is themed around "heroes", individuals\
             who went beyond the call of duty and put themselves into harm's way for the good of others.\n\n**Song\
              list:**\n1. Night Witches\n2. No Bullets Fly\n3. Smoking Snakes\n4. Inmate 4859\n5. To Hell and Back\n\
              6. The Ballad of Bull\n7. Resist and Bite\n8. Soldier of 3 Armies\n9. Far from the Fame\n\
              10. Hearts of Iron''')
        e8.add_field(
            name='Navigation:',
            value='''To see another album, use the dropdown menu below\nTo learn about any of these songs, type\
             //learn (songname)\n\nPrev: Carolus Rex (2012)\nNext: The Last Stand (2016)''',
            inline=False
        )
        e9 = nextcord.Embed(
            title='The Last Stand (2016)',
            color=0x242bff,
            description='''Sabaton's eighth released studio album. This concept album is themed around some of the\
             greatest "last stands" in history.\n\n**Song list:**\n1. Sparta\n2. Last Dying Breath\n3. Blood of\
              Bannockburn\n4. Diary of an Unknown Soldier\n5. The Lost Battalion\n6. Rorke's Drift\n7. The Last Stand\
              \n8. Hill 3234\n9. Shiroyama\n10. Winged Hussars\n11. The Last Battle\n12. Camouflage\n13. All Guns\
               Blazing\n14. Afraid to Shoot Strangers\n15. Burn in Hell'''
        )
        e9.add_field(
            name='Navigation:',
            value='''To see another album, use the dropdown menu below\nTo learn about any of these songs, type\
             //learn (songname)\n\nPrev: Heroes (2014)\nNext: The Great War (2019)''',
            inline=False
        )
        e10 = nextcord.Embed(
            title='The Great War (2019)',
            color=0x242bff,
            description='''Sabaton's ninth released studio album. This concept album tells of stories from the\
             *Great War*, World War 1.\n\n**Song list:**\n1. The Future of Warfare\n2. Seven Pillars of Wisdom\n\
             3. 82nd All the Way\n4. The Attack of the Dead Men\n5. Devil Dogs\n6. The Red Baron\n7. Great War\n\
             8. A Ghost in the Trenches\n9. Fields of Verdun\n10. The End of the War to End All Wars\n11.\
              In Flanders Fields'''
        )
        e10.add_field(
            name='Navigation:',
            value='''To see another album, use the dropdown menu below\nTo learn about any of these songs, type\
             //learn (songname)\n\nPrev: The Last Stand (2016)\nNext: The War to End All Wars (2022)''',
            inline=False
        )
        e11 = nextcord.Embed(
            title='The War to End All Wars (2022)',
            color=0x242bff,
            description='''Sabaton's upcoming tenth studio album. Another concept album about the *Great War*,\
             World War 1, following the success of their previous album, The Great War.\n\n**Song list:**\n1. Sarajevo\
             \n2. Stormtroopers\n3. Dreadnought\n4. The Unkillable Soldier\n5. Soldier of Heaven\n6. Hellfighters\n\
             7. Race to the Sea\n8. Lady of the Dark\n9. The Valley of Death\n10. Christmas Truce\n11. Versailles'''
        )
        e11.add_field(
            name='Navigation:',
            value='''To see another album, use the dropdown menu below\nTo learn about any of these songs, type\
             //learn (songname)\n\nPrev: The Great War (2019)\nNext: Singles''',
            inline=False
        )
        e12 = nextcord.Embed(
            title='Singles',
            color=0x242bff,
            description='''A list of all the singles that Sabaton has released which are not included in any of\
             their albums.\n\n**Song list:**\n1. In the Army Now (2016)\n2. Bismarck (2019)\n\
             3. The Royal Guard/Livgardet (2021)\n4. Defence of Moscow (2021)\n5. Kingdom Come (2021)\n\
             6. Steel Commanders (2021)''')
        e12.add_field(
            name='Navigation:',
            value='''To see another album, use the dropdown menu below\nTo learn about any of these songs, type\
             //learn (songname)\n\nPrev: The War to End All Wars (2022)\nNext: none''',
            inline=False
        )
        embed_pages = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12]
        reactions = ['⏪', '◀', '▶', '⏩']
        current = 0

        msg = await ctx.send(embed=e1)
        for reaction in reactions:
            await msg.add_reaction(reaction)

        while True:
            try:
                reaction, user = await self.bot.wait_for('reaction_add', check=lambda reaction,
                                                         user: user == ctx.author and reaction.emoji in reactions,
                                                         timeout=60.0)
            except asyncio.TimeoutError:

                embed = embed_pages[current]
                embed.set_footer(text='Timed Out.')
                await msg.clear_reactions()
            else:
                previous_page = current

                if reaction.emoji == '⏪':
                    current = 0
                    await msg.remove_reaction(reaction, ctx.author)
                elif reaction.emoji == '◀':
                    if current > 0:
                        current -= 1
                        await msg.remove_reaction(reaction, ctx.author)
                    else:
                        await msg.remove_reaction(reaction, ctx.author)
                elif reaction.emoji == '▶':
                    if current < len(embed_pages) - 1:
                        current += 1
                        await msg.remove_reaction(reaction, ctx.author)
                    else:
                        await msg.remove_reaction(reaction, ctx.author)
                elif reaction.emoji == '⏩':
                    current = len(embed_pages) - 1
                    await msg.remove_reaction(reaction, ctx.author)
                if current != previous_page:
                    await msg.edit(embed=embed_pages[current])


def setup(bot: commands.Bot):
    bot.add_cog(Album(bot))

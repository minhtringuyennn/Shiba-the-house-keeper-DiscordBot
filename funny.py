import discord
from discord.ext import commands
from discord.ext import tasks
from random import randint
import random
import praw
import configparser
import os
from PIL import Image, ImageDraw, ImageFont
import time
from datetime import datetime
from datetime import timedelta
import requests

PATH = "/root/Shiba-the-house-keeper/"

read_config = configparser.ConfigParser()
path = os.path.join(os.path.dirname(__file__), "config", "config.ini")
read_config.read(path)

REDDIT_ID = read_config.get("config", "redditCilentID")
REDDIT_SECRET = read_config.get("config", "redditSecretKey")
TENOR_API_KEY = read_config.get("config", "tenorAPIKey")

reddit = praw.Reddit(client_id = REDDIT_ID,
                     client_secret= REDDIT_SECRET,
                     user_agent= "github - minhtringuyennn")

class Funny(commands.Cog):
    #OwO what's this
    @commands.command()
    async def mock(self, ctx, *, input= ""):
        await ctx.message.delete()
        output = ""
        for char in input: 
            if char.isalpha(): 
                if random.choice([True, False]): 
                    output += char.upper()
                else: 
                    output += char.lower()
            else: 
                output += char 
        
        if output == "":
            output = ctx.author.name  
            temp = ""
            for char in output: 
                if char.isalpha(): 
                    if random.choice([True, False]): 
                        temp += char.upper()
                    else:
                        temp += char.lower()
                else: 
                    temp += char
                output = temp
    
        await ctx.send(f"{output}")

        #send nud...gif
        embed = discord.Embed()
        embed.set_image(url='https://cdn.discordapp.com/attachments/775431017053945868/787667035580530728/minhtringu-ran-this-command.gif')
        await ctx.send(embed=embed)

    #Shouting to someone
    @commands.command()
    async def shout(self,ctx, *, input= ""):
        await ctx.message.delete()
        output = ""
        for char in input: 
            if char.isalpha(): 
                if char.islower(): 
                    output += char.upper()
                else: 
                    output += char
            else: 
                output += char

        if output != "":
            l = 1
            while l < 5:
                if input[len(input)-1].isalpha():
                    output += input[len(input)-1].upper()
                l += 1
            while l < 10:
                output += "!"
                l+=1
            await ctx.send(f"{output}")
        else:
            await ctx.send(f"ARGHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
        await ctx.send(f"- _{ctx.message.author.name}_")
        #send nud...gif
        embed = discord.Embed()
        embed.set_image(url='https://media1.tenor.com/images/9b29ee560a03a7441490e95778922aaa/tenor.gif')
        await ctx.send(embed=embed)

    @commands.command(aliases=['uwu', 'UwU', 'owo', 'OwO'])
    async def uwuwu(self, ctx):
        await ctx.message.delete()
        await ctx.send("**uwu**")
        await ctx.send(f"- _{ctx.message.author.name}_")

    #etou...
    @commands.command()
    async def etou(self, ctx, *, input = ""):
        await ctx.message.delete()
        if input == "":
            await ctx.send("etou... 👉👈")
        else:
            await ctx.send(f"{input}... 👉👈")
        await ctx.send(f"- _{ctx.message.author.name}_")
        
    #how long is your dick?
    @commands.command()
    async def penis(self,ctx, *, name=""):
        l = 0
        penis = "8D"
        s = randint(0, 15)
        if (ctx.message.author.id == 443116194275524619 and name == ""):
            s = 15
        while l<s:
            penis = penis[:1] + '=' + penis[1:]
            l+=1

        if len(name) == 0:
            name = "your"
        if len(penis)<5:
            await ctx.send(f"get rekt kid, {name} dick is just this {penis} long <:meow_lovelybutt:759037054507810838>")
        elif len(penis)>12:
            name = name[0].upper() + name[1:]
            await ctx.send(f"WOW! {name} is this {penis} long! <:pepe_jesuschrist:758735706267844650>")
        else:
            name = name[0].upper() + name[1:]
            await ctx.send(f"{name} dick is this {penis} long")

    #simp rate?
    @commands.command()
    async def simprate(self,ctx, *, name=""):
        rate = randint(0, 100)
        realsimp =  [340643391618547712]
        if (ctx.message.author.id in realsimp):
            rate = randint(90, 100)
        for id in realsimp:
            if (str(id) in ctx.message.content):
                rate = randint(90, 100)
                break
        tobe = "is"
        if len(name) == 0:
            name = "you"
            tobe = "are"

        if rate<15:
            await ctx.send(f"Ah I see, just {rate}%. {name} {tobe} the man of culture as well. <:hutthuoc:779543902617206804>")
        elif rate>80:
            name = name[0].upper() + name[1:]

            await ctx.send(f"WOW! {rate}%! {name} {tobe} such a simp! <:pepe_jesuschrist:758735706267844650>")
        else:
            name = name[0].upper() + name[1:]
            await ctx.send(f"{name} {tobe} {rate}% simp")

    @commands.command()
    async def meme(self, ctx):
        # await ctx.message.delete()
        await ctx.send("Hể í yỏu mêm <:meo_phecan:772700153806716928>")

        communities_list = ["memes", "dankmemes", "HolUp", "me_irl", "Whatcouldgowrong", "HistoryMemes"]
        commuinity = random.choice(communities_list)
        post_to_pick = random.randint(1, 50)
        
        _submissions = reddit.subreddit(commuinity).top("week")
        submission = _submissions

        # https://i. -> image, v -> video
        while str(submission.url)[8] != 'i':
            for i in range(0, post_to_pick):
                submission = next(x for x in _submissions if not x.stickied)

        await ctx.send(submission.url)

    @commands.command()
    async def mademeuwu(self, ctx):
        # await ctx.message.delete()
        await ctx.send("Nè, vui lên đi, bitch <:meow_lovelybutt:759037054507810838>")

        communities_list = ["aww", "wholesomegifs", "Eyebleach", "MadeMeSmile"]
        commuinity = random.choice(communities_list)
        post_to_pick = random.randint(1, 50)
        
        _submissions = reddit.subreddit(commuinity).top("week")
        submission = _submissions

        # https://i. -> image, v -> video
        while str(submission.url)[8] != 'i':
            for i in range(0, post_to_pick):
                submission = next(x for x in _submissions if not x.stickied)

        await ctx.send(submission.url)

    @commands.command(aliases=['ponk', 'bonk'])
    async def pong(self, ctx, *, name = ""):
        # await ctx.message.delete()
        
        base = Image.open(PATH + "meme_img/bonk.png").convert("RGBA")
        txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
        fnt = ImageFont.truetype(PATH + "Montserrat.ttf", 50)
        
        if len(name) == 0:
            tag_name = ctx.message.author.name
            author_name = "Shiba Bot"
        elif len(name) == 22:
            userID = name[3:-1]
            user_name = await ctx.guild.fetch_member(userID)
            tag_name = user_name.nick
            author_name = ctx.message.author.nick
        else:
            tag_name = name
            author_name = ctx.message.author.nick
            
        author = ImageDraw.Draw(txt)
        author.text((30, 500), author_name, font=fnt, fill=(0, 0, 0, 255))
        
        tag = ImageDraw.Draw(txt)
        tag.text((450, 20), tag_name, font=fnt, fill=(0, 0, 0, 255))

        out = Image.alpha_composite(base, txt)
        out.save('bonk.png')
        
        await ctx.send(file=discord.File('bonk.png'))

    @commands.command(aliases=['luv', 'sendluv'])
    async def luvu(self, ctx, *, name = ""):
        # await ctx.message.delete()
        
        base = Image.open(PATH + "meme_img/luv.jpg").convert("RGBA")
        txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
        fnt = ImageFont.truetype(PATH + "Montserrat.ttf", 50)
        fnt2 = ImageFont.truetype(PATH + "Montserrat.ttf", 20)
        
        if len(name) == 0:
            tag_name = ctx.message.author.name
            author_name = "Shiba Bot"
        elif len(name) == 22:
            userID = name[3:-1]
            user_name = await ctx.guild.fetch_member(userID)
            tag_name = user_name.nick
            author_name = ctx.message.author.nick
        else:
            tag_name = name
            author_name = ctx.message.author.nick
        
        author = ImageDraw.Draw(txt)
        author.text((170, 45), author_name, font=fnt, fill=(0, 0, 0, 255), anchor = "mm")
        
        tag = ImageDraw.Draw(txt)
        tag.text((210, 195), tag_name, font=fnt2, fill=(0, 0, 0, 255), stroke_width=2, stroke_fill=(255, 255, 255, 255), anchor = "mm")

        out = Image.alpha_composite(base, txt)
        out.save('luv.png')
        
        if len(name) != 0:
            tag_name = name

        await ctx.send(f"**{author_name}** đã gửi tình yêu siêu bự đến **{tag_name}** đóooooo <:meow_xoadau:759037054431658036>")
        await ctx.send(file=discord.File('luv.png'))

    @commands.command(aliases=['nhagiatran', 'nvat'])
    async def at(self, ctx, *, input="trầm cảm"):
        str_title = "Nhà giả trân học Nguyễn Võ Anh Thư đã từng nói rằng:"

        str_des = f"'*Đừng {input}!\nTại sao bạn lại {input} khi bạn có thể không {input} nữa?* '"

        return await ctx.send(content=str_title + '\n' + str_des)

    @commands.command(pass_context=True)
    async def shiba(self, ctx):
        # await ctx.message.delete()
        embed = discord.Embed()
        embed.set_image(url='https://i.redd.it/y0o3u4ddkfs71.gif')
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def corgi(self, ctx):
        # await ctx.message.delete()
        embed = discord.Embed()
        embed.set_image(url='https://c.tenor.com/QfBQk0quoS8AAAAM/corgi-cute.gif')
        await ctx.send(embed=embed)

    @commands.command(aliases=['gudbot', 'gudboy'])
    async def gud(self, ctx):
        await ctx.send(f"Cảm ơn nheee {ctx.author.name} <:meow_lovelybutt:759037054507810838>")
        embed = discord.Embed()
        embed.set_image(url='https://i.redd.it/isvpnmalxks71.gif')
        await ctx.send(embed=embed)

    @commands.command(aliases=['hasagi', 'yasou'])
    async def hasagiii(self, ctx):
        qoutes = [
            "Death is like the wind - always by my side.",
            "No cure for fools.",
            "Whispers in the wind speak of a masked swordsman with two blades.",
            "A sword's poor company for a long road.",
            "My honor left a long time ago.",
            "No-one is promised tomorrow.",
            "Follow the wind, but watch your back.",
            "This blade never gets any lighter.",
            "Virtue is no more than a luxury.",
            "The road to ruin is shorter than you think.",
            "Sleep is for the guiltless.",
            "Justice. That's a pretty word.",
            "Hmph. One step ahead of the past.",
            "A wanderer isn't always lost.",
            "Just looking for a road home.",
            "Never could stay in one place.",
            "I will follow this path until the end.",
            "Honor is in the heart, not the name.",
            "I will not forget who I am.",
            "This story is not yet finished.",
            "Is a leaf's only purpose to fall?",
            "Hmh... dying's the easy part.",
        ]
        
        choose_qoute = random.choice(qoutes)
        url = "https://c.tenor.com/WGSFhjmEBm4AAAAC/yasuo-lol.gif"
        result = requests.get(f"https://api.tenor.com/v1/search?q=yasuo&key={TENOR_API_KEY}&limit=50")
        
        if result.status_code == 200:
            json_result = result.json()
            json_check = json_result['next']
            if json_check == "0":
                await ctx.send("{} I didn't found any yasuo gifs".format(ctx.message.author.mention))
            else:
                gif = random.choice(json_result['results'])
                url = gif['media'][0]['gif']['url']
                #url = gif['media']['gif']['url']
        await ctx.send(f"**{choose_qoute}** - *_Yasou_*")
        await ctx.send(str(url))
    
    @commands.command(pass_context=True)
    async def kkk(self, ctx):
        img_list = [PATH + 'meme_img/kkk.jpg', PATH + 'meme_img/kkk2.jpg', PATH + 'meme_img/kkk3.jpg']

        laugh = "ka"
        cou = random.randint(3, 10)
        msg = ""
        if cou <= 5:
            choice = 0
        elif cou > 5 and cou <=8:
            choice = 1
        else:
            choice = 2

        for i in range(0, cou):
            msg += laugh

        await ctx.send(f"*{msg}*")
        await ctx.send(file=discord.File(img_list[choice]))
        await ctx.message.delete()

    @commands.command(aliases=['fine', 'imfine'])
    async def finee(self, ctx, *, name = ""):
        if len(name) == 0:
            tag_name = ctx.message.author.name
        elif len(name) == 22:
            userID = name[3:-1]
            user_name = await ctx.guild.fetch_member(userID)
            tag_name = user_name.nick

            if tag_name == "None":
                tag_name = user_name.name
        else:
            tag_name = name

        msg = "đã cố tỏ ra là mình ổn, nhưng sâu bên trong nước mắt là protein (lysozyme, lactoferrin và lipocalin), enzyme, chất béo, chất chuyển hóa (metabolites) và chất điện phân (electrolytes)"
        await ctx.send(f"**{tag_name}** {msg}")

    @commands.command(aliases=['thankyou', 'thankyouAT'])
    async def tyat(self, ctx, *, name = ""):
        if len(name) == 0:
            tag_name = ctx.message.author.name
        elif len(name) == 22:
            userID = name[3:-1]
            user_name = await ctx.guild.fetch_member(userID)
            tag_name = user_name.nick

            if tag_name == "None":
                tag_name = user_name.name
        else:
            tag_name = name
        
        splitName = tag_name.split(" ")
        hashTag = ""

        for token in splitName:
            hashTag += str(token).capitalize()

        tag_name = "**" + tag_name + "**"

        await ctx.send(f"...Nhớ ngày nào tôi cùng {tag_name} còn dẫn dắt từng bước chân chập chững trên con đường chơi LOL. Nôm vậy mà cũng đã được gần một năm. Sao mà quên đường những lúc cùng {tag_name} và những người anh em FWB khác chinh phục biết bao trận chiến, chu du qua bao nhiệm vụ. Thậm chí có lúc tưởng chừng như gục ngã, song, mọi người đã cùng nhau mỉm cười và vượt qua.\n\n\tGiờ đây, {tag_name} đã cũng tìm được những bến đỗ mới, nơi thực sự đem lại những khoảnh khắc tỏa sáng và hạnh phúc cho mình. Dẫu khó khăn để chấp nhận ngày 1 ngày 2 nhưng hơn ai hết, tôi biết rằng ai cũng nên cho những sự lựa chọn. Và {tag_name} chọn điểm đến mới cho cuộc đời mình.\n\n\tNhưng không sao, miễn là chúng ta còn nhớ nhau, còn yêu thương nhau, còn đùm bọc nhau thì không gì là không thể, {tag_name} nhỉ? Mong là team FWB sẽ không lạc vào nhà kho cũ kĩ trong tận sâu góc tối ký ức của {tag_name}. Và cũng không quên chúc {tag_name} luôn vui vẻ và thành công trên con đường và hành trình mới. Chúng tôi, team FWB, cũng sẽ tiếp tục mà không có {tag_name}. Mong cả hai sẽ phát triển ngày càng vững mạnh và phồn vinh.\n\n\tMột lần nữa, chân thành cảm ơn {tag_name} vì tất cả.\n\n#ThankYou{hashTag} #TeamFWB_MãiMặn")
    
    @commands.command(aliases=['tth', 'ca'])
    async def trongtruonghop(self, ctx, *, name = "discord"):
        await ctx.message.delete()
        await ctx.send(f"Trong trường hợp {name} này bị điều tra bởi các cơ quan trực thuộc bộ công an (hoặc các tổ chức chính trị tương tự phục vụ cho nhà nước CHXHCNVN), tôi khẳng định mình không liên quan tới {name} hoặc những cá nhân khác trong {name} này. Tôi không rõ tại sao mình lại có mặt ở đây vào thời điểm này, có lẽ tài khoản của tôi đã được thêm bởi một bên thứ ba. Tôi cũng xin khẳng định rằng mình không hề giúp sức cho những hành động chống phá Đảng và nhà nước của các thành viên trong {name} này. Tôi cũng không quên khẳng định quyết tâm chiến thắng đại dịch Covid-19, nhấn mạnh chủ quyền không thể tranh cãi với quần đảo Hoàng Sa và Trường Sa, cũng như tính chính nghĩa của cuộc chiến giải phóng người dân Campuchia khỏi thảm họa diệt chủng Khmer Đỏ.")
        
    @commands.command(aliases=['thuocanthan', 'anthan'])
    async def thuoc(self, ctx, *, input = ""):
        sz = len(input)
        author = ctx.message.author
        list = input.split(", ")

        if len(list) > 2:
            await ctx.send("Dư tên rồi má!")
            return

        name = list[0]

        if len(list) == 1:
            name2 = ctx.message.author.name
        elif len(list) == 2:
            name2 = list[1]

        if len(name) == 0:
            tag_name = ctx.message.author.name
        elif len(name) == 22:
            userID = name[3:-1]
            user_name = await ctx.guild.fetch_member(userID)
            tag_name = user_name.nick

            if tag_name == "None":
                tag_name = user_name.name
        else:
            tag_name = name

        if len(name2) == 22:
            userID = name2[3:-1]
            user_name = await ctx.guild.fetch_member(userID)
            tag_name2 = user_name.nick

            if tag_name2 == "None":
                tag_name2 = user_name.name
        else:
            tag_name2 = name2

        await ctx.send(f"Tại sao lúc vui {name} bao giờ cũng đang bận ?\nLúc bên {name2} bao giờ cũng đang giận ?\nNói chung {name2} chỉ là thuốc an thần\nVới {name} {name2} chỉ là thuốc an thần <:PepeKMS:916687813582393384>")

    @commands.command(aliases=['hug', 'sendhug'])
    async def hugmeuwu(self, ctx, *, name = ""):
        # await ctx.message.delete()
        if len(name) == 0:
            tag_name = ctx.message.author.name
            author_name = "Shiba Bot"
        elif len(name) == 22:
            userID = name[3:-1]
            user_name = await ctx.guild.fetch_member(userID)
            tag_name = user_name.nick
            author_name = ctx.message.author.nick

            if author_name == "None":
                author_name = ctx.message.author.name
        else:
            tag_name = name
            author_name = ctx.message.author.nick

        # Image editor
        base1 = Image.open(PATH + "meme_img/hug1.png").convert("RGBA")
        base2 = Image.open(PATH + "meme_img/hug2.png").convert("RGBA")
        
        txt1 = Image.new("RGBA", base1.size, (255, 255, 255, 0))
        txt2 = Image.new("RGBA", base2.size, (255, 255, 255, 0))

        fnt = ImageFont.truetype(PATH + "Montserrat.ttf", 75)
        fnt2 = ImageFont.truetype(PATH + "Montserrat.ttf", 60)
        
        author1 = ImageDraw.Draw(txt1)
        tag1 = ImageDraw.Draw(txt1)
        author1.text((520, 600), author_name, font=fnt, fill=(0, 0, 0, 255), stroke_width=6, stroke_fill=(255, 255, 255, 255), anchor = "mm")
        tag1.text((700, 195), tag_name, font=fnt2, fill=(0, 0, 0, 255), stroke_width=6, stroke_fill=(255, 255, 255, 255), anchor = "mm")

        author2 = ImageDraw.Draw(txt2)
        tag2 = ImageDraw.Draw(txt2)
        author2.text((460, 300), author_name, font=fnt, fill=(0, 0, 0, 255), stroke_width=6, stroke_fill=(255, 255, 255, 255), anchor = "mm")
        tag2.text((500, 750), tag_name, font=fnt2, fill=(0, 0, 0, 255), stroke_width=6, stroke_fill=(255, 255, 255, 255), anchor = "mm")

        out1 = Image.alpha_composite(base1, txt1)
        out1.save('hug1.png')

        out2 = Image.alpha_composite(base2, txt2)
        out2.save('hug2.png')
        
        if len(name) != 0:
            tag_name = name

        await ctx.send(f"**{author_name}** đã gửi một cái ôm đến **{tag_name}** đóooooo <:meow_lovelybutt:759037054507810838>")
        await ctx.send(file=discord.File('hug1.png'))
        await ctx.send(file=discord.File('hug2.png'))

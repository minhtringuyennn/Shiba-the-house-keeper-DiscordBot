from discord.ext import commands
from discord.ext import tasks
import configparser
import discord
import os
import time
import asyncio
from datetime import datetime

class DefaultCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        read_config = configparser.ConfigParser()
        path = os.path.join(os.path.dirname(__file__), "config", "config.ini")
        read_config.read(path)
        self.LogID = read_config.get("config", "LogChannel")
    
    @commands.Cog.listener()
    async def on_command(self, ctx):
        # you'll need this because you're also using cmd decorators
        channel = self.bot.get_channel(int(self.LogID))
        await channel.send(f'{ctx.message.author} run `{ctx.message.content}` in channel `{ctx.message.channel}` in server `{ctx.message.guild}`')

    @commands.Cog.listener()
    async def on_ready(self):
        print('Ready!')
        print('Logged in as ---->', self.bot.user)
        print('ID:', self.bot.user.id)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Tưởng rằng lệnh sẽ được thực thi sao??? Không! Đây là Dio <:jco:781338022078840832>")
            return
        channel = self.bot.get_channel(int(self.LogID))
        await channel.send(f'command `{ctx.message.content}` at channel `{ctx.message.channel}` in server `{ctx.message.guild}` error: `{error}')

        #if isinstance(error, commands.CommandNotFound):
        #    await ctx.send(f"Nhập sai lệnh rồi bạn ơi, thất bại quá đi <:pepe_suicide:758735705882361887>")
        #    await ctx.send(f"`{ctx.message.content}` không phải là một lệnh được bot hỗ trợ ở thời điểm hiện tại")
        #    await ctx.send(f"Các lệnh mà bot hỗ trợ:")
        #    await self.help(ctx)
        #    return
    
    # @commands.command(name="pong")
    # async def pong(self, ctx: commands.Context):
    #   start_time = time.time()
    #   end_time = time.time()
    #   await message.edit(content=f"Pong! {round(self.bot.latency * 1000)}ms\nAPI: {round((end_time - start_time) * 1000)}ms")

    @commands.command(aliases=['rmmsg', 'delete'])
    async def remove_msg(self, ctx, *, number = 5):
        this_channel = ctx.message.channel.id
        
        # logs channel, confession channel and request channel
        accepted_channel = [899925135279132683, 789157458647711785, 791112384924090389]
        
        if this_channel in accepted_channel:
            number += 1
            await ctx.message.delete();
            await ctx.channel.purge(limit=number)
            await ctx.send(f"**{ctx.message.author.nick}** *đã phong ấn {number - 1} tin nhắn vào hư vô* ***mãi mãi.***")
        else:
            await ctx.send(f"Êi, đừng lạm dụng phong ấn, sẽ bị tha hoá bởi quyền lực đó bạn ơi <:pepe_deepthink:758735705912115203>")

    @commands.command(pass_context=True)
    async def help(self, ctx): 
        # author = ctx.message.author
        embed = discord.Embed(
            coulour=discord.Color.red()
        )
        embed.set_author(name='Thông tin nhanh:')
        embed.add_field(name='Về bot',
                        value='Tác giả: Bạch Ngọc Minh Tâm và Nguyễn Minh Trí \n Một bot đơn giản để phục vụ server cho nhóm bạn của tác giả.',
                        inline=True)
        embed.add_field(name='>roll',
                        value='Có 2 kiểu: " >roll " với mặc định là 5s và " >roll {số giây còn lại} " \n Thời gian roll tối thiểu là 5s và thời gian tối đa là 90s.',
                        inline=False)
        embed.add_field(name='>rollroom',
                        value='Có 2 kiểu: " >rollroom " với mặc định là 5s và " >rollroom {số giây còn lại} " \n Thời gian roll tối thiểu là 5s và thời gian tối đa là 90s.',
                        inline=False)
        embed.add_field(name='>listroom', value='Trả về thông tin channel hiện tại mà người chơi đang tham gia.',
                        inline=False)
        embed.add_field(name='>remainTurn',
                        value='Có 2 kiểu: " >remainTurn " và " >remainTurn {số lượt ít nhất} {số lượt nhiều nhất} " \n Trả về số lượt chơi còn lại của trò chơi \n Giá trị trả về ít nhất 1 lượt chơi và tối đa 20 lượt chơi.',
                        inline=False)
        embed.add_field(name='>choose',
                        value='Chỉ cần gõ " >choose {danh sách lựa chọn ngăn cách bởi dấu phẩy}"" \n Trả về sự lựa chọn ngẫu nhiên \n Có thể trả về dù chỉ với 1 hay rất nhiều lựa chọn',
                        inline=False)
        # embed.add_field(name='>p',
        #                 value='Chỉ cần gõ " >p {đường link Youtube}"" \n Join channel và phát nhạc cho mọi người \n Khi không cần thiết có thể gõ >leave \n Tính năng đang được xây dựng',
        #                 inline=False)
        embed.add_field(name='>mock',
                        value='Có 2 kiểu: " >mock " và " >mock {nội dung} " \n "Trả về Câu CHữ KHIÊu khícH \n Giá trị mặc định là tên người gọi lệnh.',
                        inline=False)
        embed.add_field(name='>shout',
                        value='Có 2 kiểu: " >shout " và " >shout {nội dung} " \n "Dùng để chửi thằng lợn nào đó \n Giá trị mặc định là ARGHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH.',
                        inline=False)
        embed.add_field(name='>owo',
                        value='owo what is this',
                        inline=False)
        embed.add_field(name='>etou',
                        value='Có 2 kiểu: " >etou " và " >etou {nội dung} " \n :point_right::point_left:',
                        inline=False)
        embed.add_field(name='>penis',
                        value='Có 2 kiểu: " >penis " và " >penis {người được tag} " \n How long is yours? <:cuoi_deu:772700153806716928>',
                        inline=False)
        embed.add_field(name='>simprate',
                        value='Có 2 kiểu: " >simprate " và " >simprate {người được tag} " \n Bạn yêu người yêu bạn thế nào <:meow_woah:759037054968397904>',
                        inline=False)    
        embed.add_field(name='>createvote',
                        value='Có 2 kiểu: " >createvote " sẽ add emoji ở tin nhắn gần đó nhất và " >createvote {message id} "',
                        inline=False)
        embed.add_field(name='>nhagiatran',
                        value='Có 2 kiểu: " >nhagiatra " và " >nvat {nội dung} " \n hãy đoán xem đệ nhất giả trân, tiên tri zũ chụ nói gì về điều mà bạn muốn biết :pusheen_popcorn:',
                        inline=False)
        embed.add_field(name='>confession',
                        value='Có 2 kiểu: " >cofession" và ">cfs" \n Muốn bày tỏ lời yêu thương ư? hãy dùng lệnh này \n Lưu ý: Bạn chỉ có thể gửi riêng lệnh này cho bot \n Bước 1: hãy chọn server mà bạn muốn gửi cfs \n Bước 2: Hãy nhập nội dung của cfs mà bạn định gửi \n Bước 3: kiểm tra channel confession thôi \n bạn cũng có thể xóa và sửa confession bằng cách xóa và sửa nội dung của bạn đã gửi cho bot',
                        inline=False)
        # await author.send(embed=embed)
        await ctx.send(embed=embed)

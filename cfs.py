import os
import asyncio
import discord
import datetime
import requests
import configparser
from discord.ext import commands

read_config = configparser.ConfigParser()
path = os.path.join(os.path.dirname(__file__), "config", "config.ini")
read_config.read(path)

TENOR_API_KEY = read_config.get("config", "tenorAPIKey")

servers = {}

confession_channel = {
	# server_id : confession_channel_id
	447040511681757184 : 779746460236775495
}

class Confess(commands.Cog):
    
    def is_int(s):
        try: 
            int(s)
            return True
        except ValueError:
            return False

    def get_tenor_url(view_url):
        if view_url.lower().endswith('gif'):
            return view_url
        gif_id = view_url.split('-')[-1]
        url = f'https://api.tenor.com/v1/gifs?ids={gif_id}&key={TENOR_API_KEY}'
        res = requests.get(url)
        if res.status_code == 200:
            return res.json()['results'][0]['media'][0]['gif']['url']
        else:
            return None

    def get_giphy_url(view_url):
        if view_url.lower().endswith('gif'):
            return view_url
        else:
            gif_id = view_url.split('-')[-1]
            return f'https://media.giphy.com/media/{gif_id}/giphy.gif'

    def prepare_embed(msg):
        embedVar = discord.Embed(title='Anonymous Confession')
        embedVar.timestamp = datetime.datetime.utcnow()

        if msg.content:
            embedVar.description = msg.content

        if msg.embeds:
            data = msg.embeds[0]
            if data.type == 'image':
                embedVar.set_image(url=data.url)
                if data.url == msg.content:
                    embedVar.description = None
            if data.type == 'gifv' and data.provider.name == 'Tenor':
                embedVar.set_image(url=get_tenor_url(data.url))
                if data.url == msg.content:
                    embedVar.description = None
            if data.type == 'gifv' and data.provider.name == 'Giphy':
                embedVar.set_image(url=get_giphy_url(data.url))
                if data.url == msg.content:
                    embedVar.description = None

        if msg.attachments:
            file = msg.attachments[0]
            if file.url.lower().endswith(('png', 'jpeg', 'jpg', 'gif', 'webp')):
                embedVar.set_image(url=file.url)
            else:
                embedVar.add_field(name='Attachment', value=f'[{file.filename}]({file.url})')

        return embedVar
        
    async def check_if_delete(msg, confession, confirmation):
        def check(deleted_msg):
            return msg.id == deleted_msg.id

        try:
            await self.commands.wait_for('message_delete', timeout=120, check=check)
            await confession.delete()
            await confirmation.edit(content=f'✅ Confession với mã `{confession.id}` tại {confession.channel.mention} đã bị xoá.')
            
        except asyncio.TimeoutError:
            return
    
    @commands.command()
    @commands.dm_only()
    async def confession(self, ctx):
        mutual_servers = []
        for guild in self.commands.guilds:
            if ctx.author.id in servers[guild.id]:
                mutual_servers.append(guild)
        
        embedVar = discord.Embed(title = 'Chọn Server')
        embedVar.description = '**'
        
        i = 0
        for guild in mutual_servers:
            i = i + 1
            embedVar.description += str(i) + ' - ' + guild.name + '\n\n'
            
        embedVar.description += '**'
        embedVar.set_footer(text='Bạn có một phút để chọn - gửi "cancel" để huỷ đăng.')
        await ctx.send(embed=embedVar)

        def server_select(msg):
            return msg.channel == ctx.channel and msg.author == ctx.author and ((is_int(msg.content) and int(msg.content) <= i and int(msg.content) >= 1) or msg.content == 'cancel')

        try:
            msg = await self.commands.wait_for('message', timeout=60, check=server_select)
        except asyncio.TimeoutError:
            await ctx.send('⏳ Đã hết thời gian chọn server. Vui lòng gửi lại confession.')
            return

        if msg.content == 'cancel':
            await ctx.send('✅ Đã huỷ')
            return

        guild = mutual_servers[int(msg.content) - 1]
        confess_in = self.commands.get_channel(confession_channel[guild.id])
        embedVar = discord.Embed()
        embedVar.title = 'Gửi tại : ' + guild.name
        embedVar.description = f'Gửi confession của bạn tại đây / hoặc gửi hình ảnh / up file ảnh ẩn danh tại {confess_in.mention}.'
        embedVar.set_footer(text='Bạn có 2 phút để phản hồi - gửi "cancel" để huỷ')
        await ctx.send(embed=embedVar)

        def check_confess(msg):
            return msg.channel == ctx.channel and msg.author == ctx.author

        try:
            msg = await self.commands.wait_for('message', timeout=120, check=check_confess)
        except asyncio.TimeoutError:
            await ctx.send('⏳ Bạn đã hết thời gian. Vui lòng gửi lại confession.')
            return

        if msg.content == 'cancel':
            await ctx.send('✅ Đã huỷ')
            return

        confession = await confess_in.send(embed = prepare_embed(msg))
        confirmation = await ctx.send(f'✅ Confession của bạn đã được thêm tại {confess_in.mention}!')

        asyncio.create_task(check_if_delete(msg, confession, confirmation))

        def check_edit(before, after):
            return msg.id == after.id
        
        edit_count = 0
        
        if msg.edited_at:
            await confession.edit(embed = prepare_embed(msg))
            edit_count += 1
            await confirmation.edit(content=f'✅ Cofession với id:`{confession.id}` tại {confess_in.mention} đã chỉnh sửa ({edit_count}) lần.')
        
        while True:
            try:
                before, after = await self.commands.wait_for('message_edit', timeout=120, check=check_edit)
                await confession.edit(embed = prepare_embed(after))
                edit_count += 1
                await confirmation.edit(content=f'✅ Confession với id `{confession.id}` tại {confess_in.mention} đã chỉnh sửa ({edit_count}) lần.')
            except asyncio.TimeoutError:
                return
class VoiceRoom():
    members = []
    def __init__(self,ctx):
        if ctx.author.voice and ctx.author.voice.channel:
            self.channel = ctx.author.voice.channel
            mems = ctx.message.author.voice.channel.members
            for mem in mems:
                if not mem.bot:
                    self.members.append(mem)
        else:
            self.channel = None
    def refresh(self,ctx):
        if ctx.author.voice and ctx.author.voice.channel:
            self.channel = ctx.author.voice.channel
            self.members.clear()
            mems = ctx.message.author.voice.channel.members
            for mem in mems:
                if not mem.bot:
                    self.members.append(mem)
    def listname(self):
        member_name = []
        for mem in self.members:
            member_name.append(mem.name)
        return member_name
    def channelname(self,ctx):
       return self.channel

import requests
from nonebot import on_command, CommandSession

@on_command('sx', aliases=('缩写', 'zy', '转义', 'nhnhhsh', '/sx', '\sx'), only_to_me=False)
async def nbnhhsh(session: CommandSession):
    episode = session.current_arg_text.strip()
    if not episode:
        await session.send('请输入缩写的内容，缩写-nhnhhsh-能不能好好说话，web:https://lab.magiconch.com/nbnhhsh/，前缀sx触发', at_sender=True)
    else:
        try:
            url = f'https://lab.magiconch.com/api/nbnhhsh/guess'
            data = {
                "text" : episode
            }
            r = requests.post(url,data=data,timeout=5)
            data = r.json()[0]["trans"]
            msg = "可能拼音缩写的是："+str(data)
            await session.send(msg, at_sender=True)
        except:
            await session.send("未查询到转义，可前往https://lab.magiconch.com/nbnhhsh/ 查询/贡献词条", at_sender=True)

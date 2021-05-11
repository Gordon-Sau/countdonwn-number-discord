import operator
import asyncio

import os
from dotenv import load_dotenv

from evaluate import evaluate
from generate import generate

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='!')

data = ()
scores = {}
task = None

async def final_results(ctx):
    global data, scores
    send = ['results:']
    for k, v in sorted(scores.items(), key=operator.itemgetter(1)):
        send.append(f'{k}: {v}')
    send = '\n'.join(send)
    data = ()
    scores = {}
    await ctx.send(send)

@bot.command(name='start')
async def start(ctx, n_large: int, length: int):
    global data, scores, task
    if task != None:
        task[0].cancel()
        await task[1]
    task = None
    try:
        data = generate(n_large)
    except Exception as e:
        await ctx.send(str(e))
    scores = {}
    await ctx.send(f"numbers: {data[0]}\ntarget: {data[1]}")
    task = asyncio.create_task(asyncio.sleep(length)), final_results(ctx)
    await task[0]
    await task[1]

@bot.command(name='ans')
async def ans(ctx, exp: str):
    if data == ():
        await ctx.send("No game is running at the moment")
        return
    try:
        score = evaluate(exp, data[0], data[1])
    except Exception as e:
        await ctx.send(str(e))
        return
    mention = ctx.message.author.mention
    scores[mention] = score
    await ctx.send(f"{mention} gets {score} points")

if __name__ == '__main__':
    bot.run(TOKEN)
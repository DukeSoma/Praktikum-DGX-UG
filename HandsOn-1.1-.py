# Author: @makanyakuliah
# DO NOT SELL THIS CODE, PLEASE?

import asyncio

async def gabung_kata(kata):
    return ' '.join(kata).title()

async def main():
    kata = ['saya', 'suka', 'ai', 'hoshino']
    hasil = await gabung_kata(kata)
    print(hasil)

await main()

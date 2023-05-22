# Author: @makanyakuliah
# DO NOT SELL THIS CODE, PLEASE?
# Petunjuk : Ganti kata sesuai dengan kemauan Anda, lalu jalankan di Google Colab

import asyncio

async def gabung_kata(kata):
    return ' '.join(kata).title()

async def main():
    # Ganti kata di bawah tanpa menghilangkan tanda ' '
    kata = ['saya', 'suka', 'ai', 'hoshino']
    hasil = await gabung_kata(kata)
    print(hasil)

await main()

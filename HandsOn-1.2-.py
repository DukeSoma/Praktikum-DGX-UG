# Author: @makanyakuliah
# DO NOT SELL THIS CODE, PLEASE?
# Petunjuk: Ganti kata sesuai dengan kemauan Anda, lalu jalankan di Google Colab

import asyncio

async def gabung_kata(kata):
    return ' '.join(kata).title()

async def hitung_karakter(kalimat):
    return sum(not c.isspace() for c in kalimat)

async def main():
    # Ganti kata di bawah tanpa menghilangkan tanda ' '
    kata = ['saya', 'suka', 'ai', 'hoshino']
    hasil = await gabung_kata(kata)
    print(hasil)
    
    jumlah_karakter = await hitung_karakter(hasil)
    print(f'Jumlah karakter (tanpa spasi): {jumlah_karakter}')

await main()

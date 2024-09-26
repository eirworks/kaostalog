<template>
    <div class="md:w-2/3 container mx-auto">
        <div class="font-bold text-2xl mb-5 text-center">Product Name</div>
        <div class="flex justify-center mb-5 items-center space-x-3">
            <div>
                <button type="button" class="rounded border border-black hover:bg-gray-200 p-3">&larr;</button>
            </div>
            <div class="w-1/2 h-[400px] bg-gray-500"></div>
            <div><button type="button" class="rounded border border-black hover:bg-gray-200 p-3">&rarr;</button></div>
        </div>
        <div class="my-5 flex justify-center space-x-3 flex-wrap">
            <div v-for="n in 5">
                <div class="bg-gray-500 cursor-pointer w-[50px] h-[50px]" :class="{'border border-black shadow': n == 1}"></div>
            </div>
        </div>
        <div class="my-5">
            <div class="grid md:grid-cols-2 gap-3">
                <div>
                    <div class="mb-3 text-sm">Tentang produk ini</div>
                    <div>
                        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Laborum nobis, saepe ipsa laboriosam corporis iusto, quidem, doloribus quia odio incidunt voluptas illo. Odit quidem totam veritatis aliquam modi doloribus. Repudiandae.
                    </div>
                </div>
                <div>
                    <DataItem name="Ukuran Tersedia:">
                        <div class="flex space-x-3">
                            <div v-for="s in ['s', 'm', 'l', 'xl', 'xxl', 'xxxl']" 
                                class="uppercase" 
                                :key="s">{{ s }}</div>
                        </div>
                    </DataItem>
                    <DataItem name="Warna">
                        <div class="flex space-x-3">
                            <div v-for="s in ['merah', 'hijau', 'hitam', 'putih']" 
                                class="uppercase" 
                                :key="s">{{ s }}</div>
                        </div>
                    </DataItem>
                    <DataItem name="Material">
                        Katun (Cotton)
                    </DataItem>
                    
                </div>
            </div>
            
        </div>
        <ShopList center get-it-on />
        <Contacts />
    </div>
</template>

<script setup>
import DataItem from '../components/DataItem.vue'
import { shops, contacts } from '@/site';
import ShopList from '@/components/ShopList.vue';
import Contacts from '@/components/Contacts.vue';
</script>
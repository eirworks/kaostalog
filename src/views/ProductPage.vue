<template>
    <div class="md:w-2/3 container mx-auto">
        <div v-if="store.product === null && store.loading == false">
            <div class="text-center p-10 bg-red-200 text-red-800">
                Maaf, produk tidak ditemukan...
            </div>
        </div>
        <div v-if="store.product !== null">
            <div class="font-bold text-2xl mb-5">{{ store.product.title }}</div>
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
            <div class="grid md:grid-cols-3 gap-5">
                <div class="col-span-2">
                    <div class="mb-3 text-sm text-gray-500">Tentang produk ini</div>
                    <div>
                        {{ store.product.description }}
                    </div>
                </div>
                <div>
                    <DataItem name="Ukuran Tersedia:">
                        <div class="flex space-x-3">
                            <div v-for="s in store.product.sizes" 
                                class="uppercase" 
                                :key="s">{{ s }}</div>
                        </div>
                    </DataItem>
                    <DataItem name="Warna">
                        <div class="flex space-x-3">
                            <div v-for="s in store.product.colors" 
                                class="capitalize" 
                                :key="s">{{ s }}</div>
                        </div>
                    </DataItem>
                    <DataItem name="Material">
                        {{ store.product.material }}
                    </DataItem>
                    
                </div>
            </div>
            
        </div>
        <ShopList center get-it-on />
        <Contacts />
        </div>
    </div>
</template>

<script setup>
import DataItem from '../components/DataItem.vue'
import { shops, contacts } from '@/site';
import ShopList from '@/components/ShopList.vue';
import Contacts from '@/components/Contacts.vue';
import { useViewProductStore } from '@/store/products';
import { useRoute } from 'vue-router';

const route = useRoute()
const store = useViewProductStore()

store.getProduct(route.params.id)
</script>
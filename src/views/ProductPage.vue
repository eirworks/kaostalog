<template>
    <div class="md:w-2/3 container mx-auto p-3">
        <div v-if="store.product === null && store.loading == false">
            <div class="text-center p-10 bg-red-200 text-red-800">
                Maaf, produk tidak ditemukan...
            </div>
        </div>
        <div v-if="store.product !== null">
            <div class="font-bold text-2xl mb-5">{{ store.product.title }}</div>
            <ImageGallery :images="store.product.image_urls" />
            <div class="my-5">
                <div class="grid md:grid-cols-3 gap-5">
                    <div class="col-span-2">
                        <div class="mb-3 text-lg font-bold text-gray-500">{{ store.product.title }}</div>
                        <div v-html="marked.parse(store.product.description)" class="prose"></div>
                        <!-- <div>{{ store.product.description }}</div> -->
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

<script setup lang="ts">
import DataItem from '@/components/DataItem.vue';
import ShopList from '@/components/ShopList.vue';
import Contacts from '@/components/Contacts.vue';
import { useViewProductStore } from '@/store/products';
import { useRoute } from 'vue-router';
import ImageGallery from '@/components/ImageGallery.vue';
import { nl2br } from '@/nl2br';
import { marked } from 'marked';

const route = useRoute()
const store = useViewProductStore()

store.getProduct(route.params.id)
</script>
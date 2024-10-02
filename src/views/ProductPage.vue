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
                            <!-- <div class="flex space-x-3">
                                <div v-for="s in store.product.sizes" 
                                    class="uppercase" 
                                    :key="s">{{ s }}</div>
                            </div> -->
                            <div class="mt-3">
                                <a href="/size_guide.jpg" target="_blank" class="mb-1">
                                    <img src="/size_guide.jpg" alt="Panduan Ukuran">
                                </a>
                                <!-- <button class="w-full text-xs underline text-center text-gray-500" @click="showSizeGuide = !showSizeGuide">{{ showSizeGuide ? 'Sembunyikan' : 'Lihat panduan ukuran' }}</button> -->
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
            <Socials />
        </div>
    </div>
</template>

<script setup lang="ts">
import DataItem from '@/components/DataItem.vue';
import ShopList from '@/components/ShopList.vue';
import { useViewProductStore } from '@/store/products';
import { useRoute } from 'vue-router';
import ImageGallery from '@/components/ImageGallery.vue';
import { marked } from 'marked';
import { ref } from 'vue';
import Socials from '@/components/Socials.vue';

const route = useRoute()
const store = useViewProductStore()

const showSizeGuide = ref(false)

store.getProduct(route.params.id)
</script>
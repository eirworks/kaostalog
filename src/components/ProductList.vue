<template>
    <div>
        <div class="mb-5 flex space-x-3 items-center" v-if="store.keyword">
            <div class="flex-1">
                Hasil pencarian untuk "{{ store.keyword }}" 
                menghasilkan {{ store.products.length }} produk.
            </div>
            <div>
                <button class="text-sm text-gray-500" @click="store.clearSearch()">Hapus pencarian</button>
            </div>
        </div>
        <div class="grid grid-cols-2 md:grid-cols-3 gap-5">
            <div v-for="product in store.products">
                <RouterLink :to="`/products/${product.id}`">
                    <div class="flex justify-center">
                        <div class="shrink w-full h-full bg-gray-500 rounded">
                            <img :src="product.image_urls[0]" :alt="product.name">
                        </div>
                    </div>
                    <div class="text-center">
                        {{ product.name }}
                    </div>
                </RouterLink>
            </div>
        </div>
    </div>
    
</template>

<script setup lang="ts">
import { RouterLink } from 'vue-router';
import { useProductsStore } from '@/store/products';
const props = defineProps({
    'search': String
})

const store = useProductsStore()

store.getProducts()
</script>
<template>
    <div>
        <div class="mb-5" v-if="props.search">
            Hasil pencarian untuk "{{ props.search }}"
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
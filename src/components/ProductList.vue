<template>
    <div>
        <div class="mb-5" v-if="props.search">
            Hasil pencarian untuk "{{ props.search }}"
        </div>
        <div class="grid grid-cols-3 gap-5">
            <div v-for="n in 10">
                <RouterLink :to="`/products/${n}`">
                    <div class="flex justify-center">
                        <div class="shrink w-full h-[250px] bg-gray-500 rounded"></div>
                    </div>
                    <div class="text-center">
                        Product #{{ n }}
                    </div>
                    <div class="text-center text-gray-500 text-sm">
                        Rp. 50.000
                    </div>
                </RouterLink>
            </div>
        </div>
    </div>
    
</template>

<script setup>
import { RouterLink } from 'vue-router';
const props = defineProps({
    'search': String
})
</script>
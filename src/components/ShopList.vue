<template>
    <div>
        <div class="text-center text-sm text-gray-500 mb-5" v-if="getItOn">Dapatkan di:</div>
        <div class="flex space-x-5" :class="{'justify-center': center}">
        <div class="h-[24px]" v-for="shop in shops" key="shop.type">
            <a :href="shop.value" target="_blank">
                <img class="h-full" :src="`/${shop.type}.png`" :alt="`Marketplace ${shop.type}`">
            </a>
        </div>
    </div>
    </div>
</template>

<script setup lang="ts">
import {shops} from '@/site'
const props = defineProps({
    center: Boolean,
    getItOn: Boolean
})
</script>
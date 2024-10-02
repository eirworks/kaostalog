<template>
    <div class="my-5">
        <div class="text-gray-500 text-center text-sm mb-5" v-if="!props.noTitle">Hubungi Kami</div>
        <div class="flex flex-col md:flex-row space-y-5 md:space-y-0 md:space-x-5 items-center md:justify-center">
            <div v-for="social in socials" class="flex space-x-3 items-center">
                <div>
                    <a :href="social.value" class="flex space-x-3 items-center">
                        <img :src="`/${social.type}.png`" :alt="social.name" :class="{'w-[40px]': !props.simple, 'w-[28px]': props.simple}">
                        <div v-if="!props.simple">{{ social.text }}</div>
                    </a>
                </div>
            </div>
        </div>
    </div>
</template>
<script setup lang="ts">
import { socials } from '@/site';

const props = defineProps({
    simple: {
        type: Boolean,
        default: false,
    },
    noTitle: {
        type: Boolean,
        default: false,
    }
})
</script>
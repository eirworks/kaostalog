<template>
    <div class="my-5">
        <div class="text-gray-500 text-center text-sm mb-5">Hubungi Kami</div>
        <div class="flex space-x-5 justify-center">
            <div v-for="contact in contacts" class="flex space-x-3 items-center">
                <div v-if="contact.type !== 'whatsapp'"><img class="w-[24px] h-[24px]" :src="`/${contact.type}.svg`" :alt="contact.type"></div>
                <div v-if="contact.type === 'whatsapp'">
                    <a :href="`https://wa.me/${contact.value}`" class="flex space-x-3">
                        <img class="w-[24px] h-[24px]" :src="`/${contact.type}.svg`" :alt="contact.type">
                        <div>WhatsApp</div>
                    </a>
                </div>
                <div v-else>{{ contact.value }}</div>
            </div>
        </div>
    </div>
</template>
<script setup lang="ts">
import { contacts } from '@/site';
</script>
<template>
    <footer class="container md:w-2/3 mx-auto flex flex-col md:flex-row space-x-3 py-10 text-sm">
        <div class="flex-1 text-gray-500">
            <div class="mb-5 text-center md:text-start">&copy; {{ companyEst }} - {{ new Date().getFullYear() }} {{ appName }}</div>
            <ShopList />
        </div>
        <div>
            <menu class="flex space-x-3 justify-center md:justify-end">
                <!-- <li><a href="#">Katalog</a></li> -->
                <li><RouterLink :to="{name:'about'}">Tentang Kami</RouterLink></li>
            </menu>
            <div>
                <Socials simple no-title />
            </div>
        </div>
    </footer>
</template>

<script setup lang="ts">
import { appName, companyEst, shops } from '@/site';
import ShopList from '@/components/ShopList.vue';
import Socials from './Socials.vue';
</script>
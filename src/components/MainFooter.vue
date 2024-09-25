<template>
    <footer class="container md:w-2/3 mx-auto flex space-x-3 py-10 text-sm">
        <div class="flex-1 text-gray-500">
            <div class="mb-5">&copy; {{ companyEst }} - {{ new Date().getFullYear() }} {{ appName }}</div>
            <ShopList />
        </div>
        <div>
            <menu class="flex space-x-3">
                <li><a href="#">Tentang Kami</a></li>
                <li><a href="#">Katalog</a></li>
                <li><a href="#" class="font-bold">Hubungi Kami</a></li>
            </menu>
        </div>
    </footer>
</template>

<script setup lang="ts">
import { appName, companyEst, shops } from '@/site';
import ShopList from '@/components/ShopList.vue';
</script>
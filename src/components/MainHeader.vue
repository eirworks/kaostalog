<template>
    <div class="mb-10">
        <header class="container md:w-2/3 mx-auto flex flex-col md:flex-row space-y-3 md:space-y-0 md:space-x-3 py-3 items-center" v-if="headerType == 0">
            <div class="text-3xl md:text-2xl font-thin">
                <RouterLink to="/" class="flex space-x-3 items-center">
                    <img class="w-[50px] h-[50px]" src="/logo.png" alt="Logo">
                    <div class="brand-text">{{ appName }}</div>
                </RouterLink>
            </div>
            <div class="flex-1 flex space-x-1">
                <input type="search" name="q" v-model="query" placeholder="Cari produk"
                    class="border border-gray-500 py-2 px-5 rounded-full text-sm"
                >
                <button class="rounded-full bg-gray-200 px-3 py-1" @click="searchProduct()">Cari</button>
            </div>
            <nav>
                <menu class="flex space-x-3">
                    <!-- <li><a href="#">Kaos</a></li>
                    <li><a href="#">Aksesoris</a></li> -->
                    <li><RouterLink :to="{name: 'about'}" class="rounded-full bg-brand text-white px-3 py-2">Hubungi Kami</RouterLink></li>
                </menu>
            </nav>
        </header>

        <header class="container md:w-2/3 mx-auto flex flex-col py-3 items-center" v-if="headerType == 1">
            <div class="flex-1 text-2xl font-bold mb-5"><a href="#" v-on:click="headerType = 0">WEBSITE LOGO</a></div>
            <nav class="mb-5 flex space-x-3 items-center">
                
                <div>
                    <input type="search" name="q" placeholder="Cari produk"
                        class="border border-gray-500 py-2 px-5 rounded-full text-sm"
                    >
                </div>
                <menu class="flex space-x-3">
                    <li><a href="#">Produk</a></li>
                    <li><a href="#">Kaos</a></li>
                    <li><a href="#">Aksesoris</a></li>
                    <li><a href="#" class="rounded bg-orange-500 text-white px-3 py-1">Hubungi Kami</a></li>
                </menu>
            </nav>
            
        </header>

        <!-- <div class="mb-5 flex justify-center space-x-3">
            <div v-for="n in 3">
                <a href="#">
                    <div class="flex justify-center">
                        <div class="w-[50px] h-[50px] bg-gray-500 rounded-full"></div>
                    </div>
                    <div class="text-sm text-gray-500">Kategori {{ n }}</div>
                </a>
            </div>
        </div> -->
    </div>
</template>
<script lang="ts" setup>
    import {ref} from 'vue'
    import { RouterLink, useRouter } from 'vue-router';
    import { appName } from '@/site';
    import { useProductsStore } from '@/store/products';

    const headerType = ref(0)
    const query = ref("")
    const store = useProductsStore()
    const router = useRouter()

    function searchProduct() {
        router.push('/')
        store.keyword = query.value
        store.getProducts()
    }
</script>
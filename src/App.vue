<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import MainHeader from './components/MainHeader.vue'
import MainFooter from './components/MainFooter.vue'
</script>

<template>
  <MainHeader />

  <div class="min-h-screen">
    <RouterView />
  </div>

  <MainFooter />
</template>

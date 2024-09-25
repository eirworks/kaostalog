<template>
    <div class="mb-5">
        <div class="text-gray-500 text-sm mb-3" >{{ props.name }}</div>
        <div><slot></slot></div>
    </div>
</template>

<script setup>
const props = defineProps({
    name: String,
})
</script>
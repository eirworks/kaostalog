<template>
    <div>
        <div v-if="props.images.length === 0" class="p-10 text-center text-gray-500">
            Tidak ada gambar
        </div>
        <template v-else>
            <div class="flex justify-center mb-5 items-center space-x-3">
                <div>
                    <button type="button" class="rounded border border-black hover:bg-gray-200 p-3" @click="previousImage()">&larr;</button>
                </div>
                <div class="w-1/2 h-full bg-gray-500">
                    <img :src="currentImage" alt="Product Image">
                </div>
                <div><button type="button" class="rounded border border-black hover:bg-gray-200 p-3" @click="nextImage()">&rarr;</button></div>
            </div>
            <div class="my-5 flex justify-center space-x-3 flex-wrap">
                <div v-for="img, idx in props.images">
                    <div class="bg-gray-500 cursor-pointer w-[50px] h-[50px]" :class="{'border-2 border-black shadow': currentImage == img}">
                        <img :src="img" :alt="'Image '+(idx+1)" v-on:click="setImageByIndex(idx)">
                    </div>
                </div>
            </div>
        </template>
        
    </div>
</template>

<script setup lang="ts">
import { ref, type PropType } from 'vue';

const props = defineProps({
    'images': {
        type: Array as PropType<string[]>,
        default: []
    }
})

const currentImage = ref()
const currentIndex = ref(0)

if (props.images.length > 0) {
    currentImage.value = props.images[0]
}

function previousImage() {
    if (currentIndex.value === 0) {
        currentIndex.value = props.images.length - 1
    }
    else {
        currentIndex.value--
    }

    setImageByIndex(currentIndex.value)
}
function nextImage() {
    if (currentIndex.value === props.images.length - 1) {
        currentIndex.value = 0
    }
    else {
        currentIndex.value++
    }

    setImageByIndex(currentIndex.value)
}

function setImageByIndex(idx: number) {
    currentImage.value = props.images[idx]
    currentIndex.value = idx
}
</script>
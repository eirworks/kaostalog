import { defineStore } from "pinia";
import { ref } from "vue";
import { apiPath } from "@/site";
import axios from "axios";

export const useProductsStore = defineStore('products', () => {
    const products = ref([])

    function getProducts(keyword = "") {
        // call axios to server
        axios.get(apiPath)
            .then(function(response) {
                products.value = response.data.products
            })
    }

    return {products, getProducts}
})
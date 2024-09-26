import { defineStore } from "pinia";
import { ref } from "vue";
import { apiPath } from "@/site";
import axios from "axios";

export const useProductsStore = defineStore('products', () => {
    const products = ref([])

    function getProducts(keyword = "") {
        // call axios to server
        axios.get(apiPath, {
            params: {
                q: keyword
            }
        })
            .then(function(response) {
                products.value = response.data.products
            })
    }

    return {products, getProducts}
})

export const useViewProductStore = defineStore('product', () => {
    const product = ref(null);
    const loading = ref(false)

    function getProduct(id: Number) {
        product.value = null
        loading.value = true
        axios.get(apiPath, {
            params: {
                'product_id': id
            }
        })
            .then(function(response) {
                product.value = response.data.product
                loading.value = false
            })
    }

    return { product, getProduct, loading }
})
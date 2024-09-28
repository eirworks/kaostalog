import { defineStore } from "pinia";
import { ref, type Ref } from "vue";
import { apiPath } from "@/site";
import axios from "axios";

interface Product {
    name: string,
    title: string,
    id: string,
    description: string,
    image_urls: string[],
    images: string[],
    colors: string[],
    sizes: string[],
    material: string,
}

export const useProductsStore = defineStore('products', () => {
    const products: Ref<Product[]> = ref([])

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
    const product : Ref<Product|null> = ref(null);
    const loading = ref(false)

    function getProduct(id: any) {
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
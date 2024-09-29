import { defineStore } from "pinia";
import { ref, type Ref } from "vue";
import { productsApi, productApi, categoriesApi, descriptionApi } from "@/api";
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
        axios.get(productsApi)
            .then(function(response) {
                // filter by keyword in here
                if (keyword !== "") {
                    console.log("Filter by ", keyword)
                    products.value = response.data.filter(function(p: Product) {
                        return p.name.includes(keyword)
                    })
                } else {
                    console.debug("No filter!")
                    products.value = response.data
                }
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
        axios.get(productApi(id))
            .then(function(response) {
                product.value = response.data
                loading.value = false
            })
    }

    function getDescription(id: any) 
    {
        axios.get(descriptionApi)
            .then(function(response) {
                // update current product's description 
                if (product.value !== null) {
                    let p = product.value
                    p.description = response.data.description
                    product.value = p
                }
            })
    }

    return { product, getProduct, loading }
})